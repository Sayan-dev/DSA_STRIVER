from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()

S =int(data[0])
N =int(data[1])
M =int(data[2])



output = solution_instance.survive_island(S,N,M)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")

