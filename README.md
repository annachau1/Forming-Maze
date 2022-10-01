# Forming-Maze

For this object-oriented Python project, a maze of any dimension will be generated, as long as there is an input file containing cell locations, and respective distances from a wall in the format of E,W,N,S. Using the Python package called Pyamaze, the maze will be able to generate digitally, as well as output the organized input data in an .CSV file. 

Step 1: Understanding the input file

The input file will contain an X amount of lines (dependent on how large the desired maze will be). Within each of these lines, will contain 5 total elements: (y, x) cell location (in double quotation marks), the distance reading from the East direction (meters), distance reading from the West direction (meters), distance reading from the North direction (meters), and distance reading from the South direction (meters). 

If one of the cardinal directions is more than 0.25 meters, that will indicate that that direction's wall is open and that there is no obstacle in that direction. If a wall is open, the distance for the respective direction should turn into a float value 1. If the cardinal direction is less than 0.25 meters, this indicates that there is a wall in that direction. The value of the distance should then turn into a float value 0.

Step 2: Processing the input file 
