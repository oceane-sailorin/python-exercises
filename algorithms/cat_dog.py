#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    cat = str.count("cat")
    dog = str.count("dog")
    return cat == dog


print(cat_dog('catdog')) # → True
print(cat_dog('catcat')) #  → False
print(cat_dog('1cat1cadodog')) #  → True
print(cat_dog('catxdogxdogxcat')) # → True	True	OK	
print(cat_dog('catxdogxdogxca')) # → False	False	OK	
print(cat_dog('dogdogcat')) # → False	False	OK	
print(cat_dog('dogogcat')) # → True	True	OK	
print(cat_dog('dog')) # → False	False	OK
print(cat_dog('cat')) # → False	False	OK	
print(cat_dog('ca')) # → True	True	OK	
print(cat_dog('c')) # → True	True	OK	
print(cat_dog('')) # → True	True	OK