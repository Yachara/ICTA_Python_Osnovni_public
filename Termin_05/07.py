"""
Ustvarite program Križci in Krožci

Igralno polje lahko predstavite kot liste znotraj lista, 
kjer E predstavlja prazno polje.

board = [["X", "E", "E"],
         ["O", "E", "E"],
         ["E", "E", "E"]]
Od igralcev nato izmenično zahtevajte polje v
 katerega želijo postaviti svoj znak. Privzememo 
 lahko, da bodo igralci igrali pravično in 
 vpisovali samo prazna polja.

Primeri:


Output:
['E', 'E', 'E']
['E', 'E', 'E']
['E', 'E', 'E']
It's X's turn. Make a move (exp: 12): '00

['X', 'E', 'E']
['E', 'E', 'E']
['E', 'E', 'E']
It's O's turn. Make a move (exp: 12): '12

['X', 'E', 'E']
['E', 'E', 'O']
['E', 'E', 'E']
It's X's turn. Make a move (exp: 12): '10

['X', 'E', 'E']
['X', 'E', 'O']
['E', 'E', 'E']
It's O's turn. Make a move (exp: 12): '12

['X', 'E', 'E']
['X', 'E', 'O']
['E', 'E', 'E']
It's X's turn. Make a move (exp: 12): '20
X je ZMAGOVALEC!
"""
# shorturl.at/cgn03

# Display board
def display_board(board):
    for row in board:
        print(row)


# Make a move
def make_move(board, on_move):
    print(f"Na vrsti je {on_move}")
    row = int(input("Vnesi vrstico: "))
    col = int(input("Vnesi stolpec: "))
    board[row][col] = on_move


# Is game over
def is_game_over(board):
    # Check rows
    for row in board:
        print("Vrstic: ", row)
        if row[0] != "E" and row[0] == row[1] and row[0] == row[2]:
            return True

    # Check stolpcih
    for col in range(3):
        if (
            board[0][col] != "E"
            and board[0][col] == board[1][col]
            and board[0][col] == board[2][col]
        ):
            return True

    # Check diagonals
    if board[0][0] != "E" and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True

    if board[0][2] != "E" and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True


board = [
    ["E", "E", "E"],
    ["E", "E", "E"],
    ["E", "E", "E"],
]
on_move = "X"

for i in range(9):
    print(f"Runda: {i}")
    display_board(board)
    make_move(board, on_move)

    if is_game_over(board):
        print("KOnec igre")
        print(f"Zmagovalec je : {on_move}")
        break

    if on_move == "X":
        on_move = "O"
    else:
        on_move = "X"
    print("KOnec runde")

print("Končno stanje")
display_board(board)
