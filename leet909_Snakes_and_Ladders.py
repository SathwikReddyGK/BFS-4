# Solution

# // Time Complexity : O(N*M)
# // Space Complexity : O(N*M)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to first flat the board so that we can associate each boxnumber with the matrix index. Now starting
# from first box put all 6 possible options in a queue and keep processing each box from queue.

from collections import deque

def snakesAndLadders(board):
    flatDict = {}
    n = len(board)
    i = n-1
    j = 0
    boxNum = 1
    flag = True
    rangeSet = set()

    while i >= 0:
        flatDict[boxNum] = [i,j]
        if flag == True:
            j += 1
        else:
            j -= 1
        
        if flag == True and j>=n:
            j = n-1
            i -= 1
            flag = False
        elif flag == False and j<0:
            j = 0
            i -= 1
            flag = True
        
        boxNum += 1
    
    boardQueue = deque()
    cur = 1
    boardQueue.append(cur)
    queueSize = len(boardQueue)
    jumpNum = 1


    while boardQueue:
        cur = boardQueue.popleft()
        curIndex = flatDict[cur]
        queueSize -= 1

        tempI = curIndex[0]
        tempJ = curIndex[1]

        rangeStart = cur + 1
        rangeEnd = min(cur+6, n*n)
        if rangeEnd == n**2:
            return jumpNum
        else:
            for futIndex in range(rangeStart,rangeEnd+1):
                
                tempIdx = flatDict[futIndex]
                if board[tempIdx[0]][tempIdx[1]] != -1 and board[tempIdx[0]][tempIdx[1]] not in rangeSet:
                    if board[tempIdx[0]][tempIdx[1]] == n**2:
                        return jumpNum
                    
                    if board[tempIdx[0]][tempIdx[1]] not in rangeSet:
                        boardQueue.append(board[tempIdx[0]][tempIdx[1]])
                        rangeSet.add(board[tempIdx[0]][tempIdx[1]])
                elif board[tempIdx[0]][tempIdx[1]] == -1:
                    if futIndex not in rangeSet:
                        boardQueue.append(futIndex)
                        rangeSet.add(futIndex)
        
        if queueSize == 0:
            queueSize = len(boardQueue)
            jumpNum += 1
    
    return -1

if __name__ == "__main__":
    board = [[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]
    print(snakesAndLadders(board))