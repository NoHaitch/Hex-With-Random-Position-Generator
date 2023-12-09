from multiprocessing import Pool
from typing import Tuple
from display import *
from game import *
from generate import *

# THIS FILE FOR THE TESTING OF 2 FACTS
# 1. In Hex, There is always a winner, the game cannot be a draw
# 2. Trying to prove that going first has an advantage

def test_single_game() -> Tuple[int, int]:
    board = [[0 for _ in range(5)] for _ in range(5)]
    current_player = 1
    while not is_won(board):
        code = generate_location_code(board)
        board = set_hex(code, board, current_player)
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
    if check_win_player1(board):
        return 1, 0
    else:
        return 0, 1

def test(sample: int) -> Tuple[int, int]:
    with Pool() as pool:
        results = pool.map(test_single_game, range(sample))

    count_win_player1 = sum(result[0] for result in results)
    count_win_player2 = sum(result[1] for result in results)
    
    return count_win_player1, count_win_player2

def test_IO() -> None:
    print("How many random games do you want to do?")
    sample = -1
    while True:
        input_text = input_color("")
        if input_text.isdigit():
            sample = int(input_text)
            if(input_text < 1):
                print_red_nl("Invalid input\n")
            else:
                break
        else:
            print_red_nl("Invalid input\n")
    print("\n==================== ", end="");print_yellow("TESTING");print(" ====================")
    count_win_player1, count_win_player2 = test(sample)
    print("\n==================== ", end="");print_yellow("FINISHED");print(" ====================")
    print("RESULT :")
    print("Player 1 wins : ", end="");print_yellow_nl(str(count_win_player1))
    print("Player 2 wins : ", end="");print_yellow_nl(str(count_win_player2))
    print("Win ratio for player 1 : ", end="");print_yellow(str((count_win_player1 / (count_win_player1 + count_win_player2)) * 100));print("%")

# Run the test
if __name__ == "__main__":
    test_IO()
