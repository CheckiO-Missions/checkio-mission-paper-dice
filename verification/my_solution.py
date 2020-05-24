from numpy import array, rot90

PATTERN = [
    # O
    # OOOO
    # O
    [[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0)], 4, 0, [(0, 5), (1, 3)]],

    # O
    # OOOO
    #  O
    [[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)], 4, 1, [(0, 5), (1, 3)]],

    # O
    # OOOO
    #   O
    [[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)], 4, 1, [(0, 5), (1, 3)]],

    # O
    # OOOO
    #    O
    [[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)], 2, 1, [(0, 5), (1, 3)]],

    #  O
    # OOOO
    #  O
    [[(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)], 4, 0, [(0, 5), (1, 3)]],

    #  O
    # OOOO
    #   O
    [[(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)], 2, 1, [(0, 5), (1, 3)]],

    # O
    # OOO
    #   OO
    [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)], 4, 1, [(0, 4), (1, 3)]],

    #  O
    # OOO
    #   OO
    [[(0, 1), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)], 4, 1, [(0, 4), (1, 3)]],

    #   O
    # OOO
    #   OO
    [[(0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)], 4, 1, [(0, 4), (1, 3)]],

    # OOO
    #   OOO
    [[(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)], 2, 1, [(0, 2), (1, 4)]],

    # OO
    #  OO
    #   OO
    [[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)], 2, 1, [(0, 3), (1, 4)]],
]


def paper_dice(paper):
    for pt, dir, rev, nums in PATTERN:
        for rv in range(rev + 1):
            np_ary = array(list(map(lambda r: list(r[::(1, -1)[rv]]), paper)))

            for rot in range(dir):
                co, num = [], []

                for r, row in enumerate(rot90(np_ary, rot)):
                    for c, cell in enumerate(row):
                        if cell != ' ':
                            co.append((r, c))
                            num.append(int(cell))

                if len({(p[0] - c[0], p[1] - c[1]) for p, c in zip(pt, co)}) == 1:
                    return all({num[a] + num[b] == 7 for a, b in nums})

    return False
