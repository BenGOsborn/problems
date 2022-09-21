# def word_break_h(self, current, string, word_dict, cache):
#     if len(current) > len(string):
#         return False
#     elif current == string:
#         return True

#     for word in word_dict:
#         out = self.word_break_h(current + word, string, word_dict, cache)
#         if out:
#             return True

#     return False

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
    def word_break_h(self, n, string, word_dict, cache):
        if n in cache:
            return cache[n]

        if n > len(string):
            cache[n] = False
            return False
        if n == len(string):
            cache[n] = True
            return True

        for elem in word_dict:
            if self.word_break_h(n + len(elem), string, word_dict, cache) and elem == string[n:n+len(elem)]:
                cache[n] = True
                return True

        cache[n] = False
        return False

    def wordBreak(self, s, wordDict):
        return self.word_break_h(0, s, wordDict, {})


tests = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"])
]

for test in tests:
    print(Solution().wordBreak(test[0], test[1]))


# **** WORK IN PROGRESS - https://leetcode.com/problems/word-break/
