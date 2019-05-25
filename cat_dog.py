# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(stringer):
    cat_counter = stringer.count('cat')
    dog_counter = stringer.count('dog')

    print(cat_counter)
    print(dog_counter)

    if dog_counter != cat_counter:
        return False

    return True


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
