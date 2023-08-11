import random
import string

def generate_hard_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password

password_length = int(input("Enter the desired password length: "))
password = generate_hard_password(password_length)
print("Generated Strong Password:", password)
