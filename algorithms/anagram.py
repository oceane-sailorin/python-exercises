#anagram

# function with sorted
def anagram(string1, string2):

    #remove upper cases and spaces
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower()

    if sorted(string1) == sorted(string2):
        return True

    return False

print(anagram("Twelve plus one", "Eleven plus two"))

#function with loop without import
def another_anagram(string1, string2):

    #remove upper cases and spaces
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower() 

    if len(string1) != len(string2):
        return False

    count = {}

    for character in string1:
        if character in count: 
            count[character] += 1
        else:
            count[character] = 1

    for character in string2:
        if character in count: 
            count[character] -= 1
        else:
            count[character] = 1       

    for c in count:
        if count[c] != 0:
            return False
    
    return True


print(another_anagram("Twelve plus one", "Eleven plus two"))   
print(another_anagram("Similar","Equal"))

# function with Counter
from collections import Counter

def anagram_again(string1, string2):

    #remove upper cases and spaces
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower() 

   
    if(Counter(string1) == Counter(string2)):
        return True
    else:
        return False


print(anagram_again("Twelve plus one", "Eleven plus two"))   
print(anagram_again("Similar","Equal"))