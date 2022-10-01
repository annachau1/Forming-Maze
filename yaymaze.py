from pyamaze import maze,COLOR, agent
import shlex
import re


class YayMaze:
    def __init__(self, ifile, origPos=(1,1),size=4):
        self.ifile = ifile
        self.csvfile = 'mazerunning.csv'
        self.origPos = origPos
        self.size = size
        self.maze = maze(rows=self.size, cols=self.size)
        self.dict = {}
        self.read_and_process(ifile)
        self.fix_format(ifile)
        self.generate_csv()
        

    def read_and_process(self, ifile):
        file1 = open(self.ifile, 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            count += 1
            output = self.fix_format(line.strip())
            wall = ''
            for indx in range(1,5):
                if float(output[indx]) > 0.25:
                    wall = wall + '1,'
                else:
                    wall = wall + '0,'
            self.dict[str(output[0]).replace('  ',' ')] = wall[0:-1]

   
    def fix_format(self,line):
        line = line.replace(",", ", ")
        output = shlex.split(line)
        #print (output)
        output = [re.sub(r",$","",w) for w in output]
        return output


    def generate_csv(self):
        with open(self.csvfile,'w') as csv_file:
            csv_file.write("  cell  ,E,W,N,S")
            csv_file.write("\n")
            for i in range (1,self.size+1):
                for j in range (1,self.size+1):
                    strtoken = '({}, {})'.format(j,i)  
                    if strtoken in self.dict:
                        csv_file.write('"{}",{}'.format(strtoken,self.dict[strtoken]))
                        csv_file.write("\n")
                    else:
                        csv_file.write('"{}",{}'.format(strtoken,"0,0,0,0"))
                        csv_file.write("\n")
                   

    def createMaze(self):
        self.maze.CreateMaze(x=self.origPos[0],y=self.origPos[1],loopPercent=100, loadMaze=self.csvfile)
        self.maze.run()


if __name__=="__main__":
    a = YayMaze('inputfile.txt', (1,1), size = 4)
    a.createMaze()
