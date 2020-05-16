import pickle


class A:
    def __init__(self):
        print("A")


with open("test.pickle", "wb") as f:
    pickle.dump(A(), f)
