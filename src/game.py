from display import *
from typing import List, Tuple

def menu() -> int:
    while True:
        print("\n==================== ", end="");print_yellow("MENU");print(" ====================")
        print(" 1. Rules")
        print(" 2. Help")
        print(" 3. Play ")
        print(" 4. Generate ")
        print(" 5. Quit / Exit ")
        print("Choose Command:")
        user_input = input_color("")
        
        if user_input in ["1", "2", "3", "4", "5"]:
            return int(user_input)
        elif user_input.lower() == "rules":
            return 1
        elif user_input.lower() == "help":
            return 2
        elif user_input.lower() == "play":
            return 3
        elif user_input.lower() == "generate":
            return 4
        elif user_input.lower() == "quit" or user_input.lower() == "exit" :
            return 5
        else:
            print_red_nl("Invalid input\n")

def rules() -> None:
    print("\n==================== ", end="");print_yellow("RULES");print(" ====================")
    print(" - The Objective of the game is to connect 2 side of the board depending on which player")
    print(" - ",end="");print_blue("Player 1");print(" is represented as ",end="");print_blue("O");print(" and the color ",end="");print_blue_nl("BLUE")
    print(" - ",end="");print_blue("Player 1");print(" wins by connecting the ",end="");print_blue("left");print(" and ",end="");print_blue("right");print(" side of the board")
    print(" - ",end="");print_red("Player 2");print(" is represented as ",end="");print_red("X");print(" and the color ",end="");print_red_nl("RED")
    print(" - ",end="");print_red("Player 2");print(" wins by connecting the ",end="");print_red("top");print(" and ",end="");print_red("bottom");print(" side of the board")

def help() -> None:
    print("\n==================== ", end="");print_yellow("HELP");print(" ====================")
    print("To use the menu, input number or the command")
    print("example: ",end="");print_green_nl("1/Rules/rule/ruLe")
    print("Use the command '",end="");print_yellow("rules");print("' to get the rules of hex board game")
    print("Use the command '",end="");print_yellow("help");print("' to get the explanation of the commands")
    print("Use the command '",end="");print_yellow("play");print("' to play a game of hex")
    print("Use the command '",end="");print_yellow("generate");print("' to generate a game of hex")
   
def set_hex(valid_code: str, board: List[List[int]], player: int) -> List[List[int]]:
    splitted_code = list(valid_code)
    row = ord(splitted_code[0].upper()) - 65
    col = int(splitted_code[1]) - 1
    board[row][col] = player
    return board

def set_hex_IO(code: str, board: List[List[int]], player: int) -> Tuple[bool,List[List[int]]]:
    splitted_code = list(code)
    
    if(len(splitted_code) != 2 or not splitted_code[1].isdigit()):
        print("")
        print_red(code)
        print(" is not a Code!")
        print("correct example: A1 | E4 | C2\n")
        return False, board

    if(int(splitted_code[1]) > len(board) or int(splitted_code[1]) < 1):
        print("")
        print_red(code)
        print(" is not a Code!")
        print(f"Position {splitted_code[1]} is not valid\n")
        return False, board

    if(ord(splitted_code[0].upper()) > (65 + len(board))):
        print("")
        print_red(code)
        print(" is not a Code!")
        print(f"Position {splitted_code[0]} is not valid\n")
        return False, board
    
    row = ord(splitted_code[0].upper()) - 65
    col = int(splitted_code[1]) - 1
    if(board[row][col] != 0):
        print("")
        print_red(code)
        print(" is already filled!")
        return False, board
    
    return True, set_hex(code, board, player)

def is_connected_recursive(i: int, j: int, player: int, board: List[List[int]], visited: List[Tuple[int, int]]) -> Tuple[bool, List[Tuple[int, int]]]:
    if i >= len(board) or j >= len(board) or i < 0 or j < 0:
        return False, visited
    else:
        visited.append((i, j))
        
        if board[i][j] == player:
            if player == 1 and j == len(board) - 1:
                return True, visited
            elif player == 2 and i == len(board) - 1:
                return True, visited

            neighbors = {(0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0)}
            for neighbor_i, neighbor_j in neighbors:
                new_i = i + neighbor_i
                new_j = j + neighbor_j
                if (new_i, new_j) not in visited:
                    found, visited = is_connected_recursive(new_i, new_j, player, board, visited)
                    if found:
                        return found, visited

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
            if(result_recur[0]):
                    return result_recur[0]
    return False

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
            if(result_recur[0]):
                return result_recur[0]
    return False

def is_won(board) -> bool:
    return check_win_player1(board) or check_win_player2(board)

def play() -> None:
    print_red("\n================ ");print_yellow("STARTING A NEW GAME");print_red_nl(" ================")
    board = [[0 for _ in range(5)] for _ in range(5)]
    current_player = 1
    while(not is_won(board)):
        display_board(board)
        print(f"Player {current_player} turn")
        code = input_color("Input location code: ")
        valid, board = set_hex_IO(code, board, current_player)
        if(not valid):
            while(not valid):
                code = input_color("Input location code: ")
                valid, board = set_hex_IO(code, board, current_player)
        if(current_player == 1):
            current_player = 2
        else:
            current_player = 1
    print_yellow_nl("=========== GAME ENDED =============")
    if(check_win_player1(board)):
        print("Player 1",end="");print_green_nl(" WIN !!!")
        print("Player 2",end="");print_red_nl(" LOSE !!!")
    else:
        print("Player 2",end="");print_green_nl(" WIN !!!")
        print("Player 1",end="");print_red_nl(" LOSE !!!")
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
    while True:
        print("Do you want to play again? ")
        print("[Y/N] : ")
        save = input_color("")
        if(save.lower() == "y"):
            pass
        elif(save.lower() != "n"):
            print_red_nl("Invalid Input\n")
        else:
            break

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



