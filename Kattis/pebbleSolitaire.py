from sys import stdin


def pebSolitaire(board):
    global visited
    #default number of pebbles set to max
    numOfPeb = 23

    #if the board is already visited return the default number of pebbles
    if tuple(board) in visited:
        return numOfPeb

    #if not mark it as visited
    visited.add(tuple(board))

    for i in range(23):

        # if there is a possible move to right
        if i < 21 and board[i] and board[i+1] and not board[i+2]:
            # remove the pebble and check the minimum number of pebbles recursively
            board[i] = board[i + 1] = 0
            board[i + 2] = 1
            numOfPeb = min(numOfPeb, pebSolitaire(board))
            # put the pebble back to check further steps
            board[i] = board[i + 1] = 1
            board[i + 2] = 0

        # if there is a possible move to left
        if i > 1 and board[i] and board[i-1] and not board[i-2]:
            # remove the pebble and check the minimum number of pebbles recursively
            board[i] = board[i-1] = 0
            board[i-2] = 1
            numOfPeb = min(numOfPeb, pebSolitaire(board))
            # put the pebble back to check further steps
            board[i] = board[i-1] = 1
            board[i-2] = 0

    #return the minimum number of pebble
    return min(numOfPeb, board.count(1))


n = int(stdin.readline())
visited = set()

for _ in range(n):
    board = [1 if cavity == 'o' else 0 for cavity in stdin.readline().strip()]
    print(pebSolitaire(board))
