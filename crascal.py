n = 7
D = [[0,  9.5,  8.6,  10.8,  8.9,  7.1,  14],
[9.5,	0,	14.6,	8.6,	17, 8.9,	6.4],
[8.6,	14.6,	0,	9.5,	15,	16.6,	20.6],
[10.8,	8.6,	9.5,	0,	19.7,	15,	14.9],
[8.9,	17,	 15,	19.7,	0,  9.5,	19.3],
[7.1,	8.9,	16.6,	15,	9.5,	0,	9.8],
[14,	6.4,20.6,	14.9,	19.3,	9.8,	0]]

def f1(D,n):
    Res, col, k, L = [], [], 0, 0
    for i in range(n):
        col.append(i)
    while k<n-1:
        dmin = 30000
        for i1 in range(0,n):
            for j1 in range(i1+1,n):
                if D[i1][j1] < dmin and col[i1]!=col[j1]:
                    dmin = D[i1][j1]
                    i = i1
                    j = j1
        k = k+1
        L = L + dmin
        Res.append([i+1,j+1])
        j1 = col[j]
        for m in range(0,n):
            if col[m] == j1:
                col[m] = col[i]
    print(Res)

def f2(D,n):
    Res, col, k, L = [], [], 0, 0
    for i in range(n):
        col.append(i)
    while k<n-1:
        dmin = 30000
        for i1 in range(0,n-1):
            for j1 in range(i1+1,n):
                if D[i1][j1] < dmin and col[i1]!=col[j1]:
                    dmin = D[i1][j1]
                    i = i1
                    j = j1
        k += 1
        L += dmin
        Res.append([i,j])
        j1 = col[j]
        for m in range(0,n):
            if col[m] == j1:
                col[m] = col[i]
    print(L)

f1(D,n)
f2(D,n)