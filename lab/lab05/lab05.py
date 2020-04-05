## Review


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a < b:
        return gcd(b, a)
    if not a % b == 0:
        return gcd(b, a % b)
    return b



# Iterative solution, if you're curious
def gcd_iter(a, b):
    """Returns the greatest common divisor of a and b, using iteration.

    >>> gcd_iter(34, 19)
    1
    >>> gcd_iter(39, 91)
    13
    >>> gcd_iter(20, 30)
    10
    >>> gcd_iter(40, 40)
    40
    """
    while a % b != 0:
        a, b = b, a % b
    return b



def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    while x>0:
        next_digit = x % 10
        x = x // 10

        if next_digit < (x % 10):
            return False
    return True


def bad_list_flattener(lst1, lst2):
    """
    Flattens both lst1 and lst2, and returns the
    concatenation of the two flattened lists. Flattening
    a list means to collapse the list into one
    dimension (like np.flatten).
    >>> girls = [['Rachel', 'Green'], ['Phoebe', 'Buffay']]
    >>> boys = [['Ross', 'Geller'], ['Chandler', 'Bing']]
    >>> bad_list_flattener(girls, boys)
    ['Rachel', 'Green', 'Phoebe', 'Buffay', 'Ross', 'Geller', 'Chandler', 'Bing']
    >>> cats = [['Persian'], ['British', 'Shorthair']]
    >>> dogs = [['Golden', 'Retriever']]
    >>> bad_list_flattener(dogs, cats)
    ['Golden', 'Retriever', 'Persian', 'British', 'Shorthair']
    """
    newlist1 = []
    newlist2 = []
    for inner_lst in lst1:
        for item in inner_lst:
            newlist1.append(item)
    for inner_lst in lst2:
        for item in inner_lst:
            newlist2.append(item)
    return newlist1 + newlist2


def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    flattened = []
    for i in lst:
        if type(i) == list:
            flattened += flatten(i)
        else:
            flattened += [i]
    return flattened


# Optional, Extra Credit.
def lab05_extra_credit():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all questions from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88-lab05
  """
  okpy_email = "whtwht3061@berkeley.edu"
  practice_result_code = "a71c7b4a5df8252f3691f019abe06131"
  return (okpy_email, practice_result_code)
 
