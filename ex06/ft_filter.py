def ft_filter(func, object):
    ''' Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true. '''
    if func is None:
        return (obj for obj in object)
    return_list = (obj for obj in object if func(obj))
    return return_list
