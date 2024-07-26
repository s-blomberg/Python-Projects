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

import sys
import random
import json
import logging
logging.basicConfig(filename='vinylvaultlog.txt',
    level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
try:
    import pyinputplus as pyip
    logging.debug('Module: pyinputplus loaded successfully.')
except:
    print('Module missing! Please run "pip install --user pyinputplus" in your terminal.')
    logging.critical('Pyinputplus module missing!')
    sys.exit()

    ##----------------[Functions]---------------##

def add_album(collection): 
    logging.debug("Start add album loop.")
    while True:
        try:
            print(f"\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"\t~~~Add Album to Collection (or enter nothing to stop):~~~")
            print(f"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            title = pyip.inputStr("Enter album title: ", blank=True)
            if title == '':
                break
            artist = pyip.inputStr("Enter album artist: ", blank=True)
            if artist == '':
                break
            year = pyip.inputInt("Enter album release year: ", min=1850, max=2100, blank=True)
            if year == '':
                break
            variant = pyip.inputStr("Enter vinyl variant/color: ", blank=True)
            if variant == '':
                break
            sale = pyip.inputYesNo("Is this album for sale?: ", blank=True)
            if sale == '':
                break
            logging.debug("Album inputs receieved and formatted.")

            album = { 
                'title': title.title(),
                'artist': artist.title(),
                'year': year,
                'variant': variant.title(),
                'sale': sale.capitalize()}

            logging.debug("Ask if user input is accurate before appending collection.")
            validate_entry = pyip.inputMenu(["Yes","No"],\
                            numbered=True,\
                            prompt="\nIs this information correct?\n")
            if validate_entry == 'No':
                print("\n\tAlbum discarded!")
                logging.debug("Album discarded.")
                break
            else:
                print("\n\tAlbum added successfully!")
                collection.append(album)
                logging.debug("Album appended to collection.")
        except:
            print("\nError: Add album could not be completed.")
            logging.error("Error: Add album could not be completed.")

def remove_album(collection):
    logging.debug("Start remove album loop.")
    while True:
        try:
            if collection == []:
                print("\n\tNo albums in collection to remove.")
                logging.debug("No albums in collection to remove.")
                break
            else:
                logging.debug("Receive input to find album by title to remove.")
                print(f"\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\t~~~Remove Album from Collection (or enter nothing to stop):~~~")
                print(f"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                remove_title_album = pyip.inputStr("Enter album title: ", blank=True)
                if remove_title_album == '':
                    break
                for album in collection:
                    if album['title'] != remove_title_album.title():
                        print(f'\n\tAlbum by title "{remove_title_album.title()}" not found in collection.')
                        logging.debug("{remove_title_album.title()} not found in collection.")
                        break
                    else:
                        collection.remove(album)
                        print(f'\nAlbum Removed:')
                        print(f'    "{album['title']}" by {album['artist']} ({album['year']})')
                        print(f'        Variant: {album['variant']}')
                        print(f'        For sale: {album['sale']}')
                        logging.debug("{album['title']} removed from collection.")
                        break
        except:
            print("Error: Remove album could not be completed.")
            logging.error("Error: Remove album could not be completed.")

def find_album(collection):
    logging.debug("Start find album loop.")
    while True:
        try:
            if collection == []:
                print("\n\tNo albums in collection to find.")
                logging.debug("No albums in collection to find.")
                break
            else:
                logging.debug("Receive input to find album by title.")
                print(f"\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\t~~~Find Album in Collection (or enter nothing to stop):~~~")
                print(f"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                find_title_album = pyip.inputStr("Enter album title: ",blank=True)
                if find_title_album == '':
                    break
                else:
                    for album in collection:
                        if album['title'] != find_title_album.title():
                            print(f'\n\tAlbum by title "{find_title_album.title()}" not found in collection.')
                            logging.debug('"{find_title_album.title()}" not found in collection.')
                            break
                        else:
                            print(f'\nAlbum Found:')
                            print(f'    "{album['title']}" by {album['artist']} ({album['year']})')
                            print(f'        Variant: {album['variant']}')
                            print(f'        For sale: {album['sale']}')
                            logging.debug('"{find_title_album.title()}" found in collection.')
                            break
        except:
            print("Error: Find album could not be completed.")
            logging.error("Error: Find album could not be completed.")
            
#grouping values from each album to sort by
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

def sort_collection():
    logging.debug("Start sort loop.")
    while True:
        try:
            if collection == []:
                print("\n\tNo albums in collection to sort.")
                logging.debug("No albums in collection to sort.")
                break
            else:
                print(f"\n\t~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\t~~~Sort Collection:~~~")
                print(f"\t~~~~~~~~~~~~~~~~~~~~~~")
                logging.debug("Entering sort menu.")
                sort_select = pyip.inputMenu([
                        'Title',
                        'Artist',
                        'Year',
                        'Variant',
                        'Sale Status',
                        'Main'],
                        numbered=True,
                        prompt='\nSort by:\n')

                if sort_select == 'Title':
                    collection.sort(key=sort_title)
                    print("\n\tSorted by Title successfully!")
                    logging.debug("Sorted by Title successfully.")
                    view_collection(collection)
                    break
                elif sort_select == 'Artist':
                    collection.sort(key=sort_artist)
                    print("\n\tSorted by Artist successfully!")
                    logging.debug("Sorted by Artist successfully.")
                    view_collection(collection)
                    break
                elif sort_select == 'Year':
                    collection.sort(key=sort_year)
                    print("\n\tSorted by Year successfully!")
                    logging.debug("Sorted by Year successfully.")
                    view_collection(collection)
                    break
                elif sort_select == 'Variant':
                    collection.sort(key=sort_variant)
                    print("\n\tSorted by Variant successfully!")
                    logging.debug("Sorted by Variant successfully.")
                    view_collection(collection)
                    break
                elif sort_select == 'Sale Status':
                    collection.sort(key=sort_sale)
                    print("\n\tSorted by Sale Status successfully!")
                    logging.debug("Sorted by Sale Status successfully.")
                    view_collection(collection)
                    break
                elif sort_select == 'Main':
                    print("\n\tReturning to Main Menu!")
                    logging.debug("Returning to Main Menu.")
                    break
        except:
            print("\nError: Sort collection could not be completed.")
            logging.error("Error: Sort collection could not be completed.")

def view_collection(collection):
    logging.debug("Start view collection.")
    try:
        if collection == []:
            print("\n\tNo albums in collection to view.")
            logging.debug("No albums in collection to view.")
        else:
            logging.debug("Iterating collection with a pre-formatted display.")
            print(f"\n\t~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"\t~~~Viewing Collection:~~~")
            print(f"\t~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for index, album in enumerate(collection):
                print(f'{index+1}. "{album['title']}" by {album['artist']} ({album['year']})')
                print(f'        Variant: {album['variant']}')
                print(f'        For sale: {album['sale']}')
    except:
        print("\nError: View collection could not be completed.")
        logging.error("Error: View collection could not be completed.")

def random_album(collection):
    logging.debug("Start randomize album.")
    try:
        if collection == []:
            print("\n\tNo albums in collection to randomize.")
            logging.debug("No albums in collection to randomize.")
        else:
            random_album = random.choice(collection)
            print(f"\n\t~~~~~~~~~~~~~~~~~~~~~~")
            print(f"\t~~~Randomize Album:~~~")
            print(f"\t~~~~~~~~~~~~~~~~~~~~~~")
            print(f'\nAlbum Chosen:')
            print(f'    "{random_album['title']}" by {random_album['artist']} ({random_album['year']})')
            print(f'        Variant: {random_album['variant']}')
            print(f'        For sale: {random_album['sale']}')
            logging.debug("Random album chosen.")
    except:
        print("\nError: Randomize could not be completed.")
        logging.error("Error: Randomize could not be complete.")

def save_collection(collection):
    logging.debug("Start save collection.")
    try:
        with open('vinylvault.json', 'w') as file:
            json.dump(collection, file)
        print(f'\n\tCollection saved to "vinylvault.json"')
        logging.debug('Collection saved to "vinylvault.json"')
    except:
        print("\nError: Save collection could not be completed.")
        logging.error("Save collection could not be completed.")

def load_collection():
    logging.debug("Start load collection.")
    global collection
    try:
        with open('vinylvault.json', 'r') as file:
            collection = json.load(file)
            print(f'\n\tCollection loaded from "vinylvault.json"')
            logging.debug('Collection loaded from "vinylvault.json"')
    except FileNotFoundError:
        print("\n\tNo save file found.")
        logging.debug("No save file found.")
    except:
        print("\nError: Load could not be completed.")
        logging.error("Load could not be completed.")

    ##---------------[Main Program]----------------##

logging.debug("Program start.")
print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~Welcome to Vinyl Vault~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

logging.debug("Album collection initialized.")
collection = [] 

load_collection()

logging.debug("Start main menu loop.")
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
        logging.debug("Program end.")
        sys.exit()
