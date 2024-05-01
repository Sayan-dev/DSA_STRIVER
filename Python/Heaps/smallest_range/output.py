from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()

#     output.append(solution_instance.maximumPath(N, Matrix))

# new_controller.writeOutput(output)

t=int(data[0])
lineno = 1
for _ in range(t):
    line=data[1].strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in data[lineno+1+i].strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1]) 
    lineno += k+1 

