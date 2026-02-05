import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell
        elif cell == 'O':
            return Fore.YELLOW + cell
        else:
            return cell

    print(f" {colored(board[0])} | {colored(board[1])} | {colored(board[2])} ")
    print(Fore.CYAN + "---+---+---")
    print(f" {colored(board[3])} | {colored(board[4])} | {colored(board[5])} ")
    print(Fore.CYAN + "---+---+---")
    print(f" {colored(board[6])} | {colored(board[7])} | {colored(board[8])} ")
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? ").upper()
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    # 1. Try to win
    for i in range(9):
        if board[i].isdigit():
            board_copy = board[:]
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return

    # 2. Block player win
    for i in range(9):
        if board[i].isdigit():
            board_copy = board[:]
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return

    # 3. Random move
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    board[random.choice(possible_moves)] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == symbol for a,b,c in win_conditions)

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: ")

    while True:
        board = [str(i) for i in range(1, 10)]
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)

            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"🎉 Congratulations {player_name}, you won!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print("🤝 It's a tie!")
                    break
                else:
                    turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("🤖 AI has won the game!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print("🤝 It's a tie!")
                    break
                else:
                    turn = 'Player'

        if input("Play again? (yes/no): ").lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()
