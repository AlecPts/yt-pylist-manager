#from controller.controller import Controller
from model.linked_list import LinkedList
from view.window import Window


def main():
    playlist = LinkedList()
    window = Window(playlist)

    # Initialize category
    musicCategory = LinkedList()
    tutoCategory = LinkedList()
    asmrCategory = LinkedList()

    # Initialize playlist
    rockPlaylist = LinkedList()
    electroPlaylist = LinkedList()
    magicTutoPlaylist = LinkedList()
    minecraftTutoPlaylist = LinkedList()
    marioGameplayAsmrPlaylist = LinkedList()
    playlist = [rockPlaylist, electroPlaylist, magicTutoPlaylist, minecraftTutoPlaylist, marioGameplayAsmrPlaylist]

    # Initialiaze playlist data
    for pl in playlist:
        for j in range(3):
            pl.add(("Item", j))

    # Add playlist to category
    musicCategory.add(rockPlaylist)
    musicCategory.add(electroPlaylist)
    tutoCategory.add(magicTutoPlaylist)
    tutoCategory.add(minecraftTutoPlaylist)
    asmrCategory.add(minecraftTutoPlaylist)
    asmrCategory.add(marioGameplayAsmrPlaylist)


    # Afficher les vidéos initiales
    window.fill_playlist()

    # Run
    window.mainloop()


# Entry point
if __name__ == "__main__":
    main()
