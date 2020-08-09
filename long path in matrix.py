"""

Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that all cells

along the path are in increasing order with a difference of 1. We can move in 4 directions from a given cell (i, j), 

i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have a difference of 1.

Input:
Firstline indicates matrix size N
Next N lines gives rows of matrix

Output:
print the length of longest path

Example:

Input:
3
1 2 9
5 3 8
4 6 7

Output:
4

Exaplanation:
The longest path is 6-7-8-9.

"""
def findLongestFromACell(i, j, mat, dp):
    if (i<0 or i>= n or j<0 or j>= len(mat)): 
        return 0
    
    if (dp[i][j] != -1):  
        return dp[i][j]
    
    x, y, z, w = -1, -1, -1, -1
    
    if (j<len(mat)-1 and ((mat[i][j] +1) == mat[i][j + 1])): 
        x = 1 + findLongestFromACell(i, j + 1, mat, dp) 
  
    if (j>0 and (mat[i][j] +1 == mat[i][j-1])):  
        y = 1 + findLongestFromACell(i, j-1, mat, dp) 
  
    if (i>0 and (mat[i][j] +1 == mat[i-1][j])): 
        z = 1 + findLongestFromACell(i-1, j, mat, dp) 
  
    if (i<len(mat)-1 and (mat[i][j] +1 == mat[i + 1][j])): 
        w = 1 + findLongestFromACell(i + 1, j, mat, dp)
        
    dp[i][j] = max(x, max(y, max(z, max(w, 1)))) 
    return dp[i][j]

def findLongestOverAll(mat):
    n=len(mat)
    result = 1
    dp =[[-1 for i in range(n)]for i in range(n)]  
    for i in range(n): 
        for j in range(n): 
            if (dp[i][j] == -1): 
                findLongestFromACell(i, j, mat, dp) 
            result = max(result, dp[i][j]);  
    return result 
n=int(input())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
print(findLongestOverAll(mat))
