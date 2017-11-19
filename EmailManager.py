affirmative = ["YES", "YEAH", "GO AHEAD", "SURE", "Y"]
not_affirmative = ["NO", "NAH", "NOPE", "N", "N"]

class EmailManager:

    User = None

    def __init__(self, user):
        #TODO affirmative should also come from api
        self.User = user

    def action(self):
        input = input("Do you wish to update your email? (Y/N)")
        if input in affirmative:
            email = input("Please enter new email")
            self.update_email(email)
        elif input not in not_affirmative:
            print("I did not understand what you said")
            self.action()

    def update_email(self, email):
        self.user.set_email(email)
