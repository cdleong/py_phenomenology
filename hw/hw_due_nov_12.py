"""Fall ECE 595-08, homework due Nov 12."""
from pyphenom import lens


def ix_7():
    """Monster problem involving a million lenses."""
    m_1_aperture_diameter_cm = 50
    m_1 = lens.Lens(focal_length_cm=200)
    m_1.set_aperture_from_diameter(diameter_cm=m_1_aperture_diameter_cm)

    basically_infinity_cm = 10e11
    m_1_image_distance_cm = m_1.find_image_distance_cm(basically_infinity_cm)

    print("m_1_image_distance_cm: {0}".format(m_1_image_distance_cm))

    distance_from_m1_to_m2_cm = 150

    object_distance_for_m2_cm = distance_from_m1_to_m2_cm - m_1_image_distance_cm

    print("object_distance_for_m2_cm: {0}".format(object_distance_for_m2_cm))

    image_distance_for_m2_cm = 150 + 50
    print("image_distance_for_m2_cm: {0}".format(image_distance_for_m2_cm))

    m_2 = lens.Lens()
    m_2.set_aperture_from_diameter(diameter_cm=12.5)
    m_2.set_focal_length_cm(object_distance_cm=object_distance_for_m2_cm,
                            image_distance_cm=image_distance_for_m2_cm)

    print("m_2.focal_length_cm:{}".format(m_2.focal_length_cm))

    # Formula 5 from Lesson 17 Bonus Features slide "Two Lenses"
    # separation is less than f1 so...
    effective_focal_length_cm = -(m_1.focal_length_cm*m_2.focal_length_cm)/(distance_from_m1_to_m2_cm-m_1.focal_length_cm-m_2.focal_length_cm)

    print("effective_focal_length_cm:{}".format(effective_focal_length_cm))

    # f/# is effective focal length/ aperture
    f_number = effective_focal_length_cm/m_1_aperture_diameter_cm

    print("f_number:{}".format(f_number))




if __name__ == "__main__":
    ix_7()
