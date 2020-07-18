import random
import tkinter as tk

window = tk.Tk()
window.geometry("800x1000")
window.title("Rock Paper Scissors Game")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]


def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=16,width=60,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

button1 = tk.Button(text="       Rock       ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Paper      ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Scissor     ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)

window.mainloop()


#####################################################################################################################
'''import random

player = input("Enter your choice (rock/paper/scissors): ")
player = player.lower()
while (player != "rock" and player != "paper" and player != "scissors"):
	print(player)
	player = input("That choice is not valid. Enter your choice (rock/paper/scissors): ")
	player = player.lower()

computerInt = random.randint(0,2)
if (computerInt == 0):
	computer = "rock"
elif (computerInt == 1):
	computer = "paper"
elif (computerInt == 2):
	computer = "scissors"
else:
	computer = "Huh? Error..."

if (player == computer):
	print("Draw!")
elif (player == "rock"):
	if (computer == "paper"):
		print("Computer wins!")
	else:
		print("You win!")
elif (player == "paper"):
	if (computer == "rock"):
		print("You win!")
	else:
		print("Computer wins!")
elif (player == "scissors"):
	if (computer == "rock"):
		print("Computer wins!")
	else:
		print("You win!")

print("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!")
input("Enter any key to exit.")'''