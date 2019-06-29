# There are given N ropes of different lengths,
# we need to connect these ropes into one rope.
# The cost to connect two ropes is equal to sum of their lengths.
# The task is to connect the ropes with minimum cost.

ropes = [4, 3, 2, 6]
print(ropes)


def connect_ropes(rope):
    sum_var = 0

    for i in range(2):
        var_1 = rope.index(min(rope))
        sum_var += rope.pop(var_1)

    rope.append(sum_var)
    if len(rope) == 1:
        return rope[0]
    else:
        return sum_var + connect_ropes(rope)


print(connect_ropes(ropes))
