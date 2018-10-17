'''
Created on Oct 16, 2018

@author: cdleong
'''
import math
import numpy as np
import matplotlib.pyplot as plt

class UniformAerosol(object):
    '''
    classdocs
    '''


    def __init__(self, name, particle_size_um, particles_per_cubic_m):
        '''
        Constructor
        '''
        self.name = name
        self.particle_size_um = particle_size_um
        self.particles_per_cubic_m = particles_per_cubic_m
        self.particle_radius_um = particle_size_um/2
        
        
        self.particle_circumference_um = 2*math.pi*self.particle_radius_um
        self.particle_area = math.pi*self.particle_radius_um*self.particle_radius_um
        
        
        self.base_rayleigh_wavelength_over_circ = 100
        self.base_sigma_over_area = 10**-7
        
        self.tf_cache = dict()





            
        
        

    def calculate_effective_cross_section_sq_um(self, wavelength_um):
#         wavelength_m = wavelength_um / 1e6
        # https://en.wikipedia.org/wiki/Rayleigh_scattering
        

        
        # ONLY VALID IN RAYLEIGH REGION #TODO: more general equation?
        new_wavelength_over_circ = wavelength_um/self.particle_circumference_um
#         print(f"new_wavelength_over_circ is {new_wavelength_over_circ} ")
        old_wavelength_over_circ = self.base_rayleigh_wavelength_over_circ 
        old_sigma_over_area = self.base_sigma_over_area
        old_lamda_over_new_lambda = old_wavelength_over_circ/new_wavelength_over_circ
        
        new_sigma_over_old_sigma = (old_lamda_over_new_lambda)**4
        sigma_over_area = old_sigma_over_area*new_sigma_over_old_sigma
        
#         print(f"sigma over area is: {sigma_over_area}")
#         print(f"")
        sigma_um = sigma_over_area*self.particle_area              
        

        
        return sigma_um
        
    def calculate_transmission_factor(self, wavelength_um, path_length_m):
        """
        Just straight up Beer
        """
        args_tuple = (wavelength_um, path_length_m)
        if args_tuple in self.tf_cache:
            return self.tf_cache[args_tuple]
        else:
            particle_density_per_cubic_m = self.particles_per_cubic_m
            
            
            print(f"particle_density_per_cubic_m: {particle_density_per_cubic_m} ")
            print(f"path_length_m: {path_length_m} ")
            
            effective_cross_section_sq_um = self.calculate_effective_cross_section_sq_um(wavelength_um)
            effective_cross_section_sq_m = effective_cross_section_sq_um/1e12
            print(f"effective_cross_section_sq_m: {effective_cross_section_sq_m} m")
            
            exponent_term = -particle_density_per_cubic_m * effective_cross_section_sq_m * path_length_m
            print(f"exponent_term {exponent_term}")
            transmission_factor = math.e**exponent_term
            self.tf_cache[args_tuple] = transmission_factor
            return transmission_factor
    
    
    
def main():    
    diameter_um = 0.0796*2
    example_wavelength_um = 5.00
    
    example_aerosol = UniformAerosol("aerosol_from_slides", particle_size_um=diameter_um, particles_per_cubic_m=1000)
    ecs = example_aerosol.calculate_effective_cross_section_sq_um(example_wavelength_um)
    print(f"ECS is {ecs}")
#     return
    
    y_values = []
    sigma = 1.0

    wavelengths_um = np.arange(1,100, 0.1)
    old_wavelength_um = None
    for wavelength_um in wavelengths_um:
        if old_wavelength_um:
            
                
            old_lamda_over_new_lambda = old_wavelength_um/wavelength_um
            
            new_sigma_over_old_sigma = (old_lamda_over_new_lambda)**4
            sigma = sigma*new_sigma_over_old_sigma
            old_wavelength_um = wavelength_um
            y_values.append(sigma)
            
        else: 
            old_wavelength_um = wavelength_um
        
    plt.figure()
    plt.loglog()
    plt.plot(wavelengths_um[1:], y_values)
    
    
    
    y_values = []
    rayleigh_wavelengths_um = np.arange(1,100, 0.001)
    old_wavelength_um = None
    
    old_wavelength_um = 100 
    old_sigma_over_area = 10**-7
    for wavelength_um in rayleigh_wavelengths_um:
            
                
        old_lamda_over_new_lambda = old_wavelength_um/wavelength_um
        
        new_sigma_over_old_sigma = (old_lamda_over_new_lambda)**4
        sigma_over_area = old_sigma_over_area*new_sigma_over_old_sigma
        
        y_values.append(sigma_over_area)
        
    plt.figure()
    plt.loglog()
    
    plt.plot(rayleigh_wavelengths_um, y_values)    
    
    x_vals = [1.1, 10, 100]
    y_vals = [10, 10**-3, 10**-7]
    plt.scatter(x_vals, y_vals)
#     plt.gca().set_aspect('equal', adjustable='box')
    
    
    
    
    
    
    plt.show()
    
    
    
#     thing = UniformAerosol("example", diameter_um, 10**11)
#     ecs = thing.calculate_effective_cross_section_sq_m(example_wavelength_um)
#     print(ecs)
    
#     visible_wavelengths = np.arange(0.4, 0.7, 0.1)
#     ecs_list = []
#     for wavelength_um in visible_wavelengths:
#         ecs = thing.calculate_effective_cross_section_sq_m(wavelength_um)
#         ecs_list.append(ecs_list)
#         
#         
#     plt.figure(ecs_list)
#     for 
    
if __name__ =="__main__":
    main()
    
    