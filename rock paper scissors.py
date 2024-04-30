import random

user_wins =0
computer_wins =0

options = ["Rock", "Paper","Scissors"]

while True:
    user_input = input("type Rock/Paper/scissors or Q to Quit. ").lower()
    if user_input == "q" :
       break 
       # quit()
             
    if user_input not in options: #["ROCK","Paper","Scissors"]:
        #continue #please dont write this othrwise it ternminate in the loop


     random_number = random.randint(0,2)#rock=0,paper=1,scissors=2
    computer_pick = options[random_number].lower()

    print(" computer picked " + str(computer_pick) + " . " )#print("computer picked",computer_pick +".")you can also write in this way.
    
    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
       # continue

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1 
        #continue
    
    elif user_input == "scissors" and computer_pick =="paper":
        print("you won!")
        user_wins += 1
        #continue 
    else:        
     print("you lost..")
     computer_wins += 1
        
    
print(" you won " + str(user_wins) +" times.")#print("you won",,str(user_wins),"times.")alternate way
print(" the computer won "+ str(computer_wins) +" times.")
print("goodbye...")
