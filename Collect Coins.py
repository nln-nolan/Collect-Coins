# ╔═══════════════HI═════════════════╗
# ║    Hi user, welcome to my game   ║
# ╠═════════════CREATOR══════════════╣
# ║    Original code by nln.nolan    ║
# ╠══════════════DATE════════════════╣
# ║      Created on 18/12/2023       ║
# ╚══════════════════════════════════╝

from kandinsky import *
from ion import *
from time import *
from random import *


# Color
_colorBlack = (0,0,0)
_colorWhite = (255,255,255)
_colorGrey = (100,100,100)
_colorRed = (255,0,0)
_colorBrown = (255,204,153)

_colorBackground = (160,160,160)

def Menu():
  # Background
  fill_rect(0,0,500,500,_colorBackground)

  # Logo
  draw_string("Allumette",115,20,_colorWhite,_colorBackground)

  # Menu
  fill_rect(116,66,88,28,_colorRed)
  fill_rect(118,68,84,24,_colorBlack)
  fill_rect(120,70,80,20,_colorGrey)
  draw_string("vs Bot",130,71,_colorWhite,_colorGrey)


  fill_rect(117,127,86,26,_colorBlack)
  fill_rect(120,130,80,20,_colorGrey)
  draw_string("vs p2",130,131,_colorWhite,_colorGrey)

  draw_string("By nln.nolan",100,200,_colorWhite,_colorBackground)
  
  
  menu = 1
  cursorPlace = 1
  while menu == 1:
    if keydown(KEY_UP):
      fill_rect(116,66,88,28,_colorRed)
      fill_rect(118,68,84,24,_colorBlack)
      fill_rect(120,70,80,20,_colorGrey)
      draw_string("vs Bot",130,71,_colorWhite,_colorGrey)

      fill_rect(116,126,88,28,_colorBackground)
      fill_rect(117,127,86,26,_colorBlack)
      fill_rect(120,130,80,20,_colorGrey)
      draw_string("vs p2",130,131,_colorWhite,_colorGrey)
      cursorPlace = 1
      sleep(0.2)

    if keydown(KEY_DOWN):
      fill_rect(116,126,88,28,_colorRed)
      fill_rect(118,128,84,24,_colorBlack)
      fill_rect(120,130,80,20,_colorGrey)
      draw_string("vs p2",130,131,_colorWhite,_colorGrey)

      
      fill_rect(116,66,88,28,_colorBackground)
      fill_rect(117,67,86,26,_colorBlack)
      fill_rect(120,70,80,20,_colorGrey)
      draw_string("vs Bot",130,71,_colorWhite,_colorGrey)
      cursorPlace = 2
      sleep(0.2)

    if keydown(KEY_OK) or keydown(KEY_EXE):
      if cursorPlace == 1:
        Bot()
      elif cursorPlace == 2:
        OneVOne()



def OneVOne():
  # Background
  fill_rect(0,0,500,500,_colorBackground)

  allumettes = 0
  player = 2
  fill_rect(110,0,97,30,'yellow')
  fill_rect(113,2,91,25,'black')
  draw_string("Joueur 1",118,6,_colorWhite,_colorBlack)


  def draw(nb, baton, top):
    for i in range(nb):
      fill_rect(i*15+10,90,5,50,baton)
      fill_rect(i*15+9,80,7,10,top)
  draw(20,_colorBrown,_colorRed)

  draw_string("Enlevez 1, 2 ou 3 allumettes.",10,175,_colorWhite,_colorBackground)
  draw_string("L'autre joueur joue après vous.",10,200,_colorWhite,_colorBackground)

  while allumettes < 19:
    if keydown(KEY_ONE):
      allumettes += 1
      if player == 1:
        fill_rect(110,0,97,30,'yellow')
        fill_rect(113,2,91,25,'black')
        draw_string("Joueur 1",118,6,_colorWhite,_colorBlack)
        player = 2
      else:
        fill_rect(110,0,97,30,'yellow')
        fill_rect(113,2,91,25,'black')
        draw_string("Joueur 2",118,6,_colorWhite,_colorBlack)
        player = 1

    elif keydown(KEY_TWO):
      allumettes += 2
      if player == 1:
        fill_rect(110,0,97,30,'yellow')
        fill_rect(113,2,91,25,'black')
        draw_string("Joueur 1",118,6,_colorWhite,_colorBlack)
        player = 2
      else:
        fill_rect(110,0,97,30,'yellow')
        fill_rect(113,2,91,25,'black')
        draw_string("Joueur 2",118,6,_colorWhite,_colorBlack)
        player = 1

    elif keydown(KEY_THREE):
      allumettes += 3
      if player == 1:
        fill_rect(110,0,97,30,'yellow')
        fill_rect(113,2,91,25,'black')
        draw_string("Joueur 1",118,6,_colorWhite,_colorBlack)
        player = 2
      else:
        fill_rect(110,0,97,30,'yellow')
        fill_rect(113,2,91,25,'black')
        draw_string("Joueur 2",118,6,_colorWhite,_colorBlack)
        player = 1

    draw(allumettes,_colorBackground,_colorBackground)
    sleep(0.2)


    if player == 1:
      if allumettes > 19:
        fill_rect(0,30,300,40,_colorBackground)
        draw_string("Joueur 2 a gagné",80,40,_colorWhite,_colorBackground)
      elif allumettes == 19:
        fill_rect(0,30,300,40,_colorBackground)
        draw_string("Joueur 1 a gagné",80,40,_colorWhite,_colorBackground)

    if player == 2:
      if allumettes > 19:
        fill_rect(0,30,300,40,_colorBackground)
        draw_string("Joueur 1 a gagné",80,40,_colorWhite,_colorBackground)
      elif allumettes == 19:
        fill_rect(0,30,300,40,_colorBackground)
        draw_string("Joueur 2 a gagné",80,40,_colorWhite,_colorBackground)



def Bot():
  # Background
  fill_rect(0,0,500,500,_colorBackground)

  allumettes = 0

  def draw(nb, baton, top):
    for i in range(nb):
      fill_rect(i*15+10,90,5,50,baton)
      fill_rect(i*15+9,80,7,10,top)
  draw(20,_colorBrown,_colorRed)


  while allumettes < 19:
    while True:
      draw_string("Enlevez 1, 2 ou 3 allumettes.",10,175,_colorWhite,_colorBackground)
      draw_string("L'ordinateur joue après vous.",10,200,_colorWhite,_colorBackground)
      if keydown(KEY_ONE):
        allumettes+=1
        break

      elif keydown(KEY_TWO):
        allumettes+=2
        break

      elif keydown(KEY_THREE):
        allumettes+=3
        break
      
    draw(allumettes,_colorBackground,_colorBackground)
    sleep(0.2)

    if allumettes == 19:
      draw_string("Vous avez gagné",85,30,_colorWhite,_colorBackground)
    else:
      if (20-allumettes)%4==3:
        allumettes+=2
      else:
        if (20-allumettes)%4==0:
          allumettes+=3
        else:
          if (20-allumettes)%4==2:
            allumettes+=1
          else:
            allumettes+=randint(1,3 if allumettes < 17 else 20-allumettes-1)
      draw(allumettes,_colorBackground,_colorBackground)
      if allumettes == 19:
        draw_string("Vous avez perdu",85,30,_colorWhite,_colorBackground)


Menu()

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
