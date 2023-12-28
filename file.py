import random, math


class Player:
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, game):
        ...


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super(RandomComputerPlayer, self).__init__(letter)

    def make_move(self, game):
        square = random.choice(game.available_moves())
        return square


class AIComputerPlayer(Player):
    def __init__(self, letter):
        super(AIComputerPlayer, self).__init__(letter)

    def make_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, state, player):
        # assign variables
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'

        # check termination
        if state.current_winner == other_player:
            return {
                "position": None,
                "score": (-1, 1)[other_player == max_player] * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {
                "position": None,
                "score": 0
            }

        if player == max_player:
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}

        # check every move
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = possible_move

            state.current_winner = None
            sim_score["position"] = possible_move
            
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best


class HumanPlayer(Player):
    def __init__(self, letter):
        super(HumanPlayer, self).__init__(letter)

    def make_move(self, game):
        while True:
            square = int(input(f"choose from {game.available_moves()}\n"))
            if square in game.available_moves():
                return square
            else:
                print(square," not available")
