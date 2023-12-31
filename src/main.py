from display import *
from game import *
from generate import *
from test import *

# NOTES
# PLAYER 1 is O with the color BLUE
# PLAYER 2 is X with the color RED

# Main function
def main():
    print_green_nl("============================================== PROGRAM STARTED ==============================================")
    display_intro()
    while True:
        command = menu()
        if(command == 1): rules()
        elif(command == 2): help()
        elif(command == 3): play()
        elif(command == 4): generate()
        elif(command == 5): generate_filled()
        elif(command == 6): test_IO()
        elif(command == 7): break
    display_outro()

if __name__ == "__main__":
    main()