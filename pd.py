import random
import string

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
            and not any(password.count(c) > 2 for c in password)
        ):
            return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length < 8:
            print("Password length should be at least 8 characters.")
            return
        password = generate_secure_password(password_length)
        print("Generated Secure Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
