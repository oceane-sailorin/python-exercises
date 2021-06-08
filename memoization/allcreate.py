# write function allcreate(target,words) with arguments target string and list of strings
# function should return all  possible solutions to create target with words
# one word can be used several times
# use of recursion and memoization
# in this case, memoization has little effect because in worst case we have to write huge sub lists

def allCreate(target, words, subDict=None):

    if subDict is None:
        subDict = {} 

    if target in subDict: return subDict[target]
    if target == "": return [[]]

    result = []

    for word in words:
        if target.startswith(word):
            suffix = target[len(word):]
            allSuffixes = allCreate(suffix,words,subDict)
            allTargets = [[suf.insert(0,word) for suf in allSuffixes]]
            result.extend(allSuffixes)

    subDict[target] = result
    return result


print(allCreate("",["mil","one","tone","est"]))   
print(allCreate("milestone",["mil","one","tone","est"]))     
print(allCreate("autonomous",["nom","mous","aut","o","mo","no","us","m"]))   
print(allCreate("careless",["ca","carl","cor","car","mo","s","ele"]))      
print(allCreate("milestone",["mile","one","tone","est"]))  
print(allCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   