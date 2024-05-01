from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()


inputarr = [int(x) for x in data[0].split(",")]


output = solution_instance.stockBuyAndSell(inputarr)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")

