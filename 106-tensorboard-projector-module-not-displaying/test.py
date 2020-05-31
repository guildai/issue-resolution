import os
import time

import torch
from torch.utils.tensorboard import SummaryWriter

points = 10
logdir = os.getenv("LOGDIR") or "logs/%i" % int(time.time() * 1000)

data = torch.randn((points, 5))
metadata = ["point-%i" % (i + 1) for i in range(points)]

if not os.path.exists(logdir):
    os.makedirs(logdir)

tensorboard_writer = SummaryWriter(logdir)
tensorboard_writer.add_embedding(data, metadata=metadata, tag="embeddings")
