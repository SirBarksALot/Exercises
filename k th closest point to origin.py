points = [(-2, 4),
          (0, -2),
          (-1, 0),
          (3, 5),
          (-2, -3),
          (3, 2)]


def count_distance(tuple_var):
    output = pow((pow(tuple_var[0], 2) + pow(tuple_var[1], 2)), (1/2))
    return output


def find_kth_point(k):
    temp_array = []
    for elem in points:
        temp_array.append(count_distance(elem))

    temp_array.sort()

    return temp_array[k-1]


print(find_kth_point(2))
