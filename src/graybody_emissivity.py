'''
Created on Sep 3, 2018

@author: cdleong



'''
import logging
import csv
import numpy as np
import math
import matplotlib.pyplot as plt

import decimal
decimal.getcontext().prec = 100

# CONSTANTS
FIRST_RADIATION_CONSTANT = 3.742*10.0**8  # W*um^4*m^-2
SECOND_RADIATION_CONSTANT = 1.438*10.0**4  # um*K
SPEED_OF_LIGHT_MICRONS_PER_SECOND =  3.0*10.0**8*10.0**6 # speed of light in micrometers per second
PLANCK_CONSTANT = 6.63*10.0**-34 # J *S

class GraybodyEmissivityCalculator(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        # setup logging
        self.logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        self.logger.info(self)
        
    def read_csv(self, csv_path):
        with open(csv_path, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.wavelengths = []
            self.emissivities = []
            for row in csv_reader:
                self.wavelengths.append(row[0])
                self.emissivities.append(row[1])
                
        self.wavelengths = self.wavelengths[1:]
        self.emissivities = self.emissivities[1:]
        
        self.wavelengths = [float(i) for i in self.wavelengths]
        self.emissivities = [float(i) for i in self.emissivities]

    
    def calculate_blackbody_exitance_at_temp_and_wavelength(self, wavelength_um, temp_kelvin):
        wavelength_um = float(wavelength_um)
        temp_kelvin = float(temp_kelvin)
        e_exponent = SECOND_RADIATION_CONSTANT/(wavelength_um*temp_kelvin)  
        
        wavelength_raised_to_power = decimal.Decimal(wavelength_um**5)
        
#         e_raised_to_exponent = math.e**e_exponent # This gets very large sometimes
        e_raised_to_exponent = decimal.Decimal(math.e)**decimal.Decimal(e_exponent) # This gets very large sometimes
        bbody_exitance = decimal.Decimal(FIRST_RADIATION_CONSTANT)/((wavelength_raised_to_power)*(e_raised_to_exponent-decimal.Decimal(1.0)))
        
        return bbody_exitance
        
        
    def get_actual_emissivity_at_wavelength(self, wavelength_um):
        index = self.wavelengths.index(wavelength_um)
        return self.emissivities[index]
    
    def actual_exitance(self, wavelength_um, temp_kelvin, emissivity):
        return self.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)*decimal.Decimal(emissivity)
    
    def estimate_thing_for_temp(self, temp_kelvin):
        blackbody_exitances = []
        graybody_exitances = []
        wavelengths_um = self.wavelengths[self.wavelengths.index(1):]
        for wavelength_um in wavelengths_um:
                        
            # get blackbody emissivity
            blackbody_exitance = self.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
            
            # get actual emissivity
            emissivity = self.get_actual_emissivity_at_wavelength(wavelength_um)
            actual_exitance = self.actual_exitance(wavelength_um, temp_kelvin, emissivity)
            
            blackbody_exitances.append(blackbody_exitance)
            graybody_exitances.append(actual_exitance)
            
            
        return blackbody_exitances, graybody_exitances, wavelengths_um
            
        
def graph_things(wavelengths, blackbody_exitances, graybody_exitances, temp_kelvin):
    # Graph it
    plt.figure()
    plt.title(f"Graph for Temp:{temp_kelvin}")
    plt.loglog(wavelengths, blackbody_exitances)   
    plt.loglog(wavelengths, graybody_exitances)    
    plt.xlabel('wavelength (um)')
    plt.ylabel('Spectral Radiant Exitance (Watts per sq m per um)')    
    
      

def III_2(my_gec):
    one_nanometer_in_um = 1 * 10 ** -3
    start_wavelength = 0.555 - one_nanometer_in_um
    stop_wavelength = 0.555 + one_nanometer_in_um
    wavelength_step = 0.000001
    temp_kelvin = 2400
    exitances = []
    wavelengths = []
    for wavelength_um in np.arange(start_wavelength, stop_wavelength, wavelength_step):
        exitance = my_gec.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
        exitances.append(exitance)
        wavelengths.append(wavelength_um)
    
    max_exitance = np.max(exitances)
    print("exitances: {exitances[100:150]}")
    wavelength_of_max_exitance = wavelengths[exitances.index(max_exitance)]
    print("Max Exitance: {max_exitance}")
    print("Wavelength: {wavelength_of_max_exitance}")

def do_c_III_1(my_gec):
    
    
#     for w in my_gec.wavelengths:
#         my_gec.logger.debug(w)
#         my_gec.logger.debug(my_gec.get_actual_emissivity_at_wavelength(w))
        
        
    

    # computer_problem_c_III_1    
    temps= [300, 600, 900, 1200]
    for temp in temps:
        blackbody_exitances, graybody_exitances, wavelengths = my_gec.estimate_thing_for_temp(temp)
        graph_things(wavelengths, blackbody_exitances, graybody_exitances, temp)
                        
    plt.show()
    
if __name__ == '__main__':
    my_gec = GraybodyEmissivityCalculator()
    my_gec.read_csv("../data/evansite_emissivity.csv")
    do_c_III_1(my_gec)
     
     
     
#     III_2(my_gec)
     