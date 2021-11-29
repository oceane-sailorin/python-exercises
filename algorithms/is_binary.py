#is binary

num = int(input("please enter a number : "))
while(num > 0):
    j = num % 10
    print(j)
    if j != 0 and j != 1:
        print("number is not binary")
        break
    num = num//10
    print(num)
    if num == 0:
        print("number is binary") 