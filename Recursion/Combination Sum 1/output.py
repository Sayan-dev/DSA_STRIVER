from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()


inputarr = [int(x) for x in data[0].split(",")]
target = int(data[1])


output = solution_instance.combisum1(inputarr, target)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")

