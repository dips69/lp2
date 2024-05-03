#EnterpriseChatbot
#TIME COMPLEXITY = O(n) where n is the len of string.
# .Develop an elementary chatbot for any suitable cutomer interaction application
responses = {
    "hi": "Hello, welcome to Enterprise Bot! How can I assist you today?",
    "services": "We offer the following services:\n- IT Support\n- Software Development\n- Cloud Computing\n- Data Analytics\nWhich service are you interested in?",
    "it support": "Great, let me transfer you to our IT support team.",
    "software development": "Great, let me transfer you to our software development team.",
    "cloud computing": "Great, let me transfer you to our cloud computing team.",
    "data analytics": "Great, let me transfer you to our data analytics team.",
    "default": "I'm sorry, I didn't understand. Can you please rephrase?"
}

def get_response(user_input):
    user_input = user_input.lower()
    
    if "it support" in user_input:
        return responses["it support"]
    elif "software development" in user_input:
        return responses["software development"]
    elif "cloud computing" in user_input:
        return responses["cloud computing"]
    elif "data analytics" in user_input:
        return responses["data analytics"]
    elif "services" in user_input:
        return responses["services"]
    elif "hi" in user_input:
        return responses["hi"]
    elif "bye" in user_input:
        return "Thank you for contacting Enterprise Bot. Have a nice day!"
    else:
        return responses["default"]

print('Bot: ', "Hello, welcome to Enterprise Bot! How can I assist you today?")
while True:
    user_input = input("You: ")
    if "bye" in user_input:
        print('Bot: ', get_response(user_input))
        break
    else:
        print('Bot: ', get_response(user_input))
        print()




# def greet(bot_name, birth_year):
#     print("Hello! My name is {0}.".format(bot_name))
#     print("I was created in {0}.".format(birth_year))

# def remind_name():
#     print("Please remind me your name:")
#     name = input()
#     print("What a great name you have, {0}!".format(name))

# def guess_age():
#     print("Let me guess your age.")
#     print('Enter remainders of dividing your age by 3, 5, and 7:')
#     rem3 = int(input())
#     rem5 = int(input())
#     rem7 = int(input())
#     age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
#     print("Your age is {0}; That's a good time to start programming!".format(age))

# def count():
#     print('Now I will prove to you that I can count to any number you want.')
#     num = int(input())
#     counter = 0
#     while counter <= num:
#         print("{0}!".format(counter))
#         counter += 1

# def test():
#     print("Let's go and test your programming knowledge.")
#     print("Why do we use methods?")
#     print("1. To repeat the statement multiple times.")
#     print("2. To decompose a program into several small subroutines.")
#     print("3. To determine the execution time of a program.")
#     print("4. To interrupt the execution of a program.")
#     answer = 2
#     guess = int(input())
#     while guess != answer:
#         print("Please, try again.")
#         guess = int(input())
#     print('Completed, have a nice day!')

# def end():
#     print('Congratulations, have a nice day!')

# greet("Sbot", "2024")
# remind_name()
# guess_age()
# count()
# test()
# end()
