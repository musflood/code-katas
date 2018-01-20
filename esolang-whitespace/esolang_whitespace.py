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

    def __str__(self):
        """Print the current state of the code."""
        vis_code = self.code.replace(' ', 's')
        vis_code = vis_code.replace('\t', 't')
        vis_code = vis_code.replace('\n', 'n')
        return '{}[{}]{}'.format(vis_code[:self.p],
                                 vis_code[self.p:self.p + 1],
                                 vis_code[self.p + 1:])

    def run(self):
        """Run the interpreter and get the output."""
        output = ''

        while self.p < len(self.code):
            print(self)

            if self.code[self.p] == ' ':
                self.p += 1
                self.exec_manipulate_stack()

            elif self.code[self.p] == '\n':
                self.p += 1
                if self.exec_flow_control():
                    break
        else:
            raise ValueError('Code must terminate with an exit command.')

        return output

    def exec_manipulate_stack(self):
        """Execute commands for the Stack Manipulation IMP."""
        command = self.code[self.p:self.p + 2]

        if command[0] == ' ':
            self.p += 1
            num = self.parse_num()
            self.stack.append(num)

        elif command == '\t ':
            self.p += 2
            n = self.parse_num()
            try:
                self.stack.append(self.stack[-(n + 1)])
            except IndexError:
                raise IndexError('Duplication value is outside of stack.')

        elif command == '\t\n':
            self.p += 2
            n = self.parse_num()
            if n < 0:
                self.stack = self.stack[-1:]
            else:
                self.stack = self.stack[:-(n + 1)] + self.stack[-1:]

        elif command == '\n ':
            try:
                self.stack.append(self.stack[-1])
            except IndexError:
                raise IndexError('Cannot duplicate from empty stack.')

        elif command == '\n\t':
            try:
                self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
            except IndexError:
                raise IndexError('Not enough values in stack to swap.')

        elif command == '\n\n':
            try:
                self.stack.pop()
            except IndexError:
                raise IndexError('Cannot discard from empty stack.')

        else:
            raise ValueError('Invalid stack manipulation command.')

    def exec_flow_control(self):
        """Execute commands for the Flow Control IMP.

        Return: True - exit the program, False - continue
        """
        command = self.code[self.p:self.p + 2]

        if command == '\n\n':
            return True

        else:
            raise ValueError('Invalid flow control command.')

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
