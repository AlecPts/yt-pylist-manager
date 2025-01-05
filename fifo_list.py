from typing import Optional


class FifoNode:
    # Initialize Node
    def __init__(self, name, val):
        self._name = name
        self._value = val
        self._next = None


class FifoList:
    # Initialize class
    def __init__(self):
        self._first = None
        self._last = None
        self._nb_elt = 0


    def is_empty(self):
        b = (self._first is None)
        return b


    def add(self, name, val):
        new_node = FifoNode(name, val)
        if self.is_empty():
            self._last = new_node
            self._first = self._last
        else:
            self._last._next = new_node
            self._last = self._last._next

        self._nb_elt += 1


    def unshift(self) -> Optional[FifoNode]:
        current = self._first

        if current is None:
            return None

        self._first = current._next
        self._nb_elt -= 1

        return current


    def display(self):
        current = self._first
        count = 1

        print("\nWaiting list:")

        while True:
            if current is not None:
                print(f" {count}:", current._name, current._value)
                current = current._next
                count += 1
            else:
                break
