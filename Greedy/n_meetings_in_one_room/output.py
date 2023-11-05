from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()

n =int(data[0])

start = [int(x) for x in data[1].split(",")]

end = [int(x) for x in data[2].split(",")]
output = solution_instance.n_meetings(n,start,end)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")

