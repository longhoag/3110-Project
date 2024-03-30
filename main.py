import sys

def pre_check(input):
    #clean input
    input = input.strip()

    #empty input exception
    if not input:
        return False

def check_decinteger(input):
    pre_check(input)
    
    #check sign (if N/A)
    if input[0] in ('+', '-'):
        input = input[1:]

    #check each number
    for digit in input:
        if digit not in '0123456789':
            return False
        
    return True


def check_octal(input):
    pre_check(input)
    
    if input[0] == '0':
        if len(input) > 2 and input[1] in 'oO':
            input = input[2:]
    else:
        return False

    #check digit
    for digit in input:
        if digit not in '01234567':
            return False
    
    return True

def check_hexa(input):
    pre_check(input)

    if input[0] == '0':
        if len(input) > 2 and input[1] in 'xX':
            input = input[2:]
    else:
        return False

    #check digit
    for digit in input:
        if digit not in '0123456789abcdefABCDEF':
            return False
    
    return True


user_input = input("Enter a number: ")
if check_decinteger(user_input):
    print("Is an integer!")

elif check_octal(user_input):
    print("Is an octal")
   
elif check_hexa(user_input):
    print("Is a hexadecimal")

else:
    print("Is not valid!")


print(user_input)
