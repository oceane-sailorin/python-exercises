#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
    return a + b*2 + a

print(make_abba('Hi', 'Bye'))
print(make_abba('Yo', 'Alice'))
print(make_abba('What', 'Up'))
print(make_abba('x', 'y'))
print(make_abba('x', ''))
print(make_abba('', 'y'))
print(make_abba('aaabbbaaa', 'bbbaaabbb'))
print(make_abba('Ya', 'Bo'))