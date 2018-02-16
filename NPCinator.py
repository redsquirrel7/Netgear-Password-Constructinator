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
#  |_____|___|_|_|___|_| |_| |___|___|_| |_|_|_|__,|_| |___|_|   v0.1.0
#                                                                      
# Generates default wifi passwords for Netgear routers
#
# By: Brad Nelson (Squirrel)
# Twitter: @redsquirrel_7
#

import requests
from bs4 import BeautifulSoup
import time

adjectives = []
nouns = []
numbers = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


# Crawl Merriam-Webster.com and create a list of 
# all nouns and adjectives in the english language
# 
# THIS FUNCTION IS NOT WORKING!!!!
# Pretty sure Merriam-Webster doesn't like me crawling their site
# They seem to be denying the connection after a while and the program crashes
def dictionary_crawler(max_pages):
    global adjectives
    global nouns
    global alphabet
    l = 0
    print("Hold tight ladies and gents! \nJust getting a list of words...")
    while l < len(alphabet):
        page = 1
        letter = input("Input Letter: ") #alphabet[l]
        #print(str(letter))
        url = "https://www.merriam-webster.com/browse/dictionary/" + str(letter)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for span in soup.findAll('span', {'class': 'counters'}):
            page_numbers = span.string
            page_numbers = page_numbers.split(' ')
            max_pages = page_numbers[3]
        while page <= int(max_pages):
            url = "https://www.merriam-webster.com/browse/dictionary/" + str(letter) + "/" + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            for link in soup.findAll('a'):
                url = link.get('href')
                word = link.string
                if str(url) == "/dictionary/" + str(word):
                    page_crawler(url, word)
                    #time.sleep(5)
            page += 1
        l += 1
    adjectives = [a.split(' ')[0] for a in adjectives]
    adjectives = [a.split('-')[0] for a in adjectives]
    nouns = [n.split(' ')[0] for n in nouns]
    nouns = [n.split('-')[0] for n in nouns]
    adjectives = set(adjectives)
    adjectives = list(adjectives)
    nouns = set(nouns)
    nouns = list(nouns)
    f = open("adjectives.txt", "w+")
    for a in adjectives:
        f.write(a + "\n")
    f.close()
    f = open("nouns.txt", "w+")
    for n in nouns:
        f.write(n + "\n")
    f.close()

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



# Crawl webpage of word and determine if it's a 
# noun or adjective. If so, add it to the corresponding list.
def page_crawler(url, word):
    page_url = "https://www.merriam-webster.com" + str(url)
    page_source = requests.get(page_url)
    page_text = page_source.text
    page_soup = BeautifulSoup(page_text, "html.parser")
    print("Crawling page: %s" % page_url)
    for link in page_soup.findAll('span', {'class': 'fl'}):
        word_type = link.text
        if str(word_type) == "adjective": 
            adjectives.append(word)
        elif str(word_type) == "noun":
            nouns.append(word)

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
def smoosh():
    global adjectives
    global nouns
    global numbers
    #f = open("default-netgear-passwords.txt", "w+")
    for a in adjectives:
        for n in nouns:
            for i in numbers:
                password = str(a) + str(n) + str(i)
                print(password)
                #f.write(password + "\n")
    #f.close()





get_words()
number_gen()
smoosh()
