# Implement pow(A, B) % C.
# In other words, given A, B and C, find (A^B)%C.

A = 450
B = 768
C = 517


def fct(a, b, c):
    output = 1
    while b > 0:
        output = output * a
        b -= 1

    return output % c


print(fct(A, B, C))
output2 = pow(A, B) % C
print(output2)
