from cli_manager import run_cli
from data_test import fill_with_data_test
from fifo_list import FifoList, FifoNode
from tree import Tree, TreeNode


if __name__ == '__main__':
    waiting_list = FifoList()
    current_video = None

    tree = Tree()
    root_node = tree.root

    # Add data
    fill_with_data_test(root_node)

    # Run CLI
    run_cli(tree, root_node, waiting_list, current_video)