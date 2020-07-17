from random import *


# Type Error Handling and Board Checking remaining
def show_board(gboard):
    print(f' {gboard[0]} | {gboard[1]} | {gboard[2]}')
    print(r'-----------')
    print(f' {gboard[3]} | {gboard[4]} | {gboard[5]}')
    print(r'-----------')
    print(f' {gboard[6]} | {gboard[7]} | {gboard[8]}')


def isBoardFull():
    for i in board:
        if i == '_':
            return False
    return True


def isEmpty(pos):
    if board[pos] == '_':
        return True
    else:
        return False


def user_input():
    i = 0
    x = input(r"Enter your position to mark 'X'")
    if x == 'Q':
        print("Thank You for playing!\nBye")
        exit()
    else:
        x = int(x) - 1
        if isEmpty(x):
            if 0 <= x <= 8:
                print('you selected: ', x)
                return x
            else:
                print("Invalid position, Try again")
                return user_input()
        else:
            if isBoardFull():
                print("It's a tie!")
                exit()
            print("The position is occupied, Try again")
            return user_input()


def cpu_input(gboard):
    if isBoardFull():
        print("It's a tie!")
        exit()
    else:
        emptySpaces = []
        for x in range(len(gboard)):
            if gboard[x] == '_':
                emptySpaces.append(x)
        boardCopy = board.copy()
        #print("Empty Spaces: ", emptySpaces, " Board Copy: ", boardCopy)

        # Winning Situation  #
        for letter in ['O', 'X']:
            for pos in emptySpaces:
                #print(pos, " ", end="")
                boardCopy[pos] = letter
                if checkBoard(boardCopy, letter):
                    #print('\n')
                    return pos
                else:
                    boardCopy[pos] = '_'

        # Center Filling
        if gboard[4] == '_':
            return 4

        if gboard[4] == 'O':
            # Edge Filling
            for i in [1, 3, 5, 7]:
                if gboard[i] == '_':
                    return i
            # Corner Filling
            for i in [0, 2, 6, 8]:
                if gboard[i] == '_':
                    return i

        elif gboard[4] == 'X':
            # Corner Filling
            for i in [0, 2, 6, 8]:
                if gboard[i] == '_':
                    return i
            # Edge Filling
            for i in [1, 3, 5, 7]:
                if gboard[i] == '_':
                    return i


def checkBoard(gboard, ch):
    if (gboard[0] == ch and gboard[1] == ch and gboard[2] == ch) \
            or (gboard[3] == ch and gboard[4] == ch and gboard[5] == ch) \
            or (gboard[6] == ch and gboard[7] == ch and gboard[8] == ch) \
            or (gboard[0] == ch and gboard[3] == ch and gboard[6] == ch) \
            or (gboard[1] == ch and gboard[4] == ch and gboard[7] == ch) \
            or (gboard[2] == ch and gboard[5] == ch and gboard[8] == ch) \
            or (gboard[0] == ch and gboard[4] == ch and gboard[8] == ch) \
            or (gboard[2] == ch and gboard[4] == ch and gboard[6] == ch):
        return True
    else:
        return False


def main():
    while True:
        uval = user_input()
        board[uval] = 'X'
        show_board(board)
        if checkBoard(board, 'X'):
            print("You Won !!!")
            break
        print("-/-\-/-\-/-\- The CPU will play now -/-\-/-\-/-\-")
        cval = cpu_input(board)
        board[cval] = 'O'
        show_board(board)
        if checkBoard(board, 'O'):
            print("You Lost!")
            break
    return


print("Let's Play Tic Tac Toe!!!")
print(r"Press 'Q' to quit")
global tricks
tricks = True
board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
show_board(board)
main()
