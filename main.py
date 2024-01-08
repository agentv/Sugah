import random

R = 16
C = 16

class SugarCell:
 def __init__(self, sugar):
   self.sugar = sugar
   self.multiplier = 1

 def take_sugar(self, amount):
   self.sugar -= amount
   if self.sugar < 0:
     self.sugar = 0

class SugarSurface:
 def __init__(self, rows, cols):
   self.rows = rows
   self.cols = cols
   self.cells = [[SugarCell(random.randint(1, 10)) for _ in range(cols)] for _ in range(rows)]

 def get_cell(self, row, col):
   if 0 <= row < self.rows and 0 <= col < self.cols:
     return self.cells[row][col]
   else:
     return None

class Miner:
 def __init__(self, surface, row, col):
   self.surface = surface
   self.row = row
   self.col = col

 def getLocation(self):
    return (self.row, self.col)

 def move(self, direction):
   if direction == "up":
     self.row -= 1
   elif direction == "down":
     self.row += 1
   elif direction == "left":
     self.col -= 1
   elif direction == "right":
     self.col += 1
   elif direction == "up_left":
     self.row -= 1
     self.col -= 1
   elif direction == "up_right":
     self.row -= 1
     self.col += 1
   elif direction == "down_left":
     self.row += 1
     self.col -= 1
   elif direction == "down_right":
     self.row += 1
     self.col += 1

 def mine(self):
   cell = self.surface.get_cell(self.row, self.col)
   if cell:
     cell.take_sugar(1)

b = SugarSurface(R,C)
m = Miner(b, 8, 8)

for r in range(R):
  for c in range(C):
    print( "(" + str(r) + "," + str(c) + "): " + str(b.get_cell(r,c).sugar))

  

