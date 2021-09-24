import random

choices = ["Rock","Paper","Scissors"]

def computer_choice():
   return random.choice(choices)

def check_validity(x,y,win):
    if(y == x): win=2
    if(x == "Rock" and y == "Scissors"): win = 1
    elif(x == "Scissors" and y == "Paper"): win = 1
    elif(x == "Paper" and y == "Rock"): win = 1
    
    return win


def user_choice():
    again = True
    i=0
    while(again):
        win = 0
        print("Rock or Paper or Scissors! What's your choice?")
        x = input()
        while (not(x in choices) and i<=3):
            print("Input must be Rock or Paper or Scissors. What's your choice?")
            x = input()
            i+=1
        if(i == 4): return "End. Restart the program"
        y =  computer_choice()
        print(y)
        win = check_validity(x,y,win)
        if(win == 1) :
            print("You win! Play again? (Y or N)")
            play = input()
        elif(win == 0): 
            print("You loose! Play again ? (Y or N)")
            play = input()
        else: 
            print("Draw! Play again? (Y or N)")
            play = input()
        if(play == "N"): again = False
   
    return "Thank you ! Bye"
  
print (user_choice())