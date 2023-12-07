normal = "\033[0m"
blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"

def print_blue(text):
    print(blue + text + normal) 

def print_red(text):
    print(red + text + normal)

def print_green(text):
    print(green + text + normal)

def display_intro():
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

def start_green_text():
    print(green, end="")

def reset_text_color():
    print(normal, end="")

def input_color(input_string):
    start_green_text()
    x = input("> " + input_string)
    reset_text_color()
    return x

def main():
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