#find the difference
"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

"""

import operator
import collections
from functools import reduce

class Solution:
    def findTheDifference2(self, s: str, t: str) -> str:
        s_set = set(s)
        t_set = set(t)
        print(s_set)
        print(t_set)
        diff = ''.join(s_set.symmetric_difference(t_set))
        return diff

    def findTheDifference3(self, s: str, t: str) -> str:
        s_list = list(s)
        t_list = list(t)
        return chr(reduce(operator.xor, map(ord, s), 0) ^ reduce(operator.xor, map(ord, t), 0))

    def findTheDifference(self, s: str, t: str) -> str:     
        t_list = list(t)
        s_list = list(s)
        for i in s_list:
            t_list.remove(i)
        if t_list: return t_list[0]
        else: return ""
    




s1 = Solution()

#check examples

print(s1.findTheDifference("abcd","abcde"))

print(s1.findTheDifference("","y"))

print(s1.findTheDifference("aa","aea"))

print(s1.findTheDifference("toto","toto"))

print(s1.findTheDifference("a","aa"))

