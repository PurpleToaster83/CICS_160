from Song import Song

class Playlist:
    def __init__(self, name, songs=[], mode='in-order'):
        self.name = name
        self.songs = songs
        self.mode = mode
        self._index = 0

    def __iter__(self):
        self._index = 0
        if self.mode == 'in-order':
            self._order = list(range(len(self.songs)))
        elif self.mode == 'shuffle-no-repeats':
            pass