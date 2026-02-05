'''
doctstring = documentation that expalins purpose of file

The purpose of this file is to help students practice writing functions and using doctests.
'''





def factorial(n):
    '''
    Return the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n

    HINT:
    Use a for loop from 1 to n.
    On each iteration, multiply the current result by the current iteration number.

    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    >>> factorial(100)
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    '''
    accumulator = 1
    for i in range (1, n+1):
        accumulator *= i
    return accumulator

"""
def largest(xs):
    '''
    Return the largest element in a list.

    HINT:
    Use an integer accumulator pattern.

    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''


def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.

    HINT:
    Use a list accumulator pattern.

    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''
    """
