from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



n = int(data[0])
sum = int(data[1])
coins = [int(x) for x in data[2].split(",")]


output = solution_instance.total_coin_combo(n,sum,coins)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")


