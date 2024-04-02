##############################################################
# experiment to create a "booster table" with a known distribution
# next, move this to the constructor for SugarSurface

def distrotable():
  # Create an array with the desired distribution
  point_array = [1] * 49 + [2] * 15 + [3] * 11 + [4] * 13 + [5] * 1

  # Dump the table
  for m in range(len(point_array)):
    print(f"({str(m)},{str(point_array[m])})")