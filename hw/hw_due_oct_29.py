"""Homework due 2018-10-29 for ECE 595-08.

Created 2018-10-26.
by cdleong
"""
import math
import matplotlib.pyplot as plt
import numpy as np
from pyphenom import lens
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge


def ix_2():
    """Problem IX-2.

    LSST Telescope has 3 mirrors!
    """
    primary_lens_focal_length_m = 10
    primary_lens_focal_length_cm = primary_lens_focal_length_m*100
    primary_lens_diameter_m = 8.4
    primary_lens_diameter_cm = primary_lens_diameter_m*100
    primary_lens = lens.Lens(focal_length_cm=primary_lens_focal_length_cm)
    primary_lens.set_aperture_from_diameter(diameter_cm=primary_lens_diameter_cm)

    # I want to graph the rays.
    # Simplest method is with a triangle
    fig, ax = plt.subplots()
    patches = []

    primary_lens_focus_point = [0.0,  # arbitrary
                                primary_lens_diameter_m / 2]  # "in the middle"

    primary_lens_x = primary_lens_focus_point[0] + primary_lens_focal_length_m
    primary_lens_base_point = [primary_lens_x, 0]
    primary_lens_top_point = [primary_lens_x, primary_lens_diameter_m]
    primary_lens_points = np.array([primary_lens_focus_point,
                                    primary_lens_base_point,
                                    primary_lens_top_point])

    primary_lens_rays = plt.Polygon(primary_lens_points, fill=None)
    patches.append(primary_lens_rays)

    for index, patch in enumerate(patches):
        print("{0}:{1}:{2}".format(index, patch, patch.get_xy()))

    # ... and the more complicated way is with a Wedge
    # http://www.1728.org/radians.htm
    # https://mathbitsnotebook.com/Geometry/Circles/CRArcLengthRadian.html
    # Calculate central angle with
    # arc length/circumference = central_angle/360 degrees
    # -> central_angle_degrees = arc length/circumference*360
    # arc length is approximately the diameter of the mirror
    # central angle is solved for.
    circumference_m = 2*math.pi*primary_lens_focal_length_m
    arc_length_m = primary_lens_diameter_m
    central_angle_degrees = arc_length_m/circumference_m*360
    primary_lens_wedge = Wedge(primary_lens_focus_point,
                               r=primary_lens_focal_length_m,
                               theta1=-central_angle_degrees/2,
                               theta2=central_angle_degrees/2)

    patches.append(primary_lens_wedge)
    # Except that this overestimates the angle a bit, since the aperture is
    # calculated from the _projection_ of the mirror.

    # https://stackoverflow.com/questions/26935701/ploting-filled-polygons-in-python
    p = PatchCollection(patches,
                        cmap=plt.get_cmap('plasma'),
                        alpha=0.4)
    colors = 100*np.random.rand(len(patches))
    p.set_array(np.array(colors))
    ax.add_collection(p)
    ax.autoscale(True)


if __name__ == "__main__":
    ix_2()
    plt.show()
