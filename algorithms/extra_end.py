#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
#The string length will be at least 2.

def extra_end(str):
    return str[-2:]*3


print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))
print(extra_end('u'))
print(extra_end(''))
print(extra_end('bla'))
print(extra_end('ole'))
print(extra_end('tchou'))
print(extra_end('bouli'))