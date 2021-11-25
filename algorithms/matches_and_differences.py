#Given two sentences, return an array with the words in common and the words that are different


class Solution:
    def matchesAndDifferences(self, string1, string2):
        #change strings into sets
        set1 = set(string1.split())
        set2 = set(string2.split())
        
        #return sorted array with words in common and sorted array with words that are not
        #intersection & and symmetric difference ^ 
        return sorted(list(set1&set2)) ,sorted(list(set1^set2))

s1 = Solution()

print(s1.matchesAndDifferences("who do you think you are","whoever think you should be there"))
print(s1.matchesAndDifferences("remind me if the numbers are correct","Correct this problem for me"))