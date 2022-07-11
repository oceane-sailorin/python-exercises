#Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    return str[:n] + str[n + 1:]

def missing_char2(str, n):
    new_str = ""
  
    for i in range(len(str)):
        if i != n:
            new_str = new_str + str[i]
    return new_str

def missing_char3(str, n):
    return ''.join(str[x] for x in range(len(str)) if x != n)


def missing_char4(str, n):
    l = list(str)
    del(l[n])
    return "".join(l)

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

print(missing_char2('kitten', 1))
print(missing_char2('kitten', 0))
print(missing_char2('kitten', 4))

print(missing_char3('kitten', 1))
print(missing_char3('kitten', 0))
print(missing_char3('kitten', 4))

print(missing_char4('kitten', 1))
print(missing_char4('kitten', 0))
print(missing_char4('kitten', 4))