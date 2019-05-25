def solution(x):
    a, b = 1, 1
    for i in range(x):
        a, b = b, a + b
    return a


n = int(input("Choose fibonacci n number to display: "))
print("Fibonacci n number equals: {}".format(solution(n-1)))
