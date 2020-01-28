import torch
from torch.utils.tensorboard import SummaryWriter

tensorboard_writer = SummaryWriter(".")
tensorboard_writer.add_embedding(
    torch.randn((10, 5)), metadata=["dummy"] * 10, tag="embeddings"
)
