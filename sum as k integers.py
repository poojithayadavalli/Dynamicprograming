"""

Given N and K. The task is to find out how many different ways are there to represent N as the sum of K non-zero integers.

Input:

First line contains N
nextline contains K

Output:
print the number of ways

Example:

Input:
5
3

Output:
6

Explanation:
The possible combinations of integers are:
( 1, 1, 3 )
( 1, 3, 1 )
( 3, 1, 1 )
( 1, 2, 2 )
( 2, 2, 1 )
( 2, 1, 2 )

Example 2:

Input: 
10
4

Output:
84

"""
def binomialCoeff(n, k): 
    C = [[0 for i in range(k+1)]for i in range(n+1)]
    for i in range(0,n+1,1): 
        for j in range(0,min(i, k)+1,1): 
            if (j == 0 or j == i): 
                C[i][j] = 1
            else: 
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j] 
  
    return C[n][k]
n=int(input())
k=int(input())
print(binomialCoeff(n-1,k-1))

