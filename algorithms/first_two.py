#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
def first_two(str):
    return str[0:2]

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))
print(first_two('a'))
print(first_two(''))