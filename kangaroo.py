"""
    @file kangaroo.py
    @brief There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive
     infinity). The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump. The
     second kangaroo starts at locationx2 and moves at a rate of v2 meters per jump. Given the starting
     locations and movement rates for each kangaroo, can you determine if they'll ever land at the same
     location at the same time?
"""


def kangaroo(x1, v1, x2, v2):
    # smart formula
    if v2 >= v1:
        print('NO')
    else:
        if (x2-x1) % (v1-v2) == 0:
            print('YES')
        else:
            print('NO')

    # brute force
    # t = 0
    # make the stopping condition some ratio, when we know there's no way first kangaroo can catch up
    # if v1 < v2:
    #     return False
    # # when the
    # while t < 100000:  # however, there's no limit on time in challenge statement
    #     if x1 + v1 * t == x2 + v2 * t:
    #         return True
    #     t += 1
    # return False


# def kangaroo2(x1, v1, x2, v2):
# doesn't work
# x = (v2/v1)*(x2-x1)
# if x - round(x) == 0:
#     return True
# else:
#     return False
# not correct
# if abs(x1 - x2) % (v2 / v1) == 0:
#     return True
# else:
#     return False


kangaroo(0, 3, 4, 2)  # True
kangaroo(0, 2, 5, 3)  # False
# print()
# print(kangaroo2(0, 3, 4, 2))  # True
# print(kangaroo2(0, 2, 5, 3))  # False
