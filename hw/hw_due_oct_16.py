'''
Created on Oct 16, 2018

@author: cdleong
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import decimal
from pyphenom import uniform_aerosol as ua
from pyphenom import radiometry
from pyphenom import atmosphere

def vertical_path_beers_law_approximation(starting_particle_density_per_cubic_m, effective_cross_section_sq_m, scale_height_m):
    exponent_term = -starting_particle_density_per_cubic_m * effective_cross_section_sq_m * scale_height_m
    
    return math.e**exponent_term    

def problem_VIII_5():
 
    
    particle_density_per_cubic_cm = 3*10**14
    path_length_km = 20.0
    effective_cross_section_sq_cm = 10**-21
    path_length_cm = path_length_km *1000 *100
    exponent_term = -particle_density_per_cubic_cm * effective_cross_section_sq_cm * path_length_cm
    
    new_aerosol_transmission_factor = math.e**exponent_term
    print(f"tf for problem_VIII_5 aerosol: {new_aerosol_transmission_factor}")
    
     
def problem_VIII_6():    
    intensity_watts_per_steradian = 1.26 * 10**6
    scale_height_m = 6.00 * 1000
#     scale_height_m = scale_height_m * 10**10
    starting_particle_density_per_cubic_m = 7.36*10**9
#     starting_particle_density_per_cubic_m = starting_particle_density_per_cubic_m * 10**10
    effective_cross_section_sq_m = 7.85*10**-13
#     effective_cross_section_sq_m = effective_cross_section_sq_m *10**10
    
    sat_height_km = 36000
    sat_height_km = 36
#     top_height_km = 100
    sat_height_m = sat_height_km*1000
    heights_m = np.arange(0,sat_height_m-0.1, 1000)
    irradiances_at_heights = []
    vertical_atmospheric_transmission_factors_at_heights = []
    attenuated_irradiances_at_heights = []
    
    irradiance_to_get_target_watts_per_square_meter = 10**-10
    get_target = []
    
    for height_m in heights_m:
        distance_r_meters = sat_height_m - height_m
        theta_r_degrees = 0.0 # looking directly at it from above
        
        irradiance_at_aperture = radiometry.irradiance_on_aperture_from_point_source(distance_r_meters, 
                                                                                     intensity_watts_per_steradian, 
                                                                                     theta_r_degrees)
        irradiances_at_heights.append(irradiance_at_aperture)
        
        
        
        
        e1 = -height_m/scale_height_m
        z1_bit = math.e**(e1)
        print(f"z1_bit: {z1_bit}")
        
        e2 = -sat_height_m/scale_height_m
        z2_bit = math.e**(e2)
        print(f"z2_bit: {z2_bit}")
        parenthesis_bit = z1_bit-z2_bit
        print(f"parenthesis_bit: {parenthesis_bit}")
        exponent_term = -decimal.Decimal(starting_particle_density_per_cubic_m) * decimal.Decimal(effective_cross_section_sq_m) * decimal.Decimal(scale_height_m) * decimal.Decimal(parenthesis_bit)
        print(f"exponent term: {exponent_term}")
        vertical_atmospheric_transmission_factor = decimal.Decimal(math.e)**decimal.Decimal(exponent_term)
        vertical_atmospheric_transmission_factor = float(vertical_atmospheric_transmission_factor)
        print(f"vertical_atmospheric_transmission_factor term: {vertical_atmospheric_transmission_factor}")
        vertical_atmospheric_transmission_factors_at_heights.append(vertical_atmospheric_transmission_factor)

        attenuated_irradiance_at_heights = irradiance_at_aperture*vertical_atmospheric_transmission_factor
        attenuated_irradiances_at_heights.append(attenuated_irradiance_at_heights)
        
        if attenuated_irradiance_at_heights >= irradiance_to_get_target_watts_per_square_meter:
            get_target.append(1)
        else: 
            get_target.append(2)
        


    plt.figure()
    plt.title("target got?")
    plt.xlabel("1=yes, 2 = no")
    plt.ylabel("height, meters")    
    plt.plot(get_target, heights_m)

    plt.figure()
    plt.title("irradiances at aperture with height")
    plt.xlabel("irradiance at aperture, watts per square meter")
    plt.ylabel("height, meters")    
    plt.semilogx(irradiances_at_heights, heights_m)
#     plt.loglog(irradiances_at_heights, heights_m)
#     plt.plot(irradiances_at_heights, heights_m)


    plt.figure()
    plt.title("attenuated_irradiances_at_heights at heights")
    plt.xlabel("irradiance at aperture, watts per square meter")
    plt.ylabel("height, meters")
    plt.semilogx(attenuated_irradiances_at_heights, heights_m)
    
    plt.figure()
    plt.title("vertical_atmospheric_transmission_factors at heights")
    plt.xlabel("transmission factor")
    plt.ylabel("height, meters")
    plt.plot(vertical_atmospheric_transmission_factors_at_heights, heights_m)
    print(vertical_atmospheric_transmission_factors_at_heights)
    print(vertical_atmospheric_transmission_factors_at_heights[0])
    print(vertical_atmospheric_transmission_factors_at_heights[-1])
    
    plt.figure()
    plt.title("irradiances and attenuated irradiances at aperture with height")
    plt.xlabel("irradiance at aperture, watts per square meter")
    plt.ylabel("height, meters")    
    plt.semilogx(irradiances_at_heights, heights_m)
    plt.semilogx(attenuated_irradiances_at_heights, heights_m)

    
    

def problem_VIII_7():
    aerosol_list =[]
    aerosol_list.append(ua.UniformAerosol(name="Smoke", 
                                               particle_size_um=0.05, 
                                               particles_per_cubic_m=10**11))
    aerosol_list.append(ua.UniformAerosol(name="Fumes", 
                                               particle_size_um=0.5, 
                                               particles_per_cubic_m=10**9))
    aerosol_list.append(ua.UniformAerosol(name="Dust", 
                                               particle_size_um=5, 
                                               particles_per_cubic_m=10**5))
    aerosol_list.append(ua.UniformAerosol(name="Ash", 
                                               particle_size_um=50, 
                                               particles_per_cubic_m=10**3))
    
    wavelengths_um = [0.5, 1.0, 5.0, 10.0]
    wavelengths_um = np.arange(0.1, 10, 0.1)
      
    
    path_length_km = 8.0 
    
    # for each wavelength
    tfs_at_wavelength = []
    
    tfs_at_wavelength_by_aerosol = {}
    
    for wavelength_um in wavelengths_um:
        total_wavelength_transmission_factor = 1.0
        
        
        for aerosol in aerosol_list:
            path_length_m = path_length_km * 1000
            aerosol_transmission_factor_at_this_wavelength = aerosol.calculate_transmission_factor(wavelength_um, path_length_m)

            total_wavelength_transmission_factor = total_wavelength_transmission_factor * aerosol_transmission_factor_at_this_wavelength
            tfs_at_wavelength_by_aerosol[aerosol.name, wavelength_um] = aerosol_transmission_factor_at_this_wavelength
            
        tfs_at_wavelength.append(total_wavelength_transmission_factor)
        
    
    
    
    
    print(tfs_at_wavelength)
    plt.figure()
    plt.title("Total transmission factor at various wavelengths")
    plt.xlabel("wavelength (um)")
    plt.ylabel("Transmission factor")
    plt.scatter(wavelengths_um, tfs_at_wavelength)
    
    for aerosol in aerosol_list:
        ecs_vals_for_this_aerosol = []
        for wavelength_um in wavelengths_um:
            ecs = aerosol.calculate_effective_cross_section_sq_um(wavelength_um)
            ecs_vals_for_this_aerosol.append(ecs)
            print(f"for wavelength {wavelength_um} and {aerosol.name}, ecs = {ecs} sq um")
        
        plt.figure()
        plt.title(f"Effective Cross Section for {aerosol.name} vs wavelength")
        plt.xlabel("wavelength (um)")
        plt.ylabel("ECS, square um")
        plt.loglog(wavelengths_um, ecs_vals_for_this_aerosol)
        
        
        tfs_for_this_aerosol = []
        for wavelength_um in wavelengths_um:
            tf_for_this_aerosol_at_this_wavelength = tfs_at_wavelength_by_aerosol[aerosol.name, wavelength_um]
            tfs_for_this_aerosol.append(tf_for_this_aerosol_at_this_wavelength)
    
        plt.figure()
        plt.title(f"Transmission factor for {aerosol.name} vs wavelength")
        plt.xlabel("wavelength (um)")
        plt.ylabel("Transmission factor")
        plt.scatter(wavelengths_um, tfs_for_this_aerosol)
    
    

if __name__ == '__main__':
#     problem_VIII_5()
    problem_VIII_6()
#     problem_VIII_7()
    
    plt.show()
