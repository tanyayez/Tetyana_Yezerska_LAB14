import random
from btnode import Node


def build_tree(node):
    """
    Builds a tree with all posible boards from the given board
    Prediction: chose next move from all posssible
    :param node: Node
    :return: None
    """
    board = node.data
    if board.num_free() == 0:
        pass
    elif board.check_f('x') == "continue":
        sing = board.pre_pos[0]
        if sing == 'o':
            sing = 'x'
        elif sing == 'x':
            sing = 'o'

        free = board.get_free_lst()
        pos_r = random.choice(free)
        free.remove(pos_r)
        if len(free) > 0:
            pos_l = random.choice(free)
        else:
            pos_l = None
        right = board.get_same()
        left = board.get_same()
        right.add_pos(pos_r, sing)
        if pos_l is not None:
            left.add_pos(pos_l, sing)
            node.left = Node(left)
        node.right = Node(right)
        if node.left:
            build_tree(node.left)
        build_tree(node.right)


class BTree:
    """class for BTree representation"""
    def __init__(self, data=None):
        """
        create new BTree
        :param data: Node
        """
        self.root = Node(data)

    def build(self):
        """build tree from root"""
        build_tree(self.root)

    def f_move(self, sing):
        """
        Finds the best move after analysing already built tree
        :param sing: str
        :return: (int, int)
        """
        root1, root2 = self.root.left, self.root.right

        def check1(node):
            """
            Recursive function to get int representing num of winning boards
            :param node: Node
            :return: int
            """
            n = 0
            if node.data is not None:
                res = node.data.check_f(sing)
                if res is True:
                    n += 1
                elif res is False:
                    n -= 1
                if node.left is None:
                    k = 0
                else:
                    k = check1(node.left)
                if node.right is None:
                    m = 0
                else:
                    m = check1(node.right)
            return n + m + k
        res1 = check1(root1)
        res2 = check1(root2)
        if res1 > res2:
            move = root1.data.pre_pos[1]
        else:
            move = root2.data.pre_pos[1]
        return move
