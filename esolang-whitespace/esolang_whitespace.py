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

        self.labels = {}
        self.stack = []
        self.heap = {}

        self._call_stack = [0]

        # All commands #

        self._STACK_IMP = {
            ' ': self._push,
            '\t ': self._duplicate_nth_value,
            '\t\n': self._discard_below_top_value,
            '\n ': self._duplicate_top_value,
            '\n\t': self._swap_top_two_values,
            '\n\n': self._discard_top_value
        }

        self._ARITH_IMP = {
            '  ': '+',
            ' \t': '-',
            ' \n': '*',
            '\t ': '//',
            '\t\t': '%'
        }

        self._HEAP_IMP = {
            ' ': self._stack_to_heap,
            '\t': self._heap_to_stack
        }

        self._IO_IMP = {
            '  ': self._output_character,
            ' \t': self._output_number,
            '\t ': self._input_character,
            '\t\t': self._input_number
        }

        self._FLOW_IMP = {
            '  ': self._label_position,
            ' \t': self._call_subroutine,
            ' \n': self._jump_unconditionally,
            '\t ': self._jump_zero_conditional,
            '\t\t': self._jump_neg_conditional,
            '\t\n': self._exit_subroutine,
            '\n\n': self._exit_program
        }

    @property
    def p(self):
        """Get the current position of the pointer."""
        return self._call_stack[-1]

    @p.setter
    def p(self, value):
        """Set the current position of the pointer."""
        self._call_stack[-1] = value

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

            imp = self.code[self.p:self.p + 2]
            self.p += 2

            if imp[0] == ' ':
                self.p -= 1
                self.exec_manipulate_stack()

            elif imp == '\t ':
                self.exec_arithmetic()

            elif imp == '\t\t':
                self.exec_heap_access()

            elif imp == '\t\n':
                output += self.exec_input_output()

            elif imp[0] == '\n':
                self.p -= 1
                if self.exec_flow_control():
                    break

            else:
                raise SyntaxError('Invalid instruction modification parameter.')

        else:
            raise SyntaxError('Code must terminate with an exit command.')

        return output

    def find_labels(self):
        """Run through the code to define all the labels used."""
        pass

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
        cmd_string = self.code[self.p:self.p + 2]
        self.p += 2

        if cmd_string not in self._STACK_IMP:
            self.p -= 1
            cmd_string = cmd_string[0]

        try:
            command = self._STACK_IMP[cmd_string]
            delta = command(self.stack, self.code[self.p:])
            self.p += delta

        except KeyError:
            raise SyntaxError('Invalid stack manipulation command.')

    def _push(self, stack, code):
        """Push a number onto the memory stack."""
        num, delta = self.parse_num(code)
        stack.append(num)
        return delta

    def _duplicate_top_value(self, stack, *args):
        """Push a duplicate of the top value onto the stack."""
        if not stack:
            raise IndexError('Cannot duplicate from empty stack.')
        stack.append(stack[-1])
        return 0

    def _duplicate_nth_value(self, stack, code):
        """Push a duplicate of the nth value onto the stack."""
        if not stack:
            raise IndexError('Cannot duplicate from empty stack.')

        n, delta = self.parse_num(code)

        if n < 0 or n > len(stack):
            raise IndexError('Duplication value is outside of stack.')

        stack.append(stack[-(n + 1)])
        return delta

    def _discard_top_value(self, stack, *args):
        """Discard the top value from the stack."""
        if not stack:
            raise IndexError('Cannot discard from empty stack.')

        stack.pop()
        return 0

    def _discard_below_top_value(self, stack, code):
        """Discard top num values below top of stack.

        num < 0 and num >= len(stack) discards all but top.
        """
        n, delta = self.parse_num(code)

        n = n if 0 <= n < len(stack) else len(stack) - 1

        for _ in range(n):
            stack.pop(-2)

        return delta

    def _swap_top_two_values(self, stack, *args):
        """Swap the top two values on the stack."""
        if not stack or len(stack) == 1:
            raise IndexError('Not enough values in stack to swap.')
        stack[-1], stack[-2] = stack[-2], stack[-1]
        return 0

    def exec_arithmetic(self):
        """Execute commands for the Arithmetic IMP.

        Commands:
            ss - Pop a and b, then push b+a
            st - Pop a and b, then push b-a
            sn - Pop a and b, then push b*a
            ts - Pop a and b, then push b//a - Raises ZeroDivisionError
            tt - Pop a and b, then push b%a - Raises ZeroDivisionError
        """
        cmd_string = self.code[self.p:self.p + 2]
        self.p += 2

        try:
            op = self._ARITH_IMP[cmd_string]
            self._stack_artithmetic(op, self.stack)

        except KeyError:
            raise SyntaxError('Invalid arithmetic command.')

    def _stack_artithmetic(self, op, stack):
        """Execute operation on the top two values of the stack."""
        try:
            a, b = stack.pop(), stack.pop()
            result = eval('b{op}a'.format(op=op))
            stack.append(result)
            return stack

        except IndexError:
            raise IndexError('Not enough values in stack for operation.')
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot divide by zero.')

    def exec_heap_access(self):
        """Execute commands for the Heap Access IMP.

        Commands:
            s - Pop a and b, then store a at heap address b
            t - Pop a, then push the value at heap address a onto stack
        """
        cmd_string = self.code[self.p:self.p + 1]
        self.p += 1

        try:
            command = self._HEAP_IMP[cmd_string]
            command(self.stack, self.heap)

        except KeyError:
            raise SyntaxError('Invalid heap access command.')

    def _stack_to_heap(self, stack, heap):
        """Move a value from the stack to the heap.

        Pop a value and address, then store the value at that heap address.
        """
        try:
            value, address = stack.pop(), stack.pop()
            heap[address] = value

        except IndexError:
            raise IndexError('Not enough values in stack for heap operation.')

    def _heap_to_stack(self, stack, heap):
        """Move a value from the heap to the stack.

        Pop an address, then push the value at that heap address onto stack.
        """
        try:
            address = stack.pop()
            stack.append(heap[address])

        except IndexError:
            raise IndexError('Not enough values in stack for heap operation.')
        except KeyError:
            raise NameError('Invalid heap address.')

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
        cmd_string = self.code[self.p:self.p + 2]
        self.p += 2

        try:
            command = self._IO_IMP[cmd_string]
            output, self.input = command(self.input, self.stack, self.heap)

        except KeyError:
            raise SyntaxError('Invalid input/output command.')

        return output

    def _output_character(self, inp, stack, *args):
        """Output the top value on the stack as a character."""
        try:
            return chr(stack.pop()), inp
        except IndexError:
            raise IndexError('No values in stack to output.')

    def _output_number(self, inp, stack, *args):
        """Output the top value on the stack as a number."""
        try:
            return str(stack.pop()), inp
        except IndexError:
            raise IndexError('No values in stack to output.')

    def _input_character(self, inp, stack, heap):
        """Read a character from input and store it in the heap.

        Uses the value from the top of the stack as the heap address
        and stores the ASCII value of the character.
        """
        if not inp:
            raise IOError('No more characters in input to read.')

        try:
            value, inp = inp[0], inp[1:]
            address = stack.pop()
            heap[address] = ord(value)

            return '', inp

        except IndexError:
            raise IndexError('Not enough values in stack to acess heap')

    def _input_number(self, inp, stack, heap):
        """Read a number from the input and store it in the heap.

        Uses the value from the top of the stack as the heap address.
        """
        if not inp:
            raise IOError('No more characters in input to read.')

        value, terminal, inp = inp.partition('\n')

        if not terminal:
            raise SyntaxError('Number input must have a terminal.')

        try:
            value = int(value)
            address = stack.pop()
            heap[address] = value

            return '', inp

        except IndexError:
            raise IndexError('Not enough values in stack to acess heap')
        except ValueError:
            raise ValueError('Cannot parse input as a number.')

    def exec_flow_control(self):
        """Execute commands for the Flow Control IMP.

        Commands:
            ss (label) - Mark current position with label, must be unique
            st (label) - Call subroutine at label
            sn (label) - Jump unconditionally to position at label
            ts (label) - Pop value off stack, jump to label if value == 0
            tt (label) - Pop value off stack, jump to label if value < 0
            tn - Exit subroutine and return to where subroutine was called
            nn - Exit the program

        Return: True - exit the program, False - continue
        """
        cmd_string = self.code[self.p:self.p + 2]
        self.p += 2

        try:
            command = self._FLOW_IMP[cmd_string]
            position, exit = command(code=self.code[self.p:], labels=self.labels,
                                     call_stack=self._call_stack, stack=self.stack)

        except KeyError:
            raise SyntaxError('Invalid flow control command.')

        self.p = position
        return exit

    def _label_position(self, code, labels, call_stack, **kwargs):
        """Mark the current position with a unique label."""
        label, delta = self.parse_label(code)
        if label in labels:
            raise NameError('Cannot redefine a label.')

        position = call_stack[-1] + delta
        labels[label] = position
        return position, False

    def _get_label_position(self, label, labels, **kwargs):
        """Get the new position of pointer given by the label."""
        try:
            return labels[label]
        except KeyError:
            raise NameError('Label is not defined.')

    def _call_subroutine(self, code, labels, call_stack, **kwargs):
        """Call the subroutine marked with the next label."""
        label, delta = self.parse_label(code)
        call_stack[-1] += delta
        call_stack.append(0)
        return self._get_label_position(label, labels), False

    def _jump_unconditionally(self, code, labels, **kwargs):
        """Jump the pointer unconditionally to the labeled position."""
        label, _ = self.parse_label(code)
        return self._get_label_position(label, labels), False

    def _jump_zero_conditional(self, code, labels, call_stack, stack, **kwargs):
        """Jump the pointer to the labeled position if top of stack is zero."""
        label, delta = self.parse_label(code)
        if stack.pop() == 0:
            return self._get_label_position(label, labels), False
        return call_stack[-1] + delta, False

    def _jump_neg_conditional(self, code, labels, call_stack, stack, **kwargs):
        """Jump the pointer to the labeled position if top of stack is negative."""
        label, delta = self.parse_label(code)
        if stack.pop() < 0:
            return self._get_label_position(label, labels), False
        return call_stack[-1] + delta, False

    def _exit_subroutine(self, call_stack, **kwargs):
        """Exit the current subroutine and return to where it was called."""
        if len(call_stack) > 1:
            call_stack.pop()
        return call_stack[-1], False

    def _exit_program(self, call_stack, **kwargs):
        """Exit the program cleanly."""
        return call_stack[-1], True

    def parse_num(self, code):
        """Parse and evaluate the next number in the code.

        Numbers consist of [sign][binary][terminal].

        sign: t = negative, s = positive
        binary: s = 0, t = 1
        terminal: n

        Raises ValueError for unclean termination.

        Returns: the evaluated number, the change in the pointer's postion
        """
        if not code:
            raise SyntaxError('Numbers cannot be empty.')

        if code[0] == '\n':
            raise SyntaxError('Numbers cannot be only a terminal.')

        sign = 1 if code[0] == ' ' else -1
        position = 1
        num = '0'
        while position < len(code):
            if code[position] == '\n':
                break
            num += '0' if code[position] == ' ' else '1'
            position += 1
        else:
            raise SyntaxError('Number must end with a terminal.')

        num = sign * int(num, 2)
        position += 1
        return num, position

    def parse_label(self, code):
        """Parse and validate the next label in the code.

        Labels consist of any number of t and s ending with a [terminal], n.

        Returns: the label, the change in the pointer's postion
        """
        if not code:
            raise SyntaxError('Labels cannot be empty.')

        label, terminal, _ = code.partition('\n')

        if not terminal:
            raise SyntaxError('Lables must end with a terminal')

        position = len(label) + 1

        return label, position
