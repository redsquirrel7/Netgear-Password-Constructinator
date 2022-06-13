#!/usr/bin/env python
#
# _____     _                      _____                             _
#|   | |___| |_ ___ ___ ___ ___   |  _  |___ ___ ___ _ _ _ ___ ___ _| |
#| | | | -_|  _| . | -_| .'|  _|  |   __| .'|_ -|_ -| | | | . |  _| . |
#|_|___|___|_| |_  |___|__,|_|    |__|  |__,|___|___|_____|___|_| |___|
#              |___|
#
#   _____             _               _   _         _
#  |     |___ ___ ___| |_ ___ _ _ ___| |_|_|___ ___| |_ ___ ___
#  |   --| . |   |_ -|  _|  _| | |  _|  _| |   | .'|  _| . |  _|
#  |_____|___|_|_|___|_| |_| |___|___|_| |_|_|_|__,|_| |___|_|   v0.2.0
#                                                                      
# Generates default wifi passwords for Netgear routers
#
# By: Squ1rr3l
# Twitter: @redsquirrel_7
#
# Adjective and Noun files downloaded from: http://www.ashley-bovan.co.uk/words/partsofspeech.html
#


adjectives = []
nouns = []
numbers = []


# Get the words from adjectives.txt and nouns.txt
def get_words():
    global adjectives
    global nouns
    f = open("adjectives.txt", "r")
    a = f.read()
    adjectives = a.split('\n')
    f.close()
    
    f = open("nouns.txt", "r")
    n = f.read()
    nouns = n.split('\n')
    f.close()

# Generate a list of numbers from 000 to 999
def number_gen():
    global numbers
    number = 0
    while number <= 999:
        if len(str(number)) == 3:
            numbers.append(str(number))
            number += 1
        elif len(str(number)) == 2:
            numbers.append("0" + str(number))
            number += 1
        else:
            numbers.append("00" + str(number))
            number += 1

# Smoosh all of it together into juicy default passwords!
# Uncomment the lines in this function to create a password file
# I do not recommend you do this however...
# The file will be freaking massive!
def smoosh():
    global adjectives
    global nouns
    global numbers
    #f = open("default-netgear-passwords.txt", "w+")  
    for a in adjectives:
        for n in nouns:
            for i in numbers:
                password = str(a) + str(n) + str(i)
                password = password.lower()
                print(password)
                #f.write(password + "\n")
    #f.close()





get_words()
number_gen()
smoosh()
