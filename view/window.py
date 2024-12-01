import tkinter as tk

#import main
#from view import PlaylistView


class Window(tk.Tk):
    def __init__(self):

        # Main setup
        super().__init__()
        self.title("My YouTube playlist")
        self.geometry("800x500")

        # Initialize playlist view
        #self.playlist_menu = PlaylistView(self)

        # Create the playlist
        self.listbox = tk.Listbox(self)
        #self.fill_playlist()
        self.listbox.pack(fill="x", padx=10, pady=10)

        # Run
        self.mainloop()

    # Function that recover videos from the list and displays them in the playlist
    #def fill_playlist(self):
        #pl = main.playlist
        #self.listbox.insert(1, pl.access_by_position(1))



