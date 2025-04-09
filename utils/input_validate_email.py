import re


def input_validate_email(message="Enter your email address: "):
    while True:
        email = input(message)
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(email_regex, email):
            return email
        else:
            print("Invalid email format. Please try again.")
