from display import *
from typing import List

def menu() -> int:
    while True:
        print("\n==================== ", end="");print_yellow("MENU");print(" ====================")
        print(" 1. Rules")
        print(" 2. Help")
        print(" 3. Generate ")
        print("Choose Command:")
        user_input = input_color("")
        
        if user_input in ["1", "2", "3"]:
            return int(user_input)
        elif user_input.lower() == "rules":
            return 1
        elif user_input.lower() == "help":
            return 2
        elif user_input.lower() == "generate":
            return 3
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

def set_hex(code: str, board: List[List[int]]) -> List[List[int]]:
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

    return []

if __name__ == "__main__":
    board = [[0 for _ in range(5)] for _ in range(5)]
    board = set_hex("F0", board)
    menu()
