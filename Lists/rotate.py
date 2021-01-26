arr = eval(input("Enter a list of numbers: "))
k = int(input("Enter rotation factor: "))
n = len(arr)
k = k % n 
if k < 0:
    k += n
result = []
for i in range(n):
    if i < k:  
        result.append(arr[n + i - k]) 
    else:
        result.append(arr[i - k]) 
print("Rotated list: ", result)