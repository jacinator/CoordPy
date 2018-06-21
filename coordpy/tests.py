# -*- coding: utf-8 -*-
"""CoordPy test cases.

This module contains the tests for the CoordPy package. This includes
functions from the coordinates module, the decorators module, and the
utils module. These three modules contain the base operations for
CoordPy, the coordinate cleaners to wrap the functions, and the integer
modifications for the package respectively.
"""

import math
import unittest

from . import coordinates, decorators, utils


class CoordinateValueErrorTestCase(unittest.TestCase):
    """This is a simple testcase to test the coordinate value error.

    We want to assert that the ``CoordinateValueError`` is a subclass
    of the ``ValueError``. This probably won't break, but just to be
    safe, here's a testcase.
    """

    def test_subclasses_value_error(self):
        self.assertTrue(issubclass(decorators.CoordinateValueError, ValueError))


class CleanCoordinatesTestCase(unittest.TestCase):
    """Test the decorator and its cleaners.

    The ``clean_coordinates`` decorator and the method that it uses are
    tested by this testcase. It runs through valid strings, integers,
    and invalid strings and makes sure that the valid inputs are
    converted to floats and the invalid inputs raise errors.
    """

    def test_clean_value_str(self):
        """Test that valid strings are converted to floats."""
        self.assertEqual(decorators.clean_coordinate_value('12'), 12.0)

    def test_clean_value_int(self):
        """Test that the integers are converted to floats."""
        self.assertEqual(decorators.clean_coordinate_value(12), 12.0)

    def test_clean_value_error(self):
        """Assert that an invalid string raises an error.

        When an invalid string is passed to the cleaning method or, by
        extension, the decorator, ensure that the custom exception
        ``CoordinateValueError`` is raised.
        """

        self.assertRaisesRegex(
            decorators.CoordinateValueError,
            r'^Coordinate values must be convertible to floats, not abc$',
            decorators.clean_coordinate_value,
            'abc',
        )

    def test_clean_coordinates(self):
        """Test that the decorator cleans the values.

        Assert that the values being passed into the decorator are
        actually being cleaned.
        """

        @decorators.clean_coordinates
        def _test_function(a, b):
            return a, b
        self.assertEqual(_test_function(
            ('12', '12'), (10, 10),
        ), ((12.0, 12.0), (10.0, 10.0)))


class GetDistanceTestCase(unittest.TestCase):
    """Test that ``get_distance`` is working.

    This testcase is dedicated to ``coordinates.get_distance`` and
    ensuring that it remains operational. The distance between to
    coordinates is a large part of the coordinates package, so it needs
    to keep working.

    Most of these tests take a set of coordinates and match the output
    of ``get_distance`` to the result of the Pythagorean Theorum.
    """

    def test_using_pythagorean_theorum(self):
        """Assert that the Pythagorean Theorum is still true.

        This function is basically a working out of the Pythagorean
        Theorum. Since that is the case, we need to assert that the
        Pythagorean Theorum still matches an easily recognizable
        output.
        """

        self.assertEqual(coordinates.get_distance(
            (0, 0), (3, 4)), 5.0)

    def test_000_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (0, 3)), 3.0)

    def test_045_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (3, 3)), 4.242640687119285)

    def test_090_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (3, 0)), 3.0)

    def test_135_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (3, -3)), 4.242640687119285)

    def test_180_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (0, -3)), 3.0)

    def test_225_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (-3, -3)), 4.242640687119285)

    def test_270_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (-3, 0)), 3.0)

    def test_315_degree_angle_distance(self):
        self.assertEqual(coordinates.get_distance(
            (0, 0), (-3, 3)), 4.242640687119285)


class GetStepTestCase(unittest.TestCase):
    """Test that ``get_step`` is working properly.

    ``get_step`` is perhaps the pinnacle of CoordPy. In that case, and
    for the sake of best practices, we need a testcase to maintain that
    it continues to work.

    These tests are all in groups of two. They all check the coordinate
    set returned by ``get_step`` and match it against what should be
    returned. The groups of two are one matching against a single tick,
    and the other matching against a distance of three marks.
    """

    def assertLocation(self, a, b, marks, coord):
        """A custom assertion method for the outcome of ``get_step``.

        To prevent redundant code across this testcase, we are
        providing a custom assertion method that will test the output
        of ``get_step``. This method also will round the coordinates
        to the nearest tenth decimal place. This is because we are
        dealing with floats and every so often one of them is off by
        0.000000001 or something like that.
        """

        coord_a = [round(x, 10) for x in coordinates.get_step(a, b, marks)]
        coord_b = [round(x, 10) for x in coord]
        self.assertListEqual(coord_a, coord_b)

    def test_000_degree_angle_single_step(self):
        self.assertLocation((0, 0), (5, 0), 1, (1, 0))

    def test_000_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (5, 0), 3, (3, 0))

    def test_045_degree_angle_single_step(self):
        self.assertLocation((0, 0), (5, 5), 1, (
            0.7071067811865476,
            0.7071067811865476,
        ))

    def test_045_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (5, 5), 3, (
            2.121320343559643,
            2.121320343559643,
        ))

    def test_090_degree_angle_single_step(self):
        self.assertLocation((0, 0), (0, 5), 1, (0, 1))

    def test_090_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (0, 5), 3, (0, 3))

    def test_135_degree_angle_single_step(self):
        self.assertLocation((0, 0), (5, -5), 1, (
            0.7071067811865476,
            -0.7071067811865476,
        ))

    def test_135_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (5, -5), 3, (
            2.121320343559643,
            -2.121320343559643,
        ))

    def test_180_degree_angle_single_step(self):
        self.assertLocation((0, 0), (-5, 0), 1, (-1, 0))

    def test_180_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (-5, 0), 3, (-3, 0))

    def test_225_degree_angle_single_step(self):
        self.assertLocation((0, 0), (-5, -5), 1, (
            -0.7071067811865476,
            -0.7071067811865476,
        ))

    def test_225_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (-5, -5), 3, (
            -2.121320343559643,
            -2.121320343559643,
        ))

    def test_270_degree_angle_single_step(self):
        self.assertLocation((0, 0), (0, -5), 1, (0, -1))

    def test_270_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (0, -5), 3, (0, -3))

    def test_315_degree_angle_single_step(self):
        self.assertLocation((0, 0), (-5, 5), 1, (
            -0.7071067811865476,
            0.7071067811865476,
        ))

    def test_315_degree_angle_triple_step(self):
        self.assertLocation((0, 0), (-5, 5), 3, (
            -2.121320343559643,
            2.121320343559643,
        ))


class GetIntStepTestCase(unittest.TestCase):
    """Test that the int step is working as it should be.

    Since ``get_int_step`` is an extension of ``get_step`` the majority
    of the function's processing is already tested. This testcase tests
    the little bit that is not already tested above.
    """

    def test_045_degree_angle_double_step(self):
        self.assertEqual(utils.get_int_step((0, 0), (5, 5), 2), (1, 1))

    def test_045_degree_angle_quadruple_step(self):
        self.assertEqual(utils.get_int_step((0, 0), (5, 5), 4), (3, 3))


class GetAllStepsTestCase(unittest.TestCase):
    """Test that the getting the entire path is working.

    The ``get_all_steps`` function loops over a path and gets all the
    coordinate steps along the path. This testcase ensures that it is
    actually working. As this uses the ``get_step`` or ``get_int_step``
    functions, much of the heavy lifting is already tested.
    """

    def test_get_all_steps_default(self):
        steps = utils.get_all_steps(
            (0, 0),
            (2, 10),
        )
        self.assertListEqual(steps, [
            (0.0, 0.0),
            (0.196116135138184, 0.9805806756909201),
            (0.392232270276368, 1.9611613513818402),
            (0.588348405414552, 2.9417420270727606),
            (0.784464540552736, 3.9223227027636804),
            (0.9805806756909199, 4.9029033784546),
            (1.176696810829104, 5.883484054145521),
            (1.372812945967288, 6.864064729836441),
            (1.568929081105472, 7.844645405527361),
            (1.7650452162436558, 8.82522608121828),
            (1.9611613513818398, 9.8058067569092),
            (2.0, 10.0)
        ])

    def test_get_all_steps_int(self):
        steps = utils.get_all_steps(
            (0, 0),
            (2, 10),
            method=utils.get_int_step,
        )
        self.assertListEqual(steps, [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7),
            (2, 8),
            (2, 9),
            (2, 10),
        ])
