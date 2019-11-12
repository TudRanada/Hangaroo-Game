secretWord = raw_input("Enter the secret word: ")
def Hangaroo(secretWord):
    lettersGuessed = raw_input("Guess the word or letter: ")
    
    from getGuessedWord import getGuessedWord
    print(getGuessedWord(secretWord, lettersGuessed))
    from isWordGuessed import isWordGuessed
    print(isWordGuessed(secretWord, lettersGuessed))
    from getAvailabLetters import getAvailabLetters
    print(getAvailabLetters(lettersGuessed))
    
    return 0