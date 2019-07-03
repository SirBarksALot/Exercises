# There are N Mice and N holes are placed in a straight line.
# Each hole can accommodate only 1 mouse.
# A mouse can stay at his position,
# move one step right from x to x + 1,
# or move one step left from x to x -1.
# Any of these moves consumes 1 minute.
# Assign mice to holes so that the time when the last mouse gets
# inside a hole is minimized.


mices = [-10, -79, -79, 67, 93, -85, -28, -94]
holes = [-2, 9, 69, 25, -31, 23, 50, 78]
mices.sort()
holes.sort()


def find_nearest_hole(mice_pos, hole_pos):
    steps = abs(mice_pos - hole_pos)
    return steps


def assign_function(mices_arr, holes_arr):
    output = 0
    for i in range(len(mices_arr)):
        minutes = find_nearest_hole(mices_arr[i], holes_arr[i])
        if minutes > output:
            output = minutes

    return output


print(assign_function(mices, holes))
