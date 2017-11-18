import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]


balEnquiry = ['WHAT IS MY BALANCE']

while True:
        userInput = input(">>> ")
        if userInput in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
        elif userInput in question:
                random_response = random.choice(responses)
                print(random_response)
        elif userInput.upper() in balEnquiry:
                random_response = 'Please authenticate yourself'
                print(random_response)
        else:
                print("I did not understand what you said")