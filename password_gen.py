import random
import string

print("--- Task 3: Password Generator ---")
length = int(input("Enter how long you want your password: "))
# This mixes letters, numbers, and symbols
data = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(data) for i in range(length))
print(f"Your strong password is: {password}")
