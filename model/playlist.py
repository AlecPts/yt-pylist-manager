class Playlist:

    class Video:

        def __init__(self, val):
            self._value = val
            self._next = None

    def __init__(self):
        self._first = None
        self._last = None
        self._nb_elt = 0

    # Function to add a video to the playlist
    def add(self, val):
        new_video = Playlist.Video(val)

        if self._nb_elt == 0:
            self._first = new_video
        else:
            self._last._next = new_video
            
        self._last = new_video
        self._nb_elt += 1

    # Function to access a video via its position in the playlist
    def access_by_position(self, pos):
        val_index = None
        
        if pos >= 1:
            current = self._first
            counter = 1
            
            while current != None and counter < pos:
                current = current._next
                counter += 1
                
            if current != None:
                val_index = current._value
                
        return val_index


    # Function to access a video via its title in the playlist
    def access_by_value(self, val):
        current = self._first
        found = False

        while current != None and current._value != val:
            current = current._next

        if current != None:
            found = True

        return found


    # Function to get the position of a video in the playlist
    def get_position(self, val):
        current = self._first
        counter = 1
        
        while current._value != val:
            current = current._next
            counter += 1
            
        return counter


    # Function to remove a video from the playlist
    def remove(self, pos):
        previous = None
        current = self._first
        counter = 1

        while pos > counter:
            previous = current
            current = current._next
            counter += 1

        removed_val = current._value

        if previous == None:
            self._first = current._next
        else:
            previous._next = current._next

        if current == self._last:
            self._last = previous

        self._nb_elt = self._nb_elt - 1

        return removed_val


    """
    def set(self, p, nouvVal):
        current = self._first
        counter = 1
        while p > i:
            current = current._next
            counter += 1
        vieilleVal = current._value
        current._value = nouvVal
        return vieilleVal
    """
