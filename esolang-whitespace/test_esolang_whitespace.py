"""Tests for the esolang_whitespace module."""
import pytest


def num_to_space(num):
    """Transform a number into WhiteSpace."""
    is_neg = False
    if num < 0:
        is_neg = True
        num *= -1

    bin_num = bin(num)[2:]
    num_code = bin_num.replace('0', ' ').replace('1', '\t')
    return '{}{}\n'.format('\t' if is_neg else ' ', num_code)


FILL_STACK = '   \n   \t\n   \t \n   \t\t\n   \t  \n'
TERMINATE = '\n\n\n'


# def test_unclean_termination_raises_exception():
#     """Test that unclean termination of the code raises a ValueError."""
#     from esolang_whitespace import whitespace
#     with pytest.raises(ValueError):
#         whitespace('')

# CODES = [
#     ("   \t\n\t\n \t\n\n\n", "1"),
#     ("   \t \n\t\n \t\n\n\n", "2"),
#     ("   \t\t\n\t\n \t\n\n\n", "3"),
#     ("    \n\t\n \t\n\n\n", "0")
# ]


# @pytest.mark.parametrize('code, output', CODES)
# def test_pushing_positive_numbers_with_whitespace(code, output):
#     """Test that pushing and outputing positive numbers works."""
#     from esolang_whitespace import whitespace
#     assert whitespace(code) == output


# CODES = [
#     ("  \t\t\n\t\n \t\n\n\n", "-1"),
#     ("  \t\t \n\t\n \t\n\n\n", "-2"),
#     ("  \t\t\t\n\t\n \t\n\n\n", "-3")
# ]


# @pytest.mark.parametrize('code, output', CODES)
# def test_pushing_negative_numbers_with_whitespace(code, output):
#     """Test that pushing and outputing negative numbers works."""
#     from esolang_whitespace import whitespace
#     assert whitespace(code) == output


# CODES = [
#     ("   \t     \t\n\t\n  \n\n\n", "A"),
#     ("   \t    \t \n\t\n  \n\n\n", "B"),
#     ("   \t    \t\t\n\t\n  \n\n\n", "C")
# ]


# @pytest.mark.parametrize('code, output', CODES)
# def test_output_of_letters_with_whitespace(code, output):
#     """Test that outputing letters works."""
#     from esolang_whitespace import whitespace
#     assert whitespace(code) == output


# Tests for the Interpreter Class


def test_constructing_interpreter_cleans_code():
    """Test that creating the interpreter removes non-whitespace characters."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('Hello world')
    assert i.code == ' '


def test_constructing_interpreter_sets_all_properties_to_empty():
    """Test that the interpreter is empty when constructed."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('   \t\t')
    assert i.input == ''
    assert i.p == 0
    assert i.labels == {}
    assert i.stack == []
    assert i.heap == {}


def test_constructing_interpreter_assigns_given_input():
    """Test that interpreter has the input passed into the contructor."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ', 'Hello world')
    assert i.input == 'Hello world'


def test_run_raises_error_for_unclean_exit_of_program():
    """Test that run raises a ValueError for ending a program without a terminal."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(ValueError):
        i.run()


def test_run_can_exit_cleanly_without_error():
    """Test that run can exit the program cleanly with no errors."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n\n')
    i.run()


def test_run_can_access_the_stack_manipulation_imp():
    """Test that run can execute commands from the stack manipuation IMP."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(FILL_STACK + TERMINATE)
    i.run()
    assert i.stack == [0, 1, 2, 3, 4]


def test_run_can_access_the_arithmetic_imp():
    """Test that run can execute commands from the arithmetic IMP."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(FILL_STACK + '\t   ' + TERMINATE)
    i.run()
    assert i.stack == [0, 1, 2, 7]


def test_parse_num_empty_number_raises_error():
    """Test that parsing empty number raises a ValueError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(ValueError):
        i.parse_num()


def test_parse_num_only_terminal_raises_error():
    """Test that parsing terminal only number raises a ValueError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n')
    with pytest.raises(ValueError):
        i.parse_num()


def test_parse_num_raises_error_for_unterminated_number():
    """Test that parsing number with no terminal raises ValueError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t\t \t')
    with pytest.raises(ValueError):
        i.parse_num()


CODES = [
    (" \t\n", 1),
    (" \t \n", 2),
    (" \t\t\n", 3),
    (" \n", 0)
]


@pytest.mark.parametrize('code, output', CODES)
def test_parse_num_parses_positive_numbers_correctly(code, output):
    """Test that parse_num can parse positive numbers."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(code)
    assert i.parse_num() == output


CODES = [
    ("\t\t\n", -1),
    ("\t\t \n", -2),
    ("\t\t\t\n", -3)
]


@pytest.mark.parametrize('code, output', CODES)
def test_parse_num_parses_negative_numbers_correctly(code, output):
    """Test that parse_num can parse negative numbers."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(code)
    assert i.parse_num() == output


CODES = [
    ("  \n", 3),
    ("  \t\t \n\t\n \t\n\n\n", 6),
]


@pytest.mark.parametrize('code, pointer', CODES)
def test_parse_num_moves_pointer_to_end_of_number_code(code, pointer):
    """Test that parse_num moves the pointer to the end of the number."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(code)
    i.parse_num()
    assert i.p == pointer


def test_exec_manipulate_stack_raises_error_for_invalid_command():
    """Test exec_manipulate_stack raises a ValueError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    with pytest.raises(ValueError):
        i.exec_manipulate_stack()


def test_exec_manipulate_stack_can_push_number_onto_the_stack():
    """Test that exec_manipulate_stack can push a new value onto the stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  \n')
    i.exec_manipulate_stack()
    assert i.stack == [0]


def test_exec_manipulate_stack_raises_error_duplicate_value_outside_stack():
    """Test exec_manipulate_stack raises an IndexError for index out of stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t  \t\n')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack()


@pytest.mark.parametrize('num', [x for x in range(0, 5)])
def test_exec_manipulate_stack_can_duplicate_nth_value_from_top_of_stack(num):
    """Test that exec_manipulate_stack can duplicate nth value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ' + num_to_space(num))
    i.stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack()
    assert i.stack == [0, 1, 2, 3, 4, 4 - num]


@pytest.mark.parametrize('num', [x for x in range(-5, 0)])
def test_exec_manipulate_stack_discards_all_but_top_for_neg_num(num):
    """Test that all but top value is discarded for a negative n value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n' + num_to_space(num))
    i.stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack()
    assert i.stack == [4]


@pytest.mark.parametrize('num', [x for x in range(5, 10)])
def test_exec_manipulate_stack_discards_all_but_top_for_large_num(num):
    """Test all but top value is discarded for n value larger than stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n' + num_to_space(num))
    i.stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack()
    assert i.stack == [4]


@pytest.mark.parametrize('num', [x for x in range(0, 5)])
def test_exec_manipulate_stack_discards_top_n_values_below_top(num):
    """Test that the top n values below the top are discarded."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n' + num_to_space(num))
    i.stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack()
    assert i.stack == [0, 1, 2, 3, 4][:-(num + 1)] + [4]


def test_exec_manipulate_stack_raises_error_duplicate_value_in_empty_stack():
    """Test exec_manipulate_stack raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n ')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(1, 5)])
def test_exec_manipulate_stack_can_duplicate_the_top_value_on_the_stack(stack):
    """Test that manipulate stack can duplicate the top stack value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n ')
    i.stack = stack[:]
    i.exec_manipulate_stack()
    assert i.stack == stack + stack[-1:]


def test_exec_manipulate_stack_raises_error_swap_values_in_empty_stack():
    """Test exec_manipulate_stack raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\t')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack()


def test_exec_manipulate_stack_raises_error_swap_values_in_one_value_stack():
    """Test exec_manipulate_stack raises an IndexError for one value stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\t')
    i.stack = [0]
    with pytest.raises(IndexError):
        i.exec_manipulate_stack()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(2, 6)])
def test_exec_manipulate_stack_can_swap_the_top_values_on_the_stack(stack):
    """Test that manipulate stack can swap the top stack values."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\t')
    i.stack = stack[:]
    i.exec_manipulate_stack()
    stack[-1], stack[-2] = stack[-2], stack[-1]
    assert i.stack == stack


def test_exec_manipulate_stack_raises_error_discard_top_value_in_empty_stack():
    """Test exec_manipulate_stack raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(1, 5)])
def test_exec_manipulate_stack_can_discard_the_top_value_on_the_stack(stack):
    """Test that manipulate stack can discard the top stack value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n')
    i.stack = stack[:]
    i.exec_manipulate_stack()
    assert i.stack == stack[:-1]


def test_exec_arithmetic_raises_error_for_invalid_command():
    """Test exec_arithmetic raises a ValueError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    i.stack = [1, 2]
    with pytest.raises(ValueError):
        i.exec_arithmetic()


def test_exec_arithmetic_raises_error_sum_values_from_empty_stack():
    """Test exec_arithmetic raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    with pytest.raises(IndexError):
        i.exec_arithmetic()


def test_exec_arithmetic_raises_error_sum_values_from_one_value_stack():
    """Test exec_arithmetic raises an IndexError for one value stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    i.stack = [0]
    with pytest.raises(IndexError):
        i.exec_arithmetic()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_sum_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the sum of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    i.stack = stack[:]
    i.exec_arithmetic()
    sum_stack = stack[:-2]
    sum_stack.append(stack[-2] + stack[-1])
    assert i.stack == sum_stack


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_diff_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the diff of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t')
    i.stack = stack[:]
    i.exec_arithmetic()
    diff_stack = stack[:-2]
    diff_stack.append(stack[-2] - stack[-1])
    assert i.stack == diff_stack


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_prod_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the prod of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \n')
    i.stack = stack[:]
    i.exec_arithmetic()
    prod_stack = stack[:-2]
    prod_stack.append(stack[-2] * stack[-1])
    assert i.stack == prod_stack


def test_exec_arithmetic_throws_error_for_division_by_zero():
    """Test that if top of stack is zero, division raises ZeroDivisionError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ')
    i.stack = [1, 0]
    with pytest.raises(ZeroDivisionError):
        i.exec_arithmetic()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_quot_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the quot of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ')
    i.stack = stack[:]
    i.exec_arithmetic()
    quot_stack = stack[:-2]
    quot_stack.append(stack[-2] / stack[-1])
    assert i.stack == quot_stack


def test_exec_arithmetic_throws_error_for_modulo_by_zero():
    """Test that if top of stack is zero, modulo raises ZeroDivisionError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    i.stack = [1, 0]
    with pytest.raises(ZeroDivisionError):
        i.exec_arithmetic()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_mod_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the mod of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    i.stack = stack[:]
    i.exec_arithmetic()
    mod_stack = stack[:-2]
    mod_stack.append(stack[-2] % stack[-1])
    assert i.stack == mod_stack


@pytest.mark.parametrize('stack', [[1, 2], [1, -2], [-1, 2]])
def test_exec_arithmetic_mod_matches_sign_of_top_stack_value(stack):
    """Test that sign of the mod matches sign of the top number on stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    i.stack = stack[:]
    i.exec_arithmetic()
    if stack[-1] > 0:
        assert i.stack[-1] > 0
    else:
        assert i.stack[-1] < 0


def test_exec_heap_access_raises_error_for_invalid_command():
    """Test exec_heap_access raises a ValueError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n')
    i.stack = [1, 2]
    with pytest.raises(ValueError):
        i.exec_heap_access()


def test_exec_heap_access_raises_error_popping_from_empty_stack():
    """Test exec_heap_access raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    with pytest.raises(IndexError):
        i.exec_heap_access()


def test_exec_heap_access_raises_error_popping_from_one_item_stack_storing():
    """Test exec_heap_access raises an IndexError for one item stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    i.stack = [0]
    with pytest.raises(IndexError):
        i.exec_heap_access()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_heap_access_stores_values_into_heap_from_stack(stack):
    """Test that exec_heap_access can move values from the heap from stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    i.stack = stack[:]
    i.exec_heap_access()
    b, a = stack[-2:]
    assert i.heap[b] == a


def test_exec_heap_access_invalid_heap_address_raises_error():
    """Test that accessing an invalid heap access raises a NameError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t')
    i.stack = [0]
    with pytest.raises(NameError):
        i.exec_heap_access()


@pytest.mark.parametrize('heap', [{x: x**2 for x in range(y)} for y in range(3, 7)])
def test_exec_heap_access_stores_values_into_stack_from_heap(heap):
    """Test that exec_heap_access can move values from the stack from heap."""
    from esolang_whitespace import SpaceInterpreter
    from random import choice
    i = SpaceInterpreter('\t')
    address = choice(list(heap))
    i.stack = [address]
    i.heap = heap
    i.exec_heap_access()
    assert i.stack[-1] == heap[address]


def test_exec_input_output_raises_error_for_invalid_command():
    """Test exec_input_output raises a ValueError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n')
    with pytest.raises(ValueError):
        i.exec_input_output()


def test_exec_input_output_raises_error_for_output_char_from_empty_stack():
    """Test exec_input_output raises an IndexError for output from empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    with pytest.raises(IndexError):
        i.exec_input_output()


@pytest.mark.parametrize('stack', [[x + 33 for x in range(y)] for y in range(1, 94, 5)])
def test_exec_input_output_can_output_top_of_stack_as_character(stack):
    """Test that exec_inout_output can output top stack number as character."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    i.stack = stack[:]
    output = i.exec_input_output()
    assert output == chr(stack[-1])


def test_exec_input_output_raises_error_for_output_num_from_empty_stack():
    """Test exec_input_output raises an IndexError for output from empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t')
    with pytest.raises(IndexError):
        i.exec_input_output()


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_input_output_can_output_top_of_stack_as_number(stack):
    """Test that exec_inout_output can output top stack number."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t')
    i.stack = stack[:]
    output = i.exec_input_output()
    assert output == stack[-1]


def test_exec_flow_control_raises_error_for_invalid_command():
    """Test exec_flow_control raises a ValueError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    with pytest.raises(ValueError):
        i.exec_flow_control()


def test_execute_flow_control_exit_command_ends_program():
    """Test that execute_flow_control can end the program."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n')
    assert i.exec_flow_control() is True
