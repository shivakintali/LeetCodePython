
# Given two strings s and t, return true if s is a subsequence of t,
# or false otherwise.

# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, m, n = 0, 0, len(s), len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m
        

soln = Solution()

word1, word2 = "abc", "ahbgdc"
print("Input: {} {}".format(word1, word2))
out = soln.isSubsequence(word1, word2)
print("Output: {}".format(out))
assert(out == True)

word1, word2 = "axc", "ahbgdc"
print("Input: {} {}".format(word1, word2))
out = soln.isSubsequence(word1, word2)
print("Output: {}".format(out))
assert(out == False)

print("All tests passed")
