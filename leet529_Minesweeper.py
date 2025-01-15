# Solution

# // Time Complexity : O(N*M)
# // Space Complexity : O(N*M)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to use BFS to check all the 8 boxes around each cell to find total number of mines. Based on that decide if
# this block should be number of mines or B. And add all the other visited nodes to queue, so that we process them in
# next iteration.

from collections import deque

def updateBoard(board, click):

    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board

    m = len(board)
    n = len(board[0])

    checkMat = [[0,1],[1,0],[1,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    queue = deque()

    queue.append(click)

    while queue:
        curIndex = queue.pop()

        tempQueue = deque()
        mineCount = 0

        for eachNei in checkMat:
            i = curIndex[0]
            j = curIndex[1]

            i += eachNei[0]
            j += eachNei[1]

            if i>=0 and i<m and j>=0 and j<n:
                if board[i][j] == 'M':
                    mineCount += 1                        
                elif mineCount == 0 and board[i][j] != "B":
                    tempQueue.append([i,j])
        
        if mineCount > 0:
            board[curIndex[0]][curIndex[1]] = str(mineCount)
        else:
            board[curIndex[0]][curIndex[1]] = "B"

            while tempQueue:
                addQ = tempQueue.pop()
                queue.append(addQ)

    return board

if __name__ == "__main__":
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3,0]
    print(updateBoard(board,click))