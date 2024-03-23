#!/usr/bin/python3
"""a method that calculates the fewest number of operations
   needed to result in exactly n
"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
    to obtain n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
    If n is impossible to achieve, returns 0
    """
    if n <= 1:
        return 0

    opertns = 0
    holder = 0
    prsnt = 1

    while prsnt < n:
        if n % prsnt == 0:
            holder = prsnt
            opertns = opertns + 1

        prsnt = prsnt + holder
        opertns = opertns + 1
    return opertns
