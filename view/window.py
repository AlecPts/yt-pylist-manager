import tkinter as tk

class Window(tk.Tk):
    def __init__(self, playlist):
        # Main setup
        super().__init__()
        self.title("My YouTube Playlist")
        #self.geometry("800x500")
        self.configure(padx=10, pady=10)
        self.playlist = playlist  # Référence au contrôleur

        ## CONTROL FRAME
        #controls_frame = tk.Frame(self)
        #controls_frame.pack()

        # Add video entry
        self.entry_video = tk.Entry(self)
        self.entry_video.grid(row=0, column=0)


        # Button
        self.btn_add = tk.Button(self, text="Add", command=self.add_video)
        self.btn_add.grid(row=0, column=1)

        self.btn_remove = tk.Button(self, text="Remove", command=self.remove_video)
        self.btn_remove.grid(row=0, column=2)


        # Listbox for displaying playlist
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        #self.listbox.pack(fill="none")
        self.listbox.configure(width=50)


    def add_video(self):
        video_url = self.entry_video.get()
        if video_url:
            self.playlist.add(video_url)  # Add video to linked list
            self.entry_video.delete(0, tk.END)
            self.fill_playlist()

    def remove_video(self):
        video_to_remove = self.listbox.curselection()[0] + 1
        if video_to_remove:
            self.playlist.remove(video_to_remove)
            self.fill_playlist()

    def fill_playlist(self):
        self.listbox.delete(0, tk.END)

        nb_video = 1
        while self.playlist.access_by_position(nb_video):
            self.listbox.insert(tk.END, self.playlist.access_by_position(nb_video))
            nb_video += 1
