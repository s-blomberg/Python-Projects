import pyinputplus as pyip #pip install --user pyinputplus

class Album:
    albumCount = 0

    def __init__(self, title=None):
        if title:
            self.title = title
        else:
            self.gettitle()
        self.getartist()
        self.getyear()
        self.getvariant()
        self.getforsale()

    def gettitle(self):
        while True:
            print("What is the title of the album?")
            title = input("> ")
            if title == '':
                print("Blank input not accepted. Please try again.")
            if not title.istitle():
                print("That is not a proper title. Please try again.")
            else:
                self.title = title
                break

    def getartist(self):
        while True:
            print("What is the artist of the album?")
            artist = input("> ")
            if artist == '':
                print("Blank input not accepted. Please try again.")
            if not artist.istitle():
                print("That is not a proper artist name. Please try again.")
            else:
                self.artist = artist
                break

    def getyear(self):
        while True:
            print("What is the release year of the album?")
            year = pyip.inputNum("> ", greaterThan=0, lessThan=3000)
            if year == '':
                print("Blank input not accepted. Please try again.")
            else:
                self.year = year
                break
            
    def getvariant(self):
        while True:
            print("What is the variant/color of the vinyl?")
            variant = input("> ")
            if variant == '':
                print("Blank input not accepted. Please try again.")
            if not variant.istitle():
                print("That is not a proper variant/color. Please try again.")
            else:
                self.variant = variant
                break

    def getforsale(self):
        while True:
            print("Would you like to mark this album for resale?")
            forsale = pyip.inputYesNo(prompt='> ')
            if forsale == '':
                print("Blank input not accepted. Please try again.")
            else:
                self.forsale = forsale
                break
                
        Album.albumCount += 1
        print("\nAlbum entry completed.")
        print('Total vinyl in vault:', Album.albumCount)

    def printalbum(self):
        print("\nAlbum Details:")
        print("\tTitle: " + album1.title)
        print("\tArtist: " + album1.artist)
        print("\tYear: " + str(album1.year))
        print("\tVariant: " + album1.variant)
        print("\tFor sale: " + album1.forsale)





