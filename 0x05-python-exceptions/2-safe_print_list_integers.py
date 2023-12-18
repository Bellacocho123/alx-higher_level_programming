#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_value = 0
    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num]), end='')
            real_value = real_value + 1
        except (ValueError, TypeError):
            continue
    print()
    return real_value
