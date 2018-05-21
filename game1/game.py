from board import Board
from btree import BTree


class UserError(Exception):
    pass


class Game:
    """class for game representation"""
    def __init__(self):
        """create a new Game"""
        self.end = False
        self.board = Board()

    def handle_user(self):
        """
        Method for work with user
        :return: None
        """
        # prediction user always makes first move

        ps = input("Enter your move coords(2 ints in a row): ")
        p = ps
        if len(ps) != 2:
            print("You entered wrong coords\nTry again")
            raise UserError
        try:
            ps = int(ps)
        except ValueError:
            print("You entered wrong coords\nTry again")
            raise UserError

        a, b = int(p[0]), int(p[1])
        if not (0 <= a <= 2):
            print("You entered wrong coords\nTry again")
            raise UserError
        elif not (0 <= b <= 2):
            print("You entered wrong coords\nTry again")
            raise UserError
        if self.board.positions[a, b] is not None:
            print("You entered wrong coords\nTry again")
            raise UserError
        self.board.add_pos((a, b), 'o')
        print("You moved {}".format((a, b)))

    def handle_comp(self):
        """
        Method to work with computer
        :return: None
        """
        tree = BTree(self.board)
        tree.build()
        move = tree.f_move('x')
        if self.board.positions[move[0], move[1]] is not None:
            print("Computer made mistake")
            raise UserError
        self.board.add_pos(move, 'x')
        print("Computer moved {}".format(move))

    def play(self):
        """
        Main Function for the game
        :return: None
        """
        print("The game starts (you are 'o' computer is 'x')")
        print(self.board)
        while True:
            sm = True
            while sm:
                try:
                    self.handle_user()
                    sm = False
                except UserError:
                    pass
            print(self.board)
            res = self.board.check_f('o')
            if res is True:
                print('You won!!!')
                break
            elif res is False:
                print('Computer won! You lost!')
                break
            elif res == 'stop':
                print('Nobody won!')
                break
            self.handle_comp()
            print(self.board)
            res = self.board.check_f('x')
            if res is True:
                print('Computer won! You lost!')
                break
            elif res is False:
                print('You won!!! Computer lost!')
                break
            elif res == 'stop':
                print('Nobody won!')
                break

        print('End of game')
        self.end = True


a = Game()
a.play()
