# NumPY and random modules are used for inside of minefield.

import numpy as np 
import random

# Defining the game field.
def Field():
    area = np.zeros((10, 10), tuple)

    m = 0  # the m means amount of mines at the beginning.

    # Creating the fields on the field randomly. # That loop will be repeated until amount of mines is 10.
    while (m < 10):  
        satir = random.randint(0, 9)
        sutun = random.randint(0, 9)
        if (area[satir, sutun] == 0):  
            area[satir, sutun] = "X"  
            m += 1     
    
    
    str=0 # The variable of row when scaning the field: str

# The while loops will scan to game field.
    while(10>str>-1):
        stn=9 # The variable of col when scaning the field: stn

        while(10>stn>-1):
            
            # Left - Top
            if(area[str, stn] != 'X' and str - 1 > -1 and stn - 1 > -1 and area[str - 1, stn - 1] == 'X'):
                area[str, stn] += 1

            # Left - Mid
            elif(area[str, stn] != 'X' and str - 1 > -1 and area[str - 1, stn] == 'X'):
                area[str, stn] += 1

            # Left - Bottom
            elif (area[str, stn] != 'X' and str - 1 > -1 and 10 >stn + 1 and area[str - 1, stn + 1] == 'X'):
                area[str, stn] += 1

            # Mid - Top
            elif (area[str, stn] != 'X' and stn - 1 > -1 and area[str, stn - 1] == 'X'):
                area[str, stn] += 1

            # Bottom - Mid
            elif (area[str, stn] != 'X' and 10 > stn + 1 and area[str, stn + 1] == 'X'):
                area[str, stn] += 1

            # Right - Top
            elif (area[str, stn] != 'X' and 10 > str + 1 and stn - 1 > -1 and area[str + 1, stn - 1] == 'X'):
                area[str, stn] += 1

            # Right - Mid
            elif (area[str, stn] != 'X' and 10 > str + 1 and area[str + 1, stn] == 'X'):
                area[str, stn] += 1

            # Right - Bottom
            elif (area[str, stn] != 'X' and 10 > str + 1 and 10 > stn + 1 and area[str + 1, stn + 1] == 'X'):
                area[str, stn] += 1

            # the column variable "stn" is increased 1 for new column.
            stn = stn - 1  
        # the row variable "str" is increased 1 for new row.
        str = str + 1 
    return area

# The function definition of out-of-mine boxes. The player may click to non-mine buttons up to 90 times.
def Empty():
    # the amount of non-mine areas.
    empty = 90
    return empty

# The function definition of mine boxes. The player starts the game with a quota of 5 mine clicks.
def Mine():
    # The amount of mine areas.
    mine = 5
    return mine