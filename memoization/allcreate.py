# write function allcreate(target,words) with arguments target string and list of strings
# function should return all  possible solutions to create target with words
# one word can be used several times
# use of recursion and memoization

def allCreate(target, words):

    if target == "": return [[]]

    return []

print(allCreate("",["mil","one","tone","est"]))   
print(allCreate("milestone",["mil","one","tone","est"]))   
print(allCreate("autonomous",["nom","mous","aut","o","mo","no","us","m"]))   
print(allCreate("careless",["ca","carl","cor","car","mo","s","ele"]))      