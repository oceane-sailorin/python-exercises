# First Unique Character in a String

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
       subDict = {} 
       for char in s: 
           if char in subDict: subDict[char] += 1 
           else: subDict[char] = 1

s1 = Solution()

#check examples

print(s1.firstUniqChar("romero"))

print(s1.firstUniqChar("beauchamps"))

print(s1.firstUniqChar("nakasone"))

print(s1.firstUniqChar("toto"))

