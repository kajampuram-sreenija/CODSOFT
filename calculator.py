def start_calculator():
    print("Welcome to my Simple Calculator!")
    print("--------------------------------")

    # This 'while' loop makes it more human; 
    # it allows the user to try again if they make a mistake.
    while True:
        try:
            # Getting the first number
            val1 = float(input("Enter your first number: "))
            
            # Getting the second number
            val2 = float(input("Enter your second number: "))
            
            print("\nAvailable Operations: + , - , * , /")
            op_choice = input("Which operation would you like to perform? ")

            # Logical decisions
            if op_choice == '+':
                total = val1 + val2
                print(f"Success! {val1} + {val2} = {total}")
            elif op_choice == '-':
                total = val1 - val2
                print(f"Success! {val1} - {val2} = {total}")
            elif op_choice == '*':
                total = val1 * val2
                print(f"Success! {val1} * {val2} = {total}")
            elif op_choice == '/':
                # Handling the division by zero rule
                if val2 != 0:
                    total = val1 / val2
                    print(f"Success! {val1} / {val2} = {total}")
                else:
                    print("Error: You cannot divide a number by zero.")
            else:
                print("Wait, that isn't a valid operation symbol.")

            # Ask if they want to do another calculation
            repeat = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if repeat != 'yes':
                print("Thank you for using my calculator. Goodbye!")
                break

        except ValueError:
            # This catches errors if the user types letters instead of numbers
            print("Invalid input! Please enter numbers only.")

# Run the program
if __name__ == "__main__":
    start_calculator()

