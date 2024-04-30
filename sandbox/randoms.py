##############################################################
# experiment to create a "booster table" with a known distribution
# the idea is to add sugar to cells using a formula that favors smaller number
# but allows for higher values to occasionally occur

# next, move this to the constructor for SugarSurface


def distrotable():
  # Create an array with the desired distribution
  point_array = [1] * 18 + [2] * 25 + [3] * 21 + [4] * 18 + [5] * 7

  # Dump the table
  for m in range(len(point_array)):
    print(f"({str(m)},{str(point_array[m])})")
