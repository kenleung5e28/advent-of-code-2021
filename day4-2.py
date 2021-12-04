def bingo(board):
  for i in range(5):
    found = True
    for j in range(5):
      if board[i][j] != None:
        found = False
        break
    if found:
      return True
  for j in range(5):
    found = True
    for i in range(5):
      if board[i][j] != None:
        found = False
        break
    if found:
      return True
  return False

def mark(board, number):
  for i in range(5):
    for j in range(5):
      if board[i][j] == number:
        board[i][j] = None

def score(board):
  sum = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] is not None:
        sum += board[i][j]
  return sum

lines = []
with open('input-day4.txt') as file:
  lines = [l.rstrip() for l in file]
inputs = [int(s) for s in lines[0].split(',')]
boards = []
k = 1
while k < len(lines):
  k += 1
  board = []
  for i in range(5):
    l = lines[k + i]
    row = [int(l[3 * j:3 * j + 2]) for j in range(5)]
    board.append(row)
  boards.append(board)
  k += 5
bingo_list = []
for n in inputs:
  for i in range(len(boards)):
    board = boards[i]
    if board is None:
      continue
    mark(board, n)
    if bingo(board):
      bingo_list.append((board, n))
      boards[i] = None
bingo_board, final_number = bingo_list[-1]
print(score(bingo_board) * final_number)