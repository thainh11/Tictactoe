board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
game=True
def b(board):
    print("      TIC TAC TOE     ")
    print(" ")
    print("Player1(X) - Player2(O)")
    print("                  ")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("-------------------------------- ")

player = "X"
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def position(board):
    global player
    print(f'Player {player} choose ')
    a = int(input("Choose number 1-9: "))
    print("")
    while a>9:
        print('Invalid number')
        a = int(input("Choose number 1-9: "))
    if a>0 and a<=9:
        while board[a-1]=="X" or board[a-1]=="O":
            print("Choose another number")
            a = int(input("Choose number 1-9: "))
        if board[a-1]>"0" and board[a-1]<="9":
            board[a-1] = player
            print(f'{player} choose {a}')
            print("---------------------------")
    
def check(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8] :
        return True
    elif board[2] == board[4] == board[6]:
        return True

def ketqua(board):
    global game
    if check(board):
        b(board)
        switch_player()
        print(f"The winner is {player}!")
        exit()
    elif (board.count("1")==0) and board.count('2')==0 and board.count('3')==0 and board.count('4')==0 and board.count('5')==0 and board.count('6')==0 and board.count('7')==0 and board.count('8')==0 and board.count('9')==0 :
        b(board)
        print("Draw")
        exit()

while True:
    b(board)
    position(board)
    switch_player()
    ketqua(board)
    



