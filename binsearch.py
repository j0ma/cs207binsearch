def binary_search(da_array: list, needle, left:int=0, right:int=-1) -> int:
    """
    An algorithm that operates in O(lg(n)) to search for an element
    in an array sorted in ascending order.
    
    Parameters
    ----------
    da_array : list
        a list of "comparable"items sorted in non-descending order
    needle: an item to find in the array; it may or may not
        be in the array
    left: int, optional
        the left index in the array to search from. Default 0
    right: int, optional    
        the right index in the array to search to. Default is -1
        in which case we will use the end of the array `len(da_array) - 1`
        
    Returns
    -------
    index: int
        an integer representing the index of `needle` if found, and -1
        otherwise
        
    Notes
    -----
    PRE: 
        - `da_array` is sorted in non-decreasing order (thus items in
        - `da_array` must be comparable: implement < and ==)
        - `left` must be at least 0
        - `right` must be at least 0, at most len(`da_array`) - 1
    POST: 
        - `da_array` is not changed by this function (immutable)
        - returns `index`=-1 if `needle` is not in `da_array`
        - returns an int `index ` in [0:len(da_array)] if
          `index` is in `da_array`
    INVARIANTS:
        - If `needle` in `da_array`, needle in `da_array[rangemin:rangemax]`
          is a loop invariant in the while loop below.
          
    Examples
    --------
    >>> input = list(range(10))
    >>> binary_search(input, 5) # `da_array` contains needle
    5
    >>> binary_search(input, 4.5) # needle not in `da_array`
    -1
    >>> import numpy as np
    >>> binary_search([1,2,np.inf], np.inf) # np.inf is a valid needle
    2
    >>> binary_search(input, 2, 1,3) # subarray used, contains needle
    2
    >>> binary_search(input, 5, 1,3) # subarray used, doesn't contain needle
    -1
    >>> binary_search(input, 2, 2, 2) # rangemin=rangemax; correct position
    2
    >>> binary_search(input, 5, 2, 2) # rangemin=rangemax; incorrect position
    -1

    NOTE: In the interest of speed, the code does not check 
    that ALL values in the input array are not nan, but simply 
    tests `needle` and the midpoint element. Therefore, there are 
    cases where a nan will not break the code.

    >>> binary_search([1,2, 3, np.nan], 3) # this doesn't break
    2

    >>> from pytest import raises
    >>> binary_search([1,2, np.nan, 3], 3)
    Traceback (most recent call last):
    ...
    AssertionError: Error: elements of array should never be NaN

    """

    # import library for handling np.nan
    import numpy as np

    # check precondition that `needle` is not nan
    assert not np.isnan(needle),\
            "Error: `needle` must be comparable"

    assert left >= 0, '`Left` must be at least 0'

    if left==0:
        rangemin = 0
    else:
        rangemin = left
    if right==-1:
        rangemax=len(da_array) - 1
    else:
        rangemax=right
    while True:
        "needle in da_array => needle in da_array[rangemin:rangemax]"   
        if rangemin > rangemax:
            index = -1
            return index

        #If rangemin and rangemax are both very high we do not want overflow,
        #so get the midpoint like this:
        midpoint = rangemin + (rangemax - rangemin)//2

        # the midpoint element should never be np.nan
        assert not np.isnan(da_array[midpoint]),\
                'Error: elements of array should never be NaN'

        if da_array[midpoint] > needle: #lower part
            rangemax = midpoint - 1
        elif da_array[midpoint] < needle:
            rangemin = midpoint + 1
        else:
            index = midpoint
            return index