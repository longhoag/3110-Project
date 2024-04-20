#this is optional to handle exception, but removeable
def pre_check(input):

    #clean input
    input = input.strip()

    #empty input string handling
    if not input:
        return False

def check_decimal(input):
    pre_check(input)

    # _ would not be the last digit
    if input[len(input) - 1] in '_':
        return False
    # _ would not be next to together
    for i, digit in enumerate(input):
        if digit in ('_'):
            if input[i - 1] in '_' or input[i + 1] in '_':
                return False
    
    #note that leading zeros in a non-zero decimal number are not allowed: 001, 0001 (from docs.py)
    if input[0] == '0':
        #checking from the next digit
        input = input[1:]
        for digit in input:
            if digit not in '0_':
                return False
    
    # non-zero leading digit
    elif input[0] in '123456789':
        for digit in input:
            if digit not in '0123456789_':
                return False
    #prevent first digit is not a digit: .01 for example
    elif input[0] not in '0123456789':
        return False
    
    return True


def check_octal(input):
    pre_check(input)

    # _ would not be the last digit
    if input[len(input) - 1] in '_':
        return False
    
    # _ would not be next to together
    for i, digit in enumerate(input):
        if digit in ('_'):
            if input[i - 1] in '_' or input[i + 1] in '_':
                return False
    
    # octal integer format: 0o177, 0O234, ...
    if input[0] == '0':
        if len(input) > 2 and input[1] in 'oO':
            input = input[2:]
        else:
            return False
    else:
        return False
    
    #check each digit
    for digit in input:
        if digit not in '01234567_':
            return False
    
    
    return True

def check_hexa(input):
    pre_check(input)

    # _ would not be the last digit
    if input[len(input) - 1] in '_':
        return False
    # _ would not be next to together
    for i, digit in enumerate(input):
        if digit in ('_'):
            if input[i - 1] in '_' or input[i + 1] in '_':
                return False

    # hexadecimal format: 0xdeadbeef
    if input[0] == '0':
        if len(input) > 2 and input[1] in 'xX':
            input = input[2:]
        else:
            return False
    else:
        return False

    #check digit
    for digit in input:
        if digit not in '0123456789abcdefABCDEF_':
            return False
        
    return True


#testing floating point literals
def check_fpl(input):
    pre_check(input)

    # _ would not be the last digit
    if input[len(input) - 1] in '_':
        return False
    # _ would not be the first digit
    if input[0] in '_':
        return False
    
    # _ would not be next to together
    for i, digit in enumerate(input):
        if digit in ('_'):
            if input[i - 1] in '_' or input[i + 1] in '_':
                return False
   
    # counter for the number of 'e' and '.'
    decimal_point = 0
    exp_char = 0

    for char in input:
        if char == '.':
            decimal_point += 1
        if char == 'e':
            exp_char += 1
        if char not in '0123456789.eE+-_':
            return False
        
    if decimal_point > 1 or exp_char > 1:
        return False
    
    for i, char in enumerate(input):
        #sign can only be after 'e' or 'E'
        if char in ('+', '-'):
            #before +/- is not e/E --> false
            if input[i - 1] not in ('e', 'E'):
                return False   
        elif char in ('e', 'E'):
            # e/E won't be the first or last char
            if i == 0 or i == len(input) - 1:
                return False
            # before or after  e/E has to be digits 
            if input[i - 1] not in '0123456789.' or input[i + 1] not in '0123456789+-':
                return False
        elif char == '.':
            #before or after '.' has to be digits, '.' cannot stand alone
            if input[i - 1] not in '0123456789' or input[i + 1] not in '0123456789e':
                return False
    return True

# main
user_input = input("Enter a number: ")
if check_decimal(user_input):
    print("The input is  a decimal integer!")

elif check_octal(user_input):
    print("The input is  an octal integer!")
   
elif check_hexa(user_input):
    print("The input is  a hexadecimal integer!")

elif check_fpl(user_input):
    print("The input is floating  point literal!")

else:
    print("The input is not valid!")

#testing
#print(user_input)
