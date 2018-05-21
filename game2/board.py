from arrays import Array2D


class TakenPosition(Exception):
    pass


class Board:
    """class for Board representation"""
    SINGS = ['o', 'x']

    def __init__(self):
        """
        creates new empty Board
        """
        self.positions = Array2D(3, 3)
        self.pre_pos = [None, (-1, -1)]

    def num_free(self):
        """
        Returns a number of free positions
        :return: int
        """
        res = 0
        for i in range(3):
            for j in range(3):
                if self.positions[i, j] is None:
                    res += 1
        return res

    def c1(self, sing):
        """
        Helper function for method check_f
        :param sing: str
        :return: bool
        """
        p = self.positions
        # check for horizontal
        for i in range(3):
            a = True
            for j in range(3):
                if p[i, j] != sing:
                    a = False
            if a is True:
                return True
        # check for vertical
        for i in range(3):
            a = True
            for j in range(3):
                if p[j, i] != sing:
                    a = False
            if a is True:
                return True
        # check diag 1
        if p[0, 0] == p[1, 1] == p[2, 2] == sing:
            return True
        # check diag2
        if p[0, 2] == p[1, 1] == p[2, 0] == sing:
            return True
        return False

    def check_f(self, sing):
        """
        If the sing is a winner return True,
        if the sing is a loser return False
        return "stop" if there is no winner
        return "continue" if there is no winner
        but still some moves can be made
        :return: bool or str
        """
        if sing not in self.SINGS:
            return False
        other = 'x'
        if sing == other:
            other = 'o'
        k = self.c1(sing)
        m = self.c1(other)
        if k is True:
            return True
        elif m is True:
            return False

        if self.num_free() == 0:
            return "stop"
        else:
            return "continue"

    def add_pos(self, pos, sing=None):
        """
        Adds a symlol to given position
        :param sing: str
        :param pos: (int, int)
        :return: None
        """
        if sing is None:
            sing = self.pre_pos[0]
        if self.positions[pos[0], pos[1]] is None:
            self.positions[pos[0], pos[1]] = sing
            self.pre_pos = [sing, pos]
        else:
            raise TakenPosition

    def get_free_lst(self):
        """
        Creates and returns a list of free positions coordinates
        :return: list
        """
        res = []
        for i in range(3):
            for j in range(3):
                if self.positions[i, j] is None:
                    res.append((i, j))
        return res

    def __str__(self):
        """
        String representation of field
        :return: str
        """
        res = ''
        for i in range(3):
            for j in range(3):
                if self.positions[i, j] is None:
                    res += '#'
                else:
                    res += self.positions[i, j]
            res += "\n"
        return res

    def get_same(self):
        """
        returns a deepcopy of self
        :return: Board
        """
        pos = Array2D(3, 3)
        for i in range(3):
            for j in range(3):
                pos[i, j] = self.positions[i, j]
        res = Board()
        res.pre_pos = self.pre_pos
        res.positions = pos
        return res
