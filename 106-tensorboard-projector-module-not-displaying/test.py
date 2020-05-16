import torch
from torch.utils.tensorboard import SummaryWriter

points = 10

metadata = ["point-%i" % (i + 1) for i in range(points)]

tensorboard_writer = SummaryWriter(".")
tensorboard_writer.add_embedding(
    torch.randn((points, 5)), metadata=metadata, tag="embeddings"
)
