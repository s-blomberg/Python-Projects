# INF360 - Programming in Python
# Stephen Blomberg
# Midterm Project

#[25 points] - Does the program execute with no errors.
#[25 points] - Does the program solve a problem or create something new.
#[25 points] - The program should contain: Good flow control, good use of functions,
#           code should be as clean as possible (i.e. writing the smallest amount
#           of code necessary to complete the function), and contain examples of
#           lists or dictionaries.
#[25 points] - The midterm project should be well documented. Make use of block
#           and line comments to describe the program as a whole, individual
#           functions, and major areas of the project.

#####################################################################################################
#       My project idea is a program that allows me to catalog my record collection by entering     #
#   their album title & artist. I'd like a add/remove function, a search function if it exists,     #
#   a sorting function, a randomize function for picking something to listen to, and a way          #
#   to view the collection once entered into the system. I'd like to add more functionality         #
#   for the final such as more album details, genre, value, if it's for sale in my webshop,         #
#   a running tally of the total collection value, and total value of pending sales.                #
#####################################################################################################

import pyinputplus as pip #pip install --user pyinputplus
import pprint
import random
from myclasses import *

collection = [] #main list, simple for now, will implement a way to store albums as dicts with more
                #infomation inside them such as artist/genre/value etc to store inside the list.

print('''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~Welcome to VinylVault~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~    ''')

while True: #main menu select loop
    menuSelect = pip.inputMenu(['Add',
                                'Remove',
                                'Search',
                                'Sort',
                                'Randomize',
                                'View'],
            prompt='\nChoose an option.\n', numbered=True)
    
    if menuSelect == 'Add':
        print('\n~Add album selected~\n')
        while True: #main loop for adding albums
            print('Please enter the name of the album to add. (or enter nothing to stop):')
            albumAdd = input('> ')
            if albumAdd == '': #break loop with no entry
                print('\n~ No input detected. Returning to menu. ~')
                break
            collection.append(albumAdd) #add to collection list
            print('"' + albumAdd + '"' + ' added to collection.\n')
            
    elif menuSelect == 'Remove':
        print('\n~ Remove album selected. ~\n')
        while True: #main loop for removing albums
            print('Please enter the name of album to remove.' + ' (or enter nothing to stop):')
            try: #attempt to remove album
                albumRemove = input('> ')
                if albumRemove == '': #breaks out if nothing is entered
                   break
                collection.remove(albumRemove) #removes album from our collection list
                print('"' + albumRemove + '"' + ' removed from collection.\n')
            except ValueError:
                print('Album could not be located please try again.') #returns if album not detected
            
    elif menuSelect == 'Search':
        print('\n~ Search collection selected. ~\n')
        while True: #search to verify album exists in the collection
            print('Search an album name: (or enter nothing to stop)') 
            albumSearch = input('> ')
            if albumSearch == '': #breaks out if nothing is entered
                break
            elif albumSearch in collection: #is found
                print('"' + albumSearch + '"' + ' found in collection.')
            elif albumSearch not in collection: #not found
                print('"' + albumSearch + '"' + ' not found in collection.')
        
    elif menuSelect == 'Sort':
        print('\n~ Sort albums selected. ~\n') #sorts collection
        collection.sort(key=str.lower) #converts all items to lowercase to sort
        print('Collection has been sorted.')
                    
    elif menuSelect == 'Randomize': #will randomly select an album from collection
        print('\n~ Randomize album selected. ~\n')
        print('Your randomly selected album is: ' + random.choice(collection))
        
    elif menuSelect == 'View': #displays collection in a viewer friendly list
        print('\n~ Viewing album collection. ~\n')
        for i in collection:
            pprint.pprint(i)


