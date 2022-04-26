from guild import ipy as guild

def op():
    print("Running a fake op")

guild.run(op)

runs = guild.runs()
print(runs)
