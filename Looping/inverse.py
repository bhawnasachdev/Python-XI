# Python Program to invert a given number
num = int(input("Enter number to be inversed: "))
num2 = num

# counting number of digits in the input number
n = 0
while num2 > 0:
    num2 //= 10
    n += 1
curr = n

# creating inverse of number
res = 0
while num > 0:
    digit = num % 10
    res += curr * pow(10, n - digit)
    num //= 10
    curr -= 1
print("Inverse: ", res)
