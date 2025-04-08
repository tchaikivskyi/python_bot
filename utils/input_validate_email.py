import re


def input_validate_email():
    while True:
        email = input("Enter your email address: ")
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(email_regex, email):
            print("Valid email!")
            return email
        else:
            print("Invalid email format. Please try again.")
