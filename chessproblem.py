possible_moves = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (0, 3, 9),
    5: None,
    6: (0, 1, 7),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}

starting_position = 1
number_of_steps = 20


def count_combinations(start, number):
    output = 0
    if number == 0:
        output += 1
        return output

    if possible_moves.get(start) is None:
        return 'You are on a 5, cannot move anywhere!'

    for possibility in possible_moves.get(start):
        output += count_combinations(possibility, number-1)

    return output


print(count_combinations(starting_position, number_of_steps))
