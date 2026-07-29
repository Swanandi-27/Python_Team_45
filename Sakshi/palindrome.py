num = int(input("Enter a number: "))
# Store the original number
original = num
# Variable to store the reversed number
reverse = 0
# Reverse the number
while num > 0:
    digit = num % 10          # Get the last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove the last digit
# Check if the original number and reversed number are the same
if original == reverse:
    print(original, "is a palindrome number.")
else:
    print(original, "is not a palindrome number.")