def main():
    T = int(input())
    for t in range(T):
        board = [] # list of strings, each string is a line.
        x_0 = -1
        y_0 = -1
        for x in range(8):
            line = str(input())
            board.append(line)
            if ('o' in line):
                x_0 = x
                y_0 = line.index('o')
        try:
            dump = input()
        except EOFError:
            pass
        #printBoard(board);

        ans = countSuccess(board, x_0, y_0, False, None)
        print(ans)

def printBoard(board, title="Test: printBoard"):
    print(title)
    for i in range(8):
        print(board[i])

def countSuccess(board, x, y, isKing, prevloc):

    #printBoard(board, "(%d, %d)" %(x, y))
    if (whiteWins(board)):
        return 1
    else:
        if (x == 0):
            isKing = True

        actions = getAvailableActions(board, x, y, isKing, prevloc)
        if (len(actions) == 0):

            return 0
        ans = 0
        for a in actions:
            black_x = a[2]
            black_y = a[3]
            newboard = board[:black_x] + \
                [my_replace(board[black_x], black_y, '.')] + \
                board[black_x+1:]
            #printBoard(newboard, 'newBoard; a=%s' %str(a))
            ans += countSuccess(newboard, a[0], a[1], isKing, (x, y))
        return ans


def getAvailableActions(board, x, y, isKing, prevloc):
    # returns actions, a list of action
    # An action is a list.
    # a[0] and a[1] are new destinations
    # a[2] and a[3] records the coordinates of opponents it eats during this step
    actions = []
    if not isKing:
        # Go up
        if (x-2 >= 0 and board[x-1][y] == 'x' and board[x-2][y] != 'x'):
            a = [x-2, y, x-1, y]
            actions.append(a)
        # Go down
        if (x+2 <= 7 and board[x+1][y] == 'x' and board[x+2][y] != 'x'):
            a = [x+2, y, x+1, y]
            actions.append(a)
        # Go left
        if (y-2 >= 0 and board[x][y-1] == 'x' and board[x][y-2] != 'x'):
            a = [x, y-2, x, y-1]
            actions.append(a)
        # Go right
        if (y+2 <= 7 and board[x][y+1] == 'x' and board[x][y+2] != 'x'):
            a = [x, y+2, x, y+1]
            actions.append(a)
    else:
        ## isKing == True
        # Go left. Shouldn't if coming from left.
        if (prevloc == None) or (not (prevloc[0] == x and prevloc[1] < y)):
            cx = x; cy = y; hasOpponent = False;
            a2 = -1; a3 = -1
            while (cy >= 0):
                if (not hasOpponent and board[cx][cy] == 'x'):
                    hasOpponent = True
                    a2 = cx
                    a3 = cy
                elif (hasOpponent and board[cx][cy] != 'x'):
                    hasDest = True
                    a = [cx, cy, a2, a3]
                    actions.append(a)
                elif (hasOpponent and board[cx][cy] == 'x'):
                    break
                cy -= 1

        # Go right. Shouldn't if coming from right.
        if prevloc == None or not (prevloc[0] == x and prevloc[1] > y):
            cx = x; cy = y; hasOpponent = False;
            a2 = -1; a3 = -1
            while (cy <= 7):
                if (not hasOpponent and board[cx][cy] == 'x'):
                    hasOpponent = True
                    a2 = cx
                    a3 = cy
                elif (hasOpponent and board[cx][cy] != 'x'):
                    hasDest = True
                    a = [cx, cy, a2, a3]
                    actions.append(a)
                elif (hasOpponent and board[cx][cy] == 'x'):
                    break
                cy += 1

        # Go up
        if prevloc == None or not (prevloc[0] < x and prevloc[1] == y):
            cx = x; cy = y; hasOpponent = False;
            a2 = -1; a3 = -1
            while (cx >= 0):
                if (not hasOpponent and board[cx][cy] == 'x'):
                    hasOpponent = True
                    a2 = cx
                    a3 = cy
                elif (hasOpponent and board[cx][cy] != 'x'):
                    hasDest = True
                    a = [cx, cy, a2, a3]
                    actions.append(a)
                elif (hasOpponent and board[cx][cy] == 'x'):
                    break
                cx -= 1

        # Go down
        if prevloc == None or not (prevloc[0] > x and prevloc[1] == y):
            cx = x; cy = y; hasOpponent = False;
            a2 = -1; a3 = -1
            while (cx <= 7):


                if (not hasOpponent and board[cx][cy] == 'x'):
                    hasOpponent = True
                    a2 = cx
                    a3 = cy
                elif (hasOpponent and board[cx][cy] != 'x'):
                    hasDest = True
                    a = [cx, cy, a2, a3]
                    actions.append(a)
                elif (hasOpponent and board[cx][cy] == 'x'):
                    break
                cx += 1

    return actions

def my_replace(string, loc, tgt):
    return string[:loc] + tgt + string[loc+1:]

def whiteWins(board):
    for i in range(8):
        if ('x' in board[i]):
            return False
    return True

if __name__ == "__main__":
    main()
    #print (my_replace("...x....", 3, '.'))
    '''
    board = ['........', '........', '...x....', '........', \
        '........', '........', '........', '........']
    print (str(getAvailableActions(board, 0, 3, True, None)))

    board = ['........', '........', '...x....', '........', \
        '........', '...x....', '........', '........']
    print ("Should be 2: " + \
        str(len(getAvailableActions(board, 0, 3, True, None))))
    print ("Should be 0: " + \
        str(len(getAvailableActions(board, 0, 3, True, (6, 3)))))
    board = ['........', '........', '...x....', '...x....', \
            '........', '...x....', '........', '........']
    print ("Should be 0: " + \
        str(len(getAvailableActions(board, 0, 3, True, None))))

    board = ['.......o', '.x.x.x..', 'xxxx.xx.', '........', \
        '........', '.x.xx..x', 'x.......', '..x...x.']
    print ("Should be 2: " + \
        str(len(getAvailableActions(board, 0, 7, True, None))))
    print ("Should be 3: " + \
        str(len(getAvailableActions(board, 7, 7, True, (0, 7)))))
    print ("Should be 7: " + \
        str(len(getAvailableActions(board, 7, 4, True, (7, 7)))))
    print ("Should be 3: " + \
        str(len(getAvailableActions(board, 1, 4, True, (7, 4)))))
    '''
