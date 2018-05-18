# -*- coding: utf-8 -*-
"""Extensions off of the base provided in ``.coordinates``.

``coordpy.coordinates`` provides the basics of coordinate management,
but anything beyond that lives here. Functions here are modifications
of the utilities found in ``coordpy.coordinates``.
"""

from . import coordinates, decorators

@decorators.clean_coordinates
def get_all_steps(a, b, method=coordinates.get_step, **kwargs):
    """Get all the steps between two locations.

    This function will loop, generating another set of coordinates,
    until point ``b`` is reached. Meanwhile, it saves all the
    coordinates in a list and returns that list at the end.

    Args:
        a (list): A tuple is also acceptable. This list will have two
            items, either ``int``s or ``float``s.
        b (list): Exactly the same requirements as ``a``. It can (and
            usually will be) a different coordinate.
        method (:obj:`function`, optional): This is the step getter
            method. The default method for this is ``get_step``, but it
            can be substituted for ``get_int_step``.
        **kwargs: A dictionary of extra arguments that will be passed
            to the step getter method.

    Returns:
        list: The returned list is a list of tuples, each of which is a
            set of coordinates in a line between ``a`` and ``b``.
    """

    steps = [a]
    while steps[-1] != b:
        steps.append(method(steps[-1], b, **kwargs))
    return steps

@decorators.clean_coordinates
def get_int_step(a, b, marks=1):
    """Extend ``get_step`` to return integer values rather than floats.

    If the floats returned by ``coordinates.get_step`` aren't what you
    want, then ``get_int_step`` will provide you with the values that
    you want.

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

    step = coordinates.get_step(a, b, marks=marks)
    return (round(step[0]), round(step[1]))
