# given a string, return character which does not repeat
# if more than one, return first one

def nonrepeat(string1):
    string1 = string1.replace(' ','').lower()
    dict = {}

    for s in string1:
        if s in dict: 
            dict[s] += 1
        else:
            dict[s] = 1

    for s in string1:
        if dict[s] == 1:
            return s
        

    return None

print(nonrepeat("785217852"))
print(nonrepeat("I like peeling king apples"))

# given a string, return all characters which do not repeat

def nonrepeat2(string1):
    string1 = string1.replace(' ','').lower()
    dict = {}

    for s in string1:
        if s in dict: 
            dict[s] += 1
        else:
            dict[s] = 1

    result = []
    
    sorted_list = sorted(dict.items(), key=lambda x : x[1])

    for item in sorted_list:
        if item[1] == sorted_list[0][1]:
            result.append(item[0])

    return result

print(nonrepeat2("785217852"))
print(nonrepeat2("I like peeling king apples"))

def nonrepeat3(string1):
    string1 = string1.replace(' ','').lower()
    dict = {}

    for s in string1:
        if s in dict: 
            dict[s] += 1
        else:
            dict[s] = 1

    result = []
    result = [key  for (key, value) in dict.items() if value == 1]

    return result

print(nonrepeat2("785217852"))
print(nonrepeat2("I like peeling king apples"))