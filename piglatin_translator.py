def real_piglatin(phrase):
    suff = ""
    trans_word = ""
    alt_word = ""
    trans = ""
    for words in phrase:
        for letter in words:
            while letter in "bcdfghjklmnpqrstvwxyz":
                alt_word = words.replace(letter, "")
                suff = suff + letter
            trans_word = trans_word + alt_word + suff + "ay"
        trans = trans + trans_word
    return trans


print(real_piglatin(input("Enter a phrase: ").split()))
