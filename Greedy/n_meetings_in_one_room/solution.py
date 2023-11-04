import os
def filePath(name) -> str:
    file_name = os.path.join(os.path.dirname(__file__), name)
    return file_name
f = open(filePath("input.txt"), "r")
out = open(filePath("output.txt"), "w")
data = f.read().splitlines()

n = data[0]

start = [int(x) for x in data[1].split(",")]

end = [int(x) for x in data[2].split(",")]


out.write(f"{n} \n{start} \n{end}")
