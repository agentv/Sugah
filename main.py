import random
import sandbox.randoms as rand  # used for the "booster table"

# TODO
#
# complete the visualization of the sugar surface - print and color code the cells
# Add the initial positions of the Miners
# Create a pulse() routine for each Miner - this will be in the main loop
# create a pulse() routine for the surface - this happens after the main loop


class SugarCell:

  def __init__(self, sugar):
    self.sugar = sugar
    self.multiplier = 1

  def take_sugar(self, amount):
    self.sugar -= amount
    if self.sugar < 0:
      self.sugar = 0

  def add_sugar(self, amount):
    self.sugar += amount


class SugarSurface:

  def __init__(self, rows, cols, limit):
    self.rows = rows
    self.cols = cols

    # we populate the cells here by simply giving a random number
    # from 1 to limit
    # the real plan is to use the same distribution of value
    # used in Scrabble
    # ie. 1:49, 2:15, 3:11, 4:13, 5:1
    self.cells = [[SugarCell(random.randint(1, limit)) for _ in range(cols)]
                  for _ in range(rows)]

  def get_cell(self, row, col):
    if 0 <= row < self.rows and 0 <= col < self.cols:
      return self.cells[row][col]
    else:
      return None

  def export_sugar(self):
    # export a json structure that can be used to recreate the
    # surface. Each element should be in a JSON object that contains
    # the row, col, and sugar value
    result = []
    for r in range(self.rows):
      for c in range(self.cols):
        result.append({"row": r, "col": c, "sugar": self.cells[r][c].sugar})
    return result

  def report_sugar(
      self):  # not a standard accessor method - it's administrative
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
    self.health = 1  # health is a measure of how much sugar we have left, reach 0 and we die

  def getLocation(self):
    return (self.row, self.col)

  def move(self, direction):  # up, down, left, right, up_left, and the rest...
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

  def mine(self, qty):
    cell = self.surface.get_cell(self.row, self.col)
    if cell:
      cell.take_sugar(qty)

  def scan(self, sugarSurface):
    result = {}
    # get sugar allotment from self.row -1, self.col
    result["up"] = sugarSurface.get_cell(self.row - 1, self.col).sugar
    # get sugar from self.row+1, self.col
    result["down"] = sugarSurface.get_cell(self.row + 1, self.col).sugar
    # get sugar from self.row, self.col-1
    result["left"] = sugarSurface.get_cell(self.row, self.col - 1).sugar
    # get sugar from self.row, self.col+1
    result["right"] = sugarSurface.get_cell(self.row, self.col + 1).sugar
    # get sugar from self.row-1, self.col+1
    result["up_right"] = sugarSurface.get_cell(self.row - 1,
                                               self.col + 1).sugar
    # get sugar from self.row-1, self.col-1
    result["up_left"] = sugarSurface.get_cell(self.row - 1, self.col - 1).sugar
    # get sugar from self.row+1, self.col+1
    result["down_right"] = sugarSurface.get_cell(self.row + 1,
                                                 self.col + 1).sugar
    # get sugar from self.row+1, self.col-1
    result["down_left"] = sugarSurface.get_cell(self.row + 1,
                                                self.col - 1).sugar

    return result


class ScenarioOne:

  def __init__(self):

    # define constants for Game 0
    R = 16
    C = 16
    sugarLimit = 16
    movePrompt = 4  # if a neighbor has more than this amount of sugar more than the current cell, move there

    # populate surface
    self.surface = SugarSurface(R, C, sugarLimit)

    # populate players' positions
    self.players = []
    startpoints = [(6, 4), (7, 4), (8, 4), (3, 6), (10, 7), (11, 11), (15, 11),
                   (1, 11), (5, 11), (9, 11), (5, 13), (7, 13), (2, 14),
                   (12, 14), (13, 14), (14, 14), (15, 14)]

    for i in range(len(startpoints)):
      self.players.append(
          Miner(self.surface, startpoints[i][0], startpoints[i][1]))

  # dump Miners info
  def showMiners(self):
    for m in range(len(self.players)):
      print(
          f"Miner {m+1} at {self.players[m].getLocation()} - Sugar: {self.surface.get_cell(self.players[m].row, self.players[m].col).sugar}"
      )

  # untested and dysfunctional
  def pulse(self):
    # for each miner, mine or move
    for m in range(len(self.players)):
      # scan neighborhood
      neighborhood = self.players[m].scan(self.surface)
      # find the neighbor with the most sugar
      max_neighbor = max(neighborhood, key=neighborhood.get)
      # if the neighbor has more sugar than the current cell, move there
      if neighborhood[max_neighbor] > (self.surface.get_cell + movePrompt)(
          self.players[m].row, self.players[m].col):
        # move to the richer neighbor - use cardinal directions (ie: up, down, left ...)
        self.players[m].move(max_neighbor)


##############################################################
#main()

s = ScenarioOne()
# print (s.surface.export_sugar())
# s.showMiners()
print(s.players[0].scan(s.surface))

# rand.distrotable()
