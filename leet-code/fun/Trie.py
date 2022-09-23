class Node:
    def __init__(self):
        self.map = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.map:
                current.map[char] = Node()
            current = current.map[char]

        current.end = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.map:
                return False
            current = current.map[char]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.map:
                return False
            current = current.map[char]

        return True


trie = Trie()

trie.insert("apple")

print(trie.search("apple"))  # return True
print(trie.search("app"))  # return False
print(trie.startsWith("app"))  # return True

trie.insert("app")

print(trie.search("app"))  # return True
