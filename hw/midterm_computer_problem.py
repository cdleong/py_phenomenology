"""Computer Problem for ECE 595 Midterm 2.

Created 2018-10-31
by cdleong
"""
import random

from pyphenom import atmosphere


def setup_fpa():
    """FPA object setup, whatever that is.

    The only info from the problem is that it is a silicon detector,
    and we have a graph of quantum efficiency vs wavelength.

    Based on the graph, it is
    """
    # it is a silicon detector. Based on the graph, the quantum efficiency
    # at 1.06 um is ~50%.
    fpa = {}
    fpa["quantum_efficiency"] = 0.5
    return fpa


def setup_telescope(optical_transmission_factor, aperture_diameter_cm):
    pass


def calculate_photons_leaving_source():
    laser_output_in_bandpass_watts = 10

    number_of_horizontal_sections = 10
    length_of_horizontal_sections_m = 10

    number_of_vertical_sections = 9
    length_of_vertical_sections_m = 0.5
    path_length_of_laser_m = ((number_of_horizontal_sections*length_of_horizontal_sections_m)
                              + (number_of_vertical_sections*length_of_vertical_sections_m))
    pass


def setup_spatial_info():
    spatial_info = {}
    spatial_info['distance_from_source_to_sensor_km'] = 5
    return spatial_info


def setup_atmosphere():
    pass


def calculate_photons_hitting_telescope_aperture_per_sec(source_info, spatial_info, atmosphere):
    pass


def calculate_photons_hitting_fpa_per_second(telescope, photons_hitting_telescope_aperture_per_sec):
    pass


def calculate_electrons_out_per_sec(fpa, electrons_hitting_fpa_per_sec):
    electrons_out_per_sec = random.randint(1, 2*10**6)
    return electrons_out_per_sec


if __name__ == "__main__":

    # Scattering

    telescope = setup_telescope()

    photons_leaving_source = calculate_photons_leaving_source()

    spatial_info = setup_spatial_info()

    atmosphere = setup_atmosphere()

    photons_hitting_telescope_aperture_per_sec = calculate_photons_hitting_telescope_aperture_per_sec(photons_leaving_source,
                                                                                                      spatial_info,
                                                                                                      atmosphere)

    photons_hitting_fpa_per_sec = calculate_photons_hitting_fpa_per_second(telescope, photons_hitting_telescope_aperture_per_sec)

    fpa = setup_fpa()
    electrons_out_per_sec = calculate_electrons_out_per_sec(fpa, photons_hitting_fpa_per_sec)

    electrons_out_per_sec_threshold = 10**6
    print("Electrons out of FPA per second: {}".format(electrons_out_per_sec))
    if electrons_out_per_sec > electrons_out_per_sec_threshold:
        print("Not detectable")
    else:
        print("Detectable")
