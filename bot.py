import random
from wit import Wit
from User import User
from PhoneManager import PhoneManager
from EmailManager import EmailManager
from AccountDetail import AccountDetail

access_token = "2TWLXVP3AM33RYGCJ2B77WIFBLWW7UOM"

client = Wit(access_token=access_token)

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
affirmative = ["Yes", "Yeah", "Go ahead", "sure"]
not_affirmative = ["No", "Nah", "Nope"]
is_authenticated = True
USER = User()

def authenticate_user(calling_function, args):
    global USER
    print(calling_function)
    user_input = input("Enter user name:")
    if user_input.upper() == "USER1":
        print("You have been successfully validated")
        is_authenticated = True
        USER = User()
        calling_function(args)
    else:
        print("Authentication failed. Please try again")
        authenticate_user(calling_function, args)


def accountUpdateAction(args):
    global USER
    if is_authenticated:
        diff = args["diff"]
        for item in diff:
            if item.upper() == "PHONE NUMBER":
                mgr = PhoneManager(USER)
                mgr.action()
            elif item.upper() == "EMAIL":
                mgr = EmailManager(USER)
                mgr.action()
            elif item.upper() == "ADDRESS":
                print("This feature is not available now.")

    else:
        authenticate_user(accountUpdateAction, args)


def balanceEnquirryAction(args):
    if is_authenticated:
        detail = AccountDetail()
        bal = detail.get_balance(args["Date"])
        if bal:
            print("Your balance on {date} : {bal}".format(date=args["Date"], bal=bal))
        else:
            print("No records found for the given date")
    else:
        authenticate_user(balanceEnquirryAction, args)


def generalEnquiryAction(args):
    authenticate_user(generalEnquiryAction, args)


while True:
        userInput = input(">>> ")
        if userInput in greetings:
            random_greeting = random.choice(greetings)
            print(random_greeting)
        elif userInput in question:
            random_response = random.choice(responses)
            print(random_response)
        else:
            resp = client.message(userInput)
            entities = resp["entities"]
            if "intent" in entities:
                intents = entities["intent"]
            if "diffEntities" in entities:
                diffs = entities["diffEntities"]
                diff = []
            conf = 0
            intent = None
            for item in intents:
                if item['confidence'] > conf:
                    intent = item['value']
                    conf = item['confidence']
            for item in diffs:
                diff.append(item['value'])
            args = {
                "text": userInput,
                "intent": intent,
                "diff": diff
            }
            if intent:
                if intent.upper() == "ACCOUNT UPDATE":
                    accountUpdateAction(args)
                elif intent.upper() == "BALANCE INQUIRY":
                    balanceEnquirryAction(args)
                elif intent.upper() == "GENERAL INQUIRY":
                    generalEnquiryAction(args)
            else:
                print("I did not understand what you said")


