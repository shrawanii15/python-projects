import random


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration})"


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist, duration):
        new_song = Song(title, artist, duration)

        if not self.head:
            self.head = new_song
            return new_song

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_song
        new_song.prev = temp
        return new_song

    def delete_song(self, title):
        temp = self.head

        while temp:
            if temp.title.lower() == title.lower():

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print(f"Deleted: {temp}")
                return temp

            temp = temp.next

        print("Song not found.")

    def search_song(self, title):
        temp = self.head
        pos = 1

        while temp:
            if temp.title.lower() == title.lower():
                print(f"Found at position {pos}: {temp}")
                return temp

            temp = temp.next
            pos += 1

        print("Song not found.")

    def display(self, current=None):
        print("\nPlaylist:")
        print("-" * 50)

        temp = self.head
        i = 1

        while temp:
            marker = " <-- Playing" if temp == current else ""
            print(f"{i}. {temp}{marker}")
            temp = temp.next
            i += 1

        print("-" * 50)


class Player:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current = playlist.head
        self.repeat = False

    def play(self):
        print(f"\nNow Playing: {self.current}")

    def next(self):
        if self.repeat:
            print(f"Repeating: {self.current}")
            return

        if self.current.next:
            self.current = self.current.next
            print(f"Next Song: {self.current}")
        else:
            print("End of playlist")

    def prev(self):
        if self.current.prev:
            self.current = self.current.prev
            print(f"Previous Song: {self.current}")
        else:
            print("At beginning")

    def shuffle(self):
        songs = []
        temp = self.playlist.head

        while temp:
            songs.append(temp)
            temp = temp.next

        self.current = random.choice(songs)
        print(f"Shuffled to: {self.current}")

    def toggle_repeat(self):
        self.repeat = not self.repeat
        print(f"Repeat Mode: {'ON' if self.repeat else 'OFF'}")



def main():
    playlist = Playlist()

   
    songs = [
        ("Shape of You", "Ed Sheeran", "3:53"),
        ("Blinding Lights", "The Weeknd", "3:20"),
        ("Believer", "Imagine Dragons", "3:24"),
        ("Levitating", "Dua Lipa", "3:23"),
        ("Perfect", "Ed Sheeran", "4:40"),
    ]

    print("\nAdding Songs...")
    for t, a, d in songs:
        playlist.add_song(t, a, d)

    player = Player(playlist)

  
    playlist.display(player.current)

  
    player.play()

  
    player.next()
    player.next()

  
    player.prev()

   
    print("\nSearching for 'Believer'")
    playlist.search_song("Believer")

  
    print("\nDeleting 'Levitating'")
    playlist.delete_song("Levitating")

  
    playlist.display(player.current)

  
    print("\nShuffle:")
    player.shuffle()

  
    print("\nToggle Repeat:")
    player.toggle_repeat()
    player.next()

    print("\nFinal Playlist State:")
    playlist.display(player.current)


if __name__ == "__main__":
    main()