from typing import List

def read_integers() -> List[int]:
    numbers = []
    line=input()
    strings=line.split(",")

    for x in strings:
      numbers.append(int(x))
    return numbers

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
