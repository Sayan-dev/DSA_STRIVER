from solution import Solution,Sack
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



n = int(data[0])
w = int(data[1])
sacks=[]
values = [int(x) for x in data[2].split(",")]
weights = [int(x) for x in data[3].split(",")]
for i in range(n):
    sacks.append(Sack(values[i],weights[i],values[i]/weights[i]))


output = solution_instance.fractional_knapsack(n,w,sacks)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")


