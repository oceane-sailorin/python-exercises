# write function cancreate(target,words) with arguments target string and list of strings
# function should return boolean whether it is possible to create target with words
# one word can be used several times
# use of recursion and memoization

def canCreate(target, words, subDict=None):

    if subDict is None:
        subDict = {}   

    if target in subDict: return subDict[target]
    if target == "": return True

    for word in words:
        if target.startswith(word):
            suffix = target[len(word):]
            if(canCreate(suffix, words, subDict)) == True:
                subDict[target] = True
                return True
    
    subDict[target] = False
    return False

print(canCreate("milestone",["mil","one","tone","est"]))   
print(canCreate("autonomous",["nom","mous","aut","o","mo"]))   
print(canCreate("careless",["ca","carl","cor","car","mo","s","ele"]))   
print(canCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   