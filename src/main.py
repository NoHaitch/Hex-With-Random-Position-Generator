from display import *
from game import *
from typing import List

# NOTES
# PLAYER 1 is O with the color BLUE
# PLAYER 2 is X with the color RED

# Main function
def main():
    display_intro()
    command = menu()
    if(command == 1): rules()
    elif(command == 2): help()
    elif(command == 3): None
    elif(command == 4): None

if __name__ == "__main__":
    main()
