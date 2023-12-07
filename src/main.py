from display import *
from game import *
from typing import List

# NOTES
# PLAYER 1 is O with the color BLUE
# PLAYER 2 is X with the color RED

# Function to check if Player 1 has won
def is_player1_winner(board: List[List[int]]) -> bool:
    def dfs(row, col):
        if col < 0 or col >= 5:
            return False

        if board[row][col] != 1:
            return False

        if visited[row][col]:
            return False

        visited[row][col] = True

        if col == 4:
            return True  # Player 1 has connected the left and right sides

        for dr, dc in neighbors:
            if dfs(row + dr, col + dc):
                return True

        return False

    neighbors = [(0, 1), (0, -1), (-1, 1), (1, -1), (-1, 0), (1, 0)]
    visited = [[False] * 5 for _ in range(5)]

    # Check for a path from the left side (column 0) to the right side (column 4) for Player 1
    for r in range(5):
        if board[r][0] == 1 and dfs(r, 0):
            return True

    return False

# Function to check if Player 2 has won
def is_player2_winner(board: List[List[int]]) -> bool:
    def dfs(row, col):
        if row < 0 or row >= 5:
            return False

        if board[row][col] != 2:
            return False

        if visited[row][col]:
            return False

        visited[row][col] = True

        if row == 4:
            return True  # Player 2 has connected the top and bottom sides

        for dr, dc in neighbors:
            if dfs(row + dr, col + dc):
                return True

        return False

    neighbors = [(0, 1), (0, -1), (-1, 1), (1, -1), (-1, 0), (1, 0)]
    visited = [[False] * 5 for _ in range(5)]

    # Check for a path from the top side (row 0) to the bottom side (row 4) for Player 2
    for c in range(5):
        if board[0][c] == 2 and dfs(0, c):
            return True

    return False


# Function to check if any player has won
def is_game_won(board: List[List[int]]) -> bool:
    return is_player1_winner(board) or is_player2_winner(board)


# Main function
def main():
    # Example board
    display_intro()
    command = menu()
    if(command == 1): rules()
    elif(command == 2): help()
    elif(command == 3): None

if __name__ == "__main__":
    main()
