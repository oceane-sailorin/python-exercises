#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    return str[:len(str)//2]





print(first_half('WooHoo'))
print(first_half('HelloThere')) 
print(first_half('abcdef'))
print(first_half('sayhellotothecow'))
print(first_half('dontforgetthemilkonthetable'))
print(first_half('abs'))