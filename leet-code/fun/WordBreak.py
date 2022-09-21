# Algorithm

# - Take all of the word dictionaries and add them to a single Trie structure
# - Loop through the characters in the string and compare them to the trie structure. If we encounter an element that is not at the next node in the trie structure, return an error.
# - If we get to an element that is at the end of the trie structure, go to the beginning
# - When we terminate, if we terminate at the end of a trie loop, we will return true, otherwise we will return false

# Time complexity: O(n + k * m) (where k is the maximum size of a word in the dict and m is the size of the dict) | Space complexity: O(k * m)

# ALTERNATVIE: Dynamic programming - https://youtu.be/Sx9NNgInc3A

# Algorithm (dynamic programming)
# - Build a tree featuring the different words until the lengths match or we have a word out of place
# - For each word we add, we just need to check if the current word matches what we require, and then we can move on to the next part and so on

class Solution:
    def wordBreak(self, s, wordDict):
        pass


tests = [("leetcode", ["leet", "code"]), ("applepenapple", [
    "apple", "pen"]), ("catsandog", ["cats", "dog", "sand", "and", "cat"])]

for test in tests:
    print(Solution().wordBreak(test[0], test[1]))
