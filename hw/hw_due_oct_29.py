"""Homework due 2018-10-29 for ECE 595-08.

Created 2018-10-26.
by cdleong
"""
import matplotlib.pyplot as plt
import numpy as np
from pyphenom import lens
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon


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

    primary_lens_rays = Polygon(primary_lens_points, fill=None)
    patches.append(primary_lens_rays)

    for index, patch in enumerate(patches):
        print("{0}:{1}:{2}".format(index, patch, patch.get_xy()))

    #    plt.gca().add_patch(patch)
    # https://stackoverflow.com/questions/26935701/ploting-filled-polygons-in-python
    p = PatchCollection(patches,
                        cmap=plt.get_cmap('plasma'),
                        alpha=0.4)
    colors = 100*np.random.rand(len(patches))
    p.set_array(np.array(colors))
    ax.add_collection(p)
    ax.autoscale(True)
#    ax.set_xlim([0,10])
#    ax.set_ylim([0,10])


if __name__ == "__main__":
    ix_2()
    plt.show()
