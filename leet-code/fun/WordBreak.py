# Algorithm

# - Take all of the word dictionaries and add them to a single Trie structure
# - Loop through the characters in the string and compare them to the trie structure. If we encounter an element that is not at the next node in the trie structure, return an error.
# - If we get to an element that is at the end of the trie structure, go to the beginning
# - When we terminate, if we terminate at the end of a trie loop, we will return true, otherwise we will return false

# Time complexity: O(n + k * m) (where k is the maximum size of a word in the dict and m is the size of the dict) | Space complexity: O(k * m)

# ALTERNATVIE: Dynamic programming - https://youtu.be/Sx9NNgInc3A
