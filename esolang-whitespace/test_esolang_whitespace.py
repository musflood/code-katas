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


def test_unclean_termination_raises_exception():
    """Test that unclean termination of the code raises a SyntaxError."""
    from esolang_whitespace import whitespace
    with pytest.raises(SyntaxError):
        whitespace('')

CODES = [
    ("   \t\n\t\n \t\n\n\n", "1"),
    ("   \t \n\t\n \t\n\n\n", "2"),
    ("   \t\t\n\t\n \t\n\n\n", "3"),
    ("    \n\t\n \t\n\n\n", "0")
]


@pytest.mark.parametrize('code, output', CODES)
def test_pushing_positive_numbers_with_whitespace(code, output):
    """Test that pushing and outputing positive numbers works."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ("  \t\t\n\t\n \t\n\n\n", "-1"),
    ("  \t\t \n\t\n \t\n\n\n", "-2"),
    ("  \t\t\t\n\t\n \t\n\n\n", "-3")
]


@pytest.mark.parametrize('code, output', CODES)
def test_pushing_negative_numbers_with_whitespace(code, output):
    """Test that pushing and outputing negative numbers works."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ("   \t     \t\n\t\n  \n\n\n", "A"),
    ("   \t    \t \n\t\n  \n\n\n", "B"),
    ("   \t    \t\t\n\t\n  \n\n\n", "C")
]


@pytest.mark.parametrize('code, output', CODES)
def test_output_of_letters_with_whitespace(code, output):
    """Test that outputing letters works."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ("blahhhh   \targgggghhh     \t\n\t\n  \n\n\n", "A"),
    (" I heart \t  cats  \t \n\t\n  \n\n\n", "B"),
    ("   \t  welcome  \t\t\n\t\n to the\nnew\nworld\n", "C")
]


@pytest.mark.parametrize('code, output', CODES)
def test_output_of_letters_with_commented_whitespace(code, output):
    """Test that outputing letters works with inline comments."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ("   \t\t\n   \t\t\n\t\n \t\t\n \t\n\n\n", "33"),
    ("   \t\t\n \n \t\n \t\t\n \t\n\n\n", "33"),
    ("   \t\n   \t \n   \t\t\n \t  \t \n\t\n \t\n\n\n", "1"),
    ("   \t\n   \t \n   \t\t\n \t  \t\n\t\n \t\n\n\n", "2"),
    ("   \t\n   \t \n   \t\t\n \t   \n\t\n \t\n\n\n", "3"),
    ('   \t\t\n   \t \n \n\t\t\n \t\t\n \t\n\n\n', '32'),
    ('   \t\t\n   \t \n \n\t \n\n\t\n \t\n\n\n', '2'),
    ('   \t\t\n   \t \n   \t\n   \t  \n   \t\t \n   \t \t\n   \t\t\t\n \n\t \t\n \t\t\n\t\n \t\t\n \t\t\n \t\t\n \t\n\n\n', '5123')
]


@pytest.mark.parametrize('code, output', CODES)
def test_stack_functionality(code, output):
    """Test that stack functionality works properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ('  \t\n\t\n \t\n\n\n', '0'),
    ('   \t\n   \t \n   \t\t\n \t\n\t\t     \n\t\n \t\n\n\n', '3'),
    ('   \t\n   \t \n   \t\t\n \t\n\t \t  \n\t\n \t\n\n\n', '3')
]


@pytest.mark.parametrize('code, output', CODES)
def test_stack_edge_cases(code, output):
    """Test that stack edge cases work properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    (' \n \n\n\n', IndexError),
    (' \n\n\n\n\n', IndexError),
    ('   \t\n   \t \n   \t\t\n \t  \t\t\n\t\n \t\n\n\n', IndexError),
    ('   \t\n   \t \n   \t\t\n \t \t\t\n\t\n \t\n\n\n', IndexError),
    ('   \t\n   \t \n   \t\t\n \t \n\t\n \t\n\n\n', SyntaxError),
    ('   \t\n   \t \n   \t\t\n \t\n\t\t     \n\t\n \t\t\n \t\n\n\n', IndexError),
    ('   \t\n   \t \n   \t\t\n \t\n\t \t  \n\t\n \t\t\n \t\n\n\n', IndexError)
]


@pytest.mark.parametrize('code, error', CODES)
def test_stack_edge_cases_raise_errors(code, error):
    """Test that stack edge cases work properly."""
    from esolang_whitespace import whitespace
    with pytest.raises(error):
        whitespace(code)


CODES = [
    ('   \t\n   \t\n   \t \n\t\t \t\t\t\t\n \t\n\n\n', '2'),
    ('   \t\n   \t\n   \t  \n   \t\n   \t \n\t\t \t\t \t\t\t\t\n \t\n\n\n', '4'),
    ('   \t\n   \t \n   \t\n   \t  \n   \t \n   \t \n\t\t \t\t \t\t\t \n\t\t\t\t\t\n \t\t\n \t\n\n\n', '42')
]


@pytest.mark.parametrize('code, output', CODES)
def test_heap_functionality(code, output):
    """Test that heap works properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ('   \t\n\t\t\t\t\n \t\n\n\n', NameError),
    ('   \t\n   \t \n\t\t \t\t\t\n\n\n', IndexError),
    ('   \t\n\t\t \n\n\n', IndexError)
]


@pytest.mark.parametrize('code, error', CODES)
def test_heap_edge_cases_raise_errors(code, error):
    """Test that heap edge cases work properly."""
    from esolang_whitespace import whitespace
    with pytest.raises(error):
        whitespace(code)


CODES = [
    ('  \t\t\n   \t  \n\t   \t\n \t\n\n\n', '3'),
    ('  \t\t \n   \t  \n\t  \t\t\n \t\n\n\n', '-6'),
    ('   \t  \n   \t  \n\t  \n\t\n \t\n\n\n', '16'),
    ('   \t   \n   \t \n\t \t \t\n \t\n\n\n', '4'),
    ('   \t   \n   \t\t\n\t \t\t\t\n \t\n\n\n', '2'),

]


@pytest.mark.parametrize('code, output', CODES)
def test_arithmetic_functionality(code, output):
    """Test that arithmetic works properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ('   \t   \n   \t\t\n\t \t \t\n \t\n\n\n', '2'),
    ('  \t\t   \n   \t\t\n\t \t \t\n \t\n\n\n', '-3'),
    ('   \t \t\n  \t\t \n\t \t\t\t\n \t\n\n\n', '-1'),
    ('   \t \t\n  \t\t\t\n\t \t\t\t\n \t\n\n\n', '-1'),
    ('  \t\t \t\n   \t \n\t \t\t\t\n \t\n\n\n', '1'),
    ('  \t\t \t\n   \t\t\n\t \t\t\t\n \t\n\n\n', '1'),
    ('  \t\t \t\n  \t\t \n\t \t\t\t\n \t\n\n\n', '-1'),
    ('  \t\t \t\n  \t\t\t\n\t \t\t\t\n \t\n\n\n', '-2')
]


@pytest.mark.parametrize('code, output', CODES)
def test_arithmetic_edge_cases(code, output):
    """Test that arithmetic edge cases work properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


CODES = [
    ('\t   \t\n \t\n\n\n', IndexError),
    ('   \t  \n\t   \t\n \t\n\n\n', IndexError),
    ('\t  \t\t\n \t\n\n\n', IndexError),
    ('   \t  \n\t  \t\t\n \t\n\n\n', IndexError),
    ('\t  \n\t\n \t\n\n\n', IndexError),
    ('   \t  \n\t  \n\t\n \t\n\n\n', IndexError),
    ('\t \t \t\n \t\n\n\n', IndexError),
    ('   \t \n\t \t \t\n \t\n\n\n', IndexError),
    ('\t \t\t\t\n \t\n\n\n', IndexError),
    ('   \t\t\n\t \t\t\t\n \t\n\n\n', IndexError),
    ('   \t   \n    \n\t \t \t\n \t\n\n\n', ZeroDivisionError),
    ('   \t   \n    \n\t \t\t\t\n \t\n\n\n', ZeroDivisionError)
]


@pytest.mark.parametrize('code, error', CODES)
def test_arithmetic_edge_cases_raise_errors(code, error):
    """Test that arithmetic edge cases work properly."""
    from esolang_whitespace import whitespace
    with pytest.raises(error):
        whitespace(code)


CODES = [
    ('   \t\n\t\n\t\t   \t \n\t\n\t\t   \t\t\n\t\n\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n \t\t\n \t\t\n \t\n\n\n', '1\n2\n3\n', '123'),
    ('   \t\n\t\n\t\t   \t \n\t\n\t\t   \t\t\n\t\n\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n \t\t\n \t\t\n \t\n\n\n', '8\n6\n7\n', '867'),
    ('   \t\n\t\n\t\t   \t \n\t\n\t\t   \t\t\n\t\n\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n \t\t\n \t\t\n \t\n\n\n', '9\n1\n8\n2\n7\n3\n5\n4\n', '918'),
    ('   \t\n\t\n\t    \t \n\t\n\t    \t\t\n\t\n\t    \t  \n\t\n\t    \t \t\n\t\n\t    \t \t\n\t\t\t   \t  \n\t\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n  \t\n  \t\n  \t\n  \t\n  \n\n\n', '12345', '12345'),
    ('   \t\n\t\n\t    \t \n\t\n\t    \t\t\n\t\n\t    \t  \n\t\n\t    \t \t\n\t\n\t    \t \t\n\t\t\t   \t  \n\t\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n  \t\n  \t\n  \t\n  \t\n  \n\n\n', '86755', '86755'),
    ('   \t\n\t\n\t    \t \n\t\n\t    \t\t\n\t\n\t    \t  \n\t\n\t    \t \t\n\t\n\t    \t \t\n\t\t\t   \t  \n\t\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n  \t\n  \t\n  \t\n  \t\n  \n\n\n', '91827354', '91827'),
    ('   \t\n\t\n\t    \t \n\t\n\t    \t\t\n\t\n\t    \t  \n\t\n\t    \t \t\n\t\n\t    \t \t\n\t\t\t   \t  \n\t\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n  \t\n  \t\n  \t\n  \t\n  \n\n\n', 'Hello', 'Hello'),
    ('   \t\n\t\n\t    \t \n\t\n\t    \t\t\n\t\n\t    \t  \n\t\n\t    \t \t\n\t\n\t    \t \t\n\t\t\t   \t  \n\t\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n  \t\n  \t\n  \t\n  \t\n  \n\n\n', 'World', 'World')
]


@pytest.mark.parametrize('code, inp, output', CODES)
def test_input_functionality(code, inp, output):
    """Test that input works properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code, inp) == output


CODES = [
    ('   \t\n\t\n\t\t   \t \n\t\n\t\t   \t\t\n\t\n\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n \t\t\n \t\t\n \t\n\n\n', '1\n2\n', OSError),
    ('   \t\n\t\n\t    \t \n\t\n\t    \t\t\n\t\n\t    \t  \n\t\n\t    \t \t\n\t\n\t    \t \t\n\t\t\t   \t  \n\t\t\t   \t\t\n\t\t\t   \t \n\t\t\t   \t\n\t\t\t\t\n  \t\n  \t\n  \t\n  \t\n  \n\n\n', 'Hell', OSError),
    ('\t\n\t\t\n\n\n', '1\n2\n', IndexError),
    ('\t\n\t \n\n\n', '12', IndexError)
]


@pytest.mark.parametrize('code, inp, error', CODES)
def test_input_edge_cases_raise_errors(code, inp, error):
    """Test that input edge cases work properly."""
    from esolang_whitespace import whitespace
    with pytest.raises(error):
        whitespace(code, inp)


CODES = [
    ('   \t\n   \t\t\n   \n   \t \n   \n   \t\n\n  \n\t\n \t\n\t \n\n\n\n', '123'),
    ('  \t\t\t\n\n  \n \n   \t\t\n\t  \n\t\n \t   \t\n\t    \n \n\t\t\n\n\n\n', '321'),
    ('   \t\n   \t \n   \t\t\n\t\n \t\n \n\n\t\n \t\t\n \t\n  \n\n\n\n', '')
]


@pytest.mark.parametrize('code, output', CODES)
def test_unconditional_jump_functionality(code, output):
    """Test that unconditional jump works properly."""
    from esolang_whitespace import whitespace
    assert whitespace(code) == output


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
    assert i._call_stack == [0]
    assert i.p == 0
    assert i.labels == {}
    assert i.stack == []
    assert i.heap == {}


def test_p_property_accesses_top_of_call_stack():
    """Test that the p property accesses the top of the call stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    i._call_stack = [0, 1, 2, 3]
    assert i.p == 3


def test_p_property_sets_the_top_of_call_stack():
    """Test that the p property sets the top of the call stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    i._call_stack = [0, 1, 2, 3]
    i.p = 9
    assert i._call_stack[-1] == 9


def test_constructing_interpreter_assigns_given_input():
    """Test that interpreter has the input passed into the contructor."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ', 'Hello world')
    assert i.input == 'Hello world'


def test_run_raises_error_for_unclean_exit_of_program():
    """Test that run raises a SyntaxError for ending a program without a terminal."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(SyntaxError):
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


def test_run_can_access_the_heap_access_imp():
    """Test that run can execute commands from the heap access IMP."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(FILL_STACK + '\t\t ' + TERMINATE)
    i.run()
    assert i.stack == [0, 1, 2]
    assert i.heap == {3: 4}


def test_run_can_access_the_input_output_imp():
    """Test that run can execute commands from the input/output IMP."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(FILL_STACK + '\t\n \t' + TERMINATE)
    output = i.run()
    assert i.stack == [0, 1, 2, 3]
    assert output == '4'


def test_run_can_access_the_flow_control_imp():
    """Test that run can execute commands from the flow control IMP."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(FILL_STACK + '\n  \n' + TERMINATE)
    i.run()
    assert i.stack == [0, 1, 2, 3, 4]
    assert i.labels == {'': 32}


def test_parse_num_empty_number_raises_error():
    """Test that parsing empty number raises a SyntaxError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(SyntaxError):
        i.parse_num('')


def test_parse_num_only_terminal_raises_error():
    """Test that parsing terminal only number raises a SyntaxError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(SyntaxError):
        i.parse_num('\n')


def test_parse_num_raises_error_for_unterminated_number():
    """Test that parsing number with no terminal raises SyntaxError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(SyntaxError):
        i.parse_num(' \t\t \t')


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
    i = SpaceInterpreter('')
    num, _ = i.parse_num(code)
    assert num == output


CODES = [
    ("\t\t\n", -1),
    ("\t\t \n", -2),
    ("\t\t\t\n", -3)
]


@pytest.mark.parametrize('code, output', CODES)
def test_parse_num_parses_negative_numbers_correctly(code, output):
    """Test that parse_num can parse negative numbers."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    num, _ = i.parse_num(code)
    assert num == output


CODES = [
    ("  \n", 3),
    ("  \t\t \n\t\n \t\n\n\n", 6),
]


@pytest.mark.parametrize('code, pointer', CODES)
def test_parse_num_moves_pointer_to_end_of_number_code(code, pointer):
    """Test that parse_num moves the pointer to the end of the number."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    _, delta = i.parse_num(code)
    assert delta == pointer


def test_parse_label_raises_error_for_empty_label():
    """Test that parse_label raises a SyntaxError for an empty label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(SyntaxError):
        i.parse_label('')


def test_parse_label_raises_error_for_non_terminated_label():
    """Test that parse_label raises a SyntaxError for non terminated label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    with pytest.raises(SyntaxError):
        i.parse_label(' \t \t')


def test_parse_label_returns_label_without_terminal():
    """Test that parse_label returns the label without the terminal char."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    label, _ = i.parse_label(' \t \t \n')
    assert label == ' \t \t '


def test_parse_label_can_parse_terminal_as_label():
    """Test that parse_label accepts just a terminal as a valid label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    label, _ = i.parse_label('\n')
    assert label == ''


def test_parse_label_moves_pointer_to_after_label():
    """Test that parse_label moves the pointer to after the label terminal."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('')
    _, delta = i.parse_label('\t\t\n  \t')
    assert delta == 3


def test_exec_manipulate_stack_raises_error_for_invalid_command():
    """Test exec_manipulate_stack raises a SyntaxError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    with pytest.raises(SyntaxError):
        i.exec_manipulate_stack('\t\t', [], [0])


def test_exec_manipulate_stack_can_push_number_onto_the_stack():
    """Test that exec_manipulate_stack can push a new value onto the stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  \n')
    stack = []
    i.exec_manipulate_stack('  \n', stack, [0])
    assert stack == [0]


def test_exec_manipulate_stack_raises_error_duplicate_value_outside_stack():
    """Test exec_manipulate_stack raises an IndexError for index out of stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t  \t \n')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack('\t  \t \n', [0], [0])


def test_exec_manipulate_stack_raises_error_duplicate_value_at_neg_index():
    """Test exec_manipulate_stack raises an IndexError for negative index."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t \t\t\n')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack('\t \t\t\n', [0], [0])


@pytest.mark.parametrize('num', [x for x in range(0, 5)])
def test_exec_manipulate_stack_can_duplicate_nth_value_from_top_of_stack(num):
    """Test that exec_manipulate_stack can duplicate nth value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ' + num_to_space(num))
    stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack('\t ' + num_to_space(num), stack, [0])
    assert stack == [0, 1, 2, 3, 4, 4 - num]


@pytest.mark.parametrize('num', [x for x in range(-5, 0)])
def test_exec_manipulate_stack_discards_all_but_top_for_neg_num(num):
    """Test that all but top value is discarded for a negative n value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n' + num_to_space(num))
    stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack('\t\n' + num_to_space(num), stack, [0])
    assert stack == [4]


@pytest.mark.parametrize('num', [x for x in range(5, 10)])
def test_exec_manipulate_stack_discards_all_but_top_for_large_num(num):
    """Test all but top value is discarded for n value larger than stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n' + num_to_space(num))
    stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack('\t\n' + num_to_space(num), stack, [0])
    assert stack == [4]


@pytest.mark.parametrize('num', [x for x in range(0, 5)])
def test_exec_manipulate_stack_discards_top_n_values_below_top(num):
    """Test that the top n values below the top are discarded."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n' + num_to_space(num))
    stack = [0, 1, 2, 3, 4]
    i.exec_manipulate_stack('\t\n' + num_to_space(num), stack, [0])
    assert stack == [0, 1, 2, 3, 4][:-(num + 1)] + [4]


def test_exec_manipulate_stack_raises_error_duplicate_value_in_empty_stack():
    """Test exec_manipulate_stack raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n ')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack('\n ', [], [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(1, 5)])
def test_exec_manipulate_stack_can_duplicate_the_top_value_on_the_stack(stack):
    """Test that manipulate stack can duplicate the top stack value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n ')
    test_stack = stack[:]
    i.exec_manipulate_stack('\n ', test_stack, [0])
    assert test_stack == stack + stack[-1:]


def test_exec_manipulate_stack_raises_error_swap_values_in_empty_stack():
    """Test exec_manipulate_stack raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\t')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack('\n\t', [], [0])


def test_exec_manipulate_stack_raises_error_swap_values_in_one_value_stack():
    """Test exec_manipulate_stack raises an IndexError for one value stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\t')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack('\n\t', [0], [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(2, 6)])
def test_exec_manipulate_stack_can_swap_the_top_values_on_the_stack(stack):
    """Test that manipulate stack can swap the top stack values."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\t')
    test_stack = stack[:]
    i.exec_manipulate_stack('\n\t', test_stack, [0])
    stack[-1], stack[-2] = stack[-2], stack[-1]
    assert test_stack == stack


def test_exec_manipulate_stack_raises_error_discard_top_value_in_empty_stack():
    """Test exec_manipulate_stack raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n')
    with pytest.raises(IndexError):
        i.exec_manipulate_stack('\n\n', [], [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(1, 5)])
def test_exec_manipulate_stack_can_discard_the_top_value_on_the_stack(stack):
    """Test that manipulate stack can discard the top stack value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n')
    test_stack = stack[:]
    i.exec_manipulate_stack('\n\n', test_stack, [0])
    assert test_stack == stack[:-1]


def test_exec_arithmetic_raises_error_for_invalid_command():
    """Test exec_arithmetic raises a SyntaxError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    with pytest.raises(SyntaxError):
        i.exec_arithmetic(' ', [1, 2], [0])


def test_exec_arithmetic_raises_error_sum_values_from_empty_stack():
    """Test exec_arithmetic raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    with pytest.raises(IndexError):
        i.exec_arithmetic('  ', [], [0])


def test_exec_arithmetic_raises_error_sum_values_from_one_value_stack():
    """Test exec_arithmetic raises an IndexError for one value stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    with pytest.raises(IndexError):
        i.exec_arithmetic('  ', [0], [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_sum_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the sum of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    test_stack = stack[:]
    i.exec_arithmetic('  ', test_stack, [0])
    sum_stack = stack[:-2]
    sum_stack.append(stack[-2] + stack[-1])
    assert test_stack == sum_stack


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_diff_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the diff of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t')
    test_stack = stack[:]
    i.exec_arithmetic(' \t', test_stack, [0])
    diff_stack = stack[:-2]
    diff_stack.append(stack[-2] - stack[-1])
    assert test_stack == diff_stack


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_prod_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the prod of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \n')
    test_stack = stack[:]
    i.exec_arithmetic(' \n', test_stack, [0])
    prod_stack = stack[:-2]
    prod_stack.append(stack[-2] * stack[-1])
    assert test_stack == prod_stack


def test_exec_arithmetic_throws_error_for_division_by_zero():
    """Test that if top of stack is zero, division raises ZeroDivisionError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ')
    with pytest.raises(ZeroDivisionError):
        i.exec_arithmetic('\t ', [1, 0], [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_quot_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the quot of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ')
    test_stack = stack[:]
    i.exec_arithmetic('\t ', test_stack, [0])
    quot_stack = stack[:-2]
    quot_stack.append(stack[-2] // stack[-1])
    assert test_stack == quot_stack


def test_exec_arithmetic_throws_error_for_modulo_by_zero():
    """Test that if top of stack is zero, modulo raises ZeroDivisionError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    with pytest.raises(ZeroDivisionError):
        i.exec_arithmetic('\t\t', [1, 0], [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_arithmetic_pushes_mod_of_top_values_on_the_stack(stack):
    """Test that arithmetic pushes the mod of top two values in stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    test_stack = stack[:]
    i.exec_arithmetic('\t\t', test_stack, [0])
    mod_stack = stack[:-2]
    mod_stack.append(stack[-2] % stack[-1])
    assert test_stack == mod_stack


@pytest.mark.parametrize('stack', [[1, 2], [1, -2], [-1, 2]])
def test_exec_arithmetic_mod_matches_sign_of_top_stack_value(stack):
    """Test that sign of the mod matches sign of the top number on stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    test_stack = stack[:]
    i.exec_arithmetic('\t\t', test_stack, [0])
    if stack[-1] > 0:
        assert test_stack[-1] > 0
    else:
        assert test_stack[-1] < 0


def test_exec_heap_access_raises_error_for_invalid_command():
    """Test exec_heap_access raises a SyntaxError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n')
    with pytest.raises(SyntaxError):
        i.exec_heap_access('\n', [1, 2], {}, [0])


def test_exec_heap_access_raises_error_popping_from_empty_stack():
    """Test exec_heap_access raises an IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    with pytest.raises(IndexError):
        i.exec_heap_access(' ', [], {}, [0])


def test_exec_heap_access_raises_error_popping_from_one_item_stack_storing():
    """Test exec_heap_access raises an IndexError for one item stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    with pytest.raises(IndexError):
        i.exec_heap_access(' ', [0], {}, [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_heap_access_stores_values_into_heap_from_stack(stack):
    """Test that exec_heap_access can move values from the heap from stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    test_stack = stack[:]
    test_heap = {}
    i.exec_heap_access(' ', test_stack, test_heap, [0])
    b, a = stack[-2:]
    assert test_heap[b] == a


def test_exec_heap_access_invalid_heap_address_raises_error():
    """Test that accessing an invalid heap access raises a NameError."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t')
    with pytest.raises(NameError):
        i.exec_heap_access('\t', [0], {}, [0])


@pytest.mark.parametrize('heap', [{x: x**2 for x in range(y)} for y in range(3, 7)])
def test_exec_heap_access_stores_values_into_stack_from_heap(heap):
    """Test that exec_heap_access can move values from the stack from heap."""
    from esolang_whitespace import SpaceInterpreter
    from random import choice
    i = SpaceInterpreter('\t')
    address = choice(list(heap))
    test_stack = [address]
    i.exec_heap_access('\t', test_stack, heap, [0])
    assert test_stack[-1] == heap[address]


def test_exec_input_output_raises_error_for_invalid_command():
    """Test exec_input_output raises a SyntaxError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n')
    with pytest.raises(SyntaxError):
        i.exec_input_output('\n', '', [], {}, [0])


def test_exec_input_output_raises_error_for_output_char_from_empty_stack():
    """Test exec_input_output raises an IndexError for output from empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    with pytest.raises(IndexError):
        i.exec_input_output('  ', '', [], {}, [0])


@pytest.mark.parametrize('stack', [[x + 33 for x in range(y)] for y in range(1, 94, 5)])
def test_exec_input_output_can_output_top_of_stack_as_character(stack):
    """Test that exec_inout_output can output top stack number as character."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  ')
    test_stack = stack[:]
    _, output, _ = i.exec_input_output('  ', '', test_stack, {}, [0])
    assert output == chr(stack[-1])


def test_exec_input_output_raises_error_for_output_num_from_empty_stack():
    """Test exec_input_output raises an IndexError for output from empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t')
    with pytest.raises(IndexError):
        i.exec_input_output(' \t', '', [], {}, [0])


@pytest.mark.parametrize('stack', [[x for x in range(y)] for y in range(3, 7)])
def test_exec_input_output_can_output_top_of_stack_as_number(stack):
    """Test that exec_inout_output can output top stack number."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t')
    test_stack = stack[:]
    _, output, _ = i.exec_input_output(' \t', '', test_stack, {}, [0])
    assert output == str(stack[-1])


def test_exec_input_output_raises_error_when_reading_char_from_empty_input():
    """Test that exec_inout_output raises IOError reading from empty input."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ')
    with pytest.raises(IOError):
        i.exec_input_output('\t ', '', [], {}, [0])


def test_exec_input_output_raises_error_when_reading_char_for_empty_stack():
    """Test that exec_inout_output raises IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ', 'Hello')
    with pytest.raises(IndexError):
        i.exec_input_output('\t ', 'Hello', [], {}, [0])


@pytest.mark.parametrize('inp', [''.join([chr(x + 33) for x in range(y, 0, -1)])
                                 for y in range(1, 94, 5)])
def test_exec_input_output_stores_char_from_input_as_ascii_in_heap(inp):
    """Test that the character from input is stored in heap as its ASCII value."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t ', inp)
    heap = {}
    i.exec_input_output('\t ', inp, [0], heap, [0])
    assert heap[0] == ord(inp[0])


def test_exec_input_output_raises_error_when_reading_num_from_empty_input():
    """Test that exec_inout_output raises IOError reading from empty input."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t')
    with pytest.raises(IOError):
        i.exec_input_output('\t\t', '', [], {}, [0])


def test_exec_input_output_raises_error_when_reading_num_for_empty_stack():
    """Test that exec_inout_output raises IndexError for empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t', '1241\n')
    with pytest.raises(IndexError):
        i.exec_input_output('\t\t', '1241\n', [], {}, [0])


def test_exec_input_output_raises_error_when_reading_non_number_as_num():
    """Test that exec_inout_output raises ValueError for reading char as num."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t', 'Hello\n')
    with pytest.raises(ValueError):
        i.exec_input_output('\t\t', 'Hello\n', [0], {}, [0])


def test_exec_input_output_raises_error_when_reading_terminal_as_num():
    """Test that exec_inout_output raises ValueError for reading terminal as num."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t', '\n')
    with pytest.raises(ValueError):
        i.exec_input_output('\t\t', '\n', [0], {}, [0])


def test_exec_input_output_raises_error_when_reading_num_with_no_terminal():
    """Test exec_inout_output raises SyntaxError for reading num with no terminal."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t', '1234')
    with pytest.raises(SyntaxError):
        i.exec_input_output('\t\t', '1234', [0], {}, [0])


@pytest.mark.parametrize('inp', [(''.join([str(x) for x in range(y, 0, -1)]) + '\n')
                                 for y in range(3, 7)])
def test_exec_input_output_stores_num_from_input_as_int_in_heap(inp):
    """Test that the number from input is stored in heap as int."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t', inp)
    heap = {}
    i.exec_input_output('\t\t', inp, [0], heap, [0])
    assert heap[0] == int(inp)


def test_exec_flow_control_raises_error_for_invalid_command():
    """Test exec_flow_control raises a SyntaxError for an invalid command."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' ')
    with pytest.raises(SyntaxError):
        i.exec_flow_control(' ', {}, [], [0])


def test_exec_flow_control_marking_with_duplicate_label_raises_error():
    """Test exec_flow_control raises a NameError for a duplicate label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  \t\n')
    i.labels = {'\t': 0}
    with pytest.raises(SyntaxError):
        i.exec_flow_control('  \t\n', {'\t': 0}, [], [0])


def test_exec_flow_control_can_mark_current_location_with_label():
    """Test exec_flow_control marks current position with a label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('  \t\n\t\n  ')
    labels = {}
    i.exec_flow_control('  \t\n\t\n  ', labels, [], [0])
    assert labels == {'\t': 4}


def test_exec_flow_control_calling_subroutine_with_bad_label_raises_error():
    """Test exec_flow_control raises a NameError for a undefined label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t\t\n')
    with pytest.raises(NameError):
        i.exec_flow_control(' \t\t\n', {}, [], [0])


def test_exec_flow_control_moves_pointer_to_labeled_suroutine():
    """Test exec_flow_control moves pointer to subroutine at the label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t\t\n\t\n  ')
    p, _ = i.exec_flow_control(' \t\t\n\t\n  ', {'\t': 9}, [], [0])
    assert p == 9


def test_exec_flow_control_adds_level_to_call_stack_keeping_prev_position():
    """Test exec_flow_control adds level to call-stack on top of prev position."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \t\t\n\t\n  ')
    call_stack = [0]
    p, _ = i.exec_flow_control(' \t\t\n\t\n  ', {'\t': 9}, [], call_stack)
    assert len(call_stack) == 2
    assert call_stack[0] == 4
    assert p == 9


def test_exec_flow_control_jump_unconditionally_with_bad_label_raises_error():
    """Test exec_flow_control raises a NameError for a undefined label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \n\t\n')
    with pytest.raises(NameError):
        i.exec_flow_control(' \n\t\n', {}, [], [0])


def test_exec_flow_control_jumps_pointer_unconditionally_to_label():
    """Test exec_flow_control jumps pointer unconditionally to the label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \n\t\n\t\n  ')
    p, _ = i.exec_flow_control(' \n\t\n\t\n  ', {'\t': 9}, [], [0])
    assert p == 9


def test_exec_flow_control_jumps_current_pointer_unconditionally():
    """Test exec_flow_control does not add to call stack when jumping pointer."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter(' \n\t\n\t\n  ')
    call_stack = [0]
    i.exec_flow_control(' \n\t\n\t\n  ', {'\t': 9}, [], call_stack)
    assert len(call_stack) == 1


def test_exec_flow_control_jump_when_zero_with_bad_label_raises_error():
    """Test exec_flow_control raises a NameError for a undefined label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t \t\n')
    with pytest.raises(NameError):
        i.exec_flow_control('\t \t\n', {}, [0], [0])


def test_exec_flow_control_jump_when_zero_empty_stack_raises_error():
    """Test exec_flow_control jump raises IndexError for an empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t \t\n\t\n  ')
    with pytest.raises(IndexError):
        i.exec_flow_control('\t \t\n\t\n  ', {'\t': 9}, [], [0])


def test_exec_flow_control_jump_when_zero_moves_pointer_when_popping_zero():
    """Test exec_flow_control jumps pointer to the label when stack top is zero."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t \t\n\t\n  ')
    p, _ = i.exec_flow_control('\t \t\n\t\n  ', {'\t': 9}, [0], [0])
    assert p == 9


def test_exec_flow_control_jumps_current_pointer_when_zero():
    """Test exec_flow_control does not add to call stack when jumping pointer."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t \t\n\t\n  ')
    call_stack = [0]
    i.exec_flow_control('\t \t\n\t\n  ', {'\t': 9}, [0], call_stack)
    assert len(call_stack) == 1


def test_exec_flow_control_jump_when_zero_does_not_move_pointer_for_non_zero():
    """Test exec_flow_control does not jump pointer when stack top is not zero."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t \t\n\t\n  ')
    p, _ = i.exec_flow_control('\t \t\n\t\n  ', {'\t': 9}, [5], [0])
    assert p == 4


def test_exec_flow_control_jump_when_neg_with_bad_label_raises_error():
    """Test exec_flow_control raises a NameError for a undefined label."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t\t\n')
    with pytest.raises(NameError):
        i.exec_flow_control('\t\t\t\n', {}, [-5], [0])


def test_exec_flow_control_jump_when_neg_empty_stack_raises_error():
    """Test exec_flow_control jump raises IndexError for an empty stack."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t\t\n\t\n  ')
    with pytest.raises(IndexError):
        i.exec_flow_control('\t\t\t\n\t\n  ', {'\t': 9}, [], [0])


def test_exec_flow_control_jump_when_neg_moves_pointer_when_popping_neg():
    """Test exec_flow_control jumps pointer to the label when stack top is neg."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t\t\n\t\n  ')
    p, _ = i.exec_flow_control('\t\t\t\n\t\n  ', {'\t': 9}, [-5], [0])
    assert p == 9


def test_exec_flow_control_jumps_current_pointer_when_neg():
    """Test exec_flow_control does not add to call stack when jumping pointer."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t\t\n\t\n  ')
    call_stack = [0]
    i.exec_flow_control('\t\t\t\n\t\n  ', {'\t': 9}, [-5], call_stack)
    assert len(call_stack) == 1


def test_exec_flow_control_jump_when_neg_does_not_move_pointer_for_pos_num():
    """Test exec_flow_control does not jump pointer when stack top is pos."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t\t\n\t\n  ')
    p, _ = i.exec_flow_control('\t\t\t\n\t\n  ', {'\t': 9}, [5], [0])
    assert p == 4


def test_exec_flow_control_jump_when_neg_does_not_move_pointer_for_zero():
    """Test exec_flow_control does not jump pointer when stack top is zero."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\t\t\n\t\n  ')
    p, _ = i.exec_flow_control('\t\t\t\n\t\n  ', {'\t': 9}, [0], [0])
    assert p == 4


def test_exec_flow_control_exit_command_from_subroutine_returns_to_call_position():
    """Test exec_flow_control sub exit returns control to where it was called."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n')
    call_stack = [8, 0]
    i.exec_flow_control('\t\n', {}, [], call_stack)
    assert call_stack[-1] == 8
    assert len(call_stack) == 1


def test_exec_flow_control_exit_command_from_subroutine_does_not_exit_program():
    """Test exec_flow_control subroutine exit does not exit program."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n')
    _, exit = i.exec_flow_control('\t\n', {}, [], [0])
    assert exit is False


def test_exec_flow_control_exit_command_from_subroutine_does_nothing_not_in_sub():
    """Test exec_flow_control sub exit does nothing if not in subroutine."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\t\n')
    call_stack = [0]
    i.exec_flow_control('\t\n', {}, [], call_stack)
    assert call_stack[-1] == 2
    assert len(call_stack) == 1


def test_exec_flow_control_exit_command_ends_program():
    """Test that execute_flow_control can end the program."""
    from esolang_whitespace import SpaceInterpreter
    i = SpaceInterpreter('\n\n')
    _, exit = i.exec_flow_control('\n\n', {}, [], [0])
    assert exit is True
