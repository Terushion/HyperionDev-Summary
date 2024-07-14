"""Practical Task 1 model answers"""

class Album:
    """Class for representing an album"""

    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


# Add 5 instances of an Album to the albums1 list
albums1 = [Album("Album1", "Artist1", 12),
           Album("Album2", "Artist2", 18),
           Album("Album3", "Artist3", 16),
           Album("Album4", "Artist4", 10),
           Album("Album5", "Artist5", 20)]

# Add 5 instances of an Album to the albums2 list

albums2 = [Album("Album6", "Artist6", 14),
           Album("Album7", "Artist7", 15),
           Album("Album8", "Artist8", 17),
           Album("Album9", "Artist9", 11),
           Album("Album10", "Artist10", 13)]


def display_albums(albums):
    """
    Argument: The chosen album to display (either album1 or album2 list)
    Return: Displays the content of the chosen album
    """
    for album in albums:
        print(album)


def sort_number_of_songs(albums):
    """
    Argument: The chosen album to sort by number of songs
    Return: Sorts the chosen album by number of songs (ascending order)
    """
    # Reference: https://docs.python.org/3/howto/sorting.html#key-functions
    albums.sort(key=lambda album: album.number_of_songs)

    # Display the sorted albums1 list
    print("\nAlbum sorted by number of songs:")
    display_albums(albums)


def swap_positions(albums, position1, position2):
    """
    Arguments: The chosen album to swap elements, and the positions to swap
    Return: Swaps the elements at the given positions
    """
    # Used -1 since it's using indexes
    albums[position1 - 1], albums[position2 - 1] = albums[position2 - 1], albums[position1 - 1]
    print(f"\nAlbum after swapping positions {position1} and {position2}: ")
    display_albums(albums1)


def find_index(albums, album_name):
    """
    Arguments: The chosen album to search and the album name to search for
    Return: Returns the index of the album name in the chosen album
    """
    for index, album in enumerate(albums):
        if album.album_name == album_name:
            print(f"\nIndex of '{album_name}': {index}")


# Display the albums1 list
print("Album 1:")
display_albums(albums1)

# Display albums1 sorted by number of songs in ascending order
sort_number_of_songs(albums1)

# Display the albums1 list after swapping albums 1 and 2 in the list
swap_positions(albums1, 1, 2)

# Display album2 list
print("\nAlbum 2:")
display_albums(albums2)

# Copy all the albums from albums1 into albums2 and display it
albums2.extend(albums1)
print("\nAlbum 2 after copying Album 1 into it:")
display_albums(albums2)

# Add 2 more albums to albums2
albums2.extend([
    Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!... I Did It Again", "Britney Spears", 16)
])

# Sort albums alphabetically by album name and display it
albums2.sort(key=lambda album: album.album_name)
print("\nAlbum 2 sorted alphabetically:")
display_albums(albums2)

# Displays the index of "Dark Side of the Moon" in albums2
find_index(albums2, "Dark Side of the Moon")
