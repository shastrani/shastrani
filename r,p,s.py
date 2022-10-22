import random

choice = {
    1: "rock",
    2: "scissors",
    3: "paper"
}

def r_p_s():
    ppl_c = input("Enter your choice: ")
    com_points = 0
    ppl_points = 0
    i = 0
    com_c = random.randint(1, 3)
    print("The computer picked " + choice[com_c] + ".")

    while i < 5:
        if choice[com_c] == ppl_c.lower():
            print("Its a draw\n")
            ppl_c = input("Play again: ")
            com_c = random.randint(1, 3)
            print("The computer picked " + choice[com_c] + ".")
        elif choice[com_c] == "rock" and ppl_c.lower() == "paper":
            print("Well done! You win!\n")
            ppl_points = ppl_points + 1
        elif choice[com_c] == "rock" and ppl_c.lower() == "scissors":
            print("The computer wins!\n")
            com_points = com_points + 1
        elif choice[com_c] == "paper" and ppl_c.lower() == "scissors":
            print("Well done! You win!\n")
            ppl_points = ppl_points + 1
        elif choice[com_c] == "paper" and ppl_c.lower() == "rock":
            print("The computer wins!\n")
            com_points = com_points + 1
        elif choice[com_c] == "scissors" and ppl_c.lower() == "paper":
            print("The computer wins!\n")
            com_points = com_points + 1
        elif choice[com_c] == "scissors" and ppl_c.lower() == "rock":
            print("Well done! You win!\n")
            ppl_points = ppl_points + 1
        ppl_c = input("play again: ")
        com_c = random.randint(1, 3)
        print("The computer picked " + choice[com_c] + ".")
        i = i + 1


    if ppl_points > com_points:
        print("You won. The score is " + str(ppl_points) + "-" + str(com_points))
    else:
        print("The computer won. The score is " + str(ppl_points) + "-" + str(com_points))


r_p_s()
