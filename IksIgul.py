from colorama import Fore, Back, Style

PLACE_DICT = { #lists:
        'A': [0, 0],
        'B': [0, 1],
        'C': [0, 2],
        'D': [1, 0],
        'E': [1, 1],
        'F': [1, 2],
        'G': [2, 0],
        'H': [2, 1],
        'I': [2, 2]
        }

WIN_OPT_DICT = { # contains all the options for a player to win (on every row, col and criss cross dunno)
    1: [PLACE_DICT['A'], PLACE_DICT['B'], PLACE_DICT['C']],
    2: [PLACE_DICT['D'], PLACE_DICT['E'], PLACE_DICT['F']],
    3: [PLACE_DICT['G'], PLACE_DICT['H'], PLACE_DICT['I']],
    4: [PLACE_DICT['A'], PLACE_DICT['D'], PLACE_DICT['G']],
    5: [PLACE_DICT['B'], PLACE_DICT['E'], PLACE_DICT['H']],
    6: [PLACE_DICT['C'], PLACE_DICT['F'], PLACE_DICT['I']],
    7: [PLACE_DICT['A'], PLACE_DICT['E'], PLACE_DICT['I']],
    8: [PLACE_DICT['C'], PLACE_DICT['E'], PLACE_DICT['G']]
}

def init_board():
    return [['A','B','C'],['D','E','F'],['G','H','I']]

def print_map(board):
    print("-------------")
    for curr_row in range(len(board)):
        for curr_column in range(len(board[0])):
            if board[curr_row][curr_column] == "X":
                print(Fore.RED + board[curr_row][curr_column])
            elif board[curr_row][curr_column] == "O":
                print(Fore.GREEN + board[curr_row][curr_column])
            else:
                print(Fore.WHITE + board[curr_row][curr_column], end=" ")
        print("")
    print("-------------")

def get_sign(num):
    return (Fore.RED + 'X') if num%2 == 0 else (Fore.GREEN + 'O')

def if_winner(board):
    for variant in range(1,9):
        curr_var = WIN_OPT_DICT[variant]
        if board[curr_var[0][0]][curr_var[0][1]] == board[curr_var[1][0]][curr_var[1][1]] and board[curr_var[1][0]][curr_var[1][1]] == board[curr_var[2][0]][curr_var[2][1]]:
            return True
    return False

def run_game():
    board = init_board()
    list = ['A','B','C', 'D','E','F','G','H','I']
    for turn in range(1, 10): # max turns is 9 anyway
        print_map(board)
        print(get_sign(turn),"'s turn")
        place = input(f"Enter letter to place sign:")
        while not(place in list):
            place = input("Wrong, enter letter to place sign again: ")
        board[PLACE_DICT[place][0]][PLACE_DICT[place][1]] = get_sign(turn)
        list.remove(place)
        if if_winner(board):
            print("Player",get_sign(turn), "wins.")
            break
        if turn == 9:
            print(Fore.WHITE + "Tie")
    try_again = input(Fore.WHITE + "Do you want to try again? (yes/anything else)")
    if try_again.upper() == "YES":
        run_game()
    else:
        print(Fore.BLUE + "G A M E  O V E R")

run_game()


