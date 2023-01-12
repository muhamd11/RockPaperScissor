# Rock , Paper , Scissor
from random import randint

#moves
moves = ["rock","paper","scissor"]
while True:
    computer = moves[randint(0,2)]
    player = input("rock or paper or scissor!!? (or end the game) ").lower()
    if player == "end tha game":
        print("the gamed ended")
        break
    elif computer == player:
        print("tie!!")
    elif player == "rock":
        if computer == "paper":
            print("you lose ", computer ,"beats" , player)
        else:
            print("you win ", player, "beats", computer)
    elif player == "paper":
        if computer == "scissor":
            print("you lose ", computer, "beats", player)
        else:
            print("you win ", player, "beats", computer)
    elif player == "scissor":
        if computer == "rock":
            print("you lose ", computer, "beats", player)
        else:
            print("you win ", player, "beats", computer)

    else:
        print("please check your spelling")



