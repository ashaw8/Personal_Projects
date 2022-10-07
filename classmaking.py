
def alphabet_dict():
    a_dict =  { "a":int, 
                "b":int,
                "c":int,
                "d":int,
                "e":int,
                "f":int,
                "g":int,
                "h":int,
                "i":int,
                "j":int,
                "k":int,
                "l":int,
                "m":int,
                "n":int,
                "o":int,
                "p":int,
                "q":int,
                "r":int,
                "s":int,
                "t":int,
                "u":int,
                "v":int,
                "w":int,
                "x":int, 
                "y":int,
                "z":int,  }
    for key, values in range(a_dict):
        # iterate out all keys, put in list, combine list of random numbers
        # pass back in w/ alternate key and random num as value in dict
        print(key, values)
    
def guess_word(guess):
    word = "orange"
    if guess in word:
        return guess
    else:
        return False
        

def display_found_letters(letters):
    joined_word = ''.join(letters)
    word = "orange"
    
    

def main():
    
    flag = True
    guessed_letters = []
    
    while flag is True:
        
        print("Enter a letter to guess word")
        guess = guess_word(input())
        
        if guess != False:
            
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                print(display_found_letters(guessed_letters))
                
            else:
                print("You've already used this letter")

        else:
            print("not in letter")
        

main()