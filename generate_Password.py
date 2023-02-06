import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for i in range(length))
    return password

print("Geramos uma senha para você: \n" + generate_password(16))