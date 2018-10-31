"""Homework due 2018-10-31 for ECE 595-08.

Created 2018-10-29.
by cdleong
"""
import matplotlib.pyplot as plt
from pyphenom import photon


def x_3():
    irradiance_watts_per_sq_m = 1.09 * 10**-6
    print(f"irradiance_watts_per_sq_m: {irradiance_watts_per_sq_m}")
    sq_um_per_sq_m = 1e12
    irradiance_watts_per_sq_um = irradiance_watts_per_sq_m/sq_um_per_sq_m
    print(f"irradiance_watts_per_sq_um: {irradiance_watts_per_sq_um}")

    area_sq_um = 100*100
    print(f"area_sq_um: {area_sq_um}")

    total_watts = irradiance_watts_per_sq_um * area_sq_um
    print(f"total_watts: {total_watts}")

    wavelength_of_light_um = 2.67
    print(f"wavelength_of_light_um: {wavelength_of_light_um}")

    photons_per_second = photon.calculate_number_of_photons_per_second(wavelength_of_light_um,
                                                                       total_watts)
    print(f"photons hitting sensor per second: {photons_per_second}")

    duration_of_sample_sec = 0.1
    print(f"Sample duration: {duration_of_sample_sec}")

    photons_per_sample = photons_per_second*duration_of_sample_sec
    print(f"photons_per_sample: {photons_per_sample}")

    quantum_efficiency = 0.35
    electrons_per_sample = quantum_efficiency * photons_per_sample
    print(f"electrons_per_sample: {electrons_per_sample}")


if __name__ == "__main__":
    x_3()

    plt.show()
