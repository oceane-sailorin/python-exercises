# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxsub = 0
        res = []
        for car in s:
            if car not in res:
                res.append(car)
                if len(res) > maxsub:
                    maxsub = len(res)
            else:
                res = res[res.index(car)+1:]
                res.append(car)
        return maxsub

       

  
s1 = Solution()

print(s1.lengthOfLongestSubstring("abcabcbb"))
print(s1.lengthOfLongestSubstring("bbbbb"))
print(s1.lengthOfLongestSubstring("pwwkew"))
print(s1.lengthOfLongestSubstring(""))
print(s1.lengthOfLongestSubstring("aabbaacc"))
print(s1.lengthOfLongestSubstring("abcdefghi"))
print(s1.lengthOfLongestSubstring("brutalineb"))
print(s1.lengthOfLongestSubstring("abcdefghiajklmnop"))
print(s1.lengthOfLongestSubstring("cc"))
print(s1.lengthOfLongestSubstring("c"))
