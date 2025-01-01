from model import LinkedList


class PlaylistTree:

    class TreeNode:
        def __init__(self, name, is_video=False, is_playlist=False):
            self._name = name
            self._is_video = is_video
            self._is_playlist = is_playlist
            self._children = LinkedList if not is_video else None  # Videos are leaf (no childs)

    def __init__(self):
        self.root = self.TreeNode("Root")  # Root of the tree

    def add_category(self, parent_name, category_name):
        # Add category under another category or root
        parent_node = self._find_node(self.root, parent_name)
        if parent_node is not None and not parent_node._is_playlist:
            new_category = self.TreeNode(category_name, is_video=False, is_playlist=False)
            parent_node._children.append(new_category)
        else:
            raise ValueError("Parent '", parent_name,"' not found or not a category")

    def add_playlist(self, category_name, playlist_name):
        # Add playlist under category
        category_node = self._find_node(self.root, category_name)
        if category_node is not None and not category_node._is_playlist:
            new_playlist = self.TreeNode(playlist_name, is_video=False, is_playlist=True)
            category_node._children.append(new_playlist)
        else:
            raise ValueError("Category '", category_name, "' not found or not a category")

    def add_video(self, playlist_name, video_name):
        # Add video in playlist
        playlist_node = self._find_node(self.root, playlist_name)
        if playlist_node is not None and playlist_node._is_playlist:
            new_video = self.TreeNode(video_name, is_video=True)
            playlist_node._children.append(new_video)
        else:
            raise ValueError("Playlist '", playlist_name, "' not found or not a playlist")

    def remove(self, name):
        # Remove category, playlist or video
        self._remove_recursive(self.root, name)

    def _remove_recursive(self, node, name):
        # Search and recursive remove
        for child in node._children:
            if child._name == name:
                node._children.remove(child)
                return True
            if not child._is_video and self._remove_recursive(child, name):
                return True
        return False

    def _find_node(self, node, name):
        # Search tree node by name
        if node._name == name:
            return node
        for child in node._children or []:
            result = self._find_node(child, name)
            if result is not None:
                return result
        return None

    def display(self):
        # Display tree
        self._display_recursive(self.root)

    def _display_recursive(self, node, level=0):
        type_label = "(Video)" if node._is_video else "(Playlist)" if node._is_playlist else "(Category)"
        print("  " * level + f"- {node._name} {type_label}")
        for child in node._children or []:
            self._display_recursive(child, level + 1)
