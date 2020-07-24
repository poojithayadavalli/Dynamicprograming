"""

Given two numbers N and K. Find the number of ways to represent N as the sum of K Fibonacci numbers.

Examples:

Input :

12 1 

Output : 

0

Input :

13 3

Output :

2

Explanation :
2 + 3 + 8, 3 + 5 + 5.

"""
 
def fibonacci(n,fib): 
    fib[0] = 1
    fib[1] = 2
    for i in range(2,n):  
        fib[i] = fib[i - 1] + fib[i - 2] 
def rec(x, y, last,fib):
    if y == 0:  
        if x == 0:  
            return 1
        return 0
      
    Sum, i = 0, last 
    while i >= 0 and fib[i] * y >= x:  
        if fib[i] > x: 
            i -= 1
            continue
        Sum += rec(x - fib[i], y - 1, i,fib)  
        i -= 1
          
    return Sum

n,k=map(int,input().split())
fib = [0] * n
fibonacci(n,fib)
print(rec(n,k,n-1,fib))

