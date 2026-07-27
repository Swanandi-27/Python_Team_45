print("\n--- Palindrome Checker ---")

text = input("Enter a word or number: ").strip()

cleaned_text = text.lower()

# Check if the string is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print(f"Result: '{text}' IS a palindrome! \n")
else:
    print(f"Result: '{text}' is NOT a palindrome.\n")
