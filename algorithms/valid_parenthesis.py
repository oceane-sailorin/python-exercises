# valid parenthesis

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"]":"[", "}":"{", ")":"("}
        li = ["]","[", "}","{", ")","("]
        res = []
        for car in s:
            if car not in li:
                return False
            
            if car in dict.keys():
                if not res or dict[car] != res.pop(): 
                    return False
            elif car in dict.values():
                res.append(car)
        return len(res) == 0

  
s1 = Solution()

print(s1.isValid("()"))
print(s1.isValid("()[]{}"))
print(s1.isValid("(]"))
print(s1.isValid("([)]"))
print(s1.isValid("{[]}"))

