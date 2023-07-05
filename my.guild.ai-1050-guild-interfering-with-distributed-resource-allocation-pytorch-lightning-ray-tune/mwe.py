"""MWE following https://docs.ray.io/en/latest/tune/examples/tune-pytorch-lightning.html"""
import os
from typing import Any
from numpy import array, ndarray
from numpy.random import default_rng
from pandas import DataFrame, Index, Series
from pytorch_lightning import LightningDataModule, LightningModule
from pytorch_lightning.loggers import TensorBoardLogger
import torch
import torch.nn as nn
from torch import from_numpy
from torch.optim import Adam
from torch.utils.data import DataLoader, Dataset
from ray import tune, air
from ray.tune.schedulers import ASHAScheduler
from ray.air.config import RunConfig, ScalingConfig, CheckpointConfig
from ray.train.lightning import LightningTrainer, LightningConfigBuilder

SEED = 239
NUM_TRAIN_SAMPLES = 8000
NUM_VAL_SAMPLES = 20
NUM_IN_FEATURES = 10

NUM_DATALOADER_WORKERS = 7
NUM_TRAINER_WORKERS = 1
NUM_TRAINER_CPUS = 3
NUM_TRAINER_GPUS = 0
USE_GPU = NUM_TRAINER_GPUS > 0

class MyLightningModule(LightningModule):
    def __init__(
        self,
        lr: float,
        arg_with_index: Index,
        arg_with_Series: Series,
        arg_with_dataframe: DataFrame,
        arg_with_ndarray: ndarray,
    ):
        super().__init__()
        self.save_hyperparameters()
        self.loss = nn.MSELoss()
        self.fc1 = nn.Linear(NUM_IN_FEATURES, 5)
        self.fc2 = nn.Linear(5, NUM_IN_FEATURES)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x

    def training_step(self, train_batch, batch_idx):
        return self.shared_step("train", train_batch, batch_idx)

    def validation_step(self, train_batch, batch_idx):
        return self.shared_step("val", train_batch, batch_idx)

    def shared_step(self, split, batch, batch_idx):
        x, y = batch
        output = self(x)
        loss = self.loss(output, y)
        self.log(f"{split}/loss", loss)
        return loss

    def configure_optimizers(self) -> Any:
        return Adam(self.parameters(), lr=self.hparams.lr)


class MyDataset(Dataset):
    def __init__(self, X, y) -> None:
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.y)

    def __getitem__(self, index) -> Any:
        return from_numpy(self.X[index]).to(torch.float), from_numpy(self.y[index]).to(
            torch.float
        )


class MyDataModule(LightningDataModule):
    def setup(self, stage=None):
        rng = default_rng(SEED)
        self.train = rng.random((NUM_TRAIN_SAMPLES, NUM_IN_FEATURES))
        self.train_true = rng.random((NUM_TRAIN_SAMPLES, NUM_IN_FEATURES))

        self.val = rng.random((NUM_VAL_SAMPLES, NUM_IN_FEATURES))
        self.val_true = rng.random((NUM_VAL_SAMPLES, NUM_IN_FEATURES))

        self.test = rng.random((NUM_VAL_SAMPLES, NUM_IN_FEATURES))
        self.test_true = rng.random((NUM_VAL_SAMPLES, NUM_IN_FEATURES))

    def train_dataloader(self):
        return DataLoader(
            MyDataset(self.train, self.train_true),
            batch_size=10,
            num_workers=NUM_DATALOADER_WORKERS
        )

    def val_dataloader(self):
        return DataLoader(
            MyDataset(self.val, self.val_true),
            batch_size=10,
            num_workers=NUM_DATALOADER_WORKERS
        )

    def test_dataloader(self):
        return DataLoader(
            MyDataset(self.test, self.test_true),
            batch_size=10,
            num_workers=NUM_DATALOADER_WORKERS
        )


num_epochs = 5
num_tuning_samples = 2
accelerator = "cpu" # gpu


if __name__ == "__main__":
    dm = MyDataModule()
    logger = TensorBoardLogger(save_dir=os.getcwd(), name="mwe")

    # Define constant configs and searchable configs separately
    config = {
        "arg_with_index": Index([1, 2, 3, 4]),
        "arg_with_Series": Series(
            [1, 2, 3, 4], index=["a", "b", "c", "d"], name="name"
        ),
        "arg_with_dataframe": DataFrame(
            [[1, 2, 3, 4], [5, 6, 7, 8]],
            index=["a", "b"],
            columns=["col1", "col2", "col3", "col4"],
        ),
        "arg_with_ndarray": array([1, 2, 3, 4]),
    }

    search_config = {
        "lr": tune.loguniform(1e-4, 1e-1),
    }

    lightning_config = (
        LightningConfigBuilder()
        .module(cls=MyLightningModule, **config)
        .trainer(max_epochs=num_epochs, accelerator=accelerator, logger=logger)
        .fit_params(datamodule=dm)
        .checkpointing(monitor="val/loss", save_top_k=1, mode="min")
        .build()
    )

    run_config = RunConfig(
        checkpoint_config=CheckpointConfig(
            num_to_keep=1,
            checkpoint_score_attribute="val/loss",
            checkpoint_score_order="min",
        ),
    )
    
    scaling_config = ScalingConfig(
        num_workers=NUM_TRAINER_WORKERS,
        use_gpu=USE_GPU,
        resources_per_worker={
            "CPU": NUM_TRAINER_CPUS,
            "GPU": NUM_TRAINER_GPUS
        }
    )

    search_lightning_config = LightningConfigBuilder().module(**search_config).build()

    # Initialize your trainer with constant configs first
    lightning_trainer = LightningTrainer(
        lightning_config=lightning_config,
        scaling_config=scaling_config,
        run_config=run_config,
    )

    # Then, feed the search space to Tuner
    tuner = tune.Tuner(
        lightning_trainer,
        param_space={"lightning_config": search_lightning_config},
        tune_config=tune.TuneConfig(
            metric="val/loss",
            mode="min",
            num_samples=num_tuning_samples,
            scheduler=ASHAScheduler(
                max_t=num_epochs,
                grace_period=1,
                reduction_factor=2,
            ),
        ),
        run_config=air.RunConfig(
            local_dir="./ray_results",
            name="mwe",
        ),
    )
    results = tuner.fit()
