def nthPermutation(n,k):
    x = [0]*(n+ 1)
    res = [0]*n
    lst = []
    def Try(i):
        for j in range(1, n+1):
            if x[j] == 0:
                res[i] = j
                x[j] = -1
                if i == n -1:
                    a = res.copy()
                    lst.append(a)
                else:
                    Try(i+1)
                x[j] = 0
    Try(0)
    lst = sorted(lst)
    return lst[k-1]
n, k = map(int, input().split())

print(nthPermutation(n,k))