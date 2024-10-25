class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def display_board(self):
        print("Current Board:")
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]}")
            if i < 2:
                print("---------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_board_full(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.display_board()
            position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
            if position < 0 or position > 8:
                print("Invalid move. Please enter a position between 0 and 8.")
                continue

            if self.make_move(position):
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"Player {winner} wins!")
                    break
                if self.is_board_full():
                    self.display_board()
                    print("It's a tie!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player
            else:
                print("This position is already taken. Try again.")

# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
