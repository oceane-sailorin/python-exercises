#Repeated DNA Sequences
"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Constraints:

    1 <= s.length <= 105
    s[i] is either 'A', 'C', 'G', or 'T'.
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        dict = {}
        result = []
        for i in range(len(s)):
            seq = s[i:i+10]
            if seq in dict: 
                dict[seq] += 1
            else:
                dict[seq] = 1
        for key, val in dict.items():
            if val > 1:
                result.append(key)
        return result

s1 = Solution()

print(s1.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s1.findRepeatedDnaSequences("AAAAAAAAAAAAA"))