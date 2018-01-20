"""Kata: Whitespace Interpreter."""


# to help with debugging
def unbleach(n):
    """Replace whitespace characters with visible characters."""
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')


# solution
def whitespace(code, inp=''):
    """Evaluate the given code written in the WhiteSpace esolang."""
    return SpaceInterpreter(code, inp).run()


class SpaceInterpreter(object):
    """Interpreter for the WhiteSpace esolang."""

    def __init__(self, code, inp=''):
        """Create an interpreter for a given code and input."""
        self.code = ''.join([ch for ch in code if ch == ' ' or ch == '\n' or ch == '\t'])
        self.input = inp
        self.p = 0
        self.labels = {}
        self.stack = []
        self.heap = {}

    def run(self):
        """Run the interpreter and get the output."""
        output = ''

        while self.p < len(self.code):
            if self.code[self.p] == ' ':
                self.p += 1
                self.manipulate_stack()
            break
        else:
            raise ValueError('Code must terminate with an exit command.')

        return output

    def manipulate_stack(self):
        """Execute commands for the Stack Manipulation IMP."""
        command = self.code[self.p:self.p + 2]

        if command[0] == ' ':
            self.p += 1
            num = self.parse_num()
            self.stack.append(num)

        elif command == '\t ':
            self.p += 2
            i = self.parse_num()
            self.stack.append(self.stack[-i])

    def parse_num(self):
        """Parse and evaluate the next number."""
        if not self.code or self.code[self.p] == '\n':
            raise ValueError('Numbers cannot be only a terminal.')

        sign = 1 if self.code[self.p] == ' ' else -1
        self.p += 1
        num = '0'
        while self.p < len(self.code):
            if self.code[self.p] == '\n':
                break
            num += '0' if self.code[self.p] == ' ' else '1'
            self.p += 1
        else:
            raise ValueError('Number must end with a terminal.')

        num = sign * int(num, 2)
        self.p += 1
        return num
