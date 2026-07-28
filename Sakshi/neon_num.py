num = int(input("Enter a number: "))

square = num * num
sum = 0

while square > 0:
    digit = square % 1
    sum = sum + digit
    square = square // 10

if sum == num:
    print("Neon Number")
else:
    print("Not a Neon Number")
