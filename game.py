from file import HumanPlayer, RandomComputerPlayer, AIComputerPlayer


def isnumeric(i):
    return i in range(10)


class TicTacToe:
    def __init__(self):
        self.board = [_ for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for i in range(0, 9, 3):
            print("|" + "|".join(str(i) for i in self.board[i:i + 3]) + "|")

    @staticmethod
    def print_board_numbers():
        number_board = [str(j + 3 * i) for i in range(3) for j in range(3)]
        for i in range(0, 9, 3):
            print("|" + "|".join(number_board[i:i + 3]) + "|")

    def available_moves(self):
        return [i for i in self.board if str(i).isnumeric()]

    def empty_squares(self):
        return self.board.count("x") + self.board.count("o") < 9

    def num_empty_squares(self):
        return sum([1 for i in self.board if isnumeric(i)])

    def make_move(self, square, letter):
        if self.board[square] != letter:
            self.board[square] = letter
            if self.winner():
                self.current_winner = letter
            return True
        return False

    def winner(self):
        b = self.board
        for case in [(b[0] == b[1] == b[2] != ' '),
                  (b[3] == b[4] == b[5] != ' '),
                  (b[6] == b[7] == b[8] != ' '),
                  (b[0] == b[3] == b[6] != ' '),
                  (b[1] == b[4] == b[7] != ' '),
                  (b[2] == b[5] == b[8] != ' '),
                  (b[2] == b[4] == b[6] != ' '),
                  (b[0] == b[4] == b[8] != ' ')]:
            if case:
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()
    letter = x_player.letter
    while game.empty_squares():
        if letter == o_player.letter:
            square = o_player.make_move(game)
        else:
            square = x_player.make_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + " make move to square " + str(square))
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter + " wins! ,woohoooo!!!")
                return letter
            letter = o_player.letter if letter == x_player.letter else x_player.letter
        if print_game and not game.available_moves():
            print("it's a tie!")


# winner = play(tic_tac_toe(), HumanPlayer("x"), AIComputerPlayer("o"))


def test_game(rounds, x_player, o_player):
    w, l, d = 0, 0, 0
    for i in range(rounds):
        winner = play(TicTacToe(), x_player("x"), o_player("o"))
        if winner == "x":
            w += 1
        elif winner == "o":
            l += 1
        else:
            d += 1
    print("x_player won = " + str(w) + "\no_player won = " + str(l) + "\ndraws = " + str(d))


test_game(10, RandomComputerPlayer, AIComputerPlayer)
