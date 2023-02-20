# Created by Hakim 'Azizan on 28/3/2022
# This is tic-tac-toe python terminal game

# Welcome string
welcome = """
______________________________________________________________________________________________

                         _    _       _                 _             
                        | |  (_)     | |               | |            
                        | |_  _  ___ | |_  __  _   ___ | |_  _____   ___ 
                        | __|| |/  _|| __|/  _` | / __|| __|/  _  \ / _ \\
                        | |_ | || (_ | |_ | (_| || (__ | |_ | (_) ||  __/
                        \___||_|\___|\___|\__,__| \___| \__|\_____/ \___|

                           Created by Hakim 'Azizan, 28th March 2022
______________________________________________________________________________________________
"""

# Initialize board state
board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

# Count number of moves
count =  1

# Turn state: O = 0, X = 1
turn = 0

# Printing the board
def print_board(board):
    column = "    1   2   3"
    print(column)
    print("  -------------")
    for i in range(3):
        print(i+1,end =" ")
        for x in range(3):
            print("|",board[i][x],"", end = "")
        
        print("|",end="")
        print("\n  -------------")

# Checking board for win
# Check every rows
def check_row(board):    
    for x in range(len(board)):
        if board[x].count("O") == 3:
            for y in range(len(board[x])):
                board[x][y] = "O"
            return 1
        elif board[x].count("X") == 3:
            for y in range(len(board[x])):
                board[x][y] = "X"
            return 2
        else:
            return 0
    
# Check every column
def check_column(board):
    t_board = []
    r1 = []
    r2 = []
    r3 = []
    for row in board:
        for i in range(len(row)):
            if i == 0:
                r1.append(row[i])
            if i == 1:
                r2.append(row[i])
            if i == 2:
                r3.append(row[i])
    t_board.append(r1)
    t_board.append(r2)
    t_board.append(r3)
    return check_row(t_board)

# Check diagonal
def check_diagonal(board):
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]
    d_all = [d1, d2]
    for d in d_all:
        if d.count("O") == 3:
            return 1
        elif d.count("X") == 3:
            return 2
        else:
            return 0

# Check total board for win
def check(board):
    c = check_column(board)
    r = check_row(board)
    d = check_diagonal(board)
    
    if c != 0:
        return c
    elif r != 0:
        return r
    elif d != 0:
        return d
    else:
        return 0

# Inquiry input from player
def input_move(player, board):
    print("{}, it is your turns ({})".format(player.name, player.symbol))
    print("Please input coordinate for your move, (row<space>column), example: '1 1'")
    state = 0
    while state == 0:
        coordinate = input()
        try :
            coordinate = coordinate.split(" ")
            coordinate = [int(i)-1 for i in coordinate]
            if board[coordinate[0]][coordinate[1]] == " ":
                board[coordinate[0]][coordinate[1]] = player.symbol
                state = 1
            else:
                print("Invalid coordinate, please enter again")
        except:
            print("Invalid coordinate, please enter again")
        

# Player class
class Player():

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


print(welcome)
print("Please input 1st player's ('O') name:")
o_name = input()
o_player = Player(o_name, "O")
print("Welcome,", o_player.name+"!")

print("Please input 2nd player's ('X') name:")
x_name = input()
x_player = Player(x_name, "X")
print("Here comes the challenger,", x_player.name+"!")

state = 0
while state == 0 and count < 9:
    print_board(board)
    if turn == 0:
        input_move(o_player, board)
        turn = 1
    else:
        input_move(x_player, board)
        turn = 0
    state = check(board)
    count += 1
print_board(board)
if state == 1:
    print("{} (O) wins!".format(o_player.name))
elif state == 2:
    print("{} (X) wins!".format(x_player.name))
else:
    print("Nobody wins, it is a draw!")
print("Thanks for playing!")


