#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    cat = str.count("cat")
    dog = str.count("dog")
    return cat == dog


print(cat_dog('catdog')) # → True
print(cat_dog('catcat')) #  → False
print(cat_dog('1cat1cadodog')) #  → True