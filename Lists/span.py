arr = eval(input("Enter a list of integers: "))
n = len(arr)
max = arr[0]
min = arr[0]
for i in range(n):
    max = arr[i] if max < arr[i] else max
    min = arr[i] if min > arr[i] else min
print("Span of list: ", max - min)
