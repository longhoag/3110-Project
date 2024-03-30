import sys

def pre_check(input):

    #clean input
    input = input.strip()

    #empty input string handling 
    if not input:
        return False

def check_decimal(input):
    pre_check(input)
    
    #check positive, negative sign, shift target to the digits 
    if input[0] in ('+', '-'):
        input = input[1:]

    #check each digit
    for digit in input:
        if digit not in '0123456789':
            return False
        
    return True


def check_octal(input):
    pre_check(input)
    
    # octal integer format: 0o177, 0O234, ...
    if input[0] == '0':
        if len(input) > 2 and input[1] in 'oO':
            input = input[2:]
    else:
        return False

    #check each digit
    for digit in input:
        if digit not in '01234567':
            return False
    
    return True

def check_hexa(input):
    pre_check(input)

    # hexadecimal format: 0xdeadbeef
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


#testing floating point literals
def check_fpl(input):
    pre_check(input)

    
# main
user_input = input("Enter a number: ")
if check_decimal(user_input):
    print("The input is  a decimal integer!")

elif check_octal(user_input):
    print("The input is  an octal integer!")
   
elif check_hexa(user_input):
    print("The input is  a hexadecimal integer!")

else:
    print("The input is not valid!")


print(user_input)
