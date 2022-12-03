#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:52:26 2022

@author: Andrew
"""

# A = [0, 0, 0, 1, 1]
# B = [1, 0, 1, 1, 1]

# SumSlots = [0] * 5

# print(SumSlots)

# for i in range(len(A)):
#     SumSlots[i] = int(A[i]) + int(B[i])
    
# print(SumSlots)



# dictionary method

# A = [0, 0, 0, 1, 1]
# B = [1, 0, 1, 1, 1]

# AB_dict = {'A': A, 'B': B}

# open_slots = {'A': [1]*5, 'B': [1]*5}

# for day,slots in AB_dict.items():
#     print(day)
#     for i in range(len(slots)):
#         if AB_dict[day][i] == 1:
#             open_slots[day][i] = 0

# print(open_slots)



# dictionary method with multiple people

# first person
A1 = [0, 0, 0, 1, 1]
A2 = [1, 0, 1, 0, 1]

# second person
B1 = [1, 0, 1, 1, 0]
B2 = [1, 1, 1, 0, 1]

A_dict = {'Mon': A1, 'Tue': A2}
B_dict = {'Mon': B1, 'Tue': B2}

listPeople = [A_dict, B_dict]

open_slots = {'Mon': [1]*5, 'Tue': [1]*5}

for i in range(len(listPeople)):
    for day,slots in listPeople[i].items():
        for j in range(len(slots)):
            if listPeople[i][day][j] == 1:
                open_slots[day][j] = 0

print(open_slots)