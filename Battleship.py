# Battle Ship Game

""" In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 4 guesses to try to sink the ship."""

# generate an empty board
from random import randint
  
board = []
for x in range(5):
    row = []
    for y in range(5):
        row.append("X")
    board.append(row)

# make the board look nice by removing quotation marks and linking 'X's with spaces
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

# let the machine generate the random location of the ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Let the gamer try four times to guess the location of the ship
for turn in range(4):
  guess_row = int(raw_input("Enter a row number:")) #int changes String into Integer
  guess_col = int(raw_input("Enter a column number:"))
  
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!" 
    break # no need to continue the game; break from the for loop
  else:
    if guess_row not in range(5) or \       # situation: input the location outside the board
    guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X": # situation: already guess that one
      print "You guessed that one already."
    else:
      print "You missed my battleship!" # lose the game. Make an X mark on the guessed place
      board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 3:
      print "Game Over"
  
  # print turn + 1 here
  print "Turn", turn+1
