import torch

from impl import main_worker

n_gpus = 1
args = ["foo", "bar"]

if __name__ == "__main__":
    torch.multiprocessing.spawn(main_worker, nprocs=n_gpus, args=(n_gpus, args))
