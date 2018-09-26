def max_with_none(a, b):
    """
    Returns the maximum of two elements.
    If one them is None, the other is returned.
    """
    if a is None:
        return b
    if b is None:
        return a
    return max(a, b)


def solution(x, y, T):
    # write your code in Python 2.7
    """
    :param A: int, lower bound of range
    :param B: int, upper bound of range
    :param T: BinarySearchTree
    :return: returns size of a largest subtree of tree T in which all the values are contained in the range [A..B].
      If there is no such subtree, the function returns 0.
    """
    if T is None:
        return 0

    left, size, min, _ = solution(x, y, T.left)
    right_ans, right_size, _, right_max = solution(x, y, T.right)

    # The size of this subtree
    cur_size = 1 + size + right_size

    # left side of subtree is T.val or the smallest element in the
    # left subtree (if it's not empty)
    if min and T.val:
        cur_min = min(T.val, min)
    elif not min:
        cur_min = T.val
    elif not T.val:
        cur_min = min

    # The right border of the subtree is T.val or the largest element in the
    # right subtree (if it's not empty)
    if min and T.val:
        cur_min = min(T.val, min)
    elif not min:
        cur_min = T.val
    elif not T.val:
        cur_min = min

    # The answer is the maximum of answer for the left and for the right
    # subtree
    cur_ans = max(left, right_ans)
    # If the current subtree is within the [x, y] range, it becomes the new answer,
    # as any subtree of this subtree is smaller than itself
    if x <= cur_min and cur_max <= y:
        cur_ans = cur_size

    return cur_ans


def main():
    tree = (15, 29, (
        25, (19, (12, (4, None, None), None), (22, None, (23, None, None))), (37, (29, None, (30, None, None)), None)))

    print(solution(15, 29, tree))


main()
