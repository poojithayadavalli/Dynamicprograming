"""

Given n fruits, each one can remain single or can be paired up with some other fruit. 

Each fruit can be paired only once. Find out the total number of ways in which fruits can remain single or can be paired up.

Input:

Firstline indicates number of fruits N

Output:

print the total possible ways

Example1:

Input:
3

output:
4

Example 2:

Input:
4

Output:

10

"""
def countFruitsPairings(n): 
  
    dp = [0 for i in range(n + 1)]
    for i in range(n + 1): 
  
        if(i <= 2): 
            dp[i] = i 
        else: 
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2] 
  
    return dp[n] 
 n=int(input())
 print(countFruitsPairings(n))
