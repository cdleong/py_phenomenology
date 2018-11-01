"""Computer Problem for ECE 595 Midterm 2.

Created 2018-10-31
by cdleong
"""
import random

def setup_fpa():
    pass

def setup_telescope():
    pass

def calculate_photons_leaving_source():
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
    electrons_out_per_sec = random.randint(1,2*10**6)
    return electrons_out_per_sec


if __name__ == "__main__":

    # Scattering

    fpa = setup_fpa()
    telescope = setup_telescope()

    photons_leaving_source = calculate_photons_leaving_source()

    spatial_info = setup_spatial_info()
    print(spatial_info)

    atmosphere = setup_atmosphere()

    photons_hitting_telescope_aperture_per_sec = calculate_photons_hitting_telescope_aperture_per_sec(photons_leaving_source,
                                                                                                      spatial_info,
                                                                                                      atmosphere)

    photons_hitting_fpa_per_sec = calculate_photons_hitting_fpa_per_second(telescope, photons_hitting_telescope_aperture_per_sec)

    electrons_out_per_sec = calculate_electrons_out_per_sec(fpa, photons_hitting_fpa_per_sec)

    electrons_out_per_sec_threshold = 10**6
    print(f"Electrons out of FPA per second: {electrons_out_per_sec}")
    if electrons_out_per_sec > electrons_out_per_sec_threshold:
        print("Not detectable")
    else:
        print("Detectable")
