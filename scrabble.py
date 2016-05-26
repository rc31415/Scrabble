import re
import itertools

# ~~~~~~ READ FILE ~~~~~ #

def read():
    content = []
    with open("words.txt") as f:
	content = f.read().splitlines()
    return content

# ~~~~~ GET LETTERS ~~~~~ #

def input():
    LetterPattern = re.compile('[a-z_]')

    print("Type your characters below.")
    print("You may type up to 8 characters (7 tiles and a letter already on the board)")
    print("To indicate a blank tile, use an underscore.\n")


    valid = 0
    while valid == 0:
	input = raw_input("Enter Letters Here: ").lower()
	print('')
        letters = re.findall(LetterPattern, input)

        if letters.count("_") > 1:
            print("I'm sorry, I haven't figure out how to handle more than one blank space")
        else:    
            if len(''.join(letters))>8:
                print("You entered more than 8 letters. Please re-enter your letters")
            elif len(''.join(letters))<7:
                ans = raw_input("\n You entered fewer than 7 letters. Press \"y\" to confirm that this is correct, and \"n\" to try again. ")
	        if ans == 'y':
                    valid = 1
                    return letters
            else:
                valid = 1
                return letters


# ~~~~~ FIND VALUE OF WORD ~~~~~ #

def value(letters):
    values = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3, 'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4, 'x': 8, 'z': 10}
    sum = 0
    for i in letters:
         sum = sum + values[i]
    return sum


# ~~~~~ FIND WORDS FROM A LIST OF LETTERS ~~~~ #

def words(letters):
    length = 2
    while length <= len(letters):
        for i in list(itertools.permutations(letters, length)):
            if content.count(''.join(i)) == 1:
  		results[''.join(i)]=value(i)            
        length += 1



# --- OH NO AN UNDERSCORE!!! --- #

def underscore(letters):
    for ltr in range(97,123):
        words(letters.replace("_",chr(ltr)))

# ~~~~~~ MAIN PROGRAM ~~~~~ #

content = read()

print("Welcome to my program")

letters = input()
results = {}

underscore(''.join(letters))


print('  WORD \t|  POINTS  ')
print('-------------------')
for key, value in sorted(results.items()):
	print(str(key) + "\t|  " + str(value))



