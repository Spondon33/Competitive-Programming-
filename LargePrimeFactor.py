t = int(input().strip())
prime = []
if 1 <= t <= 10:
    for i in range(t):
        n = int(input().strip())
        if 10 <= n <= 10**12:
            factors = []
            while n % 2 == 0:
                n //= 2
                factors.append(2)

            i = 3
            while i * i <= n:
                while n % i == 0:
                    n //= i
                    factors.append(i)
                i += 2

            if n > 2:
                factors.append(n)

            LargestFactor = 0
            for factor in factors:
                if factor > LargestFactor:
                    LargestFactor = factor
            prime.append(LargestFactor)

for num in prime:
    print(num)


