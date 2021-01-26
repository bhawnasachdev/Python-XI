num = int(input("Enter a number: "))
r = int(input("Enter rotation factor:"))
digits = 0
n = num
while num > 0:
    digits += 1
    num //= 10
r = (r % digits + digits) % digits
mul = 1
div = 1
for i in range(1, digits + 1):
    if i <= r:
        div *= 10
    else:
        mul *= 10
a = n % div
b = n // div
res = a * mul + b
print("Rotated number: ", res)