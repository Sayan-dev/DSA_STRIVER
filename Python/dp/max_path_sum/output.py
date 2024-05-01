from solution import Solution
from controller import Controller

new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()



t = int(data[0])
odd = -1 
even = 0
output = []
for i in range(t):

    odd+=2
    even+=2
    N = int(data[odd])
    print(N)
    arr = data[even].split()
    Matrix = [[0]*N for i in range(N)]
    for itr in range(N*N):
        Matrix[(itr//N)][itr%N] = int(arr[itr])

    output.append(solution_instance.maximumPath(N, Matrix))

new_controller.writeOutput(output)


