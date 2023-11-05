import os

from decorators import IODecorator


class Controller:
    
    def filePath(self,name) -> str:
        file_name = os.path.join(os.path.dirname(__file__), name)
        return file_name
    def readInput(self):

        f = open(self.filePath("input.txt"), "r")
        data = f.read().splitlines()

        return data
    

    def writeOutput(self, data):
        out = open(self.filePath("output.txt"), "w")
        out.write(data)
        return
    

