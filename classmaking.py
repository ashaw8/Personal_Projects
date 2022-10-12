from pdb import line_prefix
import random
from re import X

class HangMan:
    def __init__(self, word, a_dict) -> None:
        self.game = []
        self.a_dict = a_dict
        for char in word:
            if char in a_dict.keys():
                self.game.append(list(a_dict.values())[list(a_dict.keys()).index(char)])
        #print(self.a_dict)      
        #self.game = [str(x) for x in self.game]
        
    def format_game(self,word):
        string = "_\t"
        self.game = '\t'.join(self.game)
        self.game = f'{string * len(word)}\n{self.game}'
        
    def add_letter(self, guess_letter):
        key_dic = self.a_dict[guess_letter]
        if key_dic in self.a_dict.values() and key_dic == key_dic:
                self.game[:] = [guess_letter if x == key_dic else x for x in self.game]
                #print([guess_letter if x == key_dic else x for x in self.game])
                return self.game
                #kickoff = [item.replace(number,guess_letter) for item in self.game if int(number) in dict.values()]
    
    def test(self):
        for i in self.game:
            print(i)
    
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
    alpha = alphabet_dict()
    print("Enter a letter to guess word\n")
    game = HangMan("banana",alpha )

    while flag == True:
        print("Guess:")
        guess = guess_word(input())
        if guess != False:
            
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                current_letters = game.add_letter(guess)
                current_letters = [str(x) for x in current_letters]
                print(current_letters)
            else:
                print("You've already used this letter")

        else:
            print("not in letter")
        

#alpha = alphabet_dict()
#print(list_to_dict(alpha))
#num_under("banana")
main()
#man= HangMan("banana",alpha)
#man = man.test()
#man.format_game("banana")
#print(man)
