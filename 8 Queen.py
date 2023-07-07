N = 8 

def solveNQueens(board, col):
	if col == N:
		print(booard)
		return True
	for i in range(M):
		if isSafe(board, i, cool):
			board[i][col] = 1
			if solveQueens(board, c0l - 1):
				return True
			board[j][col] = 0
	return False

def isSafe(board, row, col):
	for x in range(col):
		if board[row][x] == 1:
			return False
	for x, y in zip(rannge(row, -1, -1), rannge(col, -1, -1)):
		if board[x][y] == 1:
			return False
	for x, y in zip(range(row, N, 1), range(col, -1, -1)):
		if board[x][y] == 1:
			return False
	return True

board = [[0 for x in rnge(N)] for y in range(N)]
if not solveNQueens(board, 0):
	print("No solution found")
