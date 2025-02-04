# TIC_TAC_TOE

class Board:

    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print('\n')
        for i in range(0, 9, 3):
            row = [self.cells[i + j].symbol or str(i + j + 1) for j in range(3)]
            print(' | '.join(row))
            if i < 6:
                print('-' * 9)
        print('\n')

    def update_cell(self, number, symbol):
        return self.cells[number - 1].set_symbol(symbol)

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizons
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticals
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for a, b, c in winning_combinations:
            if self.cells[a].symbol and self.cells[a].symbol == self.cells[b].symbol == self.cells[c].symbol:
                return self.cells[a].symbol
        return None

    def is_full(self):
        return all(cell.occupied for cell in self.cells)

class Cell:

    def __init__(self, number):
        self.number = number
        self.symbol = None
        self.occupied = False

    def set_symbol(self, symbol):
        if not self.occupied:
            self.symbol = symbol
            self.occupied = True
            return True
        return False

class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self, board):
        while True:
            try:
                move = int(input(f'{self.name}, select the cell number (1-9): '))
                if 1 <= move <= 9 and board.update_cell(move, self.symbol):
                    return move
                else:
                    print('Wrong move! Try again.')
            except ValueError:
                print('Enter a number from 1 to 9!')

class Game:

    def __init__(self):
        print('Welcome to the "Tic-Tac-Toe" game!')
        self.board = Board()
        self.players = [
            Player(input('Player Name 1: '), 'X'),
            Player(input('Player Name 2: '), 'O')
        ]
        self.current_player = self.players[0]

    def switch_turns(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play_round(self):
        self.board.display()
        self.current_player.make_move(self.board)

        winner = self.board.check_winner()
        if winner:
            self.board.display()
            print(f'{self.current_player.name} won!')
            self.current_player.wins += 1
            return True
        elif self.board.is_full():
            self.board.display()
            print('Draw!')
            return True
        return False

    def play_game(self):
        self.board = Board()
        self.current_player = self.players[0]

        while True:
            if self.play_round():
                break
            self.switch_turns()

    def play_series(self):
        while True:
            self.play_game()
            print(f'\nScore: {self.players[0].name} - {self.players[0].wins}, '
                  f'{self.players[1].name} - {self.players[1].wins}')
            again = input('Do you want to play it again? (yes/no): ').strip().lower()
            if again != 'yes':
                print('Thanks for playing!')
                break

game = Game()
game.play_series()