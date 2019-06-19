# FIFO queue
queue = []


def queue_add(x):
    return queue.append(x)


def queue_pop():
    return queue.pop(0)


while True:
    action = input('add or pop')

    if action == 'add':
        add_var = input('what to add? x: ')
        queue_add(add_var)
    elif action == 'pop':
        if len(queue) > 0:
            print(queue_pop())
        else:
            print('Empty queue')
    else:
        print('Wrong action syntax')

    print(queue)
