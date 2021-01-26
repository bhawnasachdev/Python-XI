num = int(input("Enter a number: "))
digit = int(input("Enter digit to find: "))
count = 0
while num > 0:
    if num%10 == digit:
        count += 1
    num //= 10
print("Frequency of digit: ", count)