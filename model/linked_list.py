class LinkedList:

    class NewNode:
        # Initialize Node
        def __init__(self, val):
            self._value = val
            self._next = None

    # Initialize class
    def __init__(self):
        self._first = None
        self._last = None
        self._nb_elt = 0


    def add(self, val):
        new_node = self.NewNode(val)

        if self._nb_elt == 0:
            self._first = new_node
        else:
            self._last._next = new_node
            
        self._last = new_node
        self._nb_elt += 1

        ## DEBUG
        for elt in range(self._nb_elt):
            print(self.access_by_position(elt + 1))


    def remove(self, pos):
        # Check empty list
        if self._first is None:
            raise ValueError("ERROR : List is empty")

        # Check invalid position
        if pos < 1 or pos > self._nb_elt:
            raise IndexError("ERROR : Position value out of range")

        previous = None
        current = self._first
        counter = 1

        while pos > counter:
            previous = current
            current = current._next
            counter += 1

        removed_val = current._value

        # Remove node
        if previous is None:  # Remove first node
            self._first = current._next
        else:
            previous._next = current._next

        # Update last node
        if current == self._last:
            self._last = previous

        # Update number of element
        self._nb_elt = self._nb_elt - 1

        ## DEBUG
        for elt in range(self._nb_elt):
            print(self.access_by_position(elt + 1))

        return removed_val


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
