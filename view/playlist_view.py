from tkinter import *


class PlaylistView(Frame):
    def __init__(self, parent):

        super().__init__(parent)
        self.listbox = Listbox(parent)


