def getAvailabLetters(lettersGuessed):    
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                   'n','o','p','q','r','s','t','u','v','w','x','y','z']
        x = list(lettersGuessed)
        
        for x in letters:
            if x == lettersGuessed:
                letters.remove(x)    
                
        print(letters)