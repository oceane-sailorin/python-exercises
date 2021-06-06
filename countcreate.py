# write function countcreate(target,words) with arguments target string and list of strings
# function should return number of possible solutuons to create target with words
# one word can be used several times
# use of recursion and memoization

def countCreate(target, words, subDict=None):

    if subDict is None:
        subDict = {}   

    if target in subDict: return subDict[target]
    if target == "": return 1

    total = 0

    for word in words:
        if target.startswith(word):
            suffix = target[len(word):]
            num = countCreate(suffix, words, subDict)
            total += num
    
    subDict[target] = total
    return total

print(countCreate("milestone",["mil","one","tone","est"]))   
print(countCreate("autonomous",["nom","mous","aut","o","mo","no","us","m"]))   
print(countCreate("careless",["ca","carl","cor","car","mo","s","ele"]))   
print(countCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   
print(countCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aab","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   