# -*- coding: utf-8 -*-

#Northam Airline Problem 

import os
import pandas as pd
import csv
import numpy as np
import numpy.random
from gurobipy import*

# Initilizaing Profit in Economy, Business and 1st Class Scenarios
profit = [1,2,3] 

# Seat Allotment in all three scenarios  
Seating =   [[200,175,150],
             [50,25,10],
             [20,10,5]]

# Space allotment for Economy, Business and 1st Class scenarios
Space = [1, 1.5, 2]

#initiate the model 
m=Model('Northam_Airlines')
m.update()

#Define decision variables

x={}
for i in range(3):
    x[i]=m.addVar(vtype = GRB.CONTINUOUS, name = "x%d" %i)


s={}
for i in range(3):   #use only first two elements of the Products
   for j in range(3):
        s[i,j]=m.addVar(vtype = GRB.CONTINUOUS, name = "s%d_%d" %(i,j))
    
m.update()

# Objective Function
Total_Profit = quicksum((x[i]-s[i,j])*profit[i] for i in range(3) for j in range(3))

Total_Profit = Total_Profit/3

m.setObjective(Total_Profit,GRB.MAXIMIZE)


# Constraints Addition

# First Stage Constriants 
m.addConstr(quicksum(x[i]*Space[i] for i in range(3))<=200)
for i in range(3):
    m.addConstr(x[i]>=0)

# Second stage constraints
for j in range(3):
    for i in range(3):
        m.addConstr(x[i] - s[i,j] <= Seating[i][j])
        
for j in range(3):
    for i in range(3):
        m.addConstr(s[i,j]>=0)

for j in range(3):
    for i in range(3):
        m.addConstr(x[i]>= s[i,j])
m.update()
                        
m.optimize()  
   # m.ComputeIIS();


# Printing Optimized Total Profit
print('Total_Profit = %g' % m.objVal)


# Printing the values of decision variables
for v in m.getVars():
    if v.x >0:
        print('%s = %g' %(v.varName, v.x)) 

# Total_Profit = 208.333
# x0 = 150
# x1 = 20
# x2 = 10
# s1_2 = 10
# s2_2 = 5

