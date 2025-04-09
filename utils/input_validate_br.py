from datetime import datetime


def input_validate_br(message="Enter your birthday in DD.MM.YYYY format: "):
    while True:
        try:
            value = input(message)
            if value and isinstance(value, str):
                parse_date = datetime.strptime(value, "%d.%m.%Y").date()
                return parse_date
            else:
                raise ValueError(
                    "Value must be a non-empty string in DD.MM.YYYY format."
                )
        except ValueError:

            print("The date you entered is invalid. Please try again.")
