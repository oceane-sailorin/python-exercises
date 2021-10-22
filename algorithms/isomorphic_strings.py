#isomorphic strings

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       
        subDict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):

            if s[i] in subDict.keys() and subDict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in subDict.values():
                    return False
            
                subDict[s[i]] = t[i]
        return True           
    
        

      
s1 = Solution()

#check examples

print(s1.isIsomorphic("egg","add"))
print(s1.isIsomorphic("foo","bar"))
print(s1.isIsomorphic("paper","title"))
print(s1.isIsomorphic("rommen","arccod"))
print(s1.isIsomorphic("nakanome","moromiwe"))
print(s1.isIsomorphic("nakanome","mamarite"))