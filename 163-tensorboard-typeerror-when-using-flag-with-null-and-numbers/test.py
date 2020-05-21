import tensorboardX

L1 = 5
L2 = None

print("loss: 1.123")
print("acc1: null")
print("acc2: None")
print("acc3: 0")

with tensorboardX.SummaryWriter(".") as w:
    w.add_scalar("acc4", 2.234)
