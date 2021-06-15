# write function cancreate(target,words) with arguments target string and list of strings
# function should return boolean whether it is possible to create target with words
# one word can be used several times
# use of tabulation

def canCreate(target, words):

    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    if target == "": return True

    for n in range(len(table)):
        if table[n] == True:        
            for word in words:
                #if the word matches the characters starting at position n
                if n + len(word) <= len(table) and target[n:n + len(word)] == word :
                    table[n + len(word)] = True
                       
    return table[len(target)]

print(canCreate("milestone",["mil","one","tone","est"]))   
print(canCreate("autonomous",["nom","mous","aut","o","mo"]))   
print(canCreate("careless",["ca","carl","cor","car","mo","s","ele"]))   
print(canCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   
print(canCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"])) 