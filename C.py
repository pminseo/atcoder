n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = []

X = A.copy()
for b in B:
    X.append(b)
X.sort(reverse=True)
d = 0
ans = []
for i in range(2*n - 1):
    if len(ans) == n:
        print("Yes")
        d = 1
        break
    if abs(X[i] - X[i+1]) <= k:
        ans.append(X[i])
    else:
        ans = []
        continue

if d == 0:
    print("No")
    
    
##################
# n = 4, k = 90
# A = 1 1 1 100
# B = 1 2 3 100
# X = 1 1 1 1
# 
# Yes 근데 답은 No임
#
# Xi = Ai or Xi = Bi, for every i
# |Xi - Xi+1| <= k, for every i