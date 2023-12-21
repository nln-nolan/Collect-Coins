from kandinsky import *
from random import *
from ion import *
from time import *

# Color
_colorWhite = (255,255,255)
_colorBlack = (0,0,0)
_colorRed = (255,0,0)

_colorLifeGreen = (0,255,0)
_colorLifeOrange = (200,100,0)
_colorLifeRed = (255,0,0)

_colorBackgroundGameOver = (30,30,30)


def GameOver():
  # Background
  fill_rect(0,0,500,500,_colorBackgroundGameOver)

  fill_rect(100,80,120,30,_colorRed)
  draw_string("Game Over",115,85,_colorWhite,_colorRed)
  
  draw_string("Score : ",110,130,_colorWhite,_colorBackgroundGameOver)
  draw_string(str(score),190,130,_colorWhite,_colorBackgroundGameOver)

  draw_string("By nln.nolan",100,200,_colorWhite,_colorBackgroundGameOver)


def start():
  # Background
  fill_rect(0,0,500,500,_colorWhite)

  # Player Position
  playerPositionX = 140
  # Clear Player Position
  playerClearPositionX = playerPositionX - 30

  
  piecePositionX = randrange(2,308)
  piecePositionY = 0

  pieceClearPositionX = piecePositionX
  pieceClearPositionY = piecePositionY - 10

  global score
  score = 0

  life = 3    
  lifeChange = 1

  gameOver = 0

  while gameOver == 0:
    # Player display
    fill_rect(playerPositionX,210,30,5,_colorBlack)
    # Clear Player display
    fill_rect(playerClearPositionX,210,30,5,_colorWhite)

    
    fill_rect(piecePositionX,piecePositionY,10,10,'yellow')
    fill_rect(pieceClearPositionX,pieceClearPositionY,10,10,_colorWhite)
    piecePositionY += 2
    pieceClearPositionY = piecePositionY - 10
    sleep(0.01)


    # Mouvemente Left
    if keydown(KEY_LEFT):
      playerPositionX -= 2
      playerClearPositionX = playerPositionX + 30
    # Mouvemente Right            
    if keydown(KEY_RIGHT):
      playerPositionX += 2
      playerClearPositionX = playerPositionX - 30

    # Border Left
    if playerPositionX == 290:
      playerPositionX -= 2
    # Border Right
    if playerPositionX == 0:
      playerPositionX += 2


    # Score
    if piecePositionY == 210:
      if playerPositionX - 10 < piecePositionX < playerPositionX + 30:
        pieceClearPositionY += 8
        fill_rect(pieceClearPositionX,pieceClearPositionY,10,10,_colorWhite)
        piecePositionX = randrange(2,308)
        piecePositionY = 0
        pieceClearPositionX = piecePositionX
        pieceClearPositionY = piecePositionY - 10
        score += 1
      else:
        pieceClearPositionY += 8
        fill_rect(pieceClearPositionX,pieceClearPositionY,10,10,_colorWhite)
        piecePositionX = randrange(2,308)
        piecePositionY = 0
        pieceClearPositionX = piecePositionX
        pieceClearPositionY = piecePositionY - 10
        lifeChange = 1
        life -= 1
                    
    draw_string(str(score),1,1)

    # Life
    if piecePositionX >= 250 and pieceClearPositionY <= 20:
      lifeChange = 1

    if lifeChange == 1:
      if life <= 0:
        gameOver = 1
        GameOver()
      if life == 3:
        fill_rect(252,2,61,15,_colorBlack)
        fill_rect(254,4,57,11,_colorLifeGreen)
        lifeChange = 0
      if life == 2:      
        fill_rect(252,2,61,15,_colorBlack)
        fill_rect(274,4,37,11,_colorLifeOrange)
        lifeChange = 0
      if life == 1:      
        fill_rect(252,2,61,15,_colorBlack)
        fill_rect(294,4,17,11,_colorLifeRed)
        lifeChange = 0

  
start()
