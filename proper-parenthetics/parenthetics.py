"""Interview Challenge: Proper Parenthetics."""


def proper_parenthetics(parens):
    """Determine if the given string has properly pared parentheses.

    Returns: int, value that corresponds to the following:
             1 - string is 'open' (not all open parens are closed)
             0 - string is 'balanced' (equal number of open and closed parens)
            -1 - string is 'broken' (closing parens before one that opens)
    """
    parens_stack = []
    for ch in parens:
        if ch == '(':
            parens_stack.append(ch)
        if ch == ')':
            try:
                parens_stack.pop()
            except IndexError:
                return -1
    return 1 if parens_stack else 0
