a = eval(input("Enter a list of numbers: "))
b = eval(input("Enter another list of numbers: "))

len_a = len(a)
len_b = len(b)
max_len = len_a if len_a > len_b else len_b
result = []
i = 0
while i < max_len:
    if i < len_a and i < len_b:
        result.append(a[i] + b[i])
    elif i < len_a:
        result.append(a[i])
    else:
        result.append(b[i])
    i += 1

print("Sum of lists: ", result)
