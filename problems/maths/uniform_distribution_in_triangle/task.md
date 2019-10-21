# Task

Generate single random point within the given triangle on plane,
using as few `random()` calls as possible.
The resulting distribution should be uniform.

# Solution

## Generating two random numbers from one
Generated 64-bit random number is split into two random numbers
by using the bits `12-31` for first number and bits `32-63` for second.
(first 12 bits is an exponent, which has non-uniform distribution and
 thus is cut off).


## Generating point in the unit square
Then, using two random numbers t1, t2, we can generate a random point
in the square `[0,1] x [0,1]`.


## Generating point in the triangle (half of the unit square)
If the point lays above the "main diagonal",
we can translate it using simple affine transform:

```python
if t1 + t2 > 1:
    t1, t2 = 1 - t1, 1 - t2
```

Hence the point will certainly lie in the triangle `[0, 0], [0, 1], [1, 0]`.

## Generating the point in given triangle
Another affine transform will translate it into given triangle (trivial).

