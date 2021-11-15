#questions

#yield keyword
def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index+1]

day = testgen(0)
print(next(day), next(day))

# list to string
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)

#count number of occurrences
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])

#random
import random 
print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10) )

#is number palindrome
num = 1881
print(int(str(num)[::-1])==num)

#program for prime number
a=int(input("Enter number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1

if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")



# Python program to check if the number is an Armstrong number or not 
#sum of cubes of each digit equal number

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
s = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   s+= digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# other Armstrong number
n=int(input("Enter any number: "))
a=list(map(int,str(n)))
print(a)
b=list(map(lambda x:x**3,a))
print(b)

if(int(sum(b))==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")


# is perfect number = sum of all positive divisors
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")   


#check common letters in 2 strings
s1 = input("Enter first string:")
s2 = input("Enter second string:")
a = list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)