class Counter():
    def __init__(self, value):
        self.value = value

    def inc(self):
        self.value += 1 # passes tests
        # self.value -= 1 # fails tests
        return self.value
