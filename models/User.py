if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

from data.db import DB


class _User:
    """This is an abstract base class for Users

    Attributes:
        first_name: A string representing the User's first name
        last_name: A string representing the User's last name
        street: A string representing the User's street
        state: A string representing the User's state
        zip_code: A string representing the User's zip code
        email: A string representing the email address
        phone_number: A string representing the phone number

    Methods:
        getFirst_name: Returns User's first name
        getLast_name: Returns User's last name
        getStreet: Returns User's street
        getState: Returns User's state
        getZip_code: Returns User's zip code
        getPhone_number: Returns User's phone number
        getEmail: Returns User's email

        setFirst_name: Sets User's first name to a new one
        setLast_name: Sets User's last name to a new one
        setStreet: Sets User's street to a new one
        setState: Sets User's state to a new one
        setZip_code: Sets User's zip code to a new one
        setPhone_number: Sets User's phone number to a new one
        setEmail:  Sets User's email to a new one
    """

    def __init__(
        self, first_name, last_name, street, city, state, zip_code, phone_number, email
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def getFirst_name(self):
        return self.first_name

    def setFirst_name(self, first):
        self.first_name = first

    def getLast_name(self):
        return self.last_name

    def setLast_name(self, last):
        self.last_name = last

    def getStreet(self):
        return self.street

    def setStreet(self, streetName):
        self.street = streetName

    def getState(self):
        return self.state

    def setState(self, stateName):
        self.state = stateName

    def getZip_code(self):
        return self.zip_code

    def setZip_code(self, zip):
        self.zip_code = zip

    def getPhone_number(self):
        return self.phone_number

    def setPhone_number(self, number):
        self.phone_number = number

    def getEmail(self):
        return self.email

    def setEmail(self, emailAddress):
        self.email = emailAddress
