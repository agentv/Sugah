A little project that explores replit, python
based (loosely) on Sugarscape, this is a simple
cellular automata amusement

start with a 16x16 grid, place about 16 miners
in the grid and ramdomly populate it with "sugar"

each pulse, the miners either mine sugar in their
current location or move to the richest neighboring
cell. 

each miner:
  scan surroundings
  move if a richer neighbor exists
  when moving, a miner will exhaust energy, but not succeed if the cell is occupied
  otherwise mine locally

when an miner runs out of sugar, they are done
if an miner tries to move to a populated spot, it waits for a turn
last miner standing wins (just by being the most interesting)

(TODO) - current state of project in replit

 - finish work for drawing the sugarscape and coloring the cells
 - review and finish the move pulse
 - create the cell update pulse
 - create the cell update that will place a miner in that cell (adjust move pulse to handle this)
