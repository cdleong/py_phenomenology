import pyphenom_physical_constants as ppc
import decimal


def calculate_watts_per_photon(wavelength_um):
    # hc/lambda
    watts_per_photon = ppc.PLANCK_CONSTANT_JOULES_SECONDS * ppc.SPEED_OF_LIGHT_MICRONS_PER_SECOND / decimal.Decimal(wavelength_um)
    return float(watts_per_photon)


def calculate_number_of_photons(wavelength_um, num_watts=1):
    watts_per_photon = calculate_watts_per_photon(wavelength_um)
    total_photons = num_watts/watts_per_photon
    return total_photons


def calculate_watts(wavelength_um, total_photons):
    watts_per_photon = calculate_watts_per_photon(wavelength_um)
    total_watts = total_photons*watts_per_photon
    return total_watts


if __name__ == "__main__":
    # https://labrigger.com/blog/2010/12/15/watts-per-photon/
    wavelength_um = 0.52
    total_photons = 50*10e6
    total_watts = calculate_watts(wavelength_um, total_photons)

    total_photons_backcalculated = calculate_number_of_photons(wavelength_um, total_watts)

    print(f"total watts (should equal about 1.9e-11 watts): {total_watts}")
    print(f"total photons (should equal ~{total_photons}: {total_photons_backcalculated}")
