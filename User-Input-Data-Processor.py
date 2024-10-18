# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

user_first = input("Enter first: ")
user_last = input("Enter your last name: ")

def length_check():
        if len(user_first) >= 2:
            if len(user_last) >= 2:
                print(len(user_first + user_last))
            else:
                print("Error: Both first and last name inputs must be at least 2 characters long.")          
        else:
            print("Error: Both first and last name inputs must be at least 2 characters long.")
length_check()