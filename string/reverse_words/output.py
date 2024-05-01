from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



s = f'{data[0]}'


output = solution_instance.find_pairs(s)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")


