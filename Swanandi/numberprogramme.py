print("Number Programming")
print("\n1.Palindrome No\n2.Armstrong No\n3.Neon No\n4.Exit")
choice=int(input("enter your  choice: "))
match choice:
    case 1:
        print("\n--- Palindrome Checker ---")

        text = input("Enter a word or number: ").strip()
        
        cleaned_text = text.lower()
        
        # Check if the string is equal to its reverse
        if cleaned_text == cleaned_text[::-1]:
            print(f"Result: '{text}' IS a palindrome! \n")
        else:
            print(f"Result: '{text}' is NOT a palindrome.\n")
    case 2:
        print("\n--- Armstrong checker---")
        num=int(input("Enter a number: "))
        temp=num
        sum=0

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** len(str(num)) 
            temp = temp//10

        if sum == num:
            print(num, "is an Armstrong number")
        else:
            print(num, "is not an Armstrong number")

    case 3:
        pass
    case 4:
        exit()
    case _:
        print("Invalid choice")