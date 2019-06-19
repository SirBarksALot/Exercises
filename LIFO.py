# LIFO stack
stack = []


def stack_add(x):
    return stack.append(x)


def stack_pop():
    return stack.pop()


while True:
    action = input('add or pop')

    if action == 'add':
        add_var = input('what to add? x: ')
        stack_add(add_var)
    elif action == 'pop':
        if len(stack) > 0:
            print(stack_pop())
        else:
            print('Empty stack')
    else:
        print('Wrong action syntax')

    print(stack)
