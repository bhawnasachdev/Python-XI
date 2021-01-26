arr = eval(input())
maximum = max(arr)
n = len(arr)
for i in range(maximum, 0, -1):
    for j in range(n):
        if arr[j] >= i:
            print("*", end = "\t")
        else:
            print(end = "\t")
    print()