
import random


class HangMan:
    def __init__(self, word, a_dict) -> None:
        self.game = [] #Number values representing each letter in given game
        self.a_dict = a_dict
        for char in word:
            if char in a_dict.keys():
                self.game.append(list(a_dict.values())[list(a_dict.keys()).index(char)])

        #print(self.a_dict)      
        #self.game = [str(x) for x in self.game]
        
    def add_letter(self, guess_letter):
        key_dic = self.a_dict[guess_letter]
        if key_dic in self.a_dict.values() and key_dic == key_dic:
                self.game[:] = [guess_letter if x == key_dic else x for x in self.game]
                #print([guess_letter if x == key_dic else x for x in self.game])
                return self.game
                #kickoff = [item.replace(number,guess_letter) for item in self.game if int(number) in dict.values()]
    def start_of_game(self):
       return format_game(self.game,1)
    
def display_art(round):
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
            return wrong3
        elif round == 5:
            wrong4 = '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    ========='''
            return wrong4
        elif round == 6:
            wrong5 = '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    ========='''
            return wrong5
        else:
            wrong6 = '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    ========='''
            return wrong6

def format_game(list_of_letter, round):
    print(display_art(round))
    letter_list = [str(x) for x in list_of_letter] #Change our list of ints and stings to list of only strings
    print('\t'.join(letter_list)) #print our strings with tab spaces inbetween

            
        
def alphabet_dict():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p", \
               "q","r","s","t","u","v","w","x","y","z"]
    random_nums = random.sample(range(1,27), 26)#Numbers 1-26 in a random sequence each time
    final_list = [] #List of letter and random number alternating

    for num, letter in zip(letters, random_nums):#Combining our two lists random numbers and letters
            final_list.append(num)#Number first to be key in dict
            final_list.append(letter)#alternate with number to be value

    dict = {final_list[i]: final_list[i + 1] for i in range(0, len(final_list), 2)}
    return dict
  
    
def guess_word(guess):
    word = "banana"
    if guess in word:
        return guess
    else:
        return False
        

def main():
    
    flag = True
    guessed_letters = []
    alpha = alphabet_dict()
    print("Enter a letter to guess word\n")
    game = HangMan("banana",alpha)
    round_counter = 1 #Round counter, starts at so user sees 1 first instead 0

    while True:
        
        if round_counter == 7: #When user failed 7 attempts, game ends
            
            break
        
        else:
            game.start_of_game()
            print("Guess:")
            guess = guess_word(input())#sending user input to be checked if correct
            
            if guess != False:
                print(f'Counter : {round_counter}')
                
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
                    current_letters = game.add_letter(guess)
                    format_game(current_letters, round_counter)
                
                    
                else:
                    print("You've already used this letter")
                    round_counter += 1
                    format_game(current_letters, round_counter)

            else:
                print(f'Counter : {round_counter}')
                print("not in letter")
                round_counter += 1
                format_game(current_letters, round_counter)
                
        


main()

