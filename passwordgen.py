# -*- coding: utf-8 -*-
"""
Written by Robert Alfrey
05/06/2022
"""

import secrets as s
import argparse as ap
import pyperclip

def randNumPicker(numStrings):
    #Generate numStrings amount of numbers
    wordsMax = 236736
    numList = []
    for i in range(numStrings):
        numList.append(s.randbelow(wordsMax))
    return numList
    
def getLines(words, numList):
    #Enumerates a file line by line for ease of access
    return (x for i, x in enumerate(words) if i in numList)

def wordPicker(numStrings):
    #Takes a list of numbers and then picks the corresponding words
    with open('Words.txt', 'r') as words:
        lines = getLines(words, numStrings)
        returnList = []
        for line in lines:
            returnList.append(line.strip().lower())
        return returnList


def capitilizeRandomLetters(strList):
    upperList = []
    for i in strList:
        oldString = i
        newString = ''
        for j in oldString:
            fiftyFifty = s.randbelow(2)
            if fiftyFifty == 0:
                newString += j
            elif fiftyFifty == 1:
                newString = newString + j.upper()
            else:
                raise("fiftyFifty gave bad value")
        upperList.append(newString)
    return upperList

def addSpecialCharacters(strList):
    specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '.', '?']
    listWithSpecialChars = []
    for i in strList:
        beforeOrAfter = s.randbelow(2)
        character = specialChars[s.randbelow(len(specialChars))]
        if beforeOrAfter == 0:
            i = str(character) + i
        elif beforeOrAfter == 1:
            i = i + str(character)
        else:
            raise Exception("Before or After gave a bad value")
        listWithSpecialChars.append(i)
    return listWithSpecialChars

    
# def generatePassword(numWords):
#     #Generates a password using the functions above, also allows varaiability in the password type
#     password = []
#     doCapitalize = str(input("Do you want capitial letters? (y)/n: "))
#     if doCapitalize == "n":
#         password = wordPicker(randNumPicker(numWords))
#     else:
#         password = (capitilizeRandomLetters(wordPicker(randNumPicker(numWords))))

    
#     specialChars = str(input("Do you want special characters? (y)/n: "))
#     if specialChars == "n":

#         pass
#     else:
#         password = addSpecialCharacters(password)
      
#     returnPhrase = "".join(password)
       
#     withNumbers = str(input("Do you want numbers on the end? (y)/n: "))
#     if withNumbers == "n":
#         pass
#     else:
#         numMax = 999999
#         number = s.randbelow(numMax)
#         returnPhrase = returnPhrase + str(number)
#
#        
#
#    return returnPhrase

parser = ap.ArgumentParser()
parser.add_argument('-w', '--words', dest="words", metavar="words", type=int, required=True,
                    help ="The number of words in the password")
parser.add_argument('-n', '--numbers', dest="numbers", metavar="numbers", type=str, default="y",
                    help="Adds numbers to the end of the password y for yes, n for no. Defaults to y")
parser.add_argument('-u', '--uppercase', type=str, dest="caps", metavar="Uppercase", default="y",
                    help="Adds capital letters y for yes, n for no. Defaults to y")
parser.add_argument('-s', '--specials', type=str, dest="specials", metavar="specials", default="y",
                    help="Adds special characters to the password y for yes, n for no. Defaults to y")
parser.add_argument('-c', '--copy', type=str, dest="copy", metavar="copy", default="n",
                    help="Allows copying to clipboard y for yes, n for no. Defaults to n")

args = parser.parse_args()

def generatePassword():
    password = []
    numWords = args.words
    if args.caps == "n":
        password = wordPicker(randNumPicker(numWords))
    elif args.caps == "y":
        password = (capitilizeRandomLetters(wordPicker(randNumPicker(numWords))))
    else:
        print("Invalid argument in --caps, please enter in y or n format")
        quit()
        
    if args.specials == "n":
        pass
    elif args.specials == "y":
        password = addSpecialCharacters(password)
    else:
        print("Invalid argument in --specials, please enter in y or n format")
        quit()
    returnPhrase = "".join(password)
    
    if args.numbers == "n":
        pass
    elif args.numbers == "y":
        numMax = 999999
        number = s.randbelow(numMax)
        returnPhrase = returnPhrase + str(number)
    else:
        print("Invalid argument in --numbers, please enter in y or n format")
        quit()
    
    return returnPhrase



finalPassword = generatePassword()
if args.copy == "y":    
    pyperclip.copy(finalPassword)
    print("Password is copied to clipboard!")
elif args.copy == "n":
    pass
else:
    print("Invalid argumenht in --copy, please enter in y or n format")
print(finalPassword)





