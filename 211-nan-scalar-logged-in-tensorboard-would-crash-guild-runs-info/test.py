from tensorboardX import SummaryWriter
import numpy as np

writer = SummaryWriter()

writer.add_scalar('loss', np.nan, 1)
