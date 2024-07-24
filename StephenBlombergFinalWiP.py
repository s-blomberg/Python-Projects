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


    ##----------------[Functions]---------------##

#collect album input
def add_album(collection): 

    #add loop
    while True:

        #collect input to fill album dict, pyip for input sanitation
        try:
            title = pyip.inputStr("\nEnter album title: ")
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
            validate_entry = pyip.inputMenu(['Yes','No'],\
                            numbered=True,\
                            prompt="\nIs this information correct?\n")
            if validate_entry == 'No':
                print("Album discarded.")
                break
            else:
                print("\n\tAlbum added successfully!")
                collection.append(album)

            #asks user if they would like to add more albums, or exit
            continue_entry = pyip.inputMenu(['Yes','No'],\
                            numbered=True,\
                            prompt="\nWould you like to enter another album?\n")
            if continue_entry == 'No':
                print("\n\tReturning to Main Menu!")
                break
            else:
                continue
        except:
            print("\nAction could not be completed.")

#identify similar values from each 'category' to remove/search/sort by
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

#function to remove album
def remove_album(collection):

    #remove loop
    while True:
        
        #collect input to remove album
        try:
            remove_album_title = pyip.inputStr("\nEnter album to remove: ")

            #find and remove
            album_found = False
            for album in collection:
                if album['title'] == remove_album_title:
                    collection.remove(album)
                    print(f"\nAlbum Removed: \
            \n   \"{album['title']}\" by {album['artist']} ({album['year']}) \
                \n\tVariant: {album['variant']} \
                \n\tFor sale: {album['sale']}")
                    album_found = True
                    break
            if not album_found:
                print(f"\nAlbum by title \"{remove_album_title}\" not found.")
                
            #asks user if they would like to add more albums, or exit
            continue_remove = pyip.inputMenu(['Yes','No'],\
                            numbered=True,\
                            prompt="\nWould you like to remove another album?\n")
            if continue_remove == 'No':
                print("\n\tReturning to Main Menu!")
                break
            
        except:
            print('Action can not be completed.') 

#function to search collection for album
def find_album(collection):

    #search loop
    while True:  
        find_album = pyip.inputStr("\nEnter album to find: ")

        if find_album == '':
            break
        
        #is found
        elif find_album in collection: 
            print(f"{find_album} found in collection.")
            
        #not found
        else:
            find_album not in collection 
            print(f"{find_album} not found in collection.")

    #asks user if they would like to add more albums, or exit
        continue_entry = pyip.inputMenu(['Yes','No'],\
                        numbered=True,\
                        prompt="\nWould you like to find another album?\n")
        if continue_entry == 'No':
            print("\n\tReturning to Main Menu!")
            break
        else:
            continue

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
                        'Sale',
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
                elif sort_select == 'Sale':
                    print("\n\tSorted by Sale Status successfully!")
                    collection.sort(key=sort_sale)
                    view_collection(collection)
                    break

                #return to main
                if sort_select == 'Main':
                    print("\n\tReturning to Main Menu!")
                    break
    except:
        print("\nAction could not be completed.")

#function to view collection
def view_collection(collection):

    #checks if collection is empty
    try:
        if collection == []:
            print("\n\tNo albums in collection to view.")
            
        #loops through each album in collection in a pre-formatted display
        else:
            print("\nCollection:")
            for i, album in enumerate(collection):
                print(
                f"{i + 1}. \"{album['title']}\" by {album['artist']} ({album['year']}) \
                \n\tVariant: {album['variant']} \
                \n\tFor Sale: {album['sale']}")
    except:
        print("\nAction could not be completed.")

#randomly chooses an album from collection
def random_album(collection):

    #checks if collection is empty
    try:
        if collection == []:
            print("\n\tNo albums in collection to randomize.")

        #display random album if possible
        else:
            random_album = random.choice(collection)
            print(f"\nAlbum Chosen: \
            \n   \"{random_album['title']}\" by {random_album['artist']} ({random_album['year']}) \
                \n\tVariant: {random_album['variant']} \
                \n\tSell: {random_album['sale']}")
    except:
        print("\nAction could not be completed.")


    ##---------------[Main Program]----------------##

#initialize albums repository
collection = [] 

#banner signals program start
print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~Welcome to Vinyl Vault~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

#main
while True: 
    main_select = pyip.inputMenu([
        'Add',
        'Remove',
        'Find',
        'Sort',
        'View',
        'Random',
        'Exit'],
        numbered=True,
        prompt='\nMain Menu:\n')

    #add album in collection
    if main_select == 'Add':
        add_album(collection)

    #remove album in collection
    elif main_select == 'Remove':
        remove_album(collection)

    #search for an album in collection
    elif main_select == 'Find':
        find_album(collection)

    #sort albums by 'category' and view
    elif main_select == 'Sort':
        sort_collection()

    #choose random album in collection
    elif main_select == 'Random':
        random_album(collection)

    #view current collection
    elif main_select == 'View': 
        view_collection(collection)

    #exit program, banner signals program end
    elif main_select == 'Exit':
        print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~Thanks for using Vinyl Vault~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        sys.exit()
