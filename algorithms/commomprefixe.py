#commonprefixe

class Solution:
    def longestCommonPrefix(self, arr1) -> str:
        
        if not arr1 or len(arr1) > 200: return ""
        
        car = min(arr1, key=len)
        if len(car) == 0: return ""
        if len(max(arr1, key=len)) > 200: return ""

        res = ""

        for i, s in enumerate(car):
            for str in arr1 :
                if str[i] != s:
                    return res
            res += s    
        return res   


s1 = Solution()

print(s1.longestCommonPrefix(["flower","flow","flight"]))
print(s1.longestCommonPrefix(["fine","finally","finess"]))
print(s1.longestCommonPrefix(["correct","correctness","correctnessly"]))
print(s1.longestCommonPrefix(["juilo","juil",""]))
print(s1.longestCommonPrefix([]))
print(s1.longestCommonPrefix(["jkjk","ioio","gygy","vgvg","cfcf","rtrt"]))
