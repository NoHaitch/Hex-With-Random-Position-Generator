from typing import List

normal = "\033[0m"
blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"

def print_blue(text: str ) -> None:
    print(blue + text + normal) 

def print_red(text: str) -> None:
    print(red + text + normal)

def print_green(text: str) -> None:
    print(green + text + normal)

def display_board(board: List[List[int]]) -> None:
    temp = ["" for _ in range(5) for _ in range(5)]
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if(cell == 0):
                temp[(i*5)+j] = green + "." + normal
            elif(cell == 2):
                temp[(i*5)+j] = red + "X" + normal
            else:
                temp[(i*5)+j] = blue + "O" + normal

    player1_edge_backslash = blue + "\\" + normal
    player1_edge_straight = blue + "|" + normal
    print("\n       1   2   3   4   5           ")
    print_red("   ======================            ")
    print(f"    {player1_edge_backslash} / \ / \ / \ / \ / {player1_edge_backslash}          ")
    print(f"  A  {player1_edge_straight} {temp[0]} | {temp[1]} | {temp[2]} | {temp[3]} | {temp[4]} {player1_edge_straight}  A             ") # first row
    print(f"      {player1_edge_backslash} / \ / \ / \ / \ / {player1_edge_backslash}        ")
    print(f"    B  {player1_edge_straight} {temp[5]} | {temp[6]} | {temp[7]} | {temp[8]} | {temp[9]} {player1_edge_straight}  B           ") # second row
    print(f"        {player1_edge_backslash} / \ / \ / \ / \ / {player1_edge_backslash}      ")
    print(f"      C  {player1_edge_straight} {temp[10]} | {temp[11]} | {temp[12]} | {temp[13]} | {temp[14]} {player1_edge_straight}  C    ") # third row
    print(f"          {player1_edge_backslash} / \ / \ / \ / \ / {player1_edge_backslash}    ")
    print(f"        D  {player1_edge_straight} {temp[15]} | {temp[16]} | {temp[17]} | {temp[18]} | {temp[19]} {player1_edge_straight}  D  ") # fourth row
    print(f"            {player1_edge_backslash} / \ / \ / \ / \ / {player1_edge_backslash}  ")
    print(f"          E  {player1_edge_straight} {temp[20]} | {temp[21]} | {temp[22]} | {temp[23]} | {temp[24]} {player1_edge_straight}  E") # last row
    print(f"              {player1_edge_backslash} / \ / \ / \ / \ / {player1_edge_backslash} ")
    print_red("              ======================  ")
    print("               1   2   3   4   5           ")

def display_intro() -> None:
    print_red("    __    __  ________  __    __        _______                                       __      ")
    print_red("    /  |  /  |/        |/  |  /  |      /       \                                     /  |    ")
    print_red("    $$ |  $$ |$$$$$$$$/ $$ |  $$ |      $$$$$$$  |  ______    ______    ______    ____$$ |    ")
    print_red("    $$ |__$$ |$$ |__    $$  \/$$/       $$ |__$$ | /      \  /      \  /      \  /    $$ |    ")
    print_red("    $$    $$ |$$    |    $$  $$<        $$    $$< /$$$$$$  | $$$$$$  |/$$$$$$  |/$$$$$$$ |    ")
    print_red("    $$$$$$$$ |$$$$$/      $$$$  \       $$$$$$$  |$$ |  $$ | /    $$ |$$ |  $$/ $$ |  $$ |    ")
    print_red("    $$ |  $$ |$$ |_____  $$ /$$  |      $$ |__$$ |$$ \__$$ |/$$$$$$$ |$$ |      $$ \__$$ |    ")
    print_red("    $$ |  $$ |$$       |$$ |  $$ |      $$    $$/ $$    $$/ $$    $$ |$$ |      $$    $$ |    ")
    print_red("    $$/   $$/ $$$$$$$$/ $$/   $$/       $$$$$$$/   $$$$$$/   $$$$$$$/ $$/        $$$$$$$/     ")
                                                                                                
    print_blue("      ______                                                      __                         ")
    print_blue("     /      \                                                    /  |                        ")
    print_blue("    /$$$$$$  |  ______   _______    ______    ______   ______   _$$ |_     ______    ______  ")
    print_blue("    $$ | _$$/  /      \ /       \  /      \  /      \ /      \ / $$   |   /      \  /      \ ")
    print_blue("    $$ |/    |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |")
    print_blue("    $$ |$$$$ |$$    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ ")
    print_blue("    $$ \__$$ |$$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      ")
    print_blue("    $$    $$/ $$       |$$ |  $$ |$$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |      ")
    print_blue("    $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/        ")
    print()

def start_green_text() -> None:
    print(green, end="")

def reset_text_color() -> None:
    print(normal, end="")

def input_color(input_string: str) -> None:
    start_green_text()
    x = input("> " + input_string)
    reset_text_color()
    return x

def main() -> None:
    display_intro()
    print_blue("This text is in blue.")
    print_red("This text is in red.")
    print_green("This text is in green.")
    print("this is the start of input_color")
    x = input_color("name : ")
    print("this is the end of input_color")
    print_red(f"result: {x}")

if __name__ == "__main__":
    main()