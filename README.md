A little project that explores replit, python
based (loosely) on Sugarscape, this is a simple
cellular automata amusement

start with a 16x16 grid, place about 16 actors
in the grid and ramdomly populate it with "sugar"

each pulse, the actors either mine sugar in their
current location or move to the richest neighboring
cell. 

each actor:
  scan surroundings
  move if a richer neighbor exists
  otherwise mine locally
