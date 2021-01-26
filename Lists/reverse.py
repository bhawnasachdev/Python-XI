arr = eval(input("Enter a list to be reversed: "))
low = 0
high = len(arr) - 1
while low < high:
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp
    low += 1
    high -= 1
print("Reverse of list: ", arr)