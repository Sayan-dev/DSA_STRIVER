
import os

if __name__ == "__main__":
    def filePath(name) -> str:
        file_name = os.path.join(os.path.dirname(__file__), name)
        return file_name
    f = open(filePath("input.txt"), "r")

    output  = "Data"


    fw = open(filePath("output.txt"), "w")
    fw.write(output)