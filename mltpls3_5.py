import sys

t = int(input().strip())
if 1 <= t <= 10**5:
    results = []
    for i in range(t):
        n = int(input().strip())
        if 1 <= n <= 10**9:
            result = 0
            for j in range(1, n):
                if j % 3 == 0 or j % 5 == 0:
                    result += j
            results.append(result)
        else:
            sys.exit('Invalid input')
    for result in results:
        print(result)
else:
    sys.exit('Invalid input')
