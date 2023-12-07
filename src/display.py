from typing import List

normal = "\033[0m"
blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"

def print_normal() -> None:
    print(normal, end="")

def print_blue_nl(text: str ) -> None:
    print(blue + text + normal) 

def print_red_nl(text: str) -> None:
    print(red + text + normal)

def print_green_nl(text: str) -> None:
    print(green + text + normal)

def print_yellow_nl(text: str) -> None:
    print(yellow + text + normal)

def print_blue(text: str ) -> None:
    print(blue + text + normal, end="") 

def print_red(text: str) -> None:
    print(red + text + normal, end="")

def print_green(text: str) -> None:
    print(green + text + normal, end="")

def print_yellow(text: str) -> None:
    print(yellow + text + normal, end="")

def start_green_text() -> None:
    print(green, end="")

def input_color(input_string: str) -> None:
    start_green_text()
    x = input("> " + input_string)
    print_normal()
    return x

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
    print("       1   2   3   4   5           ")
    print_red_nl("   ======================            ")
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
    print_red_nl("              ======================  ")
    print("               1   2   3   4   5           ")

def display_intro() -> None:
    print_red_nl("    __    __  ________  __    __        _______                                       __      ")
    print_red_nl("    /  |  /  |/        |/  |  /  |      /       \                                     /  |    ")
    print_red_nl("    $$ |  $$ |$$$$$$$$/ $$ |  $$ |      $$$$$$$  |  ______    ______    ______    ____$$ |    ")
    print_red_nl("    $$ |__$$ |$$ |__    $$  \/$$/       $$ |__$$ | /      \  /      \  /      \  /    $$ |    ")
    print_red_nl("    $$    $$ |$$    |    $$  $$<        $$    $$< /$$$$$$  | $$$$$$  |/$$$$$$  |/$$$$$$$ |    ")
    print_red_nl("    $$$$$$$$ |$$$$$/      $$$$  \       $$$$$$$  |$$ |  $$ | /    $$ |$$ |  $$/ $$ |  $$ |    ")
    print_red_nl("    $$ |  $$ |$$ |_____  $$ /$$  |      $$ |__$$ |$$ \__$$ |/$$$$$$$ |$$ |      $$ \__$$ |    ")
    print_red_nl("    $$ |  $$ |$$       |$$ |  $$ |      $$    $$/ $$    $$/ $$    $$ |$$ |      $$    $$ |    ")
    print_red_nl("    $$/   $$/ $$$$$$$$/ $$/   $$/       $$$$$$$/   $$$$$$/   $$$$$$$/ $$/        $$$$$$$/     ")
                                                                                                
    print_blue_nl("      ______                                                      __                         ")
    print_blue_nl("     /      \                                                    /  |                        ")
    print_blue_nl("    /$$$$$$  |  ______   _______    ______    ______   ______   _$$ |_     ______    ______  ")
    print_blue_nl("    $$ | _$$/  /      \ /       \  /      \  /      \ /      \ / $$   |   /      \  /      \ ")
    print_blue_nl("    $$ |/    |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |")
    print_blue_nl("    $$ |$$$$ |$$    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ ")
    print_blue_nl("    $$ \__$$ |$$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      ")
    print_blue_nl("    $$    $$/ $$       |$$ |  $$ |$$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |      ")
    print_blue_nl("    $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/        ")
    print()

def display_outro() -> None:
    print_yellow_nl("                        *****************                     ")
    print_yellow_nl("               ******               ******                    ")
    print_yellow_nl("           ****                           ****                ")
    print_yellow_nl("        ****                                 ***              ")
    print_yellow_nl("      ***                                       ***           ")
    print_yellow_nl("     **           ***               ***           **          ")
    print_yellow_nl("   **           *******           *******          ***        ")
    print_yellow_nl("  **            *******           *******            **       ")
    print_yellow_nl(" **             *******           *******             **      ")
    print_yellow_nl(" **               ***               ***               **      ")
    print_yellow_nl("**                                                     **     ")
    print_yellow_nl("**       *                                     *       **     ")
    print_yellow_nl("**      **                                     **      **     ")
    print_yellow_nl(" **   ****                                     ****   **      ")
    print_yellow_nl(" **      **                                   **      **      ")
    print_yellow_nl("  **       ***                             ***       **       ")
    print_yellow_nl("   ***       ****                       ****       ***        ")
    print_yellow_nl("     **         ******             ******         **          ")
    print_yellow_nl("      ***            ***************            ***           ")
    print_yellow_nl("        ****                                 ****             ")
    print_yellow_nl("           ****                           ****                ")
    print_yellow_nl("               ******               ******                    ")
    print_yellow_nl("                    *****************                         ")
    print_blue_nl("THANKS FOR PLAYING !!")
    print_green_nl("Don't forget to give a star or fork this project!")

def main() -> None:
    display_intro()
    print_blue_nl("This text is in blue.")
    print_red_nl("This text is in red.")
    print_green_nl("This text is in green.")
    print_yellow_nl("This text is in yellow.")
    print("this is the start of input_color")
    x = input_color("name : ")
    print("this is the end of input_color")
    print_red_nl(f"result: {x}")

if __name__ == "__main__":
    main()