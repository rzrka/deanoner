import io
import fileinput
import os

PATH = '/home/daniil1/learn/deanoner_bd/bd_inst'
tree = os.walk(PATH)
for i in tree:
    content_dir = i
    content_dir = content_dir[1]
    break


first = True
with io.open(f'{PATH}/result.csv', "at", encoding="utf-8") as out, fileinput.input(
    files=[f"{PATH}/{i}/data.csv" for i in content_dir]) as f:
    for line in f:
        out.write(line)