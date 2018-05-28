# EECS 221 ADV APP Algorithm

# Project Part 5

# Author: YiMing Chen
# StudentID: 28328800
##################################################


This program can be executed on Python 2.7.14 and has dependencies as below

Dependency:heapq,sys,time,pdb,os,itertools,pickle,matplotlib


To run the program in batch processing mode, simply type "python Main.py warehouse-grid.csv item-dimensions-tabbed.txt warehouse-orders-v01.csv"
Then the programe will automatically generate the optimized.csv file which contain all the optimal solution for all the orders


Furthermore, the program can run in user specified mode, without specify the second argument for order list such as "python Main.py warehouse-grid.csv" 
Then you should get the response as below, and the program will ask user for the worker starting point, ending point and order list to process. 
Once all the information is given to the program, it will compute the solution for user request and generate path tour plot for user to evaluate the result

Below are sample output with worker starting from (2,2) ending at (8,8) with order list ['219130', '365285', '364695']

Be noticed that the visual tour plot will also be displayed once this script is run at local machine

##################################################
# Read warehouse
# Reading warehouse-grid.csv File..

# Warehouse dimension
# min x : 0
# max x : 18
# min y : 0
# max y : 10

# Initializing warehouse graph...
# Update items into warehouse graph

# Set up start point
# Setting up the position
# Input X point (integer):2
# Input Y point (integer):2

# Set up end point
# Setting up the position
# Input X point (integer):8
# Input Y point (integer):8

# completing path matrix

# Planning from user specified list
# Manually input the itemID
# Add the itemID or type end to quit:219130
# Added 219130 to the list
# Order lists is ['219130']
# 1 items in the list
# Add the itemID or type end to quit:365285
# Added 365285 to the list
# Order lists is ['219130', '365285']
# 2 items in the list
# Add the itemID or type end to quit:364695
# Added 364695 to the list
# Order lists is ['219130', '365285', '364695']
# 3 items in the list
# Add the itemID or type end to quit:end
# Order lists is ['219130', '365285', '364695']

# Items,219130,365285,364695
# Distinct places,3*8*pick,7*5*pick,4*2*pick
# Start Location,2*2
# End Location,8*8
# Original path,2*2,2*3,2*4,3*4,3*5,3*6,3*7,3*8,3*8*pick,3*8,3*7,4*7,4*6,5*6,6*6,7*6,7*5*pick,7*5,6*5,5*5,5*4,5*3,4*3,4*2*pick,4*3,5*3,6*3,7*3,8*3,8*4,8*5,8*6,8*7,8*8
# Original cost,300
# Shortest Path,2*2,3*2,4*2,4*2*pick,4*3,3*3,3*4,3*5,3*6,3*7,3*8,3*8*pick,3*8,3*7,4*7,4*6,5*6,6*6,7*6,7*5*pick,7*6,7*7,7*8,8*8
# Shortest Path Cost,200
# Computation Time,0.000296831130981

