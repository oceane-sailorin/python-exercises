#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    return (b + a + b) if len(a) == len(b) else (min([a,b], key=len) + max([a,b], key=len) + min([a,b], key=len))


print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))
print(combo_string('', 'b'))
print(combo_string('ku', 'kiki'))
print(combo_string('ranger', 'noumea'))
print(combo_string('loki', 'thor'))
print(combo_string('naka', 'sone'))