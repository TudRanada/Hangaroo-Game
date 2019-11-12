def getGuessedWord(secretWord, lettersGuessed):
    z = ' '
    for char in secretWord:
        if char in lettersGuessed:
            z += char
        else: 
            z += "_"
    return z