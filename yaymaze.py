from pyamaze import maze,COLOR, agent # importing from pyamaze
import shlex 
import re


class YayMaze:
    def __init__(self, ifile, origPos=(1,1),size=4): # taking arguments from main
        self.ifile = ifile
        self.csvfile = 'mazerunning.csv' # declaring where csv file should be loading to
        self.origPos = origPos
        self.size = size # allowing the dimensions of maze to be adjusted without issues
        self.maze = maze(rows=self.size, cols=self.size)
        self.dict = {} # declaring empty dictionary
        self.read_and_process(ifile)
        self.fix_format(ifile)
        self.generate_csv()
        
# function designed to read input file, categorize decimal values into floats, and build dictionary
    def read_and_process(self, ifile):
        file1 = open(self.ifile, 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines: # iterating through each line of input file
            count += 1
            output = self.fix_format(line.strip()) # calling fix_format
            wall = '' # declaring empty string to build values of the dictionary into
            for indx in range(1,5): # for loop to iterate through elements[1:5] to assign 0 or 1 for each line of input
                if float(output[indx]) > 0.25:
                    wall = wall + '1,' # 1 = no wall present, adding 1s to string wall
                else:
                    wall = wall + '0,' # 0 = wall present, adding 0s to string wall
    
            self.dict[str(output[0]).replace('  ',' ')] = wall[0:-1] # building dictionary


# function designed to split each line of input into list of string elements
    def fix_format(self,line): 
        line = line.replace(",", ", ")
        output = shlex.split(line)
        output = [re.sub(r",$","",w) for w in output]
        return output

# function designed to write into CSV file, declaring string token to navigate through dictionary,
# locating dictionary's key and value pairs, formatting these pairs into CSV file properly
    def generate_csv(self):
        with open(self.csvfile,'w') as csv_file:
            csv_file.write("  cell  ,E,W,N,S") # crucial heading to allow Pyamaze to work properly
            csv_file.write("\n")
            for i in range (1,self.size+1):
                for j in range (1,self.size+1):
                    strtoken = '({}, {})'.format(j,i) # declaration of string token (y,x) for dictionary
                    if strtoken in self.dict:
                        csv_file.write('"{}",{}'.format(strtoken,self.dict[strtoken]))
                        csv_file.write("\n")
                    else:
                        csv_file.write('"{}",{}'.format(strtoken,"token not found in dictionary"))
                        csv_file.write("\n")
                   
# function designed to build maze, imported from Pyamaze
    def createMaze(self):
        self.maze.CreateMaze(x=self.origPos[0],y=self.origPos[1],loopPercent=100, loadMaze=self.csvfile)
        self.maze.run()

# main function
if __name__=="__main__":
    a = YayMaze('inputfile1.txt', (1,1), size = 4) # calling class YayMaze with proper arguments
    a.createMaze() # calling createMaze 
