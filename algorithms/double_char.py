#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    return "".join([x*2 for x in str])

print(double_char('The')) # → 'TThhee'
print(double_char('AAbb')) # → 'AAAAbbbb'
print(double_char('Hi-There')) # → 'HHii--TThheerree'
print(double_char('Word!')) # → 'WWoorrdd!!'	'WWoorrdd!!'	OK	
print(double_char('!!')) # → '!!!!'	'!!!!'	OK	
print(double_char('')) # → ''	''	OK	
print(double_char('a')) # → 'aa'	'aa'	OK	
print(double_char('.')) # → '..'	'..'	OK	
print(double_char('aa')) # → 'aaaa'	'aaaa'	OK