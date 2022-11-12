import random


def get_unique_list_numbers() -> list[int]:
    '''
    This is a function that returns a list of 15 elements filled
    with random and unique integers from -10 to 10
    :return:
    list
    '''

    list_ = list()
    while len(set(list_)) < 15:
        list_.append(random.randint(-10, 10))
    return list(set(list_))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))