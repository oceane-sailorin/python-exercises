#Given 2 strings, return their concatenation, except omit the first char of each. 
# The strings will be at least length 1.

def non_start(a, b):
    return a[1:] + b[1:]

print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))
print(non_start('', 'j'))
print(non_start('j', 'ap'))
print(non_start('erose', 'amary'))
print(non_start('enun', 'ishaku'))
print(non_start('sc', 'gelimene'))
print(non_start('afait', 'xcho'))