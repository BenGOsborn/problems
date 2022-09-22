class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        self.stack.append(self.min)
        if self.min is None or val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self):
        self.stack.pop(-1)
        self.min = self.stack.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min
