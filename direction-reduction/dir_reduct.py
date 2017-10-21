"""Kata: Directions Reduction.

#1 Best Practices Solution by Unnamed and others
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dir_reduct(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
"""


def dir_reduct(arr):
    """Collapse a set of directions to minimize movements.

    Given a list of string directions 'NORTH', 'SOUTH', 'EAST', 'WEST',
    removes directions that will cancel each other out. That is, the
    pairs ['NORTH', 'SOUTH'] or ['EAST', 'WEST'] cancel each other
    and therefore are removed from the directions. Pairs must be
    adjacent to cancel each other out.
    """
    if not arr or len(arr) == 1:
        return arr

    direct = arr[:]
    new_direct = ['start']

    while len(new_direct) != len(direct):

        if new_direct != ['start']:
            direct = new_direct[:]
        new_direct = []

        i = 0
        while i < len(direct) - 1:
            if direct[i] == 'NORTH' and direct[i + 1] != 'SOUTH':
                new_direct.append(direct[i])
            elif direct[i] == 'SOUTH' and direct[i + 1] != 'NORTH':
                new_direct.append(direct[i])
            elif direct[i] == 'EAST' and direct[i + 1] != 'WEST':
                new_direct.append(direct[i])
            elif direct[i] == 'WEST' and direct[i + 1] != 'EAST':
                new_direct.append(direct[i])
            else:
                i += 1
            i += 1
        if i == len(direct) - 1:
            new_direct.append(direct[-1])

    return new_direct
