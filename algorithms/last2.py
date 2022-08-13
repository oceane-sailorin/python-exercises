#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
    if len(str) < 2:
        return 0
    sub = str[-2:]
    countSub = 0
    for i in range(1, len(str)-1):
        if str[i-1:i+1] == sub:
            countSub += 1
    return countSub

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxxx'))