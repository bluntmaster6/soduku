import random
def boardPrint(board):
        lineStr = " ----------------------- \n"
        for w in range(0,9,3):
            for i in range(w,w+3):
                lineStr += "| "
                for j in range(0,3):
                    lineStr+= str(board[i][j])+" "
            lineStr+="|\n"
            for i in range(w,w+3):
                lineStr += "| "
                for j in range(3,6):
                    lineStr+= str(board[i][j])+" "
            lineStr+="|\n"
            for i in range(w,w+3):
                lineStr += "| "
                for j in range(6,9):
                    lineStr+= str(board[i][j])+" "
            lineStr+="|\n ----------------------- \n"
        lineStr+=""
        print(lineStr)
def rowcol(x, y, board):
    #returns a list of all the values in the corresponding row and column
    rclist = []
    xset1, xset2, xset3 = [0, 1, 2], [3, 4, 5], [6, 7, 8]
    yset1, yset2, yset3 = [0, 3, 6], [1, 4, 7], [2, 5, 8]
    xset = xset1 if x in xset1 else xset2 if x in xset2 else xset3
    yset = yset1 if y in yset1 else yset2 if y in yset2 else yset3
    hset = xset1 if y in xset1 else xset2 if y in xset2 else xset3
    vset = yset1 if x in yset1 else yset2 if x in yset2 else yset3
    for i in xset:
        for c in hset:
            if i != x or c != y:
                rclist.append(board[i][c])
    for i in vset:
        for j in yset:
            if i != x or j != y:
                rclist.append(board[i][j])
    return rclist
def checkSubmission(board):
    for i in range (0,9):
        for j in range(0,9):
            if board[i][j] in rowcol(i,j,board):
                return False
    return True
def createBoard(board):
    for i in range(0,9):
        for j in range(0,9):
            valid = False
            count = 0
            while valid == False:
                gen = random.randint(1,9)
                count+=1
                if gen not in board[i] and gen not in rowcol(i,j,board):
                    board[i][j]=gen
                    valid = True
                if count > 25:
                    for w in range (0,9):
                        board[i][w]=0
                    j=-1
                    break
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]==0:
                return -1 
    return board
def boardHide(diff,board):
    for i in range(0,9):
        hidePos = []
        while len(hidePos)<diff:
            gen = random.randint(0,8)
            if gen not in hidePos:
                hidePos.append(gen)
        for c in hidePos:
            board[i][c]=" "
    return board
def main():
    board = [[0 for i in range(9)] for j in range(9)]
    valid = -1
    while valid ==-1:
        valid = createBoard(board)
        board = [[0 for i in range(9)] for j in range(9)]
    board = valid
    boardCopy = [[],[],[],[],[],[],[],[],[]]
    for i in range(0,9):
        for j in range(0,9):
            boardCopy[i].append(board[i][j])
    print("Select Difficulty, Enter 'E', 'M', or 'H':")
    diffValid = False
    while diffValid == False:
        difficultySelection = input()
        difficultySelection = difficultySelection.strip(" ")
        if difficultySelection == "E"or difficultySelection == "e":
            board = boardHide(4,board)
            diffValid = True
        elif difficultySelection == "M"or difficultySelection == "m":
            board = boardHide(5,board)
            diffValid = True
        elif difficultySelection == "H" or difficultySelection == "h":
            board = boardHide(7,board)
            diffValid = True
        else:
            print("Invalid selection, enter difficulty:")
            diffValid = False
    run = True
    boardPrint(board)
    lboard = board
    print("Instructions: Enter number using the following key and format:\n\
           _________\n\
          |1   2   3|\n\
          |4   5   6|\n\
          |"+"\x1B[4m" + "7   8   9" + "\x1B[0m"+"|\n")
    print("Position of 9x9 square, position within square, value to set as. Enter 0 as value to clear\nExample: 5 6 9\n\
          Other functions: Submit, Quit\n")
    while run == True:
        print("User:")
        choice = input()
        if choice.lower() == "submit":
            if checkSubmission(board):
                print("Correct Solution!\n")
                run = False
            else:
                print("Incorrect Solution\n")
                boardPrint(boardCopy)
                run = False
        if choice.lower() == "quit":
            run = False
        elif choice[0].isnumeric() and choice[1]==" " and choice[2].isnumeric() and choice[3] == " " and choice[4].isnumeric():
            nums = choice.strip("\n").split(" ")
            for i in nums:
                i = int(i)
                if i < 0 or i > 9:
                    print("Invalid Selection\n")
            if lboard[int(nums[0])-1][int(nums[1])-1] != " ":
                print("Invalid Selection\n")
            if int(nums[2])==0:
                board[int(nums[0])-1][int(nums[1])-1]= " "
            else:
                board[int(nums[0])-1][int(nums[1])-1]=int(nums[2])
            boardPrint(board)
main()

        