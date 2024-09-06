#392. is subsequence

#Given two strings s and t, return true if s is a subsequence of t, or false #otherwise.

#A subsequence of a string is a new string that is formed from the original #string by deleting some (can be none) of the characters without disturbing #the relative positions of the remaining characters. (i.e., "ace" is a #subsequence of "abcde" while "aec" is not).

#Example 1:

#Input: s = "abc", t = "ahbgdc"
#Output: true


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
        return j == len(s)

