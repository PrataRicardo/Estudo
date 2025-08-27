NC = int(input())

for i in range(1, NC + 1):
    n, k = [int(x) for x in input().split(' ')]

    result = 0
    for j in range(1, n + 1):
        result = (result + k) % j
    print(f"Case {i}: {result + 1}")