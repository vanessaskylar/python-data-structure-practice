def last_element(list):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # if len(list) == 0:
    #     return None
    
    # return list[-1]


    if list:
        return list[-1]
    # we don't need to do anything else; functions
    # return None by default