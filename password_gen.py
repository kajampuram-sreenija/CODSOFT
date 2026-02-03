input("Press Enter to close...")
import secrets
import string

print("--- Secure Password Generator ---")
try:
    length = int(input("Enter password length: "))
    if length <= 0:
        raise ValueError("Length must be positive.")

    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(chars) for _ in range(length))
    print(f"Your Password: {password}")
    print("Success! Task complete.")
except Exception as e:
    print(f"Error: {e}")

input("Press Enter to close...")
