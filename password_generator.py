import string
import random
characters = list(string.ascii_letters+string.digits+"$&^%#@!*")


password_length  = int(input("password_length"))


def gen(password_length):
    random.shuffle(characters)
    passwords = []
    for i in range(password_length):
        passwords.append(characters[i])
    
    random.shuffle(passwords)
    password = "".join(passwords)
    return password


print(gen(password_length))