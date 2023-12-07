from display import *
from typing import List, Tuple

def menu() -> int:
    while True:
        print("\n==================== ", end="");print_yellow("MENU");print(" ====================")
        print(" 1. Rules")
        print(" 2. Help")
        print(" 3. Play ")
        print(" 4. Generate ")
        print("Choose Command:")
        user_input = input_color("")
        
        if user_input in ["1", "2", "3", "4"]:
            return int(user_input)
        elif user_input.lower() == "rules":
            return 1
        elif user_input.lower() == "help":
            return 2
        elif user_input.lower() == "play":
            return 3
        elif user_input.lower() == "generate":
            return 4
        else:
            print_red_nl("Invalid input\n")

def rules() -> None:
    print("\n==================== ", end="");print_yellow("RULES");print(" ====================")
    print(" - TO win the game the player has to connect 2 side of the board")
    print(" - ",end="");print_blue("Player 1");print(" is represented as ",end="");print_blue("O");print(" and the color ",end="");print_blue_nl("BLUE")
    print(" - ",end="");print_blue("Player 1");print(" wins by connecting the left and right side of the board")
    print(" - ",end="");print_red("Player 2");print(" is represented as ",end="");print_red("X");print(" and the color ",end="");print_red_nl("RED")
    print(" - ",end="");print_red("Player 2");print(" wins by connecting the top and bottom side of the board")

def help() -> None:
    print("\n==================== ", end="");print_yellow("HELP");print(" ====================")
    print("To use the menu, input number or the command")
    print("example: 1/Rules/rule/ruLe")
    print("To generate the hex board use the third command or 'Generate'")

def set_hex(valid_code: str, board: List[List[int]], player: int) -> List[List[int]]:
    splitted_code = list(valid_code)
    row = ord(splitted_code[0]) - 65
    col = int(splitted_code[1]) - 1
    board[row][col] = player
    return board

def set_hex_IO(code: str, board: List[List[int]], player: int) -> List[List[int]]:
    splitted_code = list(code)
    
    if(len(splitted_code) != 2 or not splitted_code[1].isdigit()):
        print("")
        print_red(code)
        print(" is not a Code!")
        print("correct example: A1 | E4 | C2\n")
        return board

    if(int(splitted_code[1]) > len(board) or int(splitted_code[1]) < 1):
        print("")
        print_red(code)
        print(" is not a Code!")
        print(f"Position {splitted_code[1]} is not valid\n")
        return board

    if(ord(splitted_code[0]) > (65 + len(board))):
        print("")
        print_red(code)
        print(" is not a Code!")
        print(f"Position {splitted_code[0]} is not valid\n")
        return board
    
    row = ord(splitted_code[0]) - 65
    col = int(splitted_code[1]) - 1
    if(board[row][col] != 0):
        print("")
        print_red(code)
        print(" is already filled!")
        return board
    
    return set_hex(code, board, player)

def is_connected_recursive(i: int, j: int, player: int, board: List[List[int]], visited: List[Tuple[int, int]]) -> Tuple[bool, List[Tuple[int, int]]]:
    if i >= len(board) or j >= len(board) or i < 0 or j < 0:
        return False, visited
    else:
        visited.append((i, j))
        if(board[i][j] == player):
            if(player == 1 and j == len(board)-1):
                return True, visited
            elif(player == 2 and i == len(board)-1):
                return True, visited
            else:
                neighbors = {(0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0)}
                for (neighbor_i, neighbor_j) in neighbors:
                    new_i = i + neighbor_i
                    new_j = j + neighbor_j
                    if(not (new_i, new_j) in visited):
                        found, visited = is_connected_recursive(new_i, new_j, player, board, visited)
                        if found:
                            return found, visited
                return False, visited

        else:
            return False, visited


def check_win_player1(board: List[List[int]]) -> bool:
    # PLAYER 1 goal is connecting the left and right side of the board
    
    # simple check first
    for i in range(len(board)):
        if board[i][0] == 1:
            break
    else:
        return False

    for i in range(len(board)):
        if board[i][len(board)-1] == 1:
            break
    else:
        return False
    
    # deep check
    for i in range(len(board)):
        if board[i][0] == 1:
            visited = []
            result_recur = is_connected_recursive(i, 0, 1, board, visited)
    return result_recur[0]

def check_win_player2(board: List[List[int]]) -> bool:
    # PLAYER 2 goal is connecting the top and bottom side of the board
    
    # simple check first
    for i in range(len(board)):
        if board[0][i] == 2:
            break
    else:
        return False

    for i in range(len(board)):
        if board[len(board)-1][i] == 2:
            break
    else:
        return False
    
    # deep check
    for i in range(len(board)):
        if board[0][i] == 2:
            visited = []
            result_recur = is_connected_recursive(0, i, 2, board, visited)
    return result_recur[0]

    
if __name__ == "__main__":
    board = [[1, 1, 0, 2, 0],
             [0, 1, 0, 2, 2],
             [2, 2, 2, 1, 1],
             [2, 2, 1, 1, 0],
             [1, 1, 2, 1, 1]]    # Assuming set_hex_IO and display_board functions are defined
    display_board(board)

    result1 = check_win_player1(board)
    print(f"Player 1 : {result1}")
    result2 = check_win_player2(board)
    print(f"Player 2 : {result2}")

