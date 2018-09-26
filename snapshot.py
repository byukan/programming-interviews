# A zero-indexed array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e.
#
#     A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
#
# Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.
#
# For example, consider the following array A consisting of N = 8 elements:
#   A[0] = -1
#   A[1] =  3
#   A[2] = -4
#   A[3] =  5
#   A[4] =  1
#   A[5] = -6
#   A[6] =  2
#   A[7] =  1
#
# P = 1 is an equilibrium index of this array, because:
#
#         A[0] = −1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
#
# P = 3 is an equilibrium index of this array, because:
#
#         A[0] + A[1] + A[2] = −2 = A[4] + A[5] + A[6] + A[7]
#
# P = 7 is also an equilibrium index, because:
#
#         A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
#
# and there are no elements with indices greater than 7.
#
# P = 8 is not an equilibrium index, because it does not fulfill the condition 0 ≤ P < N.
#
# Write a function:
#
#     def solution(A)
#
# that, given a zero-indexed array A consisting of N integers, returns any of its equilibrium indices. The function should return −1 if no equilibrium index exists.
#
# For example, given array A shown above, the function may return 1, 3 or 7, as explained above.
#
# Assume that:
#
#         N is an integer within the range [0..100,000];
#         each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
#
# Complexity:
#
#         expected worst-case time complexity is O(N);
#         expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
#
# Elements of input arrays can be modified.

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# def solution(A):
#     # write your code in Python 2.7
#     """
#     expected worst-case time complexity is O(N);
#     expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
#      arguments).
#     :param A: zero-indexed array A consisting of N integers
#     :return: returns any of its equilibrium indices. The function should return −1 if no equilibrium index exists
#     """
#     for i in range(len(A)):
#         if sum(A[:i]) == sum(A[i + 1:]):
#             return i
#     return -1


# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# def solution(S, K):
#     # write your code in Python 2.7
#     """
#     :param S: non-empty string consisting of N characters representing a license key to format
#     :param K: desired length for each group of characters
#     """
#     # convert string to a list to make it a mutable type
#     # remove all dashes and convert to upper case
#     cleaned_key = list(S.replace("-", "").upper())
#     # reinsert the dashes after every K characters, staring from the last index
#     #     print(cleaned_key)
#
#     for i in range(len(cleaned_key) - K, 0, -K):
#         # insert "-" at index i
#         cleaned_key.insert(i, "-")
#
#     return "".join(cleaned_key)  #





# def main():
#     # v = [-1, 3, -4, 5, 1, -6, 2, 1]
#     # v = [1, 2, -2]
#     #
#     # print(solution(v))
#
#     s = "2-4A0r7-4k"
#     print(solution(s, 4))
#
#
# main()




def solution(x, y, T):
    if T is None:
        return 0
    size = 0
    if x < T.val:
        size += solution(x, y, T.left)
    if x <= T.val and y >= T.val:
        size += 1
    # The following if statement was my attempt at resetting the count
    # whenever we find a node outside the range, but it doesn't work
    if x > T.val or y < T.val:
        size = 0
    if B > T.x:
        size += solution(A, B, T.right)
    return size
