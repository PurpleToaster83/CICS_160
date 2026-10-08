class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def play(self):
        return f'🎵 {self.title} 🎵'
    def __str__(self):
        #__float__
        #__int__
        #__list__
        # how to construct a string from a song object 
        # str(song) looks into __str__ for how to convert a Song object to string
        return f'{self.title} by {self.artist}'
    def __repr__(self):
        # representation of object - helps you look at type
        # repr(1) --> 1 ; repr('1') --> 1
        return f'Song({self.title}, {self.artist})'