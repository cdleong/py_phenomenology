'''
Created on Sep 3, 2018

@author: cdleong
'''
import logging
import csv
import numpy as np
# import matplotlib.pyplot as plt



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
    
    def blackbody_exitance_at_temp_and_wavelength(self, wavelength_um, temp_kelvin):
        print("TODO")
        
    def get_actual_emissivity_at_wavelength(self, wavelength_um):
        index = self.wavelengths.index(wavelength_um)
        return self.emissivities[index]
    
    def actual_exitance(self, wavelength_um, temp_kelvin):
        print("TODO")
    
    def estimate_graybody_emissivity_at_temp_for_band(self, temp_kelvin):
        ratios = []
        for wavelength_um in self.wavelengths:
            
            
            # get blackbody emissivity
            blackbody_exitance = self.blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
            
            # get actual emissivity
            actual_exitance = self.get_actual_emissivity_at_wavelength(wavelength_um)*blackbody_exitance
            self.logger.debug(actual_exitance)
            
            # Get the ratio
            ratio = blackbody_exitance/actual_exitance
            ratios.append(ratio)
            
        
        return np.average(ratios)


            

if __name__ == '__main__':
    my_gec = GraybodyEmissivityCalculator()
    my_gec.read_csv("../data/evansite_emissivity.csv")
    
    for w in my_gec.wavelengths:
        my_gec.logger.debug(w)
        my_gec.logger.debug(my_gec.get_actual_emissivity_at_wavelength(w))
        
        
    

    # computer_problem_c_III_1    
    temps= [300, 600, 900, 1200]
    for temp in temps:
        my_gec.estimate_graybody_emissivity_at_temp_for_band(temp)
        