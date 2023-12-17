from kandinsky import *
from random import *
from ion import *
from time import *

def GameOver():
  # Background
  fill_rect(0,0,500,500,'black')

  fill_rect(100,80,120,30,'red')
  draw_string("Game Over",115,85,color(255,255,255),color(255,0,0))
  
  draw_string("Score : ",110,130,color(255,255,255),color(0,0,0))
  draw_string(str(score),190,130,color(255,255,255),color(0,0,0))


def start():
  # Background
  fill_rect(0,0,500,500,'white')

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
  gameOver = 0

  while gameOver == 0:
    # Player display
    fill_rect(playerPositionX,210,30,5,color(0,0,0))
    # Clear Player display
    fill_rect(playerClearPositionX,210,30,5,color(255,255,255))

    
    fill_rect(piecePositionX,piecePositionY,10,10,'yellow')
    fill_rect(pieceClearPositionX,pieceClearPositionY,10,10,color(255,255,255))
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
        fill_rect(pieceClearPositionX,pieceClearPositionY,10,10,color(255,255,255))
        piecePositionX = randrange(2,308)
        piecePositionY = 0
        pieceClearPositionX = piecePositionX
        pieceClearPositionY = piecePositionY - 10
        score += 1
      else:
        pieceClearPositionY += 8
        fill_rect(pieceClearPositionX,pieceClearPositionY,10,10,color(255,255,255))
        piecePositionX = randrange(2,308)
        piecePositionY = 0
        pieceClearPositionX = piecePositionX
        pieceClearPositionY = piecePositionY - 10
        life -= 1
                    
    draw_string(str(score),1,1)

    # life
    if life <= 0:
      gameOver = 1
      GameOver()
    if life == 3:      
      fill_rect(280,1,10,10,'red')
      fill_rect(293,1,10,10,'red')
      fill_rect(306,1,10,10,'red')
    if life == 2:      
      fill_rect(280,1,10,10,'white')
      fill_rect(293,1,10,10,'red')
      fill_rect(306,1,10,10,'red')
    if life == 1:      
      fill_rect(280,1,10,10,'white')
      fill_rect(293,1,10,10,'white')
      fill_rect(306,1,10,10,'red')
    
    
start()
