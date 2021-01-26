a = eval(input("Enter a list: "))
res = {x: [idx for idx in range(len(a)) if a[idx] == x] for x in a}
print(res)