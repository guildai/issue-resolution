from types import SimpleNamespace


class CFG:
    flag_a = 1
    flag_b = 2


cfg = CFG()
print("cfg:", cfg.flag_a, cfg.flag_b)

cfg2 = SimpleNamespace(flag_c=3, flag_d=4)
print("cfg2:", cfg2.flag_c, cfg2.flag_d)
