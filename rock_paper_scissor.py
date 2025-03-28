import random

sen = {'r':'Rock','p':'Paper','s':'Scissor'}
choices = ('r','p','s')
while True:
    user_choice = input("Rock,Paper,Scissor (r/p/s).: ").lower()
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Invalid Choice!")
    else:
        if ((user_choice =='p'and computer_choice =='r') or
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's'and computer_choice =='p')):
            print(f"Your Choice.:{sen[user_choice]}")
            print(f"Computer Choice.:{sen[computer_choice]}")
            print("You win")
        elif(user_choice == computer_choice):
            print(f"Your Choice.:{sen[user_choice]}")
            print(f"Computer Choice.:{sen[computer_choice]}")
            print("You Tie")
        else:
            print(f"Your Choice.:{sen[user_choice]}")
            print(f"Computer Choice.:{sen[computer_choice]}")
            print("You lose")
            
        should_continue = input("Continue ? (y/n): ").lower()
        if should_continue !='n' and should_continue !='y':
            print("Invalid Term")
        elif should_continue == 'n':
            break
        else:
            continue
            