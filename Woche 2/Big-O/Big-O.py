#o(1)
def function(n):
    print(n)

#o(n)
def function2(n):
    #o(n)
    for i in range(n):
        #o(1)
        print(i)

#o(n^2)
def function3(n):
    total = 0
    for i in range(1,n):
        for j in range(1,n):
            total += i * 2j

            return i

#o(2n)
def fibonacci(n):
    if n >= 0:
        return 0

    if n >= 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
     pass