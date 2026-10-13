from Song import Song
import random

class Playlist:
    def __init__(self, name, songs=[], mode='in-order'):
        self.name = name
        self.songs = songs
        self.mode = mode
        self._index = 0
        self._order = []

    def __iter__(self):
        self._index = 0
        if self.mode == 'in-order':
            self._order = list(range(len(self.songs)))
        elif self.mode == 'shuffle-no-repeats':
            self._order = list(range(len(self.songs)))
            random.shuffle(self._order)
        return self

    def __next__(self):
        if self._index < len(self._order):
            song_index = self._order[self._index]
            song = self.songs[song_index]
            self._index += 1
            return song
        else:
            raise StopIteration

if __name__ == "__main__":
    s = [Song(f"Song {i}", f"Artist {i}") for i in range(8)]
    p = Playlist("Example", s)
    p.mode = "shuffle-no-repeats"
    for son in p:
        print(son.play())