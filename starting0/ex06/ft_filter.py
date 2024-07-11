def ft_filter(function, iterable):
    if function:
        return [item for item in iterable if function(item)]
    else:
        return [item for item in iterable if item]

