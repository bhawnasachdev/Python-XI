arr = eval(input("Enter a nested list of numbers: "))
n = len(arr)
m = len(arr[0])
res = []
for i in range(n):
    for j in range(m):
        sum = 0
        num = arr[i][j]
        while(num > 0):
            sum += num % 10
            num //= 10
        res.append(sum)
print(res)