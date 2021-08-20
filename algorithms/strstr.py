# strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        table = [False for _ in range(len(haystack) + 1)]

        if needle == "": return 0
        elif haystack == "": return -1

        for n in range(len(table)):
            #if the needle matches the characters starting at position n
            if n + len(needle) <= len(table) and haystack[n:n + len(needle)] == needle :
                return n
                        
        return -1

s1 = Solution()

print(s1.strStr("hello","ll"))

print(s1.strStr("hello","h"))

print(s1.strStr("",""))

print(s1.strStr("hello",""))

print(s1.strStr("","ll"))

print(s1.strStr("hello in the closet hidden in the cups","hid"))

print(s1.strStr("aaaaaaaaaaaaa","aaab"))

print(s1.strStr("hello in the closet hidden in the cups jouhbui iu ib d k kjd knd kndkndkj nkjd njkd kd kjd kjn jkdn jkdn kjn kdfnkdnjkdnjk djk nkdj ndkj njkd jk","njkd"))