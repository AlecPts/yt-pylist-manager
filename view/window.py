import tkinter as tk

from model.playlist import Playlist

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


        ## CONTROL FRAME
        controls_frame = tk.Frame(self)
        controls_frame.pack()


        ## BUTTON
        # Create the add button
        self.btn_add = tk.Button(controls_frame, text="Add")
        self.btn_add.grid(row=0, column=0, padx=10)


        # Initialiaze playlist data
        self.pl = Playlist()
        self.pl.add("https://youtu.be/rrrbO-MaerM?si=VHbSvdLtzcV602Dc")
        self.pl.add("https://youtu.be/rrrbO-MaerM?si=VHbSvdLtzcV602Dc")
        self.pl.add("https://youtu.be/rrrbO-MaerM?si=VHbSvdLtzcV602Dc")
        self.pl.add("https://youtu.be/rrrbO-MaerM?si=VHbSvdLtzcV602Dc")
        self.pl.add("https://youtu.be/rrrbO-MaerM?si=VHbSvdLtzcV602Dc")

        # Create the listbox
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill="x", padx=10, pady=10)

        # Fill the playlist
        self.fill_playlist()

        # Run
        self.mainloop()



    # Function that recover videos from the list and displays them in the playlist
    def fill_playlist(self):
        video_pos = 1

        while self.pl.access_by_position(video_pos) is not None:
            self.listbox.insert(tk.END, self.pl.access_by_position(video_pos))
            video_pos += 1



