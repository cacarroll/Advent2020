# 99 = halt
# OpCode 1 = adds position 1 and 2 and stores result in position 3
# OpCode 2 = multiplies position 1 and 2 and stores result in position 3

from typing import List


Program = List[int]

def run(program: Program) -> None:
    pos = 0

    while program[pos] != 99:
        opcode, loc1, loc2 = program[pos], program[pos +1], program[pos + 2]
        if program[pos] == 1:
            print("We are in a 1 and adding")
            pos += 4
        elif program[pos] == 2:
            print("We are multiplying")
            pos += 4
        else:
            raise RuntimeError(f"Invalid opcode: {program[pos]}")

prog0 = [1,9,10,3,2,3,11,0,99,30,40,50]; run(prog0); assert prog0 == [1,9,10,70,2,3,11,0,99,30,40,50] 
prog1 = [1,0,0,0,99]; run(prog1); assert prog1 == [2,0,0,0,99]
prog2 = [2,3,0,3,99]; run(prog2); assert prog2 == [2,3,0,6,99]
prog3 = [2,4,4,5,99,0]; run(prog3); assert prog3 == [2,4,4,5,99,9801]
prog4 = [1,1,1,4,99,5,6,0,99]; assert prog4 == [30,1,1,4,2,5,6,0,99]

# list1 = [1,9,10,3,2,3,11,0,99,30,40,50]
# list2 = [1,9,10,70,2,3,11,0,99,30,40,50]
# assert function(list1) == list2
# assert function([1, 9,10,3,2,3,11,0,99,30,40,50]) == [1,9,10,70,2,3,11,0,99,30,40,50]

program([1,9,10,3,2,3,11,0,99,30,40,50])