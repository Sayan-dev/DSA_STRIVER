from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()

n =int(data[0])
m =int(data[1])
a = [int(x) for x in data[2].split(",")]

output = solution_instance.chocolate_distribution(n,m,a)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")

