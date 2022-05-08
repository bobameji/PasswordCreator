# -*- coding: utf-8 -*-
"""
Written by Robert Alfrey
05/06/2022
"""

import secrets as s


def randNumPicker(numStrings):
    #Generate numStrings amount of numbers
    numList = []
    for i in range(numStrings):
        numList.append(s.randbelow(236736))
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

    
def generatePassword(numWords):
    #Generates a password using the functions above, also allows varaiability in the password type
    password = []
    doCapitalize = str(input("Do you want capitial letters? (y)/n: "))
    if doCapitalize == "n":
        password = wordPicker(randNumPicker(numWords))
    else:
        password = (capitilizeRandomLetters(wordPicker(randNumPicker(numWords))))

    
    specialChars = str(input("Do you want special characters? (y)/n: "))
    if specialChars == "n":

        pass
    else:
        password = addSpecialCharacters(password)
      
    returnPhrase = "".join(password)
       
    withNumbers = str(input("Do you want numbers on the end? (y)/n: "))
    if withNumbers == "n":
        pass
    else:
        number = s.randbelow(999999)
        returnPhrase = returnPhrase + str(number)

        

    return returnPhrase
    
    

finalPass = generatePassword(int(input("How many words? ")))
print(finalPass)    






