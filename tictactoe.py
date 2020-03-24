from typing import List

def checkio(game_result: List[str]) -> str:
    # check verticals
    for col in range(3):
        if game_result[0][col] == "X" and game_result[1][col] == "X" and game_result[2][col] == "X":
            return "X"
        elif game_result[0][col] == "O" and game_result[1][col] == "O" and game_result[2][col] == "O":
            return "O"
    # check horizontals
    for row in range(3):
        if game_result[row][0] == "X" and game_result[row][1] == "X" and game_result[row][2] == "X":
            return "X"
        elif game_result[row][0] == "O" and game_result[row][1] == "O" and game_result[row][2] == "O":
            return "O"
    
    # check diagonals
    if game_result[0][0] == "X" and game_result[1][1] == "X" and game_result[2][2] == "X":
        return "X"
    elif game_result[0][2] == "X" and game_result[1][1] == "X" and game_result[2][0] == "X":
        return "X"
    elif game_result[0][0] == "O" and game_result[1][1] == "O" and game_result[2][2] == "O":
        return "O"
    elif game_result[0][2] == "O" and game_result[1][1] == "O" and game_result[2][0] == "O":
        return "O"    
    
    else return "D"

print (checkio([
    "X.O",
    "XX.",
    "XOO"]))