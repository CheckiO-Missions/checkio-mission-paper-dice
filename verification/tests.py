"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

from random import choice, shuffle
from my_solution import paper_dice

BASE = (5, 5)
DIF = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_adj_cells(cells):
    adj_cells = set()
    for y, x in cells:
        adj_cells |= {(y + dy, x + dx) for dy, dx in DIF}
    return list(adj_cells - cells)


def check_square(faces):
    for y, x in faces:
        if {(y, x), (y, x + 1), (y + 1, x), (y + 1, x + 1)} <= faces:
            return False
    return True


def make_random_paper_dice():
    while True:
        faces = {BASE}
        for _ in range(5):
            faces.add(choice(get_adj_cells(faces)))
        if check_square(faces):
            break

    all_x = [x for _, x in faces]
    all_y = [y for y, _ in faces]
    min_y = min(all_y)
    min_x = min(all_x)
    height = max(all_y) - min_y + 1
    width = max(all_x) - min_x + 1

    paper = []
    shuffle(nums := list('123456'))
    for y in range(height):
        row = ''.join(' ' if (y + min_y, x + min_x) not in faces else nums.pop() for x in range(width))
        paper.append(' ' + row + ' ')

    empty_row = ' ' * (width + 2)
    return [empty_row] + paper + [empty_row]


def make_random_tests(num):
    random_tests = []
    right = False
    while True:
        if right and len(random_tests) == num:
            break
        paper = make_random_paper_dice()
        if answer := paper_dice(paper):
            right = True
        random_tests = random_tests[:num - 1] + [{'input': paper,
                                                  'answer': answer}]
    return random_tests


TESTS = {
    "1. Basics": [
        {
            "input": [
                '      ',
                ' 1    ',
                ' 2354 ',
                ' 6    ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '2354',
                ' 6  ',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '2354',
                '  6 ',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '2354',
                '   6',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                ' 1  ',
                '2354',
                ' 6  ',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                ' 1  ',
                '2354',
                '  6 ',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '235 ',
                '  64',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                ' 1  ',
                '235 ',
                '  64',
                '    ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   1  ',
                ' 235  ',
                '   64 ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '       ',
                ' 126   ',
                '   354 ',
                '       ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                ' 12   ',
                '  36  ',
                '   54 ',
                '      ',
            ],
            "answer": True,
        },
    ],
    "2. Rotate": [
        {
            "input": [
                '     ',
                ' 126 ',
                '  3  ',
                '  5  ',
                '  4  ',
                '     ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                '    6 ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '     ',
                '  4  ',
                '  5  ',
                '  3  ',
                ' 621 ',
                '     ',
            ],
            "answer": True,
        },
        {
            "input": [
                '     ',
                '  21 ',
                '  3  ',
                '  5  ',
                ' 64  ',
                '     ',
            ],
            "answer": True,
        },
        {
            "input": [
                '     ',
                '   1 ',
                '  32 ',
                ' 56  ',
                ' 4   ',
                '     ',
            ],
            "answer": True,
        },
    ],
    "3. Reverse": [
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                '   6  ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                '  6   ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                ' 6    ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   1  ',
                ' 4532 ',
                '  6   ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                '  532 ',
                ' 46   ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   1  ',
                '  532 ',
                ' 46   ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '  1   ',
                '  532 ',
                ' 46   ',
                '      ',
            ],
            "answer": True,
        },
        {
            "input": [
                '       ',
                '   621 ',
                ' 453   ',
                '       ',
            ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   21 ',
                '  63  ',
                ' 45   ',
                '      ',
            ],
            "answer": True,
        },
    ],
    "4. Wrong": [
        {
            "input": [
                '     ',
                ' 12  ',
                '  3  ',
                '  4  ',
                '  56 ',
                '     ',
            ],
            "answer": False,
        },
        {
            "input": [
                '      ',
                ' 12   ',
                '  34  ',
                '   56 ',
                '      ',
            ],
            "answer": False,
        },
        {
            "input": [
                '      ',
                ' 1  6 ',
                ' 2354 ',
                '      ',
            ],
            "answer": False,
        },
        {
            "input": [
                '      ',
                ' 1    ',
                ' 2    ',
                ' 6354 ',
                '      ',
            ],
            "answer": False,
        },
        {
            "input": [
                '     ',
                ' 12  ',
                '  36 ',
                '   5 ',
                '   4 ',
                '     ',
            ],
            "answer": False,
        },
        {
            "input": [
                ' 12',
                ' 3 ',
                ' 65',
                ' 4 ',
            ],
            "answer": False,
        },
    ],
    "5. Randoms": make_random_tests(20),
}
