n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
b = 0

for c in range(len(a)):
    if a[c] == b:
        b += 1
    else:
        print(b)
