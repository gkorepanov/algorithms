import numpy as np
from typing import Tuple


def generate_random_points_in_triangle(
        random_numbers: np.ndarray,
        triangle_coordinates: Tuple[np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
    """Generate point within given triangle for each random number in provided 1D array
    """
    MAX_4_BYTES_INT = 2**32 - 1
    N = random_numbers.shape[0]

    # Make two random points from each single random point
    random_pairs = (random_numbers.view('<I')).reshape((N, -1))

    # Cut off exponent, see IEEE754 for details
    N_BITS_TO_CUT_FROM_LEFT = 12
    random_pairs[:, 1] = np.left_shift(random_pairs[:, 1], N_BITS_TO_CUT_FROM_LEFT)
    random_pairs = random_pairs / MAX_4_BYTES_INT

    # A = 1 - A and B = 1 - B where A + B > 1 to transform unit square into triangle
    mask = (random_pairs[:, 0] + random_pairs[:, 1]) > 1
    random_pairs[mask] = 1 - random_pairs[mask]

    # Calculate new coordinates using simple affine transform
    p1, p2, p3 = triangle_coordinates
    r0, a, b = p1, p2 - p1, p3 - p1

    points = np.dot(random_pairs, np.vstack([a, b]))
    points += np.repeat([r0], N, axis=0)

    return points

