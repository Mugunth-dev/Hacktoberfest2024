import random

def create_board():
    icons = ['🍎', '🍌', '🍒', '🍇', '🍉', '🍓']
    icons = icons * 2  # Create pairs
    random.shuffle(icons)
    return [icons[i:i+4] for i in range(0, 8, 4)]

def print_board(board, revealed):
    for i in range(len(board)):
        row = ''
        for j in range(len(board[i])):
            if revealed[i][j]:
                row += board[i][j] + ' '
            else:
                row += '❓ '
        print(row)

def memory_game():
    board = create_board()
    revealed = [[False] * 4 for _ in range(2)]
    pairs_found = 0
    
    print("Welcome to the Memory Card Game!")
    
    while pairs_found < 6:
        print_board(board, revealed)
        try:
            row1, col1 = map(int, input("Select first card (row and column): ").split())
            row2, col2 = map(int, input("Select second card (row and column): ").split())
            
            if revealed[row1][col1] or revealed[row2][col2]:
                print("One or both of these cards are already revealed. Try again.")
                continue
            
            revealed[row1][col1] = True
            revealed[row2][col2] = True
            
            print_board(board, revealed)
            
            if board[row1][col1] == board[row2][col2]:
                print("You found a pair!")
                pairs_found += 1
            else:
                print("Not a pair. Try again.")
                revealed[row1][col1] = False
                revealed[row2][col2] = False
            
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")
    
    print("Congratulations! You've found all pairs!")

if __name__ == "__main__":
    memory_game()
