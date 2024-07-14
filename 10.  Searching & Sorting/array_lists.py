""" Practical Task One"""


"""

Task:
1. Design a class called Album. The class should contain:
The data fields album_name (String), number_of_songs (int) and
album_artist (String).

2. A __str__ method that returns a string that represents an Album
object in the following format:
(album_name, album_artist, number_of_songs).

3. Create a new list called albums1, add five albums to it and print it out.
4. Sort the list according to the number_of_songs and print it out. (You may
want to understand the key parameter in the sort method).
5. Swap the element at position 1 of albums1 with the element at position 2
and print it out.

6. Create a new list called albums2.
Add five albums to the albums2 List and print it out.
Copy all of the albums from albums1 into albums2.

7. Add the following two elements to albums2:
(Dark Side of the Moon, Pink Floyd, 9)
(Oops!... I Did It Again, Britney Spears, 16)

8. Sort the albums in albums2 alphabetically according to the album name
and print it out.
9. Search for the album Dark Side of the Moon in albums2 and print out the
index of the album in the List

"""

from operator import itemgetter, attrgetter


class Album():

    # Constructor Method that allows us to set the characteristics
    # as instance variables
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = str(album_name)
        self.album_artist = str(album_artist)
        self.number_of_songs = int(number_of_songs)
    def __str__(self):
        return str((self.album_name, self.album_artist, self.number_of_songs))

# Initialised an empty list to store the email objects.
album1 = []
album2 = []

# Method to populate multiple albums to seperate lists
def populate_lsts():

    first = Album("Power of the dollar", "50 cent", 18)
    second = Album("Get Rich or Die Tryin'", "50 cent", 16)
    third = Album("Big Conspiracy", "J Hus", 13)
    fourth = Album("Real Back in Style", "Potter Payper", 15)
    fifth = Album("Made in Lagos", "Wizkid", 14)
    sixth = Album("Good Kid, M.A.A.D City", "Kendrick Lamar", 12)
    seventh = Album("Born Sinner", "J Cole", 16)
    eighth = Album("One and Only", "Sheff G", 12)
    ninth = Album("Ella Mai", "Ella Mai", 16)
    tenth = Album("If Orange Was A Place", "Tems", 5)
    

    album1.append(first)
    album1.append(second)
    album1.append(third)
    album1.append(fourth)
    album1.append(fifth)

    album2.append(sixth)
    album2.append(seventh)
    album2.append(eighth)
    album2.append(ninth)
    album2.append(tenth)

populate_lsts()


# Method to iterate through objects using enumerate function
def list_albums(lst):
    print("\nAlbum List:\n")
    for idx, album in enumerate(lst):
        print(f"{idx+1}.\n"
              f"Album name: {album.album_name}\n"
              f"Artist: {album.album_artist}\n"
              f"Number of songs: {album.number_of_songs}\n")

        # Using '.album_name' ensures we print out every album_name,
        # in the first list
        # as opposed to a singular one e.g. album.album_name


print()

# We can print the object below because of the __str__ function
print(Album("Power of the dollar", "50 cent", 18))
print()

# This line sorts the list album1 based on the attribute 'number_of_songs',
# of the Album objects in descending order.
album1 = sorted(album1, key=attrgetter('number_of_songs'), reverse=True) 


print("List of Album One before swap:")
list_albums(album1)
print()


# Method for swapping two albums in different lists
def swap(lst1, index, index2, lst2=0):
#     if index < len(lst1) and index2 < len(lst2):
    lst1[index], lst2[index2] = lst2[index2], lst1[index] 
    return lst1, lst2

album1, album2 = swap(album1, 0, 1, album2)

# Method for swapping two albums in one list
def change(lst, index, index2):
    lst[index], lst[index2] = lst[index2], lst[index] 
    return lst


print("List of Album One after swap:")
list_albums(album1)
print()
album1 = change(album1, 0, 1)
list_albums(album1)


print("\nList of Album Two:")
list_albums(album2)
print()

# .extend method allows us to join contents of one list
# to another (album2)
album2.extend(album1)

# .append method allows us to add another album object to list
album2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
album2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

print(Album("Dark Side of the Moon", "Pink Floyd", 9))
print()
print(Album("Oops!... I Did It Again", "Britney Spears", 16))

print("\n\nList of Album Two after additions and sorting:")


# Now, we will sort list using the attribute album_name
album2 = sorted(album2, key=attrgetter('album_name')) 
list_albums(album2)
print()


# Method for linear search
def linear_search(value, my_list):
    
    # Iterate over otems until correct value is found
    # Return value otherwise return none if value is not found
    for i in range(len(my_list)):
        # To iterate through list properly 
        # whilst trying to find a name of an album
        # [i].album_name is needed 
        if my_list[i].album_name == value:
            return (
                f"The album '{value}' has the index: {i}, in the list"
                )
        
        
print(linear_search("Dark Side of the Moon", album2))




