"""Kata: Esolang: Ticker.

#1 Best Practices Solution by anter69
def interpreter(tape):
    memory, ptr, output = {0: 0}, 0, ""

    for command in tape:
        if   command == ">":  ptr += 1
        elif command == "<":  ptr -= 1
        elif command == "!":  memory[len(memory)] = 0
        elif command == "*":  output += chr(memory.get(ptr, 0) % 256)
        elif ptr in memory:
            if   command == "+":  memory[ptr] += 1
            elif command == "-":  memory[ptr] -= 1
            elif command == "/":  memory[ptr] = 0

    return output
"""


def interpreter(tape):
    """Interpret a tape written in the esoteric language Ticker.

    tape: str, Character commands to be executed.
               All non-command characters are ignored.
    returns: str, ASCII characters that were printed to the output tape

    Ticker has the following commands:
        >: increment the selector by 1
        <: decrement the selector by 1
        *: add the ascii value of selected cell to the output tape
        +: increment selected cell data by 1. If 256, then it is 0
        -: increment selected cell data by -1. If less than 0, then 255
        /: set selected cell data to 0
        !: add new data cell to the end of the array

    The selector starts at 0 and memory is one cell with a value of 0.
    If selector goes out of bounds, that cell is assumed to be 0 but
    it is not added to the memory. If a + or - is made, the value of
    the assumed cell is not changed. It will always stay 0 unless it
    is added to the memory.
    """
    p, mem, out = 0, [0], ''
    for c in tape:
        if c == '>':
            p += 1
        elif c == '<':
            p -= 1
        elif c == '!':
            mem.append(0)
        try:
            if c == '*':
                out += chr(mem[p])
            if c == '+':
                mem[p] = (mem[p] + 1) % 256
            if c == '-':
                mem[p] = (mem[p] - 1) % 256
            if c == '/':
                mem[p] = 0
        except IndexError:
            if c == '*':
                out += chr(0)
    return out
