import os
import pandas as pd
import csv
import numpy as np
import numpy.random
from gurobipy import*


os.chdir('/Users/shrilekha/Documents/Fall 2018/Operations Research')

# Scenario 1 
# Initilize the ratio of profit
profit=[1,2,3]

space = [1,1.5,2]

Seating = [150,10,5]

# Initiate the model
m = Model("Case_1")
m.update()

# Define Decision Variables
x={}
for i in range(3):
 x[i] = m.addVar(vtype = GRB.CONTINUOUS, name = "y%d" %i)
 
s={}
for i in range(3):
 s[i] = m.addVar(vtype = GRB.CONTINUOUS, name = "s%d" %i) 
 
 
 
m.update()
 
# Objective Function 
Total_Profit = quicksum(profit[i]*(x[i]-s[i]) for i in range(3))
m.setObjective(Total_Profit, GRB.MAXIMIZE)
 
# Constraint Addition
m.addConstr(quicksum(space[i]*x[i] for i in range(3))<= 200)
for i in range(3):
    m.addConstr((x[i]-s[i]) <= Seating[i])
    m.addConstr(x[i]>=0)
    m.addConstr(s[i]>=0)
    
    

m.update()

m.optimize()
 
print("Total_Profit = %g" %m.objVal)

for v in m.getVars():
    if v.x > 0:
        print('%s = %g' %(v.varName, (v.x)))
        
)
# Total_Profit = 185
# y0 = 150
# y1 = 10
# y2 = 5
 
 
m.write("Northam_3.lp")  







