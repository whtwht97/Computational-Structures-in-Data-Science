######################
# Required Questions #
######################

def harmonic_mean(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic_mean(2, 6)
    3.0
    >>> harmonic_mean(1, 1)
    1.0
    >>> harmonic_mean(2.5, 7.5)
    3.75
    >>> harmonic_mean(4, 12)
    6.0
    """
    return 2/(1/x+1/y)


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a*a+b*b,a*a+c*c,b*b+c*c)


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for i in lst:
        if i != 0:
            return i


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    if n in lst:
        return True
    else:
        return False


def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    pred,curr=1,0
    k=0
    while k<n:
        pred,curr=curr,pred+curr
        k = k + 1
    return curr


def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    return [[x[0][0]+y[0][0],x[0][1]+y[0][1]], [x[1][0]+y[1][0],x[1][1]+y[1][1]]]



def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> def fn(x):
    ...     return x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[i, fn(i)] for i in seq if fn(i)>=lower and fn(i)<=upper]
