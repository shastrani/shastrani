from quiz_game_class import Que

Questions_Prompts = [
    "what colour are apples?\n(a)red\n(b)blue\n(c)yellow\n\n",
    "what colour are bananas?\n(a)blue\n(b)red\n(c)yellow\n\n",
    "what colour are strawberries?\n(a)blue\n(b)red\n(c)yellow"

]

QS = [
    Que(Questions_Prompts[0], "a"),
    Que(Questions_Prompts[1], "c"),
    Que(Questions_Prompts[2], "b")
]

def test():
    score = 0
    for Q in Questions_Prompts:
        print(Q)
        if input("Enter a, b or c: ") == QS[Questions_Prompts.index(Q)].ans:
            print("\ncorrect!\n")
            score = score + 1
        else:
            print("\nincorrect\n")
            score = score
    print("Well done! You got " + str(score) + " out of 3!")


test()
