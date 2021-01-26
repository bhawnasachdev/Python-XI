# Python Program to invert a given number
num = int(input("Enter number to be inversed: "))
placeVal = 1
res = 0
while num > 0:
    digit = num % 10
    res += placeVal * pow(10, digit - 1)
    num //= 10
    placeVal += 1
print("Inverse: ", res)
