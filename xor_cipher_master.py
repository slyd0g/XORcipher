from sys import exit
import binascii
import getpass
import pickle

def str_to_ascii(text):
    """Function: Convert string to ascii
    Input: String
    Output: List of chars in string in ascii
    """
    text_split = list(text)
    
    for i, x in enumerate(text_split):
        text_split[i] = ord(x)
    
    return text_split

def XOR_list(text, key):
    """Function: Perform bitwise XOR on two lists of ascii values and return list
    Input: Two ascii lists
    Output: XORed ascii list
    """
    xor_result = []
    index = range(0,len(text))
    
    for index, (x,y) in enumerate(zip(text, key)):
        xor_result.insert(index, chr(x^y))

    return xor_result

def encrypt():
    """Function: Takes plain text and key and XOR encrypts
    Input: Two strings
    Output: Pickle file
    """
    plain_text = raw_input("Enter a word/phrase you want to encrypt.\n> ")
    pt_length = len(plain_text)

    key = getpass.getpass("Enter a keyword/phrase, note it's length must be >= your plain text\n> ")
    confirm_key = getpass.getpass("Please confirm your key.\n> ")
    key_length = len(key)

    if ((key != confirm_key) or (key_length < pt_length)):
        print "Either the keys did not match or your key is too short. Exiting ..."
        exit(1)

    pt_ascii = str_to_ascii(plain_text)
    key_ascii = str_to_ascii(key)
    cipher = XOR_list(pt_ascii, key_ascii)
    
    pickle_file = raw_input("Enter a name for your encrypted file, it will automatically have a .pickle extension.\n> ") + ".pickle"
    with open(pickle_file, 'wb') as f:
        pickle.dump(cipher,f)
    print "Your message has been encrypted and stored in %s" % pickle_file

def decrypt():
    """Function: Read list from pickle file and decrypt using key
    Input: Pickle file
    Output: Plain text message
    """
    pickle_file = raw_input("Enter the name of the *.pickle file you want to decrypt\n> ") + ".pickle"
    
    with open(pickle_file, 'rb') as f:
        cipher = pickle.load(f)
    print "%s successfully loaded." % pickle_file

    key = raw_input("Enter the decryption keyword/phrase\n> ")
    
    key_ascii = str_to_ascii(key)
    plain_text = XOR_list(str_to_ascii(cipher), key_ascii)
    
    print "Assuming you have the correct key, the secret message was:", ''.join(plain_text)

if __name__ == "__main__":
    
    choice = raw_input("Are you looking to 'encrypt' or 'decrypt' a message?\n> ")
    
    if choice == 'encrypt':
        encrypt()
        exit(1)
    elif choice == 'decrypt':
        decrypt()
        exit(1)
    else:
        print "Not sure what you said, exiting ..."
        exit(1)
