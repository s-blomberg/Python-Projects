# INF360 - Programming in Python
# Stephen Blomberg
# Final Project


    ##-----------------[Rubric]-----------------##

##[20 points] Does the program execute with no errors?
##[20 points] The program should contain: Good flow control, good use of functions,
##      code should be as clean as possible (i.e. writing the smallest amount
##      of code necessary to complete the function), and contain examples
##      of lists or dictionaries.
##[20 points] The project should be well documented. Make use of block and line
##      comments to describe the program as a whole, individual functions,
##      and major areas of the project.
##[20 points] Use of the logging module. This should be used in place of where you
##      might have had print statements (unless your project was intended to
##      have console output. Refer to Chapter 10 – Debugging. You should
##      import the module, setup the basic config, and then you must have a
##      combination of logging.debug and logging.critical statements used
##      appropriately. You can use any additional logging level you choose,
##      possibly logging.warning
##[20 points] Use of Object-Oriented Programming. This can be you creating your
##      own classes and modules OR the use of third party modules. If using
##      third party modules, be sure to put in the comments the
##      packages that need to be installed (probably from pip).


    ##-----------------[Concept]----------------##

##  My project idea is a "Vinyl Vault", a program that takes user input to build a database.
##  The program should be able to:
##      1. Add/remove albums.
##      2. Search database for existing entry.
##      3. Sort collection by title or artist.
##      4. Randomly choose an album from the collection.
##      5. View the collection in a pleasant format.
##      6. Write collection to file/read file to load collection.


    ##-----------------[Modules]----------------##

#please run "pip install --user pyinputplus" in your terminal to install.
import pyinputplus as pyip
import random
import sys
import json


    ##----------------[Functions]---------------##

#collect album input
def add_album(collection): 

    #add loop
    while True:

        #collect input to fill album dict, pyip for input sanitation
        try:
            print("\n\tAdd Album to Collection:\n")
            title = pyip.inputStr("Enter album title: ")
            artist = pyip.inputStr("Enter album artist: ")
            year = pyip.inputInt("Enter album release year: ", min=1850, max=2100)
            variant = pyip.inputStr("Enter vinyl variant/color: ")
            sale = pyip.inputYesNo("Is this album for sale?: ")

            #album to be added to collection, auto formats inputs
            album = { 
                'title': title.title(),
                'artist': artist.title(),
                'year': year,
                'variant': variant.title(),
                'sale': sale.capitalize()}

            #asks if user input is accurate before appending
            validate_entry = pyip.inputMenu(["Yes","No"],\
                            numbered=True,\
                            prompt="\nIs this information correct?\n")
            if validate_entry == 'No':
                print("\n\tAlbum discarded!")
                break
            else:
                print("\n\tAlbum added successfully!")
                collection.append(album)

            #asks user if they would like to add more albums, or exit
            continue_entry = pyip.inputMenu(["Yes","No"],\
                            numbered=True,\
                            prompt="\nWould you like to enter another album?\n")
            if continue_entry == 'No':
                print("\n\tReturning to Main Menu!")
                break
        except:
            print("\nError: Add album could not be completed.")

#function to remove album
def remove_album(collection):

    #checks if collection is empty
    while True:
        try:
            if collection == []:
                print("\n\tNo albums in collection to remove.")
                break

            #iterate through collection to find title to remove, case insensitive
            else:
                print("\n\tRemove album from collection:\n")
                remove_title_album = pyip.inputStr("Enter album title: ")
                for album in collection:
                    if album['title'] != remove_title_album.title():
                        print(f'\n\tAlbum by title "{remove_title_album.title()}" not in collection.')
                        break
                    else:

                        collection.remove(album)
                        print(f'\nAlbum Removed:')
                        print(f'    "{album['title']}" by {album['artist']} ({album['year']})')
                        print(f'        Variant: {album['variant']}')
                        print(f'        For sale: {album['sale']}')
                        break
                    
                #asks user if they would like to remove more albums, or exit
                continue_remove = pyip.inputMenu(["Yes","No"],\
                                numbered=True,\
                                prompt="\nWould you like to remove another album?\n")
                if continue_remove == 'No':
                    print("\n\tReturning to Main Menu!")
                    break
                
        except:
            print("Error: Remove album could not be completed.") 

#function to search collection for album
def find_album(collection):

    #checks if collection is empty
    while True:
        try:
            if collection == []:
                print("\n\tNo albums in collection to find.")
                break

            #iterate through collection to find title, case insensitive
            else:
                print("\n\tFind album in collection:\n")
                find_title_album = pyip.inputStr("Enter album title: ")
                for album in collection:
                    if album['title'] != find_title_album.title():
                        print(f'\n\tAlbum by title "{find_title_album.title()}" not in collection.')
                        break
                    else:
                        print(f'\nAlbum Found:')
                        print(f'    "{album['title']}" by {album['artist']} ({album['year']})')
                        print(f'        Variant: {album['variant']}')
                        print(f'        For sale: {album['sale']}')
                        break
                    
                #asks user if they would like to remove more albums, or exit
                continue_remove = pyip.inputMenu(["Yes","No"],
                                numbered=True,
                                prompt="\nWould you like to find another album?\n")
                if continue_remove == 'No':
                    print("\n\tReturning to Main Menu!")
                    break
                
        except:
            print("Error: Find album could not be completed.")  
            
#identify similar values from each album to sort by
def sort_artist(albums):
    return albums['artist']
def sort_title(albums):
    return albums['title']
def sort_year(albums):
    return albums['year']
def sort_variant(albums):
    return albums['variant']
def sort_sale(albums):
    return albums['sale']

#function to access sort menu
def sort_collection():

    #checks if collection is empty
    try:
        if collection == []:
            print("\n\tNo albums in collection to sort.")

        #sort menu loop
        else:
            while True:
                sort_select = pyip.inputMenu([
                        'Title',
                        'Artist',
                        'Year',
                        'Variant',
                        'Sale Status',
                        'Main'],
                        numbered=True,
                        prompt='\nSort by:\n')

                #sort by title
                if sort_select == 'Title':
                    print("\n\tSorted by Title successfully!")
                    collection.sort(key=sort_title)
                    view_collection(collection)
                    break

                #sort by artist
                elif sort_select == 'Artist':
                    print("\n\tSorted by Artist successfully!")
                    collection.sort(key=sort_artist)
                    view_collection(collection)
                    break

                #sort by year
                elif sort_select == 'Year':
                    print("\n\tSorted by Year successfully!")
                    collection.sort(key=sort_year)
                    view_collection(collection)
                    break

                #sort by variant
                elif sort_select == 'Variant':
                    print("\n\tSorted by Variant successfully!")
                    collection.sort(key=sort_variant)
                    view_collection(collection)
                    break

                #sort by sale status
                elif sort_select == 'Sale Status':
                    print("\n\tSorted by Sale Status successfully!")
                    collection.sort(key=sort_sale)
                    view_collection(collection)
                    break

                #return to main
                if sort_select == 'Main':
                    print("\n\tReturning to Main Menu!")
                    break
    except:
        print("\nError: Sort collection could not be completed.")

#function to view collection
def view_collection(collection):

    #checks if collection is empty
    try:
        if collection == []:
            print("\n\tNo albums in collection to view.")
            
        #loops through each album in collection with a pre-formatted display
        else:
            print("\nCollection:")
            for i, album in enumerate(collection):
                print(f'{i+1}. "{album['title']}" by {album['artist']} ({album['year']})')
                print(f'        Variant: {album['variant']}')
                print(f'        For sale: {album['sale']}')
    except:
        print("\nError: View collection could not be completed.")

#randomly chooses an album from collection
def random_album(collection):

    #checks if collection is empty
    try:
        if collection == []:
            print("\n\tNo albums in collection to randomize.")

        #display random album if possible
        else:
            random_album = random.choice(collection)
            print(f'\nRandom Album:')
            print(f'    "{random_album['title']}" by {random_album['artist']} ({random_album['year']})')
            print(f'        Variant: {random_album['variant']}')
            print(f'        For sale: {random_album['sale']}')
    except:
        print("\nError: Randomize could not be completed.")

#commits our album collection to permanent 'vault' file
def save_collection(collection):
    try:
        with open('vinylvault.json', 'w') as file:
            json.dump(collection, file)
        print(f'\n\tCollection saved to "vinylvault.json"')
    except:
        print("\nError: Save collection could not be completed.")

#loads existing 'vault' file to our album collection
def load_collection():
    global collection
    try:
        with open('vinylvault.json', 'r') as file:
            collection = json.load(file)
            print(f'\n\tCollection loaded from "vinylvault.json"')
            return
    except FileNotFoundError:
        print("\n\tNo save file found.")
    except:
        print("\nError: Load could not be completed.")
        

    ##---------------[Main Program]----------------##

#banner signals program start
print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~Welcome to Vinyl Vault~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

#initialize albums repository
collection = [] 

#load collection if exists
load_collection()

#main menu loop
while True: 
    main_select = pyip.inputMenu([
        'Add',
        'Remove',
        'Find',
        'Sort',
        'View',
        'Random',
        'Save & Exit'],
        numbered=True,
        prompt='\nMain Menu:\n')

    if main_select == 'Add':
        add_album(collection)
    elif main_select == 'Remove':
        remove_album(collection)
    elif main_select == 'Find':
        find_album(collection)
    elif main_select == 'Sort':
        sort_collection()
    elif main_select == 'Random':
        random_album(collection)
    elif main_select == 'View': 
        view_collection(collection)
    elif main_select == 'Save & Exit':
        save_collection(collection)
        print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~Thank you for using Vinyl Vault~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        sys.exit()
