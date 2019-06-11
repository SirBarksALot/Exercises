# Given a list of non negative integers,
# arrange them in such a manner that they form
# the largest number possible.The result is going to be very large,
# hence return the result in the form of a string.

arr = [0, 99234, 3, 9, 997, 78, 9432]
str_arr = []

# transform array of ints into array of strings
for i in range(len(arr)):
    str_arr.append(str(arr[i]))

print(str_arr)

output_array = []


def find(array, x, ind):
    temp_array = []
    rest_array = []
    for num in array:
        if num == str(x):
            output_array.append(num)
        elif num[ind] == str(x):
            temp_array.append(num)
        else:
            rest_array.append(num)

    print(output_array)
    print(temp_array)
    print(rest_array)

    if len(temp_array) == 1:
        output_array.append(temp_array[0])
    elif len(temp_array) > 1:
        find(temp_array, x, ind+1)

    if len(rest_array) > 0:
        find(rest_array, x-1, ind)


# fct execution, arr is array,
# x is current digit to look for,
# i is an index to check
find(str_arr, 9, 0)
print(''.join(output_array))

