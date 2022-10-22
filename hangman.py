def play():
    ans = "mouse"
    mys = ["_", "_", "_", "_", "_"]
    print(mys)
    ppl_ans = input("Enter a letter: ")
    counter = 0
    tries_left = 8
    while counter < 8:
        if ppl_ans in ans:
            mys[ans.index(ppl_ans)] = ppl_ans
            print(mys)
            ppl_ans = input("Enter a letter: ")
        elif not (ppl_ans in ans):
            counter += 1
            print("Wrong letter, You have " + str((tries_left + 1) - counter) + "tries left.")
            print(mys)
            ppl_ans = input("Enter a letter: ")
        if not("_" in mys):
            print("Well  done! Word guessed")
            break


play()
