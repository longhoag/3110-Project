# 3110 Project: Python Numerical Literal Checker

## NFA Design Coding Implementation 

![Screenshot 2024-04-19 at 11 46 11 PM](https://github.com/longhoag/3110-Project/assets/99232763/ee45caf6-6854-40ca-976e-b77e93298de2)

We use this object so that we can simulate the NFA design in our code. With the design of the NFA, we will then define how many states in the NFA, the alphabet of the language, the state transition, the starting state and the eccepting states. When the input is passed onto the object, the function in the object will loop through each characters and change the current state based on the coded transition table made from the NFA. Since we have already defined our accepting states, if the current state is the accepting state after looping through the last character, the input is recognized by the NFA. Otherwise, the input is not recognized.

![Screenshot 2024-04-19 at 11 52 32 PM](https://github.com/longhoag/3110-Project/assets/99232763/cd45ef99-b373-4b09-b9da-43ff9db22990)

This is a small part of our code showing the example of the coded transition table. We have the current state, and after a value is passed, it will go to the next state, the same as the design of the NFA.

**When you compare the NFA designs with the transtion tables in our code, you can easily trace the branches and understand where we are getting.**

## Recognize Python decimal integer literals

![Screenshot 2024-04-19 at 11 54 31 PM](https://github.com/longhoag/3110-Project/assets/99232763/9a5f7c64-397c-46e6-ac07-b8cacd7f94a0)

## Recognize Python octal integer literals

<img width="802" alt="Screenshot 2024-04-08 at 5 50 25 PM" src="https://github.com/longhoag/3110-Project/assets/99232763/70135cda-282d-4cc0-b515-2cac4da3cd3d">

## Recognize Python hexadecimal integer literals

<img width="788" alt="Screenshot 2024-04-08 at 5 54 34 PM" src="https://github.com/longhoag/3110-Project/assets/99232763/8475205c-e4d8-4cc3-afab-5851ec3be7b4">


## Recognize Python floating point literals

<img width="985" alt="Screenshot 2024-04-08 at 6 07 23 PM" src="https://github.com/longhoag/3110-Project/assets/99232763/42e9883f-69cc-40fd-8de2-aaaffcc4750f">


## Information regarding the code
All the code is packed in one file, main.py
