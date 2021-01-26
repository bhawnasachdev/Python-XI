a = eval(input("Enter a list: "))
res = {}
for x in a:
    indices = []
    for idx in range(len(a)):
        if a[idx] == x:
            indices.append(idx)
    res[x] = indices
print(res)