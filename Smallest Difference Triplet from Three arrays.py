# Three arrays of same size are given.
# Find a triplet such that maximum – minimum in that triplet is minimum of all the triplets.
# A triplet should be selected in a way such that it should have one number from each of the
# three given arrays.
# If there are 2 or more smallest difference triplets,
# then the one with the smallest sum of its elements should be displayed.

arry1 = [2, 5, 8]
arry2 = [7, 10, 12]
arry3 = [6, 9, 14]


def smallest_diff(arr1, arr2, arr3):
    output_diff = max(arr1[0], arr2[0], arr3[0]) - min(arr1[0], arr2[0], arr3[0])
    output_summ = arr1[0] + arr2[0] + arr3[0]
    output_items = [arr1[0], arr2[0], arr3[0]]

    for i in range(len(arr1)):
        for ii in range(len(arr2)):
            for iii in range(len(arr3)):
                maxi = max(arr1[i], arr2[ii], arr3[iii])
                mini = min(arr1[i], arr2[ii], arr3[iii])
                diff = maxi - mini
                summ = arr1[i] + arr2[ii] + arr3[iii]

                if diff < output_diff:
                    output_diff = diff
                    output_summ = summ
                    output_items = [arr1[i], arr2[ii], arr3[iii]]
                elif diff == output_diff:
                    if summ < output_summ:
                        output_diff = diff
                        output_summ = summ
                        output_items = [arr1[i], arr2[ii], arr3[iii]]

    return output_items


print(smallest_diff(arry1, arry2, arry3))
