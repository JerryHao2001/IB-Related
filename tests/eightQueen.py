# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 02:25:02 2018

@author: 11658
"""

class eightQueen():
        
    def __init__(self):
        self.board = list(range(8))   
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
        from random import shuffle    
        self.solution = []
        while n > 0:
           shuffle(self.board)
           if not self.boardClash():
               print("Found solution {0}".format(self.board))
               (self.solution).append(self.board)
               n -= 1

        
                  
    
    def drawOne(self,i):
        import pygame
        """ Draw a chess board with queens, as determined by the the_board. """

        pygame.init()
        colors = [(255,0,0), (0,0,0)]    # Set up colors [red, black]
    
        n = len(self.solution[i])         # This is an NxN chess board.
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
    
        while True:
    
            # Look for an event from keyboard, mouse, etc.
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
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
            for (col, row) in enumerate(self.solution[i]):
              surface.blit(queen,
                       (col*squareSize+queenOffset,row*squareSize+queenOffset))
    
            pygame.display.flip()
    
    
        pygame.quit()
    
    
    
    
    def drawBoards(self,n):
        assert n <= len(self.solution), "u don't have so many solutions!"        
        keepOn = "yes"
        for i in range(0,n):
            if keepOn == 'yes':
                self.drawOne(i)
            keepOn = input("input 'yes' to keep on").lower()
            
                
            
def testOne():
    queen = eightQueen()
    queen.toFind(2)
    queen.drawBoards(2)
             
