import random

class SugarCell:
 def __init__(self, sugar):
   self.sugar = sugar
   self.multiplier = 1

 def take_sugar(self, amount):
   self.sugar -= amount
   if self.sugar < 0:
     self.sugar = 0

class SugarSurface:
  def __init__(self, rows, cols, limit):
   self.rows = rows
   self.cols = cols

    # we populate the cells here by simply giving a random number
    # from 1 to limit
    # the real plan is to use the same distribution of value
    # used in Scrabble
    # ie. 1:49, 2:15, 3:11, 4:13, 5:1
   self.cells = [
     [SugarCell(random.randint(1, limit)) for _ in range(cols)]
        for _ in range(rows)]
  
  def get_cell(self, row, col):
   if 0 <= row < self.rows and 0 <= col < self.cols:
     return self.cells[row][col]
   else:
     return None
  
  def report_sugar(self): # not a standard accessor method - it's administrative
    # report Sugar Surface
    for r in range(self.rows):
      for c in range(self.cols):
        #print( "(" + str(r) + "," + str(c) + "): " + str(b.get_cell(r,c).sugar))
        print(f"({str(r)},{str(c)}): {str(self.get_cell(r,c).sugar)}")

class Miner:
 def __init__(self, surface, row, col):
   self.surface = surface
   self.row = row
   self.col = col
   self.sugar = 0
   self.health = 1 # health is a measure of how much sugar we have left, reach 0 and we die
   
 def getLocation(self):
    return (self.row, self.col) 

 def move(self, direction): # up, down, left, right, up_left, and the rest...
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
       
 def scan(self,sugarSurface):
   result = {}
   # N
   # get sugar allotment from self.row -1, self.col
   result["N"] = sugarSurface.get_cell(self.row - 1, self.col).sugar
   # S
   # get sugar from self.row+1, self.col
   result["S"] = sugarSurface.get_cell(self.row + 1, self.col).sugar
   # W
   # get sugar from self.row, self.col-1
   result["W"] = sugarSurface.get_cell(self.row, self.col - 1).sugar
   # E
   # get sugar from self.row, self.col+1
   result["E"] = sugarSurface.get_cell(self.row, self.col + 1).sugar
   # NE
   # get sugar from self.row-1, self.col+1
   result["NE"] = sugarSurface.get_cell(self.row - 1, self.col + 1).sugar
   # NW
   # get sugar from self.row-1, self.col-1
   result["NW"] = sugarSurface.get_cell(self.row - 1, self.col - 1).sugar
   # SE
   # get sugar from self.row+1, self.col+1
   result["SE"] = sugarSurface.get_cell(self.row + 1, self.col + 1).sugar
   # SW
   # get sugar from self.row+1, self.col-1
   result["SW"] = sugarSurface.get_cell(self.row + 1, self.col - 1).sugar
   
   return result
 
class ScenarioOne:
  def __init__(self):

    # define constants for Game 0
    R = 16
    C = 16
    sugarLimit = 100
    movePrompt = 30 # if a neighbor has more than this amount of sugar more than the current cell, move there
    
    # populate surface
    self.surface = SugarSurface(R, C, sugarLimit)
     
    # populate players' positions
    self.players = []
    startpoints = [
     (6,4), (7,4), (8,4), (3,6), (10,7), (11,11), (15,11), (1,11), 
     (5,11), (9,11), (5,13), (7,13), (2,14), (12,14), (13,14), (14,14), (15,14)
    ]
    
    for i in range(len(startpoints)):
     self.players.append(Miner(self.surface, startpoints[i][0], startpoints[i][1]))

  # dump Miners info
  def showMiners(self):
    for m in range(len(self.players)):
      print(f"Miner {m+1} at {self.players[m].getLocation()} - Sugar: {self.surface.get_cell(self.players[m].row, self.players[m].col).sugar}")

  def pulse(self):
    # for each miner, mine or move
    for m in range(len(self.players)):
      # scan neighborhood
      neighborhood = self.players[m].scan(self.surface)
      # find the neighbor with the most sugar
      max_neighbor = max(neighborhood, key=neighborhood.get)
      # if the neighbor has more sugar than the current cell, move there
      if neighborhood[max_neighbor] > self.surface.get_cell(self.players[m].row, self.players[m].col)
        # move to the richer neighbor
        self.players[m].move(max_neighbor)
  
##############################################################
#main()

s = ScenarioOne()
#s.surface.report_sugar()
#s.showMiners()
# print (s.players[0].scan(s.surface))

# distrotable()

