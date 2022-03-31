N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

if len(A) > len(C):
    A, C = C, A
a = A[0]
j=0
ans = []
for i in range(len(C)-len(A)+1):
    n = C[i] / A[0]
    D = [a*n for a in A]
    for i in range(len(A)):
        C[i+j] = C[i+j] - D[i]
    j+=1
    ans.append(int(n))


print(ans)