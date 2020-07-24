"""

Raju is learning about fibonacci numbers ,he saw a task and the task is as follows:

Given two numbers M and N, the task is to check if the M-th and N-th Fibonacci numbers perfectly divide each other or not.

Input:

Firstline indicates integer M
nextline indicates integer N

Output:

print Yes or No

Example1:

Input:
3
6

Output: Yes

Explanation:

F(3) = 2, F(6) = 8 and F(6) % F(3) = 0

Example 2:

Input:
2
9

Output:
No
"""
def check(n, m):
    if (n == 2 or m == 2 or
        n % m == 0) : 
        print( "Yes" )
    else : 
        print( "No" ) 
m = int(input())
n=int(input())
check(n, m)
