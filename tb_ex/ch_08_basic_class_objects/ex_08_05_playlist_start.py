# file: ex_08_05_playlist_start.py
import random

class Playlist:
    def __init__(self, name):
        # TODO: store _name and initialise _songs as empty list
        self._name = name
        self._songs = []

    @property
    def name(self):
        # TODO: return _name
        return self._name

    @name.setter
    def name(self, value):
        # TODO: set _name, raise ValueError if empty string
        if value.strip() == "":
            raise ValueError("kan ikke være tom")
        self._name = value
        

    def add(self, song):
        # TODO: append song to _songs
        self._songs.append(song)

    def remove(self, song):
        # TODO: remove song from _songs
        # Print a message if the song is not found
        if song in self._songs:
            self._songs.remove(song)
        else:
            print(f"{song} finnes ikke i spillelisten")

    def shuffle(self):
        # TODO: shuffle _songs in place using random.shuffle
        random.shuffle(self._songs)

    def __len__(self):
        # TODO: return number of songs
        return len(self._songs)

    def __contains__(self, song):
        # TODO: return True if song is in _songs
        return song in self._songs

    def __str__(self):
        # TODO: return formatted string with name, count, and numbered song list
        result = f"{self._name}, {len(self._songs)} song \n"
        for i, song in enumerate(self._songs, start=1):
            result += f"{i}. {song}\n"
        return result


if __name__ == "__main__":
    p = Playlist("Road Trip")
    p.add("Bohemian Rhapsody")
    p.add("Hotel California")
    p.add("Stairway to Heaven")
    p.add("Sweet Child O' Mine")

    print(p)
    print(f"'Hotel California' in playlist: {'Hotel California' in p}")
    print(f"'Yesterday' in playlist: {'Yesterday' in p}")
    print(f"Length: {len(p)}")

    p.remove("Hotel California")
    print(f"\nAfter removing 'Hotel California':")
    print(p)
