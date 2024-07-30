import re


pattern_for_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = input("Please enter your email: ")

pattern = re.compile(r'^(?=.*[$%#@]).{8,}$')
password = input("Please enter your password: ")
a = pattern.search(password)


def email_and_password_checker(email=None, password=None):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        print("The email is valid.\n")
    else:
        print("The email is invalid")

    if re.match(r'^(?=.*[$%#@]).{8,}$', password):
        print("Password is valid.\n ")
    else:
        print("Password does not meet the criteria:\n -at least 8 characters\n -symbols: $%#@")
    return ""


print(email_and_password_checker("casian@casian.co.m", "dfsdfskdfns#"))



