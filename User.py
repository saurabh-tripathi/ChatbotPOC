import json

class User:

    Name = None
    Account = None
    Phone = None
    Email = None
    Address = None

    def __init__(self):
        #TODO add write functionality
        with open('UserDetails.json') as file:
            data = json.load(file)
        self.Name = data["Name"]
        self.Address = data["Address"]
        self.Account = data["Account"]
        self.Phone = data["Phone Number"]
        self.Email = data["Email"]

    def get_all_details(self):
        return {
            'Name': self.Name,
            'Account': self.Account,
            'Phone': self.Phone,
            'Email': self.Email,
            'Address': self.Address
        }

    def get_phone(self):
        return self.Phone

    def set_phone(self, phone):
        self.Phone = phone

    def get_email(self):
        return self.Email

    def set_email(self, email):
        self.Email = email

    def get_address(self):
        return self.Address

    def set_address(self, address):
        self.Address = address


