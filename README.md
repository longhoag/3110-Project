# 3110 Project: Python Numerical Literal Checker

## Project Description

This code recognizes Python decimal, octal, and hexadecimal integers as well as floating point literals. It achieves this by taking the input and running it through an NFA, and if the next char in the input is valid for the given NFA, it will move to the next state until the entire input has gone through the NFA. If the final state is the accept state, then the code will state that the input has been accepted as a decimal, octal, hexadecimal, or floating point literal. The program starts with testing the input as a decimal integer literal, then if it does not get accepted it moves on to be tested as an octal integer literal, then hexadecimal integer literal, and finally as a floating point integer literal. If the input does not get accepted in any of the NFAs then the program will say that the input is invalid.

## NFA Design Coding Implementation 

![Screenshot 2024-04-19 at 11 46 11 PM](https://github.com/longhoag/3110-Project/assets/99232763/ee45caf6-6854-40ca-976e-b77e93298de2)

We use this object so that we can simulate the NFA design in our code. With the design of the NFA, we will then define how many states in the NFA, the alphabet of the language, the state transition, the starting state and the eccepting states. When the input is passed onto the object, the function in the object will loop through each characters and change the current state based on the coded transition table made from the NFA. Since we have already defined our accepting states, if the current state is the accepting state after looping through the last character, the input is recognized by the NFA. Otherwise, the input is not recognized.

![Screenshot 2024-04-19 at 11 52 32 PM](https://github.com/longhoag/3110-Project/assets/99232763/cd45ef99-b373-4b09-b9da-43ff9db22990)

This is a small part of our code showing the example of the coded transition table. We have the current state, and after a value is passed, it will go to the next state, the same as the design of the NFA.

**When you compare the NFA designs with the transtion tables in our code, you can easily trace the branches and understand where we are getting.**

## Recognize Python decimal integer literals

![Screenshot 2024-04-19 at 11 54 31 PM](https://github.com/longhoag/3110-Project/assets/99232763/9a5f7c64-397c-46e6-ac07-b8cacd7f94a0)

![Screenshot 2024-04-20 at 12 00 24 AM](https://github.com/longhoag/3110-Project/assets/99232763/65693d90-964a-4189-8612-b45b601be1af)

You can see how we define our parameters in the code. Since the transition table codes in the NFA are made completely from the NFA design, this attachment is shown as an example for other NFA as well.  

## Recognize Python octal integer literals

![Screenshot 2024-04-20 at 12 16 56 AM](https://github.com/longhoag/3110-Project/assets/99232763/6034484b-fc59-490f-a73d-f843301375f7)

## Recognize Python hexadecimal integer literals

![Screenshot 2024-04-20 at 12 17 31 AM](https://github.com/longhoag/3110-Project/assets/99232763/556e31eb-baa4-42a2-a7ce-4b947926b89f)


## Recognize Python floating point literals

![Screenshot 2024-04-20 at 12 18 33 AM](https://github.com/longhoag/3110-Project/assets/99232763/b77bb10d-abdf-41e2-a15f-4fbabdee8dac)


## Information regarding the code
All the code is packed in one file, main.py


## Guidlines for the NFA designs

![Screenshot 2024-04-20 at 12 24 38 AM](https://github.com/longhoag/3110-Project/assets/99232763/c9090a84-d427-46b0-b8f8-2c82a518d2ec)
![Screenshot 2024-04-20 at 12 24 54 AM](https://github.com/longhoag/3110-Project/assets/99232763/8d92d97b-cb37-4b2d-8c9f-8bcc0e240e63)

The NFA design and rules for recognizing the input strings are based on Python documentations for Integer literals and floating point literals above. You can trace the branches of the NFA designs to see how we follow the Python documentation.
