#find all prime numbers less than given number

class Solution:
    def findPrimeNumbers(self, num):
       
        res = []
        for n in range(num):
            #a prime number is > 1
            if n > 1: 
                for i in range(2, n):
                    # if % == 0, number can be divided by lower number
                    if (n % i) == 0: 
                        break
                else:
                    res.append(n)
        return res


    """numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)"""



s1 = Solution()

print(s1.findPrimeNumbers(5))
print(s1.findPrimeNumbers(43))