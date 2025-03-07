import sys

t = int(input().strip())
if 1 <= t <= 10**5:
    for i in range(t):
        n = int(input().strip())
        if 10 <= n <= 4*10**16:
            a = 1
            b = 2
            fib_sum = 0
            for _ in range(1, n):
                if a > n:
                    break
                if a % 2 == 0:
                    fib_sum += a
                temp = a
                a = b
                b = temp + b
            print(fib_sum)
        else:
            sys.exit('Invalid input')
else:
    sys.exit('Invalid input')
