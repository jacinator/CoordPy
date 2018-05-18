# -*- coding: utf-8 -*-
"""CoordPy functions.

These functions are the intention of CoordPy. The entire package
centres around them and essentially serves them.
"""

import math

from . import decorators

@decorators.clean_coordinates
def get_distance(a, b):
    """Return the distance between the two coordinates.

    This function uses the Pythagorean Theorum to determine the length
    of the distance between the two points.

    Args:
        a (list): A tuple is also acceptable. This list will have two
            items, either ``int``s or ``float``s.
        b (list): Exactly the same requirements as ``a``. It can (and
            usually will be) a different coordinate.

    Returns:
        float: The result of this function is a float representing the
            distance between ``a`` and ``b``.
    """

    return math.sqrt(sum((
        (abs(a[0] - b[0]) ** 2),
        (abs(a[1] - b[1]) ** 2),
    )))

@decorators.clean_coordinates
def get_step(a, b, marks=1):
    """Return a coordinate set between ``a`` and ``b``.

    This function returns a coordinate point between the two provided
    coordinates. It does this be determining the angle of the path
    between the two points and getting the sine and cosine from that
    angle. The returned coordinate will be ``marks`` away from ``a``.

    It is worth noting that if the distance between the two points,
    calculated by ``get_distance`` is less than the value of ``marks``,
    a copy of ``b`` is returned.

    Args:
        a (list): A tuple is also acceptable. This list will have two
            items, either ``int``s or ``float``s.
        b (list): Exactly the same requirements as ``a``. It can (and
            usually will be) a different coordinate.
        marks (:obj:`int`, optional): One mark is the measurement
            between two adjacent coordinates. To step over a greater
            number of coordinates, increase the number of ``marks``.

    Returns:
        tuple: The returned tuple is a new coordinate set. The location
            of the coordinates is determined by ``marks`` and angle
            connecting ``a`` and ``b``.
    """

    if get_distance(a, b) <= marks:
        return b[:]
    angle = math.atan2(
        -(a[1] - b[1]),
        -(a[0] - b[0]),
    )
    return (
        (math.cos(angle) * marks) + a[0],
        (math.sin(angle) * marks) + a[1],
    )
