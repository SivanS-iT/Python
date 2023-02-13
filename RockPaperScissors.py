from random import randint

playList = ["Rock", "Paper", "Scissors"]
pc = playList[randint(0,2)]

player = False
while player == False:
    player = input("Rock, Paper, Scissors?").lower()
    if player == pc:
        print("Tie!")
    elif player == "rock":
        if pc == "paper":
            print("You lose!", pc, "covers", player)
        else:
            print("You win!", player, "smashes", pc)
    elif player == "paper":
        if pc == "scissors":
            print("You lose!", pc, "cut", player)
        else:
            print("You win!", player, "covers", pc)
    elif player == "scissors":
        if pc == "rock":
            print("You lose...", pc, "smashes", player)
        else:
            print("You win!", player, "cut", pc)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    pc = playList[randint(0,2)].lower()
