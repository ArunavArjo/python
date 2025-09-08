class bird:
    def __init__(self):
        print("Iam a bird")

    def whoisthis(self):
        print("Iam a penguin")

    def fly(self):
        print("Fly faster")

class Penguin(bird):
        def __init__(self):
            super(). __init__()
            print("Iam a penguin")

        def whoisthis(self):
             print("Iam a penguin")

        def run(self):
             print("I can run faster")
peggy = Penguin
peggy.whoisthis
peggy.run
