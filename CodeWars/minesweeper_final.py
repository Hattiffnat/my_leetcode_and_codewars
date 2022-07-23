from preloaded import open
import numpy as np


def to_arr(x):
    if isinstance(x, str):
        return np.array([i.split(' ') for i in x.split('\n')], dtype=str)
        
    else:
        raise TypeError(f'x({x}) is {type(x)}, not str')

        
def from_arr(x):
    if isinstance(x, np.ndarray):
        return np.array2string(x).replace('[', '').replace(']', '').replace('\n ', '\n')
    else:
        raise TypeError(f'x({x}) is {type(x)}, not numpy.ndarray')


def cells_near(y, x, shape):
    y_max, x_max = shape
    res = []
    for x_s in range(x-1, x+2):
        for y_s in range(y-1, y+2):
            if x_s >= 0 and y_s >= 0 and x_s < x_max and y_s < y_max and (x != x_s or y != y_s):
                res.append((y_s, x_s))
    return tuple(res)


def bf_checker(gmap, n):
    
    df = to_arr(gmap)
    y_max, x_max = df.shape
    
    # Just check the matrix for errors
    for y in range(y_max):
        for x in range(x_max):
            # Getting coords of all cells near current
            c_n = cells_near(y, x, df.shape)

            if df[y,x] not in ['?', 'x']:
                bombs = int(df[y,x])    # quantity of bombs around
                quests = []                  # list for '?' coords
                find_bombs = 0               # number for bombs already found around

                # Gets amount of 'x' around
                for yn, xn in c_n:
                    if df[yn, xn] == 'x':
                        find_bombs += 1

                # If amount of 'x' around not equal the cell value, retruns errored matrix
                if find_bombs != bombs:
                    return from_arr(df), -1
                
    return from_arr(df), 0
        

def cycle_1(gmap, n):
    df = to_arr(gmap)
    y_max, x_max = df.shape
    bombs_count = 0
    
    old_df = np.array(['?'])
        
    while from_arr(old_df) != from_arr(df):
        
        old_df = df.copy()
        
        # Open clean matrix
        for y in range(y_max):
            for x in range(x_max):
                
                # Getting coords of all cells near current
                c_n = cells_near(y, x, df.shape)
                
                # If cell value greater than 0 and not '?' or 'x'
                if df[y,x] not in ['?', 'x']:
                    
                    bombs = int(df[y,x])    # quantity of bombs around
                    quests = []                  # list for '?' coords
                    find_bombs = 0               # number for bombs already found around

                    # Gets the amount and locations of '?'
                    for yn, xn in c_n:
                        if df[yn, xn] == '?':
                            quests.append((yn,xn))
                        if df[yn, xn] == 'x':
                            find_bombs += 1

                    # if bombs equal quantity of '?', changes all '?' to 'x'
                    if bombs - find_bombs == len(quests):
                        for yn, xn in quests:
                            df[yn,xn] = 'x'
                            bombs_count += 1
                            
                    # if all bombs already found, opens all '?'
                    elif find_bombs == bombs:
                        for yn, xn in quests:
                            df[yn,xn] = str(open(yn, xn))
                            
    
    return from_arr(df), n - bombs_count


def cycle_2(gmap, n):
    df = to_arr(gmap)
    y_max, x_max = df.shape
    quests = []
    for y in range(y_max):
        for x in range(x_max):
            if df[y, x] == '?':
                quests.append((y,x))

    alphabet = 'x?'
    combos = []

    for current in range(len(quests)):
        a = [i for i in alphabet]

        for y in range(current):
            a = [x+i for i in alphabet for x in a]
        
        for i in a:
            if i.count('?') == len(quests) - n and i.count('x') == n:
                combos.append(i)
    solves = []
    for combo in combos:
        bf_df = df.copy()
        n = 0
        for i in range(len(quests)):
            bf_df[quests[i]] = combo[i]
            
        bf_gmap, n = bf_checker(from_arr(bf_df), n)
        if n == 0:
            solves.append(bf_gmap)
        if len(solves) > 1:
            return '?', -1
        
    if len(solves) == 1:
        res, n = cycle_1(solves[0], 0)
        return res, n
        
    else:
        return '?', -1


def solve_mine(gmap, n):
    
    gmap, n = cycle_1(gmap, n)
    
    if gmap.count('?') or n != 0:
        gmap, n = cycle_2(gmap, n)
    
    if gmap.count('?') == 0 and n == 0:
        return gmap
                    
    else:
        return '?'
