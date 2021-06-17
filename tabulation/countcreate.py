# write function countcreate(target,words) with arguments target string and list of strings
# function should return number of possible solutuons to create target with words
# one word can be used several times
# use of tabulation

def countCreate(target, words):

    
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    if target == "": return 1

    total = 0

    for n in range(len(table)):
        if table[n] > 0:  
            for word in words:
                #if the word matches the characters starting at position n
                if n + len(word) <= len(table) and target[n:n + len(word)] == word :
                    table[n + len(word)] += table[n]
    
    return table[len(target)]
 
print(countCreate("milestone",["mil","one","tone","est"]))  
print(countCreate("autonomous",["nom","mous","aut","o","mo","no","us","m"]))   
print(countCreate("careless",["ca","carl","cor","car","mo","s","ele"]))   
print(countCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   
print(countCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aab","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   