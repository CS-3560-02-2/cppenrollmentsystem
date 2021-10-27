class _User:
    """This is an abstract base class for Users

    Attributes:
        name: A string representing the User's name
        email_address: A string representing the email address
        phone_number: A string representing the phone number
        address: A string representing the home address
    """
    def __init__(self, name, email_address, phone_number, address) -> None:
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
        self.address = address
    