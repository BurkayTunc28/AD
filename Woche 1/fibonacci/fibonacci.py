import sys
sys.setrecursionlimit(10**8)

memo = {}

testCount = int(input())

def fib(n):

    #In Memo wird das Resultat
    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = 0
        return 0

    if n == 1:
        memo[1] = 1
        return 1

    val = fib(n-1) + fib(n-2)

    memo[n] = val

    return val

for i in range(testCount):

    n = int(input())

    print(fib(n))