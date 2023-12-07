import random as rd
from display import *
from game import *
from typing import List, Tuple

def generate_location_code(board: List[List[int]]) -> str: 
    empty_positions = [(i, j) for i in range(5) for j in range(5) if board[i][j] == 0]
    random_empty_position = rd.choice(empty_positions)
    row, col = random_empty_position
    row_code = chr(row + 65)
    col_code = str(col+1)
    result = row_code + col_code
    return result
    
def generate():
    while True:
        print_red("\n================ ");print_yellow("GENERATING");print_red_nl(" ================")
        board = [[0 for _ in range(5)] for _ in range(5)]
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
    while True:
        print("Do you want to save this game? ")
        print("[Y/N] : ")
        save = input_color("")
        if(save.lower() == "y"):
            pass
        elif(save.lower() != "n"):
            print_red_nl("Invalid Input\n")
        else:
            break