arr = eval(input("Enter a list of numbers: "))
size = len(arr)
inverse = [0] * size
for i in range(size):
    inverse[arr[i] - 1] = i + 1
print("Inverse of list: ", inverse)