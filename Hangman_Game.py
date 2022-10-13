"""
Author: Aidan Shawyer
10/12/2022

Credits: 
chrishorton https://github.com/chrishorton 
For Hangman Art
"""
import random


class HangMan:
    def __init__(self, word, a_dict) -> None:
        self.game = [] #Number values representing each letter in given game
        self.a_dict = a_dict #version of dict to be used by rest of methods
        for char in word:#Each letter in the word the user must guess
            if char in a_dict.keys():#if the letter is in our dictionary of letters, keys
                self.game.append(list(a_dict.values())[list(a_dict.keys()).index(char)])#Append the value of that key to self.game

        
    def add_letter(self, guess_letter):
        if guess_letter == 123:
            return self.game
        else:
            key_dic = self.a_dict[guess_letter]#Calling the value of a key from a dict based off user, assign it to varriable
            if key_dic in self.a_dict.values() and key_dic == key_dic:#Make sure its in our dict
                    self.game[:] = [guess_letter if x == key_dic else x for x in self.game]#Replace the number with the letter the user got correct
                    return self.game#return our right/not guess list of values from word to be guessed.
        
    
    def start_of_game(self):
       return format_game(self.game,1)#Display start of game screen
    
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
               "q","r","s","t","u","v","w","x","y","z"]#List of letters
    random_nums = random.sample(range(1,27), 26)#Numbers 1-26 in a random sequence each time
    final_list = [] #List of letter and random number alternating

    for num, letter in zip(letters, random_nums):#Combining our two lists random numbers and letters
            final_list.append(num)#Number first to be key in dict
            final_list.append(letter)#alternate with number to be value

    dict = {final_list[i]: final_list[i + 1] for i in range(0, len(final_list), 2)}#Assigning each value in the list to a key:pair value in alternating order
    return dict
  
    
def guess_word(guess, word):
    if guess in word:#Checking if user guess was right
        return guess#If see return back the letter
    else:
        return False#If not return Falsey value
        

def word_bank():
    bank_of_words = ["jigsaw","psyche","jogging","youthful","kiwifruit","banana",
                     "zombie","marquis","funny","jazz","delete","pond",
                     "america","mexico","dental","oxygen","bookworm","vodka"]
    return random.choice(bank_of_words)

def if_winner(list_of_letters, playin_word):
    check = [str(x) for x in list_of_letters]
    check = "".join(check)
    if check == playin_word:
        return True
    else:
        return False
    
def main():
     
    guessed_letters = []
    alpha = alphabet_dict()
    word = word_bank()
    print("Enter a letter to guess word\n")
    game = HangMan(word,alpha)
    game.start_of_game()
    round_counter = 1 #Round counter, starts at so user sees 1 first instead 0
    current_letters = game.add_letter(123)
    
    while True:
        
        if if_winner(current_letters, word) ==  True:
            print("winner")
            break
            
        else:
        
            if round_counter == 7: #When user failed 6 attempts, game ends
                print(f'Round : {round_counter -1}/6\nNot in word, game over!')
                break
            
            else:
        
                print("Guess:")
                guess = guess_word(input(), word)#sending user input to be checked if correct
                
                if guess == word:
                    print("You won!")
                    break
                else:
                    
                    if guess != False:
                        print(f'Round : {round_counter}')
                        current_letters = game.add_letter(guess)
                        
                        if guess not in guessed_letters:
                            guessed_letters.append(guess)
                            format_game(current_letters, round_counter)
                        
                            
                        else:
                            print(f"Round : {round_counter}/6 You've already used this letter\n")
                            round_counter += 1
                            format_game(current_letters, round_counter)

                    else:
                        print(f'Round : {round_counter}/6\nNot in word, try again\n')
                        round_counter += 1
                        format_game(current_letters, round_counter)
                    
            


main()


