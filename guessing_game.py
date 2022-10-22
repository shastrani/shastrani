ppl_ans = "nothing"
ans = "cat"
i = 0

while ppl_ans != ans and i < 3:
  ppl_ans = input("Guess a word: ")
  i += 1

if ppl_ans == ans:
  print("WELL DONE! correct word.")

if i >= 3:
  print("Ran out of guesses")