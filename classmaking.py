import random


def alphabet_dict():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p", \
               "q","r","s","t","u","v","w","x","y","z"]
    dict_keys = []
    data = random.sample(range(1,27), 26)
    final_list = []
    for i in letters:
        dict_keys.append(i)

    for num, letter in zip(dict_keys, data):
            final_list.append(num)
            final_list.append(letter)

    return final_list

def list_to_dict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
        
    print(list_to_dict(final_list))

    
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
        

alphabet_dict()