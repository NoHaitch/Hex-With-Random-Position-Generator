from typing import List
import random as rd
from display import *
from game import *

# change this to change size of the board
board_size = 5

def generate_location_code(board: List[List[int]]) -> str: 
    empty_positions = [(i, j) for i in range(board_size) for j in range(board_size) if board[i][j] == 0]
    random_empty_position = rd.choice(empty_positions)
    row, col = random_empty_position
    row_code = chr(row + 65)
    col_code = str(col+1)
    result = row_code + col_code
    return result
    
def generate() -> None:
    while True:
        print_red("\n================ "); print_yellow("GENERATING"); print_red_nl(" ================")
        board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        current_player = 1
        while(not is_won(board)):
            code = generate_location_code(board)
            board = set_hex(code, board, current_player)
            if(current_player == 1):
                current_player = 2
            else:
                current_player = 1
        display_board(board)
        print_yellow_nl("=========== FINISH GENERATING =============")
        stop_generating = False
        while not stop_generating:
            print("Do you want to redo it? ")
            print("[Y/N] : ")
            save = input_color("")
            if(save.lower() == "y"):
                break
            elif(save.lower() != "n"):
                print_red_nl("Invalid Input\n")
            else:
                stop_generating = True
        if(stop_generating):
            break
    
def generate_filled() -> None:
    while True:
        print_red("\n================ "); print_yellow("GENERATING"); print_red_nl(" ================")
        while True:
            board = [[0 for _ in range(board_size)] for _ in range(board_size)]
            current_player = 1
            while(not is_won(board)):
                code = generate_location_code(board)
                board = set_hex(code, board, current_player)
                if(current_player == 1):
                    current_player = 2
                else:
                    current_player = 1
            if(is_filled(board)):
                break
        display_board(board)
        print_yellow_nl("=========== FINISH GENERATING =============")
        stop_generating = False
        while not stop_generating:
            print("Do you want to redo it? ")
            print("[Y/N] : ")
            save = input_color("")
            if(save.lower() == "y"):
                break
            elif(save.lower() != "n"):
                print_red_nl("Invalid Input\n")
            else:
                stop_generating = True
        if(stop_generating):
            break