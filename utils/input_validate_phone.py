def input_validate_phone(message="Enter your phone number: "):
    while True:
        try:
            value = input(message)
            if value.isdigit() and len(value) == 10:
                return value
            else:
                raise ValueError("Phone number must contain exactly 10 digits.")
        except ValueError as e:
            print(f"The Phone you entered is invalid: {e} Please try again.")
