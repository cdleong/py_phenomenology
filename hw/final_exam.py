"""ECE 595-08 Final exam calculations.

Author: Colin Leong
Date: 2018-12-10

"""
import numpy as np
import matplotlib as plt
import seaborn as sns

# pyphenom
from pyphenom.uniform_aerosol import UniformAerosol

sns.set()


def prob_5():
    """Calculate transmission factor for three aerosols."""
    wavelength_um = 10.6
    path_length_m = 6000

    # Calculate Smoke
    smoke = UniformAerosol("smoke", particle_size_um=0.08*2, particles_per_cubic_m=8.0*10**14)
    soot = UniformAerosol("soot", particle_size_um=1.6*2, particles_per_cubic_m=2.5*10**7)
    dust = UniformAerosol("dust", particle_size_um=32*2, particles_per_cubic_m=7.6*10**5)
    ref = UniformAerosol("ref", particle_size_um=0.0796*2, particles_per_cubic_m=7.6*10**5)
    aerosols = [ref, smoke, soot, dust]

    for aerosol in aerosols:
        name = aerosol.name
        print("\n*******")
        print("CALCULATIONS FOR {}".format(name))

        sigma = aerosol.calculate_effective_cross_section_sq_um(wavelength_um)
        atf = aerosol.calculate_transmission_factor(wavelength_um, path_length_m)

        print("{0} sigma: {1} um^2".format(name, sigma))
        print("{0} atf: {1}".format(name, atf))


if __name__ == "__main__":
    prob_5()
#    plt.show()
