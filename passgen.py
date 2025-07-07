import random
import string

print(" Password Generator")


length = int(input("Enter password length: "))


characters = string.ascii_letters + string.digits + string.punctuation


password = ""
for i in range(length):
    password += random.choice(characters)

# Show result
print("Your password is:", password)
