def ft_filter(func, object):
    if func == None:
        return (obj for obj in object)
    return_list = (obj for obj in object if func(obj))
    return return_list
