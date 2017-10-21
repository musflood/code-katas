"""Kata: Social Golfer Problem Validator.

#1 Best Practices Solution by damjan
def valid(a):
    d = {}
    day_length = len(a[0])
    group_size = len(a[0][0])
    golfers = {g for p in a[0] for g in p}

    for day in a:
        if len(day) != day_length: return False
        for group in day:
            if len(group) != group_size: return False
            for player in group:
                if player not in golfers: return False
                if player not in d:
                    d[player] = set(group)
                else:
                    if len(d[player] & set(group)) > 1: return False
                    else: d[player].add(group)
    return True
"""


def valid(a):
    """Validate a solution for the social golfers problem.

    The social golfers problem is as follows:
        "A group of N golfers wants to play in groups of G players
        for D days in such a way that no golfer plays more than
        once with any other golfer."

    The provided solution must be in the form of a list of lists
    of strings. A list of days with lists of groups written as
    strings, with golfers represented by a single character.
    """
    # Empty days
    if not a:
        return True

    # All days are equal size
    day_size = len(a[0])
    for d in a:
        if len(d) != day_size:
            return False

    # Empty groups
    if not day_size:
        return True

    # All groups are equal size
    group_size = len(a[0][0])
    groups = []
    for d in a:
        groups.extend(d)
    golfers = set()
    days = ['' for _ in a]
    for i, group in enumerate(groups):
        if len(group) != group_size:
            return False
        golfers = golfers.union(group)
        days[int(i / day_size)] += group

    # Each golfer plays exactly once
    for g in golfers:
        for d in days:
            if d.count(g) != 1:
                return False

    # Plays with others once
    partners = {g: [] for g in golfers}
    for group in groups:
        for g in group:
            others = group.replace(g, '')
            for o in others:
                if o in partners[g]:
                    return False
                partners[g].append(o)

    return True
