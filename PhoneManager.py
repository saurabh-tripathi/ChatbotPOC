affirmative = ["YES", "YEAH", "GO AHEAD", "SURE", "Y", "YUP", "YEP"]
not_affirmative = ["NO", "NAH", "NOPE", "N", "N"]

class PhoneManager:

    User = None

    def __init__(self, user):
        self.User = user

    def action(self):
        inp = input("Do you wish to update your phone number? (Y/N)")
        if inp.upper() in affirmative:
            phone = input("Please enter new phone number")
            self.update_phone(phone)
        elif inp.upper() not in not_affirmative:
            print("I did not understand what you said")
            self.action()

    def update_phone(self, phone):
        self.User.set_phone(phone)
