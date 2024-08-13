from enum import Enum
from typing import TypeAlias

class Player(Enum):
    Player1 = 1
    Player2 = 2
    Neutral = 0

Position: TypeAlias = tuple[int, int]
Board: TypeAlias = list[list[Player]]

WIDTH = 10
HEIGHT = 10

board: Board = [[Player.Neutral]*WIDTH for _ in range(HEIGHT)]

  
def makeMove(player : Player, pos: Position) -> bool:
    if not(isValidMove):
        return False
    
    addMove(player, pos)
    return True

def isValidMove(pos: Position)->bool:
    return board[pos[0]][pos[1]] == Player.Neutral

def addMove(player: Player, pos: Position)-> None:
    board[pos[0]][pos[1]] = player

def IsWinningMove(player: Player, pos: Position)->bool:
    horizontal = (1,0)
    vertical = (0,1)
    diagonal = (1,1)
    directions = [horizontal, vertical, diagonal]

    for dir in directions:
        if IsFiveInLine(player, pos, dir):
            return True
        
    return False

def isPosOutOfBound(pos):
    xOutOfBound = pos[0] < 0 or pos[0] >= WIDTH
    yOutOfBound = pos[1] < 0 or pos[1] >= HEIGHT
    return xOutOfBound or yOutOfBound

def IsFiveInLine(player: Player, pos: Position, direction)->bool:
    def countDirection(direction):
        numConsecutive = 0
        currentPos = pos
        while not(isPosOutOfBound(currentPos)) and  board[currentPos[0]][currentPos[1]] == player:
            numConsecutive = numConsecutive + 1
            currentPos = (currentPos[0] + direction[0], currentPos[1] + direction[1])
        return numConsecutive
    
    forwardDir = direction
    backwardsDir = (forwardDir[0] * -1, forwardDir[1] * -1)
    
    #Looks at both forward and backwards direction of a line
    numForDir = countDirection(forwardDir)
    numBackDir = countDirection(backwardsDir)

    total = numForDir + numBackDir - 1

    return total >=5

def startGame():
    board = [[Player.Neutral]*WIDTH for _ in range(HEIGHT)]
    winner = Player.Neutral
    playerTurn = Player.Player1
    
    while winner == Player.Neutral:
        validMoveChosen = False

        pos = userInteraction()

        addMove(playerTurn, pos)
        if IsWinningMove(playerTurn, pos):
            winner = playerTurn
        else: 
            playerTurn = Player.Player2 if playerTurn == Player.Player1 else Player.Player1
    
    display()
    print("Player: " + playerToString(playerTurn) + " won")

    return

def playerToString(player: Player):
    match player:
        case Player.Player1:
            return "P1"
        case Player.Player2:
            return "P2"
        case Player.Neutral:
            return "Neutral"
        
def userInteraction()->Position:
    display()
    validMoveChosen = False
    pos = (0,0)
    while not(validMoveChosen):
        playersTurn = Player.Player1
        print("choose square")
        inpStr = input() 
        numStrs = inpStr.split(" ")
        ints = list(map(int, numStrs))
        pos = (ints[0], ints[1])
        
        if not(isValidMove(pos)):
            print("Enter valid square")
        else:
            validMoveChosen = True   
    return pos


def display():       
    def getPlayerFromDisplayPos(displayPos):
        #Y increases upwards in game representation, but decreases upwards as stored in array
        return board[displayPos[0]][HEIGHT-displayPos[1]-1]
    def playerToChar(player: Player):
        match player:
            case Player.Player1:
                return 'X'
            case Player.Player2:
                return 'O'
            case Player.Neutral:
                return ' '
        
    display = [[playerToChar(getPlayerFromDisplayPos((x,y))) for x in range(WIDTH)] for y in range(HEIGHT)]


    for line in display:
        print(line)
    print()


startGame()






