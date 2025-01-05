class NewNode:
    # Initialize Node
    def __init__(self, name: str, val: str):
        self._name = name
        self._value = val
        self._next = None


class LinkedList:
    # Initialize class
    def __init__(self):
        self._first = None
        self._last = None
        self._nb_elt = 0

    def add(self, name: str, val: str, pos: int = None):
        print(pos)

        new_node = NewNode(name, val)

        # Default: Add to the end if no position is specified
        if pos is None:
            if self._nb_elt == 0:
                self._first = new_node
            else:
                self._last._next = new_node

            self._last = new_node
        else:
            # Check if the position is valid
            if pos < 1 or pos > self._nb_elt + 1:
                raise IndexError("ERROR: Position out of range")

            if pos == 1:  # Insert at the beginning
                new_node._next = self._first
                self._first = new_node
                if self._nb_elt == 0:  # Update _last if list was empty
                    self._last = new_node
            else:  # Insert in the middle or end
                previous = None
                current = self._first
                count = 1

                while count < pos:
                    previous = current
                    current = current._next
                    count += 1

                new_node._next = current
                if previous is not None:
                    previous._next = new_node

                if pos == self._nb_elt + 1:  # Update _last if added at the end
                    self._last = new_node

        self._nb_elt += 1


    def remove(self, pos: int):
        print(pos)

        # Check empty list
        if self._first is None:
            raise ValueError("ERROR : List is empty")

        # Check invalid position
        if pos < 1 or pos > self._nb_elt:
            raise IndexError("ERROR : Position _value out of range")

        previous = None
        current = self._first
        count = 1

        while pos > count:
            previous = current
            current = current._next
            count += 1

        removed_video = current

        # Remove node
        if previous is None:  # Remove _first node
            self._first = current._next
        else:
            previous._next = current._next

        # Update _last node
        if current == self._last:
            self._last = previous

        # Update number of element
        self._nb_elt = self._nb_elt - 1

        return removed_video

    def access_by_position(self, pos):
        val_index = None

        if pos >= 1:
            current = self._first
            count = 1

            while current != None and count < pos:
                current = current._next
                count += 1

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
        count = 1

        while current._value != val:
            current = current._next
            count += 1

        return count


    def display(self, depth):
        current = self._first

        if current is not None:
            print("[")

            i = 1
            while True:
                if current is not None:
                    print("\t" * (depth + 1), ">", i, ":", current._name, " ", current._value)
                    current = current._next
                else:
                    #print("\t" * depth, "]")
                    break
                i += 1
        else:
            print("[")



