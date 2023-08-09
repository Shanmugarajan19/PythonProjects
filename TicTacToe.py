def printBoard(b):
    print("-------------------")
    for i in b:
        print(end="|  ")
        for a in i:
            print(*a, end="  |  ")
        print("\n-------------------")


def moveCoin(pos, temp):
    if pos == 1:
        board[0][0] = temp
    elif pos == 2:
        board[0][1] = temp
    elif pos == 3:
        board[0][2] = temp
    elif pos == 4:
        board[1][0] = temp
    elif pos == 5:
        board[1][1] = temp
    elif pos == 6:
        board[1][2] = temp
    elif pos == 7:
        board[2][0] = temp
    elif pos == 8:
        board[2][1] = temp
    elif pos == 9:
        board[2][2] = temp


def checkBoard(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        win = 1
    elif board[0][1] == board[0][2] == board[0][0] and board[0][1] != " ":
        win = 1
    elif board[1][1] == board[1][2] == board[1][0] and board[1][1] != " ":
        win = 1
    elif board[2][1] == board[2][2] == board[2][0] and board[2][1] != " ":
        win = 1
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        win = 1
    elif board[0][1] == board[1][1] == board[2][1] and board[1][1] != " ":
        win = 1
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        win = 1
    elif board[0][2] == board[1][1] == board[2][0] and board[2][0] != " ":
        win = 1
    else:
        win = 0
    return win


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
win = 0

print("Welcome !!!  TIC TAK TOE ")

pn1 = str(input("\nEnter Player 1 Name : "))
pn2 = str(input("Enter Player 2 Name: "))
count = 0
i = 1
checkpos = []
while (count < 9):
    if count % 2 == 0:
        printBoard(board)
        pos = int(input(f"{pn1} can play now : "))
        batch = True
        while batch:
            if pos in checkpos:
                pos = int(
                    input(f"{pn1} can play now and position is already occupies .You should enter correct position : "))
            else:
                batch = False
        checkpos.append(pos)
        moveCoin(pos, "X")

        if checkBoard(board) == 1:
            print(f"{pn1} Wins The Tropy")
            i = 0
            break

    else:
        printBoard(board)
        pos = int(input(f"{pn2} can play now : "))
        batch = True
        while batch:
            if pos in checkpos:
                pos = int(
                    input(f"{pn1} can play now and position is already occupies .You should enter correct position : "))
            else:
                batch = False
        checkpos.append(pos)
        moveCoin(pos, "O")

        if checkBoard(board) == 1:
            print("f{pn2} Wins The Tropy")
            i = 0
            break
    count += 1
printBoard(board)
if i != 0:
    print("Match Draw")







