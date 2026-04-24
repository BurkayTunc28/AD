#Limit entfernen
import sys
sys.setrecursionlimit(10**8)

#Wie viele Testabläufe
testCount = int(input())

#Factorial Formel z.B 3! = 3x2x1 = 6. n ist die Zahl für den Test
def factorial(n):

    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)

for i in range(testCount):

    n = int(input())

    print(factorial(n))
