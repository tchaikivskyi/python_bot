from datetime import datetime
import re
from utils.colored_text import colored_input, colored_text


def input_validate_br(message="Enter your birthday in DD.MM.YYYY format: "):
    while True:
        try:
            value = colored_input(message, "cyan")
            if value and isinstance(value, str):
                parse_date = datetime.strptime(value, "%d.%m.%Y").date()
                return parse_date
            else:
                raise ValueError(
                    "Value must be a non-empty string in DD.MM.YYYY format."
                )
        except ValueError:

            colored_text("The date you entered is invalid. Please try again.", "red")



def input_validate_email(message="Enter your email address: "):
    while True:
        email = colored_input(message, "cyan")
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(email_regex, email):
            return email
        else:
            colored_text("Invalid email format. Please try again.", "red")
      
            
            
def input_validate_phone(message="Enter your phone number: "):
    while True:
        try:
            value = colored_input(message, "cyan")
            if value.isdigit() and len(value) == 10:
                return value
            else:
                raise ValueError("Phone number must contain exactly 10 digits.")
        except ValueError as e:
            colored_text(f"The Phone you entered is invalid: {e} Please try again.", "red")