from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



caps = [int(x) for x in data[0].split(",")]
n = len(caps)


output = solution_instance.max_prod_subarray(n,caps)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")


