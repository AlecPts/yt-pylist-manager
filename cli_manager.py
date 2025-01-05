from fifo_list import FifoList

def main_view(root_node, waiting_list, current_video):
    root_node.display()

    if current_video is not None:
        print(f"\nCurrent video: {current_video._name} {current_video._value}")
    else:
        print("Current video: None")

    waiting_list.display()
    print()


def run_cli(tree, root_node, waiting_list, current_video):
    display_main_view = True

    while True:
        # Show main view
        if display_main_view:
            main_view(root_node, waiting_list, current_video)

        user_input = input("> ")
        user_input = user_input.split(" ")

        match user_input[0]:

            # Command "playlist"
            case "playlist":
                display_main_view = True

                match user_input[1]:
                    case "add":
                        playlist_name = user_input[2].split("/")
                        parent_path = []

                        # Get parent path
                        part = 0
                        while part < len(playlist_name) - 1:
                            parent_path.append(playlist_name[part])
                            part += 1

                        tree.add_playlist(parent_path, playlist_name[-1])
                        continue

                    case "remove":
                        playlist_name = user_input[2].split("/")
                        parent_path = []

                        # Get parent path
                        part = 0
                        while part < len(playlist_name) - 1:
                            parent_path.append(playlist_name[part])
                            part += 1

                        tree.remove_playlist(parent_path, playlist_name[-1])
                        continue

                    case _:
                        pass

                continue

            # Command "video"
            case "video":
                display_main_view = True

                match user_input[1]:
                    case "add":
                        try:
                            # Exception
                            if len(user_input) < 3:
                                raise Exception("The path to the video to be added is missing")

                            if len(user_input) < 4:
                                raise Exception("The URL of the video to be added is missing")

                            video_name = user_input[2].split("/")
                            video_url = user_input[3]
                            position = None
                            parent_path = []

                            if len(user_input) == 5:
                                position = int(user_input[4])

                            # Get parent path
                            part = 0
                            while part < len(video_name) - 1:
                                parent_path.append(video_name[part])
                                part += 1

                            tree.add_video(parent_path, video_name[-1], video_url, position)

                        except Exception as e:
                            print(f"ERROR : {e}")

                        continue

                    case "remove":
                        playlist_name = user_input[2].split("/")
                        video_number = int(user_input[3])
                        tree.remove_video(playlist_name, video_number)
                        continue

                    case "move":
                        playlist_name = user_input[2].split("/")
                        old_position = int(user_input[3])
                        new_position = int(user_input[4])
                        tree.move_video(playlist_name, old_position, new_position)


            # Command "play"
            case "play":
                display_main_view = True

                # Clear waiting list
                waiting_list = FifoList()

                # Add playlist to waiting list
                playlist_name = user_input[1].split("/")
                tree.add_videos_to_waiting_list(playlist_name, waiting_list)

                # Play video at selected position
                if len(user_input) == 3:
                    number_to_skip = int(user_input[2])
                    for num in range(number_to_skip):
                        current_video = waiting_list.unshift()

                        if num < number_to_skip - 1:
                            waiting_list.add(current_video._name, current_video._value)
                # Play the first video
                else:
                    current_video = waiting_list.unshift()

                # Show main view
                main_view(root_node, waiting_list, current_video)

                continue

            # Command queue
            case "queue":
                display_main_view = True

                match user_input[1]:

                    case "add":
                        playlist_name = user_input[2].split("/")

                        # Add one video to waiting list
                        if len(user_input) == 4:
                            video_number = int(user_input[3])

                            # Add video selected at top of wainting list
                            tree.add_videos_to_waiting_list(playlist_name, waiting_list, video_number)

                            for video in range(waiting_list._nb_elt - 1):
                                next_video = waiting_list.unshift()
                                waiting_list.add(next_video._name, next_video._value)

                        # Add playlist to waiting list
                        else:
                            old_waiting_list_nb = waiting_list._nb_elt

                            tree.add_videos_to_waiting_list(playlist_name, waiting_list)

                            for video in range(old_waiting_list_nb):
                                next_video = waiting_list.unshift()
                                waiting_list.add(next_video._name, next_video._value)

                        continue

                    case "clear":
                        waiting_list = FifoList()


            # Command "sort"
            case "sort":
                pass

            # Command "help"
            case "help":
                display_main_view = False

                if len(user_input) < 2:

                    # Display all commands
                    if len(user_input) < 2:
                        print("COMMANDS")

                        # Command "play"
                        print(f"\tplay - choose a playlist to play")

                        # Command "playlist"
                        print(f"\tplaylist - add or remove a playlist from the tree structure")

                        # Command "video"
                        print(f"\tvideo - add or remove a video from a playlist")

                        # Command "queue"
                        print(f"\tqueue - add or remove a playlist or video from the queue")

                        # Tips
                        print("\nType “help <command>” for more details")
                else:

                    match user_input[1]:
                        # Command "play"
                        case "play":
                            print(
                                "NAME\n\tplay - choose a playlist to play\n\n"
                                "SYNOPSIS\n\tplay [PLAYLIST PATH]... [VIDEO NUMBER OPTION]...\n\n"
                                "OPTIONS\n\t[VIDEO NUMBER]\n\t\tselect the video to play in the playlist \n\n"
                                "EXAMPLE\n\tplay Music/Rock 2"
                            )

                        case "playlist":
                            print(
                                "NAME\n\tplaylist - add or remove a playlist from the tree structure\n\n"
                                "SYNOPSIS\n\tplaylist [OPTION]... [NEW PLAYLIST PATH]...\n\n"
                                "OPTIONS\n\tadd\n\t\tadds the new playlist to the selected playlist\n"
                                "\tremove\n\t\tremoves the selected playlist\n\n"
                                "EXAMPLES\n\tplaylist add Music/Rap\n\tplaylist remove Music/Rap"
                            )

                        case "video":
                            print(
                                "NAME\n\tvideo - add or remove a video from a playlist\n\n"
                                "SYNOPSIS\n\tvideo [OPTION]... [NEW VIDEO PATH]... [URL]... [POSITION NUMBER OPTION]...\n\n"
                                "OPTIONS\n\tadd\n\t\tadds the new video to the selected playlist\n"
                                "\tremove\n\t\tremoves the selected video\n\n"
                                "\tmove\n\t\tchange video position in the playlist : specify old and new position\n\n"
                                "\t[POSITION NUMBER]\n\t\tselect video position in playlist\n\n"
                                "EXAMPLE\n\tvideo add Music/Rap/NewVideo https://youtu.be/newvideo 2\n\tvideo remove Music/Rap\n\tvideo move Music/Rap 3 1"
                            )

                        case "queue":
                            print(
                                "NAME\n\tqueue - add or remove a playlist or video from the queue\n\n"
                                "SYNOPSIS\n\tqueue [OPTION]... [PLAYLIST PATH]... [VIDEO NUMBER OPTION]\n\n"
                                "OPTIONS\n\tadd\n\t\tadds the selected video to the queue\n"
                                "\tclear\n\t\tempty queue\n\n"
                                "\t[VIDEO NUMBER]\n\t\tselect video number from selected playlist\n\n"
                                "EXAMPLE\n\tqueue add Music/Rap"
                            )


            case _:
                print("Invalid input")
                continue
