def piglatin():
    trans = ""
    sen = input("Enter a phrase: ").split()
    for word in sen:
        if word[0].lower() in "bcdfghjklmnpqrstvwxyz":
            trans = trans + word.replace(word[0], "") + word[0] + "ay" + " "
        else:
            trans = trans + word + "yay" + " "

    return trans


print(piglatin())
