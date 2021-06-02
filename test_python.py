class Error(Exception):
    pass


class TooHigh(Error):
    def __init__(self):
        self.massage = ("This number is higher than 100")


def get_num(x):
    if x < 100:
        print("OK")
    else:
        raise print(TooHigh().massage)

get_num(99)
import math


def log_scale(list_of_nums):
    log_scale =list( map(lambda x: math.cos(x), list_of_nums))
    print("list_of_nums : ", list_of_nums)
    print("log_scale : ", str(log_scale))
    return list_of_nums, log_scale


def uneven(some_list):
    d = some_list[1:]
    print("lost number : ", d, some_list)

uneven([100, 200, 700,60,4,2,4])
log_scale([100, 200, 700,60,4,2,4])


def zip_it(fnck):
    def wrapper(list_of_nums, log_scale):
        assert len(log_scale) == len(list_of_nums)

        zipped = (list(zip(list_of_nums, log_scale)))

        print("log scale : zipped data ", zipped)

    return wrapper


@zip_it
def arge(listA, listB):
    d = some_list.copy()
    return (listA, listB)


arge([100, 200, 700], [6, 7, 3])
