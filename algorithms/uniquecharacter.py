# find if all characters unique in string

def uniquecharacter(string1):
    string1 = string1.replace(' ','')
    return len(set(string1)) == len(string1)


print(uniquecharacter('a b cdef'))
print(uniquecharacter('a b ccdef'))


def uniquecharacter2(string1):
    string1 = string1.replace(' ','')
    characters = set()

    for s in string1:
        if s in characters:
            return False
        else:
            characters.add(s)
    return True


print(uniquecharacter2('kirdnesw'))
print(uniquecharacter2('lpoertncweof'))