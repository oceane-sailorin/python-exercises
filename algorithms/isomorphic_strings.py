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
        #if not same length return false
        if len(s) != len(t):
            return False

        # iterate on s 
        for i in range(len(s)):

            if s[i] in subDict.keys():
                if subDict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in subDict.values():
                    return False

                # put value of same index of t as value to key of index i of s
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