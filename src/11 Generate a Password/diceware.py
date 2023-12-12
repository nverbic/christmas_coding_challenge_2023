''' Generate a password using diceware method '''
from random import randint

def read_file(file_path):
    ''' Read the file and remove text that is not needed for the password generation.
        Create a dictionary from the list of numbers and corresponding words needed for 
        generation of passphrases.'''

    with open(file_path, 'r', encoding='utf-8') as fp:
        diceware_list = fp.readlines()

    # Use slicing to remove extra text from the file
    diceware_list = diceware_list[2:7778]

    # Convert list of strings to a dictionary. Split each string in the list into a list
    #  of two elements (key and value) based on the tab ('\t') delimiter.
    diceware_dict = {}
    for item in diceware_list:
        key, value = item.split('\t')
        diceware_dict[key] = value.strip('\n')

    return diceware_dict

def generate_passphrase(words_number):
    ''' Generate a password using Diceware '''
    passphrase = ""
    generated_numbers_list = []
    file_path = "src/11 Generate a Password/diceware.wordlist.asc"

    # Read the data from the diceware wordlist file
    diceware_dict = read_file(file_path)

    # Generate random 5-digit numbers, use digits from 1 to 6
    for _ in range(words_number):
        dice_results = ""
        for _ in range(5):
            dice_results += str(randint(1, 6))
        generated_numbers_list.append(dice_results)

    # Generate passphrase from numbers generated above
    for key in generated_numbers_list:
        passphrase += diceware_dict[key] + " "

    print(f"Diceware passphrase:\n{passphrase}")
    return passphrase

if __name__ == '__main__':
    generate_passphrase(5)
