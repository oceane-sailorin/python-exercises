# replace None value with latest non None value



class Solution:
    def fillTheNones(self,arr):
        valid = 0            
        res = []                 
        for i in arr: 
            if i is not None:    
                res.append(i)
                valid = i
            else:
                res.append(valid)
        return res


s1 = Solution()

print(s1.fillTheNones([1,None,None,2,3,None,4,None]))
print(s1.fillTheNones([None,10,None,None,222,None,None,43,None]))