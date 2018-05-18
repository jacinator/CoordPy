# CoordPy

CoordPy is written with two-dimensional 'game boards' in mind. This
module will allow interaction between pieces and the board. This means
that any piece (military unit, planet, or friendly dog) can save a
location and interact with other locations. Coordinates are saved as
either tuples or lists with two integers or floats within them.

```python
>>> a = [23, 41]
>>> b = (0.6238, 3.8174)
```

There is no limit to the range of the coordinates, nor their
interaction with each other. Anything is fair game.

The other thing I feel like I should define is ``mark``. ``get_step``
has an argument named ``marks`` which defaults to ``1``. A mark is the
measure between one coordinate and any other adjacent coordinate.
``[1, 0]`` is one mark away from ``[0, 0]``.

For all of this I welcome contributions, suggestions, or an issue, if
you have one.

## Get Distance

The function ``get_distance`` gets the number of marks between any two
coordinates. Regardless of whether the coordinates are directly along
the same axis or if they are off on a 32 degree angle, this function
will draw a straight line between them and measure it.

```python
>>> distance = get_distance([0, 0], [4, 3])
>>> distance
5.0
```

This might look familiar, because it is the Pythagorean Theorum. A
right angle is easily measurable. We can find out the lenght of the
other two sides of the triangle by extracting the difference between
the ``X`` coordinates and ``Y`` coordinates. These can be used to find
the length of the hypotenuse.

## Get Step

The function ``get_step`` calculates the angle of the path from point
``a`` to point ``b``. With that angle defined it calculates the sine
and cosine of the triangle.

The optional argument ``marks`` is then multiplied to both of these
measurements. This means that you can calculate the distance 2, 3 or
more marks as you please.

The resultant sine is added to the ``Y`` coordinates and the cosine is
added to the ``X`` axis from the point of origination. This creates a
new set of coordinates that is returned from the function.

```python
>>> step = get_step([0, 0], [4, 3])
>>> step
(0.7071067811865476, 0.7071067811865475)
>>> step = get_step([0, 0], [4, 3], marks=3)
>>> step
(2.121320343559643, 2.1213203435596424)
```

All of this is thrown out however, if the distance between the two
points, provided by ``get_distance``, is less than the value of
``marks``. If that is the case, you will reach your destination
regardless and the destination coordinates are returned.
