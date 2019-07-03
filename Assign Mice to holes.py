# There are N Mice and N holes are placed in a straight line.
# Each hole can accommodate only 1 mouse.
# A mouse can stay at his position,
# move one step right from x to x + 1,
# or move one step left from x to x -1.
# Any of these moves consumes 1 minute.
# Assign mice to holes so that the time when the last mouse gets
# inside a hole is minimized.


mices = [4, -4, 2]
holes = [4, 0, 5]


def find_closest_hole(mice_pos, holes_arr):
    step_count = abs(mice_pos - holes_arr[0])
    hole_pos = 0
    for i in range(1, len(holes_arr)):
        print(step_count, abs(mice_pos-holes_arr[i]))
        if step_count > abs(mice_pos-holes_arr[i]):
            hole_pos = i
            step_count = abs(mice_pos-holes_arr[i])

    return hole_pos, step_count


print(find_closes_hole(2, holes))

#def assign_hole(mic, hol):
 #   for i in range(len(mic)):
 #       for j in range(len(hol)):
 #           if mic[i] == hol[j]:
 #               hol.pop(j)
  #          elif mic[i] > hol[]


#assign_hole(mices, holes)
