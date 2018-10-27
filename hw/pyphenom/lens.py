'''
Created on Oct 23, 2018

@author: cdleong
'''
import math


class Lens(object):
    '''
    It's a lens!
    Used for finding things like object distance, image distance
    '''

    def __init__(self, focal_length_cm=None, aperture_sq_cm=None):
        '''
        Optional to set either. If you don't set focal length here, you should set it before you use it,
        either directly or with set_focal_length_cm
        '''
        if aperture_sq_cm is not None:
            self.aperture_sq_cm = aperture_sq_cm

        if focal_length_cm is not None:
            self.focal_length_cm = focal_length_cm

    def set_aperture_from_diameter(self, diameter_cm):
        self.aperture_sq_cm = math.pi * diameter_cm**2 / 4

    def find_focal_length(self, object_distance_cm, image_distance_cm):
        one_over_object_distance = 1.0/object_distance_cm
        one_over_image_distance = 1.0/image_distance_cm
        one_over_focal_length = one_over_object_distance + one_over_image_distance
        return 1.0/one_over_focal_length

    def set_focal_length_cm(self, object_distance_cm, image_distance_cm):
        self.focal_length_cm = self.find_focal_length(object_distance_cm, image_distance_cm)

    def find_image_distance_cm(self, object_distance_cm):
        """
        Does what you'd expect from the name.
        Note: If object distance is equal to focal length,
        throws an exception
        """
        one_over_focal_distance = 1.0/self.focal_length_cm
        one_over_object_distance = 1.0/object_distance_cm
        image_distance_cm = 1.0/((one_over_focal_distance) - (one_over_object_distance))
        return image_distance_cm

    def find_object_distance_cm(self, image_distance_cm):
        """
        Does what you'd expect from the name.
        Note: If image_distance_cm distance is equal to focal length,
        throws an exception
        """
        one_over_focal_distance = 1.0/self.focal_length_cm
        one_over_image_distance = 1.0/image_distance_cm
        object_distance_cm = 1.0/((one_over_focal_distance) - (one_over_image_distance))
        return object_distance_cm

    def find_magnification(self, object_distance_cm):
        """
        Please don't give it an object distance of zero.
        It will crash.

        """
        image_distance_cm = self.find_image_distance_cm(object_distance_cm)
        magnification = image_distance_cm/object_distance_cm
        return magnification


if __name__ == '__main__':
    lens_1_from_slide_17_11 = Lens(focal_length_cm=13.3)
    object_distance_cm = 40.0

    # calculated and original should be the same

    for object_distance_cm in range(10, 50):
        image_distance_cm = lens_1_from_slide_17_11.find_image_distance_cm(object_distance_cm)
        calculated_object_distance_cm = lens_1_from_slide_17_11.find_object_distance_cm(image_distance_cm)
        magnification = lens_1_from_slide_17_11.find_magnification(object_distance_cm)
        print(f"with focal length {lens_1_from_slide_17_11.focal_length_cm} cm, and object distance {object_distance_cm} cm")
        print(f"image_distance_cm = {image_distance_cm} cm,")
        print(f"calculated_object_distance_cm = {calculated_object_distance_cm} cm, original = {object_distance_cm} cm")
        print(f"magnification = {magnification} cm")

        original_focal_length_cm = lens_1_from_slide_17_11.focal_length_cm
        lens_1_from_slide_17_11.set_focal_length_cm(object_distance_cm, image_distance_cm)
        new_focal_length = lens_1_from_slide_17_11.focal_length_cm
        # should be the same!
        print(f"original_focal_length_cm {original_focal_length_cm} cm, new focal length {new_focal_length}\n")
        lens_1_from_slide_17_11.focal_length_cm = original_focal_length_cm
