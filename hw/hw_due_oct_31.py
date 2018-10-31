"""Homework due 2018-10-31 for ECE 595-08.

Created 2018-10-29.
by cdleong
"""
import matplotlib.pyplot as plt
from pyphenom import photon
from pyphenom import graybody_emissivity


def x_3():
    problem_string = "[Problem X-3]"
    print(f"{problem_string}")
    irradiance_watts_per_sq_m = 1.09 * 10**-6
    print(f"{problem_string} irradiance_watts_per_sq_m: {irradiance_watts_per_sq_m}")
    sq_um_per_sq_m = 1e12
    irradiance_watts_per_sq_um = irradiance_watts_per_sq_m/sq_um_per_sq_m
    print(f"{problem_string} irradiance_watts_per_sq_um: {irradiance_watts_per_sq_um}")

    area_sq_um = 100*100
    print(f"{problem_string} area_sq_um: {area_sq_um}")

    total_watts = irradiance_watts_per_sq_um * area_sq_um
    print(f"{problem_string} total_watts: {total_watts}")

    wavelength_of_light_um = 2.67
    print(f"{problem_string} wavelength_of_light_um: {wavelength_of_light_um}")

    photons_per_second = photon.calculate_number_of_photons_per_second(wavelength_of_light_um,
                                                                       total_watts)
    print(f"{problem_string} photons hitting sensor per second: {photons_per_second}")

    duration_of_sample_sec = 0.1
    print(f"{problem_string} Sample duration: {duration_of_sample_sec}")

    photons_per_sample = photons_per_second*duration_of_sample_sec
    print(f"{problem_string} photons_per_sample: {photons_per_sample}")

    quantum_efficiency = 0.35
    electrons_per_sample = quantum_efficiency * photons_per_sample
    print(f"{problem_string} electrons_per_sample: {electrons_per_sample}")


def x_9():
    problem_string = "[Problem X-9]"
    print(f"{problem_string} unfinished")

    # instantiate a blackbody
    blackbody_calculator = graybody_emissivity.GraybodyEmissivityCalculator()
    start_wavelength_um = 2.0
    stop_wavelength_um = 3.5
    wavelength_step_um = 0.01
    temp_kelvin = 350
    wavelengths, blackbody_exitances, graybody_exitances = blackbody_calculator.get_blackbody_and_graybody_exitances(start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin)
    graybody_emissivity.graph_exitance_vs_wavelength_at_temp(wavelengths, blackbody_exitances, temp_kelvin)

    # instantiate a lens

    # instantiate a detector

    # calculate number of photons per wavelength hitting detector

#    print(f"{x_9_string}:{}")


def x_10():
    problem_string = "[Problem X-10]"
    print(f"{problem_string} unfinished")


if __name__ == "__main__":
    x_3()

    x_9()

    x_10()

    plt.show()
