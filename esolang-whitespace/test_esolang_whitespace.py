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


@pytest.mark.parametrize('num', [x for x in range(1, 6)])
def test_exec_manipulate_stack_can_duplicate_nth_value_from_top_of_stack(num):
    """Test that exec_manipulate_stack can duplicate nth value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ' + num_to_space(num))
    i.stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack()
    assert i.stack == [0, 1, 2, 3, 4, 5 - num]


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
