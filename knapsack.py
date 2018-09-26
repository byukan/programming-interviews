"""
    @brief knapsack problem
"""


# Queen Elizabeth has a limited number of types of cakes, but unlimited supply of each
# unbounded


def max_duffel_bag_value(cake_tuples, capacity):
    """
    takes a list of cake type tuples and a weight capacity, and
    returns the maximum monetary value the duffel bag can hold
    """
    # try optimal solutions for each capacity increment, starting at 1
    # max_value = 0

    # list to hold the maximum possible value at every
    # integer capacity from 0 to weight_capacity
    # starting each index with value 0
    m = [0] * (capacity+1)
    #     for i in range(capacity+1):
    #         m[i] = 0
    #     print(m[3])

    # every integer from 0 to the input weight_capacity
    for current_capacity in range(capacity+1):

        current_max_value = 0

        for weight, value in cake_tuples:
            # #         i = 1
            if weight <= capacity:
                # find max value
                max_value_using_cake = value + m[current_capacity - weight]
                current_max_value = max(max_value_using_cake, current_max_value)

        m[current_capacity] = current_max_value

    # if weight == 1:
    #                 m[1] = max(m[1], value)
    #     #             m[1] = max_value
    #     #             print(m[1])
    #             if weight == 2:
    #                 m[2] = max(m[1]+m[1], value)
    #     #             m[2] = max_value

    #     #         if weight == capacity:
    #     #             m[capacity] = max(m[capacity], value)

    #     #         if weight == capacity - 1:
    #     #             m[capacity] = max(m[capacity], m[capacity-1]+value)

    #             if weight == 3:
    #                 m[3] = max(m[2]+m[1], value)
    #     #             print(m[2])

    #             if weight == 4:
    #                 m[4] = max()

    #     return m[capacity]
    return m[capacity-1]


cake_tuples = [(1, 160), (2, 321), (3, 15)]
capacity = 2

print(max_duffel_bag_value(cake_tuples, capacity))


# def knapsack(capacity, selections):
#     """
#
#     :param capacity:
#     :param selections:
#     :return:
#     """
#
#     # sorted list of densities
#     v = [x.density for x in selections]
#
#     index_array = np.argsort(selections)
#     # index of the densest cake
#
#
#     # for x in lizs_stash:
#     #     v.append(x.density)
#     current_weight = 0
#     my_cakes = []
#
#     while current_weight < capacity:
#         i = 0
#         p = np.where(x == i)[0][0]  # position of ith densest cake
#
#         # add one unit of the most dense cake, if it won't overflow the capacity
#         while current_weight + v[p] < capacity:
#             current_weight += v[p]
#             my_cakes.append(selections[i])
#             #         else:  # try adding one of the next densest
