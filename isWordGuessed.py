def isWordGuessed(secretWord, lettersGuessed):
    v = str(lettersGuessed)
    w = all(elem in secretWord for elem in v)
    
    if w:
        print('True')
    else:
        print('False')
