from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



n = int(data[0])
W = int(data[1])
v = [int(x) for x in data[2].split(",")]
w = [int(x) for x in data[3].split(",")]


output = solution_instance.zeroOneknapSack(n,W,v,w)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")


