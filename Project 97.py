import random

print("Number Guessing Game!")

number=random.randint(1,9)

chances=0

print("Guess a number between 1 and 9: ")

while chances < 5:
    guess=int(input("Enter Your Guess Here: "))

    if guess == number:
        print("Congratulations You WON!!!!!")
        break
    elif guess < number:
        print("Your Guess was too low, guess a higher number")
        guess=int(input("Enter Your Guess Here: "))
        break
    else: 
        print("Your Guess was too high, guess a lower number")
        guess=int(input("Enter Your Guess Here: "))

    chances +=1

if not chances < 5:
    print("You guessed too many times! You lose! The number is: ", number)