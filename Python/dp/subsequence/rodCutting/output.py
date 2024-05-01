from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



sum = int(data[0])
costs = [int(x) for x in data[1].split(",")]
n = len(costs)


output = solution_instance.rod_cutting(n,costs,sum)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")


