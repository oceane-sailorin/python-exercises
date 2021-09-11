# Reverse Words in a String
"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        

s1 = Solution()

print(s1.reverseWords("  Bob    Loves  Alice   "))
print(s1.reverseWords("Alice does not even like bob"))
print(s1.reverseWords("  hello world  "))