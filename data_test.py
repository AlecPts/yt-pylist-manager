from tree import TreeNode

def fill_with_data_test(root_node):
    node1 = TreeNode("Music")
    node2 = TreeNode("Tutorials")
    node3 = TreeNode("ASMR")

    node4 = TreeNode("Rock")
    node5 = TreeNode("Electro")
    node6 = TreeNode("Minecraft")
    node7 = TreeNode("Python")

    # Add categories to root
    root_node._children.append(node1)
    root_node._children.append(node2)
    root_node._children.append(node3)

    # Add playlists to category
    node1._children.append(node4)
    node1._children.append(node5)
    node2._children.append(node6)
    node2._children.append(node7)

    # Add videos (name, YouTube URL)
    node4._videos.add("Best of Rock 2023", "https://youtu.be/example1")
    node4._videos.add("Rock Classics", "https://youtu.be/example2")
    node4._videos.add("Indie Rock Vibes", "https://youtu.be/example3")

    node5._videos.add("Top Electro Tracks", "https://youtu.be/example4")
    node5._videos.add("Electro Chill", "https://youtu.be/example5")
    node5._videos.add("Festival Mix", "https://youtu.be/example6")
    node5._videos.add("Electro Classics", "https://youtu.be/example7")
    node5._videos.add("New Electro Beats", "https://youtu.be/example8")

    node6._videos.add("Minecraft Survival Guide", "https://youtu.be/example9")
    node6._videos.add("Building Tutorials", "https://youtu.be/example10")
    node6._videos.add("Redstone Basics", "https://youtu.be/example11")

    node7._videos.add("Python Basics Tutorial", "https://youtu.be/example12")
    node7._videos.add("Advanced Python Techniques", "https://youtu.be/example13")
    node7._videos.add("Python for Data Science", "https://youtu.be/example14")
    node7._videos.add("Flask Web Development", "https://youtu.be/example15")
    node7._videos.add("Django in Depth", "https://youtu.be/example16")

    node3._videos.add("ASMR Relaxation Techniques", "https://youtu.be/example17")
    node3._videos.add("Soothing Whispering", "https://youtu.be/example18")
    node3._videos.add("Gentle Tapping Sounds", "https://youtu.be/example19")
