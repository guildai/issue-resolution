from tensorboardX import SummaryWriter
import numpy as np

writer = SummaryWriter()

writer.add_scalar('loss', np.nan, 1)
writer.add_scalar('loss', 1.0, 1)
writer.add_scalar('loss', 2, 1)
writer.add_scalar('loss', np.inf, 2)
