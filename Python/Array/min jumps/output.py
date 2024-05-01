from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()

n = int(data[0])

inputarr = [int(x) for x in data[1].split(" ")]


output = solution_instance.minJumps(inputarr, n)


new_controller.writeOutput(f"{output} \n\n\n\nThanks")

