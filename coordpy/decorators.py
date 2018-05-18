# -*- coding: utf-8 -*-

import functools


class CoordinateValueError(ValueError):
    """Custom ValueError class.

    Just to distinguish this exception and make tracebacks easier, we
    will use this exception when cleaning coordinate values.
    """

    def __init__(self, value):
        message = 'Coordinate values must be convertible to floats, not {}'
        super(CoordinateValueError, self).__init__(message.format(value))


def clean_coordinate_value(value):
    """Clean the coordinate value provided to the function.

    The value being passed to the function is a coordinate value. We
    want to clean the coordinate to a float, since that is what we
    primarily use.

    Args:
        value: The value could be a str, float, or int. Any of these
            types is a coordinate value that should be translatable to
            a float.

    Returns:
        float: Return the value passed in converted to a float.

    Raises:
        CoordinateValueError: If the value can't be converted to a
            float this issue is raised.
    """

    try:
        return float(value)
    except ValueError:
        raise CoordinateValueError(value)


def clean_coordinates(function):
    @functools.wraps(function)
    def inner(a, b, *args, **kwargs):
        a = (clean_coordinate_value(a[0]), clean_coordinate_value(a[1]))
        b = (clean_coordinate_value(b[0]), clean_coordinate_value(b[1]))
        return function(a, b, *args, **kwargs)
    return inner
