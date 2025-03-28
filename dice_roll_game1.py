import random

while True:
    response = input("Do you want to Play (y/n).: ").lower()
  
    if response == "y":
        total_dice = int(input("How many dice your want to roll.: "))
        
        num = []
        for i in range(1,total_dice+1):
            dices = random.randint(1,6)
            num.append(dices)
        print(f"Numbers are.:{(num)}")
    elif response =="n":
        print("Ohk, Thanks.")
        break
    else:
        print("Invalid Term.")
        
    
    
    