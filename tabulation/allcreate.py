# write function allcreate(target,words) with arguments target string and list of strings
# function should return all  possible solutions to create target with words
# one word can be used several times
# use of tabulation

def allCreate(target, words):

   
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    if target == "": return [[]]
    print(table)

    updated = []
   
    for n in range(len(table)):
        for word in words:
            print("word")
            print(word)
            #if the word matches the characters starting at position n
            if n + len(word) <= len(table) and target[n:n + len(word)] == word :
                print("tablen")
                print(table[n])
                updated= []
                updated.append(table[n])
                print("updated1")
                print(updated)
                updated2 = updated.append(word)
                print("updated2")
                print(updated)
                updated3 = table[n + len(word)].extend(updated)
                print("updated3")
                print(table[n + len(word)])
                #updated = [[suf.insert(0,word) for suf in table[n]]]
                #updated = list(map(table[n]))
                
              
    
    return table[len(target)]


print(allCreate("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
#print(allCreate("",["mil","one","tone","est"]))   
#print(allCreate("milestone",["mil","one","tone","est"]))     
#print(allCreate("autonomous",["nom","mous","aut","o","mo","no","us","m"]))   
#print(allCreate("careless",["ca","carl","cor","car","mo","s","ele"]))      
#print(allCreate("milestone",["mile","one","tone","est"]))  
#print(allCreate("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["aa","aaa","a","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaaaaaa"]))   