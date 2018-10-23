# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 02:25:02 2018

@author: 11658
"""

class eightQueen():
    """
    input: number of the queens
    """
    
    def __init__(self,number = 8):
        self.number = number
        self.board = list(range(number))   
        self.solution = []
    
    def shareDiagonal(self,x0, y0, x1, y1):
        """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
        dy = abs(y1 - y0)        
        dx = abs(x1 - x0)       
        return dx == dy         
    
    
    def columnClash(self, column):
        """ Return True if the queen at column c clashes
             with any queen to its left.
        """
        for i in range(column):     # Look at all columns to the left of c
              if self.shareDiagonal(i, self.board[i], column, self.board[column]):
                  return True
    
        return False        
     
    def boardClash(self):
        """ Determine whether we have any queens clashing on the diagonals.
            We're assuming here that the_board is a permutation of column
            numbers, so we're not explicitly checking row or column clashes.
        """
        for column in range(1,len(self.board)):
            if self.columnClash(column):
                return True
        return False
            
    def toFind(self,n = 10):
        """
        input : n = 10
        find n solutions of the quzzle
        """
        from copy import copy
        from random import shuffle    
        self.solution = []
        while n > 0:
           shuffle(self.board)
           if (not self.boardClash()) and (not self.board in self.solution):
               print("Found solution {0}".format(self.board))
               (self.solution).append(copy(self.board))
               n -= 1                  

    def drawAll(self):
        """
        show all the solutions on a board
        press "space" to show next solution
        """
        import pygame
        pygame.init()
        colors = [(255,0,0), (0,0,0)]    # Set up colors [red, black]
    
        n = len(self.solution[0])         # This is an NxN chess board.
        surfaceSize = 480           # Proposed physical surface size.
        squareSize = surfaceSize // n    # squareSize is length of a square.
        surfaceSize = n * squareSize     # Adjust to exactly fit n squares.
    
        # Create the surface of (width, height), and its window.
        surface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
        queen = pygame.image.load("queen.jpg")
        queen = pygame.transform.scale(queen,(squareSize,squareSize))
        # Use an extra offset to centre the ball in its square.
        # If the square is too small, offset becomes negative,
        #   but it will still be centered :-)
        queenOffset = (squareSize-queen.get_width()) // 2

        for i in self.solution:
            while True:
                # Look for an event from keyboard, mouse, etc.
                ev = pygame.event.poll()
                if (ev.type == pygame.QUIT) or (ev.type == pygame.KEYDOWN) :
                    break;
        
                # Draw a fresh background (a blank chess board)
                for row in range(n):           # Draw each row of the board.
                    colorIndex = row % 2           # Alternate starting color
                    for col in range(n):       # Run through cols drawing squares
                        square = (col*squareSize, row*squareSize, squareSize, squareSize)
                        surface.fill(colors[colorIndex], square)
                        # Now flip the color index for the next square
                        colorIndex = (colorIndex + 1) % 2
        
                # Now that squares are drawn, draw the queens.
                for (col, row) in enumerate(i):
                  surface.blit(queen,
                           (col*squareSize+queenOffset,row*squareSize+queenOffset))
        
                pygame.display.flip()
        
        pygame.quit()
            
def testOne():
    queen = eightQueen()
    queen.toFind(10)
    queen.drawAll()
             
