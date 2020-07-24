"""

A old seller used to carry goods and sell them to make profit.As he became old he cant able carry goods as before.So he decided to carry goods

with limited capacity W.Given the N items weights and their values.your task is to choose the maximum value of products whose sum of weights is 

less than or equal to old man capacity W.

Input:

Firstline indicates number of items N
Second line contains oldman carrying capacity W
Nextline contains array of weights of N items
Nextline contains array of values of N items

Output:
print the maximum value of products

Example1:

Input:

3
50
10 20 30
60 100 120

Output:
220

Input:
1
50
22
30

Output:
30

"""
def solution(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

n,k=map(int,input().split())
weight=list(map(int,input().split()))
val=list(map(int,input().split()))
print(solution(k,weight,val,n))
