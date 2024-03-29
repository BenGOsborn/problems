class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        while len(self.stack) > 0:
            self.temp.append(self.stack.pop(-1))
        
        self.stack.append(x)

        while len(self.temp) != 0:
            self.stack.append(self.temp.pop(-1))

    def pop(self) -> int:
        return self.stack.pop(-1)

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0