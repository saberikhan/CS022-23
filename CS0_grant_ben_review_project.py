#─│┌ ┐└ ┘├ ┤ ┬ ┴ ┼
import random
import os
import time
import turtle as t
#imports everything
size = 5
mintowin = 4
turn = 0
win = 0
#sets basic variables
choice = input("What size would you like the board to be? (3 for 3x3, 4 for 4x4,\n5 for 5x5)\n").lower()
try:
  choice = int(choice)
  if(choice > 2 and choice < 6):
    size = choice
  else:
    size = 3
    print("Defaulting to 3.")
    time.sleep(2)
except ValueError:
  size = 3
  print("Defaulting to same 3.")
  time.sleep(2)
os.system('clear')
choice = input("How many in a row do you need to win? (1-5)\n").lower()
try:
  choice = int(choice)
  if(choice > 0 and choice < 6):
    if(choice > size):
      mintowin = size
      print("Defaulting to same as size.")
      time.sleep(2)
    else:
      mintowin = choice
  else:
    mintowin = size
    print("Defaulting to same as size.")
    time.sleep(2)
except ValueError:
  mintowin = size
  print("Defaulting to same as size.")
  time.sleep(2)
os.system('clear')
#sets variables for size and mintowin based on input
if(size == 3):
  board = [[" "," "," "], 
           [" "," "," "],
           [" "," "," "]]
elif(size == 4):
  board = [[" "," "," "," "], 
           [" "," "," "," "],
           [" "," "," "," "],
           [" "," "," "," "]]
elif(size == 5):
  board = [[" "," "," "," "," "], 
           [" "," "," "," "," "],
           [" "," "," "," "," "],
           [" "," "," "," "," "],
           [" "," "," "," "," "]]
#sets board based on size
def wincheck(board, size, mintowin):
  win = 0
  full = 1
  #sets variables
  for y in range(0, size):
    for x in range(0, size):
      #loops one time on each space in a board
      if(board[y][x] == " "):
        full = 0
      #if the space is empty it sets full to 0, if full is still 1 at the end it means the entire board is full, so if that is true AND nobody has won at the end of the function, it sets win to 3 (tie)
      else:
        rightcheck = 1
        leftcheck = 1
        upcheck = 1
        downcheck = 1
        lrdowndiagonalcheck = 1
        rldowndiagonalcheck = 1
        lrupdiagonalcheck = 1
        rlupdiagonalcheck = 1
        #sets a check variable to 1 for each direction. 
        #if they are still 1 at the end of the next loop, it means that specific check was successful, and a player has won.
        for z in range(0,mintowin):
          #loops mintowin times, starting with 0.
          if(x+z < size):
            if(board[y][x+z] != board[y][x]):
              rightcheck = 0
          #if x+z < size (if the x coord is inside the board) then it checks that space.
          #if the space it is checking is not the same as the space it is on in the loop, then it sets rightcheck to 0.
          #if it is the same, rightcheck stays the same.
          else:
            rightcheck = 0
          #if the x coord is not inside the board, it sets rightcheck to 0.
          if(x-z > -1):
            if(board[y][x-z] != board[y][x]):
              leftcheck = 0
          else:
            leftcheck = 0
          #same thing but for the left (x-z > -1 instead of x+z < size)
          if(y-z > -1):
            if(board[y-z][x] != board[y][x]):
              upcheck = 0
          else:
            upcheck = 0
          #same thing but for up (y-z > -1 instead of x-z > -1)
          if(y+z < size):
            if(board[y+z][x] != board[y][x]):
              downcheck = 0
          else:
            downcheck = 0
          #same thing but for down (y+z < size instead of y-z > -1)
          if(x+z < size and y+z < size):
            if(board[y+z][x+z] != board[y][x]):
              lrdowndiagonalcheck = 0
          else:
            lrdowndiagonalcheck = 0
          #same thing but for left-right down diagonal (x+z < size and y+z < size instead of y+z < size)
          if(x-z > -1 and y+z < size):
            if(board[y+z][x-z] != board[y][x]):
              rldowndiagonalcheck = 0
          else:
            rldowndiagonalcheck = 0
          #same thing but for right-left down diagonal (x-z > -1 and y+z < size instead of x+z < size and y+z < size)
          if(x+z < size and y-z > -1):
            if(board[y-z][x+z] != board[y][x]):
              lrupdiagonalcheck = 0
          else:
            lrupdiagonalcheck = 0
          #same thing but for left-right up diagonal (x+z < size and y-z > -1 instead of x-z > -1 and y+z < size)
          if(x-z > -1 and y-z > -1):
            if(board[y-z][x-z] != board[y][x]):
              rlupdiagonalcheck = 0
          else:
            rlupdiagonalcheck = 0
          #same thing but for right-left up diagonal (x-z > -1 and y-z > -1 instead of x+z < size and y-z > -1)
        #loops starting on the space from the y x loop, and looping mintowin times through each one.
        #for instance, checks the space according to starting space changed by z depending on the direction.
        #if the space is not the same as the starting space or the checked space is outside of the board, that direction check is 0.
        #if the check is still one after the loop, a player has won, so it checks the starting space to see which player won.
        #returns win as 1 if player 1 wins, and 2 for player 2.
        if(rightcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(leftcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(upcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(downcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(lrdowndiagonalcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(rldowndiagonalcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(lrupdiagonalcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
        if(rlupdiagonalcheck == 1):
          if("X" in board[y][x]):
            win = 1
            return win
          else:
            win = 2
            return win
  if(win == 0 and full == 1):
    win = 3
    return win
  #if the win is still 0 (if there isn't a win) and full is 1 (there wasn't an empty space in the whole board), then it returns 3 as win.
  #3 means that the board is full and it is a tie.
  return win
#wincheck function
def boardprint(board, size):
  t.penup()
  t.hideturtle()
  t.pensize(2)
  t.goto(0,0)
  t.setheading(0)
  t.speed(0)
  #sets up turtle
  if(size == 3):
    xcoord = -25
    ycoord = 50
    a1x = -50
    a1y = 25
  elif(size == 4):
    xcoord = -50
    ycoord = 100
    a1x = -75
    a1y = 75
  elif(size == 5):
    xcoord = -75
    ycoord = 125
    a1x = -100
    a1y = 100
  #sets up starting coords and coord of top right box depending onn size
  for x in range(0,size-1):
    t.penup()
    t.goto(xcoord-25,ycoord)
    if(x == 0):
      t.write("1")
    elif(x == 1):
      t.write("2")
    elif(x == 2):
      t.write("3")
    elif(x == 3):
      t.write("4")
    t.goto(xcoord,ycoord)
    t.setheading(270)
    t.pendown()
    t.forward(50*size)
    xcoord = xcoord + 50
  #prints the vertical lines based on size
  t.penup()
  t.goto(xcoord-25,ycoord)
  #sets back up
  if(size == 3):
    t.write("3")
    xcoord = -75
    ycoord = 0
  elif(size == 4):
    t.write("4")
    xcoord = -100
    ycoord = 50
  elif(size == 5):
    t.write("5")
    xcoord = -125
    ycoord = 75
  #writes the last number in and sets new coords up for horizontal lines.
  for x in range(0,size-1):
    t.penup()
    t.goto(xcoord-25,ycoord+25)
    if(x == 0):
      t.write("A")
    elif(x == 1):
      t.write("B")
    elif(x == 2):
      t.write("C")
    elif(x == 3):
      t.write("D")
    t.goto(xcoord,ycoord)
    t.setheading(0)
    t.pendown()
    t.forward(50*size)
    ycoord = ycoord - 50
  #prints the horizontal lines based on size
  t.penup()
  t.goto(xcoord-25,ycoord+25)
  #sets back up
  if(size == 3):
    t.write("C")
  elif(size == 4):
    t.write("D")
  elif(size == 5):
    t.write("E")
  #writes the last letter.
  t.goto(a1x,a1y)
  xcoord = a1x
  ycoord = a1y
  #sets up for printing the Xs and Os.
  for y in range(0,size):
    for x in range(0,size):
      t.penup()
      t.goto(xcoord,ycoord)
      if("X" in board[y][x]):
        t.penup()
        t.color('green')
        t.setheading(135)
        t.pendown()
        for x in range(0,2):
          t.forward(15)
          t.right(180)
          t.forward(30)
          t.right(180)
          t.forward(15)
          t.right(90)
        t.color('black')
        t.penup()
        t.setheading(0)
      elif("O" in board[y][x]):
        t.penup()
        t.color('red')
        t.pendown()
        t.dot(30)
        t.color('white')
        t.dot(25)
        t.color('black')
        t.penup()
      xcoord = xcoord + 50
    xcoord = a1x
    ycoord = ycoord - 50
  #loops through each space in the board, starting with top left. Prints the symbol based on what is in that board space.
  #after it prints a position, it increases the x by 50 to get to the next position. If it has finished its row, it changes the y by 50 and sets the x back to the first position x.
  t.penup()
  #finishes by picking up the pen and moving the turtle offscreen
  t.goto(1000,1000)
#boardprint function that scales to board size
while win == 0:
  for x in range(0, 1):
    row = " "
    col = " "
    #sets row and col to blank
    if (turn == 0):
      os.system('clear')
      boardprint(board, size)
      choice = input("Where would you like to go?\n").lower()
      #asks for input
      if ("a" in choice):
        row = 0
      elif ("b" in choice):
        row = 1
      elif ("c" in choice):
        row = 2
      if(size > 3 and "d" in choice):
        row = 3
      if(size > 4 and "e" in choice):
        row = 4
      #sets row variable based on letter input
      if ("1" in choice):
        col = 0
      elif ("2" in choice):
        col = 1
      elif ("3" in choice):
        col = 2
      if(size > 3 and "4" in choice):
        col = 3
      if(size > 4 and "5" in choice):
        col = 4
      #sets col variable based on number inputed
      if (row == " " or col == " "):
        print("Invalid.")
        time.sleep(1)
        break
      #if either are still blank (if you didn't select at least one or selection was invalid) then it resets and loops again.
      else:
        if (board[row][col] == " "):
          board[row][col] = "\033[0;1;32mX"
          turn = 1
          break
        #if the space is blank puts X there
        else:
          print("Invalid")
          time.sleep(1)
          break
        #if space isn't blank it resets and loops again
    else:
      row = random.randint(0,(size-1))
      col = random.randint(0,(size-1))
      if (board[row][col] == " "):
        board[row][col] = "\033[0;1;31mO"
        turn = 0
        break
      #if it is the computer's turn it loops through selecting a random board position until it is empty.
      #if tthe space is emoty it sets it to O, otherwise it loops through again.
      #then sets turn 
  os.system('clear')
  win = wincheck(board, size, mintowin)
#moving selection + computer moving
if (win == 1):
  os.system('clear')
  boardprint(board, size)
  print("\033[0;1;32mPlayer " + "\033[0;1;92mwins!")
elif (win == 2):
  os.system('clear')
  boardprint(board, size)
  print("\033[0;1;31mComputer " + "\033[0;1;92mwins!")
else:
  os.system('clear')
  boardprint(board, size)
  print("\033[0;1;93mTie!")
#checks who won or if it was a tie, prints a message based on that.
