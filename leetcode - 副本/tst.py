s = [i for i in range(0, 100, 2)]
print(s)
num = 21
i, j = 0, len(s)
while i < j:
    m = (i + j) // 2
    if s[m] < num:
        i = m + 1
    else:
        j = m
    print(m, i, j, s[m])
