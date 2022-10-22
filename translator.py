def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
            print(letter)
        else:
            translation = translation + letter
    return translation


print(translator(input("word or phrase: ")))