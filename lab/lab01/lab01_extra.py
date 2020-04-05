"""Optional questions for Lab 1"""

# While Loops

def power_loop(a, b):
    """Compute a to the power b
    >>> power_loop(0, 0) # 0 ** 0 = 1
    1
    >>> power_loop(3, 0) # 3 ** 0 = 1
    1
    >>> power_loop(0, 3) # 0 ** 3 = 0
    0
    >>> power_loop(2, 5) # 2 ** 5 = 32
    32
    >>> power_loop(4, 9) # 4 ** 9 = 262144
    262144
    """
    "*** YOUR CODE HERE ***"



def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    def double_eights(n):
        while n>0:
            if n%10==8:
                n=n//10
            if n%10==8:
                return True
            else:
                n=n//10
        return False





# Boolean Operators

def right_triangle(a, b, c):
    """Determine whether a, b, and c can be sides of a right triangle
    >>> right_triangle(1, 1, 1)
    False
    >>> right_triangle(5, 3, 4)
    True
    >>> right_triangle(8, 10, 6)
    True
    """
    def right_triangle(a,b,c):
        if a**2+b**2==c**2  or b**2+c**2==a**2 or a**2+c**2==b**2:
            return True
        else:
            return False
