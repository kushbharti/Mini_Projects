import random

number_to_guess = random.randint(1,100)

while True:
    try:
        guess = int(input("Guess the Number b/w 1-100.: "))
        if guess < number_to_guess:
            print("Too Low")
        elif guess > number_to_guess:
            print("Too High")
        else:
            print("congratulatiions! You guess Correct. ")
            break
    except:
        print("Enter a valid Number.")
        
        
        
        