#strong password must be atleast 8 characters or longer and must've an uppercase, a lowercase and a digit in them
#Weak password example : abc123
#Strong password example: Abc@123321 



import re

def upper(password):
    if re.search('[A-Z]', password): #atleast one uppercase character
        return True
    return False

def lower(password):
    if re.search('[a-z]', password): #atleast one lowercase character
        return True
    return False

def digit(password):
    if re.search('[0-9]', password): #atleast one digit
        return True
    return False

def special(password):
    if re.search('[@$*-]', password): #atleast one digit
        return True
    return False


def password_check():
    password = input("Enter password : ")
        #atleast 8 character long
    if len(password) >= 8 and upper(password) and lower(password) and digit(password) and special(password):
        print("Strong Password")
    else:
        print("Weak Password")

password_check()
