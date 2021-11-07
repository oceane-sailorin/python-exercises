# is subsequence

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i = 0
               
        for c in t:
            if c == s[i]:
                i += 1
            if i >= len(s):
                break
        
        if i == len(s):     
            return True
        
        return False



s1 = Solution()

#check examples

print(s1.isSubsequence("abc","ahbgdc"))

print(s1.isSubsequence("axc","ahbgdc"))