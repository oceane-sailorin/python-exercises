# write function fibo(n) using iteration
# take n number as an argument
# return nth fibonacci number
# fibo(n) : 1, 1, 2, 3, 5, 8, 13,...


def fibo(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(len(table)):
        if (i+1) < len(table) : table[i+1] += table[i]
        if (i+2) < len(table) : table[i+2] += table[i]

    return table[n]

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(fibonacci(6))    
print(fibonacci(8))   
print(fibonacci(50))   

print(fibo(6))
print(fibo(8))
print(fibo(50))