def solution(A):
    # finding all dropped requests combinations
    for x1 in range(1, len(A)-2):
        for x2 in range(x1+2, len(A)-1):
            # checking sum of created subsets
            sub_set_1_sum = sum(A[:x1])
            sub_set_2_sum = sum(A[x1+1:x2])
            sub_set_3_sum = sum(A[x2+1:])
            if sub_set_1_sum == sub_set_2_sum == sub_set_3_sum:
                return True
    return False


li = [1, 3, 4, 2, 2, 2, 1, 1, 2]

print(solution(li))
