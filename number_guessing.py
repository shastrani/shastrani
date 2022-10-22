import random

def is_number():
    ans = random.randint(1, 5)
    ppl_ans = 0
    tries = 0
    while ppl_ans != ans:
        ppl_ans = float(input("guess a number: "))
        tries = tries + 1

    print("Well done! You guessed the Correct number in " + str(tries)hhui + " guesses")


is_number()

