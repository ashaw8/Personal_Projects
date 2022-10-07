
from asyncore import read, write
import sys
import random


def encryption(): #need to add capital letters
    encrypt_dict =  { 
                        #Cap_Letters -Letters    -Number    -Special Char
                        'A':'G88z', 'a': '1z!a', '0':'c*1!', '!':'r8V%', 
                        'B':'ReN7', 'b': '6_M!', '1':'%zS1', '@':'za!!',
                        'C':'BM!0', 'c': 'G0b!', '2':'D0i$', '#':'10z!',
                        'D':'kE#3', 'd': 'qq11', '3':'@wU@', '$':'<>10',
                        'E':'E3e3', 'e': 'B0z?', '4':'<31m', '%':'oI1*',
                        'F':'0o30', 'f': 'N3L#', '5':'#nz0', '^':'3214',
                        'G':'210!', 'g': '$M0D', '6':'91X&', '&':'09!t',
                        'H':'ZZ_Z', 'h': '21B0', '7':'1m7C', '*':'tTt!',
                        'I':'9124', 'i': 'z1M0', '8':'!@fu', ' ':'1AS0',
                        'J':'fj!Z', 'j': '##12', '9':'uU$1', '?':'00!a',
                        'K':'1*Z1', 'k': 'z._1', 
                        'L':'$%!@', 'l': '@3D0',
                        'M':'!@^$', 'm': '19z0', 
                        'N':'BVxB', 'n': '&MN7', 
                        'O':'oe3o', 'o': '09!u', 
                        'P':'9o66', 'p': '-*vM', 
                        'Q':'1224', 'q': '0Z1.', 
                        'R':'k!l1', 'r': '9JK$', 
                        'S':'&*!@', 's': 'AI67', 
                        'T':'B012', 't': 'm3_8', 
                        'U':'j3uN', 'u': 'kl!0', 
                        'V':'NNN!', 'v': 'm!K3', 
                        'W':'!NNN', 'w': 'vQ!0', 
                        'X':'L@3P', 'x': '%$MO', 
                        'Y':'LL#$', 'y': '#z3P', 
                        'Z':'l2$&', 'z': 'Yy$!',
                        }
    return encrypt_dict    
   

def encrypt_message(my_passworde):
    """Takes a string and encrypts it from our dictionary
        
        Args: str(my_passworde) The password you want to encrypt
        
        Returns: Your password as an encrypted version  
    """
    mylist_pw = []
    encrypt_key_value = encryption()
#iterate through given password and match each letter with dict key    
    for i in my_passworde:
        if i in encrypt_key_value:
            mylist_pw.append(encrypt_key_value[i])
    return ''.join(mylist_pw)

def decrypt_message(password):
    """Takes your encrypted password and decrypts it
    
        Args: str(password) Your password that was encrypted through this script
        
        Returns: Your password in its decrypted form
    """
    decrypted_password = []
    chunked_password = []
    chunk_size = 4 #Change with number of values in key:value pair
    encrypt_key_value = encryption()
    
    for i in range(0, len(password), chunk_size):
# Breaking entered str(password) into chunks of 4 in new decrypted_password = []
        chunked_password.append(password[i:i+chunk_size])
#iterate through chunked password and match values with there keys, return keys   
    for value in chunked_password:
        if value in encrypt_key_value.values():
            decrypted_password.append(list(encrypt_key_value.keys()) \
            [list(encrypt_key_value.values()).index(value)])  
    return ''.join(decrypted_password)
        
def new_password():
    enc_dic = encryption()
    random_c = random.choice(list(enc_dic.values()))
    return random_c
#Creates newly generated password for user
    return

def write_encryption_file(file_name,conent):
#write the contents of an encrypted message to a file
    f = open(file_name, "w", encoding="utf-8")
    f.write(conent)
    f.close

def read_encrypted_page(file_name):
#read the contents of an encrypted page and decrypt them
    f = open(file_name, "r", encoding="utf-8")
    for line in f:
        return decrypt_message(line)            

def main():
    """Main logic for runing other functions
    """   
    print('\n\t\t\tWelcome to my cipher script\n \
        Select the service you would like by typing in one of the following:\n\
        \tEncrypt_password\n \
        \tDecrypt_password\n \
        \tEncrypt message\n \
        \tDecrypt message\n \
        \tHelp')
    user_options = input()
    
    #Option to run encrypt password function if user calls it
    if user_options in ['Encrypt_password', 'Encrypt password', 'encrypt_password']:
        print("Enter the password you want to encrypt")
        user_encrypt_pw = input()
        print(f'Your password {user_encrypt_pw} has been encrypted to: {encrypt_message(user_encrypt_pw)}')
    
    #Option to run decrypt password function if user enters it
    elif user_options in ['decrypt_password', 'Decrypt_password', 'Decrypt password']:
        print("Enter the password you want to decrypt")
        user_decrypt_pw = input()
        print(f'Your password has been decrypted: {decrypt_message(user_decrypt_pw)}')
    
    #Encrypt a message, anything other than a password
    elif user_options in ['Encrypt message', 'encrypt message', 'encrypt_message']:
        print("\nEncrypting a message is written to a file. Choose a file"
                " ending it with .txt")
        write_file_name = input()
        print("Now enter your message you want to encrypt")
        write_user = input()
        write_user = encrypt_message(write_user)
        write_encryption_file(write_file_name, write_user) 
        
    #decrypt a message by reading it from a text file
    elif user_options in ['Decrypt message', 'decrypt message']:
        print("file name")
        read_user = input()
        ru = read_encrypted_page(read_user)
        print("Enter a file name for decrypted message to be writtent to"
                "end file name with .txt")
        decrypt_file_name = input()
        write_encryption_file(decrypt_file_name, ru)
    
    #help page for explaination on each option
    elif user_options in ['Help', 'help']:
        print("\nEncrypt_password: \
                \nDecrypt_passwords \
                \nEncrypt message: \
               \nDecrypt message:")
        print("enter the character b to go back to menu")
        user_back = input()
        if user_back == 'b':
            main()
                    
new_password()