#isAnagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(' ','').lower()
        t = t.replace(' ','').lower()

        if sorted(s) == sorted(t):
            return True

        return False

s1 = Solution()

print(s1.isAnagram("anagram","nagaram"))
print(s1.isAnagram("rat","car"))
print(s1.isAnagram("Twelve plus one", "Eleven plus two"))   
print(s1.isAnagram("Similar","Equal"))