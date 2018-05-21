class Node:
    """class for Node representation"""
    def __init__(self, data):
        """
        creates new Node
        :param data: Board
        """
        self.data = data
        self.left = None
        self.right = None
