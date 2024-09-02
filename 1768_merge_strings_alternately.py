from itertools import zip_longest

# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer
# than the other, append the additional letters onto the end of the merged
# string.

# Return the merged string.

class Solution:
    def mergeAlternately(self, word1, word2):
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))


soln = Solution()

word1, word2 = "abc", "pqr"
print("Input: {} {}".format(word1, word2))
out = soln.mergeAlternately(word1, word2)
print("Output: {}".format(out))
assert(out == "apbqcr")

word1, word2 = "ab", "pqrs"
print("Input: {} {}".format(word1, word2))
out = soln.mergeAlternately(word1, word2)
print("Output: {}".format(out))
assert(out == "apbqrs")

word1, word2 = "abcd", "pq"
print("Input: {} {}".format(word1, word2))
out = soln.mergeAlternately(word1, word2)
print("Output: {}".format(out))
assert(out == "apbqcd")

print("All tests passed")
