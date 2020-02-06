from guild import summary

with summary.SummaryWriter(".") as writer:
    writer.add_scalar("a", 1.0)
    writer.add_scalar("a/b", 2.0)
