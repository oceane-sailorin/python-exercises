# decode string

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
"""

class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        res = ''
        #initialize stack list
        temp = []
        for c in s:
            if c.isdigit():
                #multiply existing number by ten and add new digit (in case k has several digits)
                num = num * 10 + int(c)
            elif c == '[':
                #append existing values in stack list in order to recover them at the end of the brackets
                temp.append((res, num))
                #reinitialize values to take into account only what is in the brackets
                num = 0
                res = ''
            elif c == ']':
                #retrieve the values from the stack
                temp_res,temp_num = temp.pop()
                #multiply letters in the brackets by number before the brackets and add to what was the string before the brackets
                res = temp_res + temp_num * res
            else:
                #add character to current string
                res += c

        return res


s1 = Solution()

#check examples

print(s1.decodeString("3[a]2[bc]"))

print(s1.decodeString("3[a2[c]]"))

print(s1.decodeString("2[abc]3[cd]ef"))

print(s1.decodeString("abc3[cd]xyz"))

print(s1.decodeString("100[leetcode]"))

