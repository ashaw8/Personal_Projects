import random

class HangMan:
    def __init__(self, word, a_dict) -> None:
        numbers = []
        for char in word:
            if char in a_dict.keys():
                numbers.append(list(a_dict.values())[list(a_dict.keys()).index(char)])      
        
        numbers = [str(x) for x in numbers]
        string = "_\t"
        string = string * len(word)
        numbers = '\t'.join(numbers)
        print(string)
        print(numbers)

    def display_art(self,round):
        if round == 1:
            start = '''
    +---+
    |   |
        |
        |
        |
        |
    ========='''
            return start
        elif round == 2:
            wrong1 = '''
    +---+
    |   |
    O   |
        |
        |
        |
    ========='''
            return wrong1
        elif round == 3:
            wrong2 = '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ========='''
            return wrong2
        elif round == 4:
            wrong3 = '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    ========='''
            wrong4 = '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    ========='''
            wrong5 = '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    ========='''
            wrong6 = '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    ========='''
        
        
def alphabet_dict():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p", \
               "q","r","s","t","u","v","w","x","y","z"]
    random_nums = random.sample(range(1,27), 26)#Random order of numbers 1 - 26
    final_list = [] #List of letter and random number alternating

    for num, letter in zip(letters, random_nums):#Combining our two lists random numbers and letters
            final_list.append(num)#Number first to be key in dict
            final_list.append(letter)#alternate with number to be value

    dict = {final_list[i]: final_list[i + 1] for i in range(0, len(final_list), 2)}
    return dict

#def list_to_dict(lst):
    #res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}#Assign key/value pairs by alternating through range of list
    #return res_dct  

def under_Scores(num_of_char):
    #formatting under scores
    string = "  _"
    string = string * len(num_of_char)
    print(string)
    
def guess_word(guess):
    word = "banana"
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
    under_Scores("unicorn")
    print(num_under("banana"))
    
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
        

alpha = alphabet_dict()
#print(list_to_dict(alpha))
#num_under("banana")
#main() 
HangMan("banana",alpha )