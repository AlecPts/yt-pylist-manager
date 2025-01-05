import re
from typing import Optional

from linked_list import LinkedList


class TreeNode:
    def __init__(self, name: str):
        self._name = name
        self._children = []
        self._videos = LinkedList()


    def display(self, depth=0):
        print("\t" * depth, "-", self._name, end=" ")
        self._videos.display(depth)
        print()
        for child in self._children:
            child.display(depth + 1)


class Tree:
    def __init__(self):
        self.root = TreeNode("root")

    def add_playlist(self, parent_path: list[str], child_name: str):
        try:
            # Find parent
            parent_node = self.find_node_by_path(parent_path)

            if parent_node is None:
                raise Exception(f"Parent node '{parent_path}' not found in the tree")

            # Check if parent node contains videos
            if parent_node._videos._nb_elt > 0:
                raise Exception(f"Parent node '{parent_path}' contains videos")

            # Create new node and add it as a child
            new_child = TreeNode(child_name)
            parent_node._children.append(new_child)

        except Exception as e:
            print(f"ERROR : {e}")


    def add_video(self, parent_path: list[str], child_name: str, video_url: str, pos: int=None):
        try:
            # Find parent
            parent_node = self.find_node_by_path(parent_path)

            if parent_node is None:
                raise Exception(f"Parent node '{parent_path}' not found in the tree")

            # Check if parent node contains playlist
            if not self.is_leaf(parent_node):
                raise Exception(f"Parent node '{parent_path}' contains playlists")

            # Check url format
            # youtube_url_format = r"^(https?:\/\/)(youtube\.com|youtu\.be)\/(watch\?v=|embed\/|v\/)?[a-zA-Z0-9_-]{11}(&\S*)?$"
            # if not re.search(youtube_url_format, video_url):
            #     raise Exception(f"The given url, {video_url}, is not in the right format")

            # Add new video
            parent_node._videos.add(child_name, video_url, pos)

        except Exception as e:
            print(f"ERROR : {e}")


    def remove_playlist(self, parent_path: list[str], child_name: str):
        try:
            # Find parent
            parent_node = self.find_node_by_path(parent_path)

            if parent_node is None:
                raise Exception(f"Parent node '{parent_path}' not found in the tree")

            for child in parent_node._children:
                if child._name == child_name:
                    parent_node._children.remove(child)

        except Exception as e:
            print(f"ERROR : {e}")


    def remove_video(self, parent_path: list[str], child_nb: int):
        try:
            # Find parent
            parent_node = self.find_node_by_path(parent_path)

            if parent_node is None:
                raise Exception(f"Parent node '{parent_path}' not found in the tree")

            # Remove video at chosen position
            print(parent_node._videos)
            parent_node._videos.remove(child_nb)

        except Exception as e:
            print(f"ERROR : {e}")


    def find_node_by_path(self, path: list[str], current_node: Optional[TreeNode]=None) -> Optional[TreeNode]:
        # If no node specified, start from root
        if current_node is None:
            current_node = self.root

        # If path is empty, node found
        if not path:
            return current_node

        # Search node in all childs
        for child in current_node._children:
            if child._name == path[0]:
                # Recursive call with rest of path
                path.pop(0)
                return self.find_node_by_path(path, child)

        return None


    def is_leaf(self, node: Optional[TreeNode]) -> bool:
        try:
            if node is None:
                raise Exception(f"Playlist '{node}' not found")

            # Check if selected node is a leaf
            is_leaf_node = len(node._children) == 0
            return is_leaf_node

        except Exception as e:
            print(f"ERROR: {e}")
            return False


    def add_videos_to_waiting_list(self, playlist_name: list[str], waiting_list, video_nb: int=None):
        try:
            # Get playlist
            playlist_node = self.find_node_by_path(playlist_name)

            if playlist_node is None:
                raise Exception(f"Playlist {playlist_name} not found")

            # Get videos from playlist
            current_video = playlist_node._videos._first

            # Add all videos
            if video_nb is None:
                while current_video is not None:
                    waiting_list.add(current_video._name, current_video._value)
                    current_video = current_video._next
            # Add specific video
            else:
                if video_nb < 1:  # Validation pour une position valide
                    raise ValueError(f"Video number must be >= 1, got {video_nb}")

                count = 1
                while current_video is not None:
                    if count == video_nb:
                        # Add video in queue at given position
                        waiting_list.add(current_video._name, current_video._value)
                        break
                    current_video = current_video._next
                    count += 1

                if current_video is None:
                    raise Exception(f"Video number {video_nb} not found in playlist {playlist_name}")

        except Exception as e:
                print(f"ERROR : {e}")


    def move_video(self, playlist_path: list[str], old_pos: int, new_pos: int):
        try:
            # Get playlist by its path
            playlist_node = self.find_node_by_path(playlist_path)

            if playlist_node is None:
                raise Exception(f"Playlist '{playlist_path}' not found")

            # Check start position and end position
            if old_pos < 1 or new_pos < 1:
                raise ValueError("Positions must be greater than or equal to 1")

            # Check if playlist contains videos
            if playlist_node._videos._nb_elt == 0:
                raise Exception(f"Playlist '{playlist_path}' is empty")

            # Get video at old position and rmeove it
            video_to_move = playlist_node._videos.remove(old_pos)

            if video_to_move is None:
                raise Exception(f"No video found at position {old_pos} in playlist '{playlist_path}'")

            # Add video at new position
            playlist_node._videos.add(video_to_move._name, video_to_move._value, new_pos)

        except Exception as e:
            print(f"ERROR: {e}")
