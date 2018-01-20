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
        """Run the interpreter and get the output.

        Command modules:
            s - Stack Manipulation
            ts - Arithmetic
            tt - Heap Access
            tn - Input/Output
            n - Flow Control

        Raises ValueError for unclean termination.
        """
        output = ''

        while self.p < len(self.code):
            print(self)

            if self.code[self.p] == ' ':
                self.p += 1
                self.exec_manipulate_stack()

            elif self.code[self.p] == '\t':
                self.p += 1

                if self.code[self.p] == ' ':
                    self.p += 1
                    self.exec_arithmetic()

            elif self.code[self.p] == '\n':
                self.p += 1
                if self.exec_flow_control():
                    break
        else:
            raise ValueError('Code must terminate with an exit command.')

        return output

    def exec_manipulate_stack(self):
        """Execute commands for the Stack Manipulation IMP.

        Commands:
            s (num) - Push num onto stack
            ts (num) - Duplicate num-th value from top of stack
            tn (num) - Discard top num values below top of stack
                       num < 0 and num >= len(stack) discards all but top
            ns - Duplicate top value on stack
            nt - Swap top two values on stack
            nn - Discard top value on stack
        """
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
            self.p += 2
            try:
                self.stack.append(self.stack[-1])
            except IndexError:
                raise IndexError('Cannot duplicate from empty stack.')

        elif command == '\n\t':
            self.p += 2
            try:
                self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
            except IndexError:
                raise IndexError('Not enough values in stack to swap.')

        elif command == '\n\n':
            self.p += 2
            try:
                self.stack.pop()
            except IndexError:
                raise IndexError('Cannot discard from empty stack.')

        else:
            raise ValueError('Invalid stack manipulation command.')

    def exec_arithmetic(self):
        """Execute commands for the Arithmetic IMP.

        Commands:
            ss - Pop a and b, then push b+a
            st - Pop a and b, then push b-a
            sn - Pop a and b, then push b*a
            ts - Pop a and b, then push b//a - Raises ZeroDivisionError
            tt - Pop a and b, then push b%a - Raises ZeroDivisionError
        """
        command = self.code[self.p:self.p + 2]
        self.p += 2

        if command == '  ':
            try:
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            except IndexError:
                raise IndexError('Not enough values in stack for operation.')

        else:
            raise ValueError('Invalid arithmetic command.')

    def exec_heap_access(self):
        """Execute commands for the Heap Access IMP.

        Commands:
            s - Pop a and b, then store a at heap address b
            t - Pop a, then push the value at heap address a onto stack
        """
        command = self.code[self.p:self.p + 1]
        self.p += 1

    def exec_input_output(self):
        """Execute commands for the Input/Output IMP.

        Commands:
            ss - Pop value from stack and output as a character
            st - Pop value from stack and output as a number
            ts - Read character from input, a, pop value from stack, b,
                 then store ASCII value of a at heap address b
            tt - Read number from input, a, pop value from stack, b,
                 then a at heap address b

        Return: Output string
        """
        command = self.code[self.p:self.p + 2]
        self.p += 2

    def exec_flow_control(self):
        """Execute commands for the Flow Control IMP.

        Commands:
            ss (label) - Mark current position with label
            st (label) - Call subroutine at label
            sn (label) - Jump unconditionally to position at label
            ts (label) - Pop value off stack, jump to label if value == 0
            tt (label) - Pop value off stack, jump to label if value < 0
            tn - Exit subroutine and return to where subroutine was called
            nn - Exit the program

        Return: True - exit the program, False - continue
        """
        command = self.code[self.p:self.p + 2]

        if command == '\n\n':
            return True

        else:
            raise ValueError('Invalid flow control command.')

    def parse_num(self):
        """Parse and evaluate the next number in the code.

        Numbers consist of [sign][binary][terminal].

        sign: t = negative, s = positive
        binary: s = 0, t = 1
        terminal: n

        Raises ValueError for unclean termination.
        """
        if not self.code[self.p:]:
            raise ValueError('Numbers cannot be empty.')

        if self.code[self.p] == '\n':
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

    def parse_label(self):
        """Parse and validate the next label in the code.

        Labels consist of any number of t and s ending with a [terminal], n.
        Labels must be unique.
        """
        pass
