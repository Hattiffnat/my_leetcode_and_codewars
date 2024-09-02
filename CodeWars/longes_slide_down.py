#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy
import numpy as np


# In[10]:


def add_indexes(x, addable):
    # print(x)
    # print(addable)
    for i in range(len(x)):
        x[i] += addable[i]


# In[3]:


def cycle_1(pyramid, indexes):
    slides = []
    get_slides(indexes, slides)
    
    if slides:
        return [[pyramid[i][s[i]] for i in range(len(s))] for s in slides]
    else:
        return None


# In[4]:


def get_slides(indexes, slides, n=0, s=[0]):
    for j in indexes[n+1]:
        s = s[:n+1]
        if j == s[-1] or j == s[-1]+1:
            s.append(j)

            if len(s) == len(indexes):
                slides.append(s.copy())

            elif n+1 < len(indexes)-1:
                get_slides(indexes, slides, n+1, s.copy())


# In[11]:


def get_new_indexes(pile):
    
    new_indexes = [list() for i in range(len(pile))]
    # Cycle by layers of pile
    for l_index in range(len(pile)):
        
        mx = None        # Max value in layer
        maxes = []       # Indexes of max value (there may be several)
        
        # Cycle by items in layer
        for i_index in range(len(pile[l_index])):
            
            num = pile[l_index][i_index] # Value of item
            
            # If value of item not None, and max value is None or less than Item
            if num is not None:
                if mx is None or mx < num:
                    mx = num
                    maxes = [i_index]
                elif mx == num:
                    maxes.append(i_index)
        
        for i in maxes:
            pile[l_index][i] = None
        new_indexes[l_index] += maxes
    
        
    return new_indexes


# In[14]:


def longest_slide_down(pyramid):
    pile = copy.deepcopy(pyramid)
    indexes = [list() for i in range(len(pile))]
    
    chains = None
    while not chains:
        new_indexes = get_new_indexes(pile)
        
        if new_indexes:
            add_indexes(indexes, new_indexes)
            chains = cycle_1(pyramid, indexes)
    
    for i in chains: print(np.array(i), sum(i))
    return max([sum(i) for i in chains])
    


# In[15]:

if __name__ == '__main__':
    pyra = [
                                    [75],
                                  [95, 64],
                                [17, 47, 82],
                              [18, 35, 87, 10],
                            [20,  4, 82, 47, 65],
                          [19,  1, 23, 75,  3, 34],
                        [88,  2, 77, 73,  7, 63, 67],
                      [99, 65,  4, 28,  6, 16, 70, 92],
                    [41, 41, 26, 56, 83, 40, 80, 70, 33],
                  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
              [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
          [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ]



    res = longest_slide_down(pyra)
    print(res)
    print(res == 1074)