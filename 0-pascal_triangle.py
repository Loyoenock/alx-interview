def pascal_triangle(n):
    p = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    p[i].append(1)
                else:
                    p[i].append(p[i-1][j] + p[i-1][j-1])
            elif j == i:
                p[i].append(1)
    return p

n = 5
print(pascal_triangle(n))
