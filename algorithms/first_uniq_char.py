# First Unique Character in a String

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""
from collections import Counter

class Solution:
    #solution with dictionary
    def firstUniqChar(self, s: str) -> int:
        subDict = {} 
        index = -1
        for i,char in enumerate(s):
           if char in subDict: subDict[char] += 1 
           else: subDict[char] = 1

        for i,char in enumerate(s):
            if subDict[char] == 1: return i

        return index

    #solution with counter from collections
    def firstUniqChar2(self, s: str) -> int:
        count = Counter(s)
        res = {key for key,value in count.items() if value==1}
        for i in range(len(s)):
            if s[i] in res:
                return i
        else:
            return -1




s1 = Solution()

#check examples

print(s1.firstUniqChar("romero"))

print(s1.firstUniqChar("beauchamps"))

print(s1.firstUniqChar("nakasone"))

print(s1.firstUniqChar("toto"))

print(s1.firstUniqChar2("romero"))

print(s1.firstUniqChar2("beauchamps"))

print(s1.firstUniqChar2("nakasone"))

print(s1.firstUniqChar2("toto"))

