class MyHashMap:
    def __init__(self):
        self.length = 50
        self.storage = [[] for _ in range(self.length)]

    def put(self, key: int, value: int) -> None:
        hashed = hash(key) % self.length

        exists = False
        for elem in self.storage[hashed]:
            if elem[0] == key:
                exists = True
                elem[1] = value

        if not exists:
            self.storage[hashed].append([key, value])

    def get(self, key: int) -> int:
        hashed = hash(key) % self.length

        for elem in self.storage[hashed]:
            if elem[0] == key:
                return elem[1]

        return -1

    def remove(self, key: int) -> None:
        hashed = hash(key) % self.length

        for i, elem in enumerate(self.storage[hashed]):
            if elem[0] == key:
                self.storage[hashed].pop(i)
                return