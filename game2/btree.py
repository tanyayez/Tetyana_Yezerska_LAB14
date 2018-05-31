from btnode import Node


def build_tree(node):
    """
    Builds a tree with all posible boards from the given board
    Prediction: chosse next move from two posssible
    :param node: Node
    :return: None
    """
    if node is not None:
        board = node.data
        if board.num_free() == 0:
            pass
        elif board.check_f('o') == "continue":
            sing = board.pre_pos[0]
            if sing == 'o':
                sing = 'x'
            elif sing == 'x':
                sing = 'o'
            free = board.get_free_lst()
            ###########################
            for i in range(len(free)):
                new = board.get_same()
                new.add_pos(free[i], sing)
                node.boors[i] = Node(new)
            for i in range(len(node.boors)):
                build_tree(node.boors[i])


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
        roots = [self.root.boors[0], self.root.boors[1], self.root.boors[2], self.root.boors[3], self.root.boors[4],
                 self.root.boors[5], self.root.boors[6], self.root.boors[7]]

        def check1(node):
            """
            Recursive function to get int representing num of winning boards
            :param node: Node
            :return: int
            """
            if node is not None:
                n = 0
                if node.data is not None:
                    res = node.data.check_f(sing)
                    if res is True:
                        n += 1
                    elif res is False:
                        n -= 1

                    m = 0
                    for i in node.boors:
                        if i is None:
                            k = 0
                            m += k

                        else:
                            k = check1(i)
                            m += k

                    return n + m
                else:
                    pass
            else:
                pass

        nums = []
        rs = []
        for i in roots:
            if i is not None:
                nums.append(check1(i))
                rs.append(i)
        el = max(nums)
        ind = nums.index(el)
        move = rs[ind].data.pre_pos[1]
        return move
