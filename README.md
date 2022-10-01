# Generating-Maze

For this object-oriented Python project, a maze of any dimension will be generated, as long as there is an input file containing cell locations, and respective distances from a wall in the format of E,W,N,S. Using a Python package called Pyamaze, the maze will be able to generate digitally, as well as output the newly organized input data in an .CSV file.

To study about how Pyamaze exactly works: https://github.com/MAN1986/pyamaze.git

## Step 1: Understanding the input file

The input file will contain an X amount of lines (dependent on the dimensions of the desired maze). Within each of these lines, will contain 5 total elements: "(y, x)" cell location (in double quotation marks), the distance reading from the East direction (meters), distance reading from the West direction (meters), distance reading from the North direction (meters), and distance reading from the South direction (meters). 

  If one of the cardinal directions is more than 0.25 meters, it will indicate that there is no wall in that cardinal direction. If a wall is open (no wall), the distance for the respective direction should turn into a float value = 1. If the cardinal direction is less than 0.25 meters, this indicates that there is a wall in that direction. The value of the distance should then turn into a float value = 0.

## Step 2: Processing/fixing format of the input file 
As the input data is processed, each individual line from the input file will be a date type, string. In order to access and use the different elements of the string, it must be split into a list of strings. To do so is as follows:

        line = line.replace(",", ", ")
        output = shlex.split(line)
        output = [re.sub(r",$","",w) for w in output]
        
Now that the input data is formatted properly, the elements of the list can now be used. As explained in Step 1, all the cardinal directions must be converted to either a float 1 or 0, which depends on its individual value when compared to 0.25 meters. In order to accomplish this, the elements [1:5] of the list must undergo conditional statements where they will be organized and transformed into float values 1 or 0. As they are being categorized, their new float values can be appended into an empty string to build the float values for that specific input line. 

## Step 3: Creating a dictionary (key = value)
As the input data is being transformed, it is crucial to create a library to have each cell location (key) correlate to its respective float values (value). In the list of strings created, element[0] = cell location, while element[1:5] = E,W,N,S. To create a dictionary that follows this format, it is as follows:

            self.dict[str(element[0]).replace('  ',' ')] = appendedstring[0:-1]
            
## Step 4: Generating CSV file
Now that the decimal E,W,N,S values have been converted to 0 or 1, and that a dictionary has been created containing the official maze outline, a CSV file can now be written into. This CSV file will be read by Pyamaze to generate the digital maze. To format the CSV file correctly, the dictionary, along with a string token, must be put to use. If a string token, containing a (key) cell location (y,x), is found in the dictionary, it will use the dictionary's key and value system to locate and print its paired E,W,N,S values into the CSV file (on the same line). 

## Step 5: Create maze
By utilizing Pyamaze's createMaze function, all the organized input data can be transformed into a digital maze.

## Tips I found useful 
* CSV formatting is crucial 
* Remember that the generated CSV file must be IDENTICAL to the example CSV's provided in the example folders. Utilize string manipulation such as

            .replace('  ',' ')

* Remember that the cell location must be generated as (y,x)
* Create code to be universal and to have the ability to adjust to any maze dimensions
* Enjoy the coding learning process
