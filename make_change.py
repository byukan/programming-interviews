"""Use dynamic programming to write a program to make change using as few coins as possible. Suppose that you've got
an infinite supply of coins in several denominations. Suppose further that an integer from 1 to 99 cents
represents the amount you must represent with coins. Suppose that the coin denominations are flexible, but always
include a coin worth one cent. 1a. Show an equation relating the best value at stage "m" to a maximization over
earlier stages. 1b. Write a python program to solve the recursion. """


def make_change(denominations_list=[], amount=0):
    """
    Given a list of currency and the target value, return the minimum number of currency and a list of values.
    Dynamic programming (DP) is an efficient solution.
    make change using as few coins as possible
    :param denominations_list:
    :param amount: integer from 1 to 99 representing cents
    :return: min number of coins
    """
    # equation relating best value at stage "m": C(p) = min_i{C(p-vi)} + 1

    # create memo of minimum coins required at each amount
    C = [0] * (amount+1) if amount > 0 else [0]
    # print(C)

    # for each target amount we loop through the denominations
    for i in range(1, amount+1):
        t = []
        for x in denominations_list:
            if i - x >= 0:
                # print("i, x:", i, x)
                t.append(C[i-x])
        #         print(C[i-x])
        # print(t)
        C[i] = min(t) + 1
        # print(C[1])
    return C[amount]


denominations = [1, 5, 10, 25]
amt = 99
print(make_change(denominations, amt))
