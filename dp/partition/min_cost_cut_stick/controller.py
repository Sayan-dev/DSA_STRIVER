import os
import ast



class Controller:
    def is_valid_literal(self,input_string):
        try:
            ast.literal_eval(input_string)
            return True
        except (SyntaxError, ValueError):
            return False
    
    def filePath(self,name) -> str:
        file_name = os.path.join(os.path.dirname(__file__), name)
        return file_name
    def readInput(self):

        f = open(self.filePath("input.txt"), "r")
        data = f.read().splitlines()

        return data
    def readInputAst(self):
        data = []
        with open(self.filePath("input.txt"), 'r') as file:
            # Read the content and parse it into a Python object
            content = file.read().splitlines()
            print(f"{content}")
            for i in content:
                if self.is_valid_literal(i):
                    data.append(ast.literal_eval(i))
                else:
                    data.append(i)
                

        return data
    
    def writeOutput(self, data):
        out = open(self.filePath("output.txt"), "w")
        out.write(data)
        return
