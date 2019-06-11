# Stochastic Programming
##  Problem Statement: Formulate a Stochastic Program that would determine the seat assignment, while maximizing the profit
Northam Airlines is trying to decide how to partition a new plane for its Chicago-Detroit route. The plane can seat 200 economy class passengers. A section can be partitioned off for first class seats but each of these seats takes the space of 2 economy class seats. A business class section can also be included, but each of these seats takes as much space as 1.5 economy class seats. 

The profit on a first class ticket is, however, three times the profit of an economy class ticket. A business class ticket has a profit of two times an economy ticket’s profit. Once the airplane is partitioned into these seating classes, it cannot be changed. Northam knows, however, that the plane will not always be full in each section. They have decided that three scenarios will occur with about the same frequency: 
* weekday morning and evening traffic
* weekend traffic
* weekday midday traffic

Under Scenario 1, they think they can sell as many as 20 first class tickets, 50 business class tickets, 200 economy tickets. Under scenario 2, these figures are 10, 25, 175. Under scenario 3, they are 5, 10, and 150.
I am assuming that they cannot sell more tickets than seats in each of the sections.(In reality , the company may allow overbooking, then it faces the problem of passengers with reservations who do not appear for the flight (no-shows). The problem of determining how many passengers to accept is part of the field called yield management. 
Our goal is to formulate a Stochastic Program that would determine the seat assignment, while maximizing the profit.

## Seat allocation and maximum profit:
### Solved in Python Gurobi
* [Seat allocation in scenario 1](https://github.com/shrilekha17/Optimization/blob/master/Scenario_1_Final.py)
* [Seat allocation in scenario 2](https://github.com/shrilekha17/Optimization/blob/master/Scenario_2_Final.py)
* [Seat allocation in scenario 3](https://github.com/shrilekha17/Optimization/blob/master/Scenario_3_Final.py)
* [Including all three scenarios](https://github.com/shrilekha17/Optimization/blob/master/Stochastic_Model_Final.py)

## Discussion 
It will be equivalent to a simple linear program where we need to seat allocation while maximizing the profit. But, under some uncertainties, it won't remain the same problem. In my solution, I have considered that all three events are occurring with 1/3 probability. Considering uncertainties, Considering uncertainties, 
the maximum profit is 208.33 units. The seat allocated in economy class is 150, business class is 20, and first class is 10. 



