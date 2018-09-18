'''
Created on Sep 3, 2018

@author: cdleong






'''
import logging
import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import pyphenom_physical_constants as ppc
import decimal
decimal.getcontext().prec = 100



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
        self.wavelengths = []
        self.constant_emissivity = decimal.Decimal(1.0)
        self.bbody_memo = {}
        
    def set_emissivity_from_csv(self, csv_path):
        with open(csv_path, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.wavelengths = []
            self.emissivities = []
            for row in csv_reader:
                self.wavelengths.append(row[0])
                self.emissivities.append(row[1])
                
        self.wavelengths = self.wavelengths[1:]
        self.emissivities = self.emissivities[1:]
        
        self.wavelengths = [decimal.Decimal(i) for i in self.wavelengths]
        self.emissivities = [decimal.Decimal(i) for i in self.emissivities]

    
    def set_constant_emissivity(self, constant_emissivity):
        self.constant_emissivity = decimal.Decimal(constant_emissivity)
        
    
    
    def calculate_blackbody_exitance_at_temp_and_wavelength(self, wavelength_um, temp_kelvin):
        try:
            return self.bbody_memo[(wavelength_um, temp_kelvin)]
        except:
            wavelength_um = decimal.Decimal(wavelength_um)
            temp_kelvin = decimal.Decimal(temp_kelvin)
            e_exponent = ppc.SECOND_RADIATION_CONSTANT/(wavelength_um*temp_kelvin)  
            
            wavelength_raised_to_power = decimal.Decimal(wavelength_um**5)
            
    #         e_raised_to_exponent = math.e**e_exponent # This gets very large sometimes
            e_raised_to_exponent = decimal.Decimal(math.e)**decimal.Decimal(e_exponent) # This gets very large sometimes
            bbody_exitance = decimal.Decimal(ppc.FIRST_RADIATION_CONSTANT)/((wavelength_raised_to_power)*(e_raised_to_exponent-decimal.Decimal(1.0)))
            self.bbody_memo[(wavelength_um, temp_kelvin)] = bbody_exitance
            return bbody_exitance
        
        
    def get_actual_emissivity_at_wavelength(self, wavelength_um):
        try:
            index = self.wavelengths.index(wavelength_um)
            return self.emissivities[index]
        except ValueError:
            # We don't have one, just return the constant emissivity
            return self.constant_emissivity
        
    
    def calculate_actual_exitance_from_wavelength_temp_and_emissivity(self, wavelength_um, temp_kelvin, emissivity):        
        return self.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)*decimal.Decimal(emissivity)
    
    
    def calculate_actual_exitance_at_temp_and_wavelength(self, wavelength_um, temp_kelvin):
        return self.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)*self.get_actual_emissivity_at_wavelength(wavelength_um)
    
    def estimate_black_and_grey_exitances_for_temp(self, temp_kelvin):
        blackbody_exitances = []
        graybody_exitances = []
        ratios = []
        wavelengths_um = self.wavelengths[self.wavelengths.index(1):]
#         wavelengths_um = self.wavelengths[self.wavelengths.index(0.5):]
#         wavelengths_um = self.wavelengths
        for wavelength_um in wavelengths_um:
                        
            # get blackbody emissivity
            blackbody_exitance = self.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
            
            # get actual emissivity
            emissivity = self.get_actual_emissivity_at_wavelength(wavelength_um)
            actual_exitance = self.calculate_actual_exitance_from_wavelength_temp_and_emissivity(wavelength_um, temp_kelvin, emissivity)
            
            blackbody_exitances.append(blackbody_exitance)
            graybody_exitances.append(actual_exitance)
            ratios.append(actual_exitance/blackbody_exitance)
            
            
        return blackbody_exitances, graybody_exitances, wavelengths_um, ratios

    def calculate_total_power_across_all_wavelengths_for_temp_if_blackbody(self, temp_kelvin):
        return ppc.STEFAN_BOLTZMANN_CONSTANT*temp_kelvin**4

    def calculate_total_power_across_all_wavelengths_for_temp_if_constant_emissivity(self, temp_kelvin):
        blackbody_power = self.calculate_total_power_across_all_wavelengths_for_temp_if_blackbody(temp_kelvin)
        actual_power = blackbody_power*self.constant_emissivity
        return actual_power
            
    def numerically_integrate_curve(self, list_of_x_values, list_of_y_values):
        list_of_x_values = [float(item) for item in list_of_x_values]
        list_of_y_values = [float(item) for item in list_of_y_values]
        
        return np.trapz(list_of_y_values, list_of_x_values)
    
    def calculate_temp_given_wavelength(self, wavelength_um):
        return ppc.WIENS_DISPLACEMENT_LAW_APPROXIMATION/wavelength_um
        
def graph_exitance_vs_wavelength_at_temp(wavelengths, exitances, temp_kelvin):
        # Graph it
    plt.figure()
    plt.title(f"Graph for Temp:{temp_kelvin}")
    plt.loglog(wavelengths, exitances)   
    plt.xlabel('wavelength (um)')
    plt.ylabel('Spectral Radiant Exitance (Watts per sq m per um)')    
        
def graph_blackbody_and_graybody_vs_wavelength_at_temp(wavelengths, blackbody_exitances, graybody_exitances, temp_kelvin):
    # Graph it
    plt.figure()
    plt.title(f"Graph for Temp:{temp_kelvin}")

    plt.loglog(wavelengths, blackbody_exitances)   
    plt.loglog(wavelengths, graybody_exitances)    

#     plt.scatter(wavelengths, blackbody_exitances)   
#     plt.scatter(wavelengths, graybody_exitances)    
    plt.xlabel('wavelength (um)')
    plt.ylabel('Spectral Radiant Exitance (Watts per sq m per um)')
    
        

def graph_ratios(wavelengths, ratios, temp_kelvin):
    # Graph it
    plt.figure()
    plt.title(f"Ratio for Temp:{temp_kelvin}")
    plt.scatter(wavelengths, ratios)
    plt.xlabel('wavelength (um)')
    plt.ylabel('actual/blackbody')    
    

def graph_power_vs_temp(temps_kelvin, powers_for_temps):
# Graph it
    plt.figure()
    plt.title(f"Total Power for each T:")
    plt.scatter(temps_kelvin, powers_for_temps)
    plt.xlabel('Temp (Kelvin)')
    plt.ylabel('Power (W)')    
      
def iii_10(my_gec):

    start_wavelength_um = 0.1
    stop_wavelength_um = 5
    wavelength_step_um = 0.01
    temp_kelvin = 2400
    exitances = []
    wavelengths = []
    for wavelength_um in np.arange(start_wavelength_um, stop_wavelength_um, wavelength_step_um):
        
#         print("")
        exitance = my_gec.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
        exitances.append(exitance)
        wavelengths.append(wavelength_um)
    
    max_exitance = np.max(exitances)
    print("exitances: {exitances[100:150]}")
    wavelength_of_max_exitance = wavelengths[exitances.index(max_exitance)]
    print("Max Exitance: {max_exitance}")
    print("Wavelength: {wavelength_of_max_exitance}")
    
    graph_exitance_vs_wavelength_at_temp(wavelengths, exitances, temp_kelvin)
    plt.show()
    

def III_2(my_gec):
    one_nanometer_in_um = 1 * 10 ** -3
    start_wavelength_um = 0.555 - one_nanometer_in_um
    stop_wavelength_um = 0.555 + one_nanometer_in_um
    wavelength_step_um = 0.000001
    temp_kelvin = 2400
    exitances = []
    wavelengths = []
    for wavelength_um in np.arange(start_wavelength_um, stop_wavelength_um, wavelength_step_um):
        exitance = my_gec.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
        exitances.append(exitance)
        wavelengths.append(wavelength_um)
    
    max_exitance = np.max(exitances)
    print("exitances: {exitances[100:150]}")
    wavelength_of_max_exitance = wavelengths[exitances.index(max_exitance)]
    print("Max Exitance: {max_exitance}")
    print("Wavelength: {wavelength_of_max_exitance}")

def do_c_III_1(my_gec):
    
    

    # computer_problem_c_III_1    
    temps= [300, 600, 900, 1200, 2400, 6000]
    for temp in temps:
        blackbody_exitances, graybody_exitances, wavelengths, ratios = my_gec.estimate_black_and_grey_exitances_for_temp(temp)
        graph_blackbody_and_graybody_vs_wavelength_at_temp(wavelengths, blackbody_exitances, graybody_exitances, temp)
        graph_ratios(wavelengths, ratios, temp)
                        
    plt.show()
    

def calculate_and_graph_total_power_for_temp_range(my_gec, start_temp_kelvin, stop_temp_kelvin, temp_step_kelvin):
    temps_kelvin = range(start_temp_kelvin, stop_temp_kelvin, temp_step_kelvin)
    powers_for_temps = []
    for cand_temp_kelvin in temps_kelvin:
        power_for_temp = my_gec.calculate_total_power_across_all_wavelengths_for_temp_if_constant_emissivity(cand_temp_kelvin)
        powers_for_temps.append(power_for_temp)
    
    graph_power_vs_temp(temps_kelvin, powers_for_temps)


def get_blackbody_and_graybody_exitances(my_gec, start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin):
    blackbody_exitances = [] 
    graybody_exitances = []
    wavelengths = np.arange(start_wavelength_um, stop_wavelength_um, wavelength_step_um)
    for wavelength_um in wavelengths:
        bbody_exitance = my_gec.calculate_blackbody_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
        blackbody_exitances.append(bbody_exitance)
        gbody_exitance = my_gec.calculate_actual_exitance_at_temp_and_wavelength(wavelength_um, temp_kelvin)
        graybody_exitances.append(gbody_exitance)
    
    return wavelengths, blackbody_exitances, graybody_exitances

def get_blackbody_and_graybody_and_ratios_and_graph_them(my_gec, start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin):

    wavelengths, blackbody_exitances, graybody_exitances = get_blackbody_and_graybody_exitances(my_gec, start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin)
    
    
    
    ratios = []
    for index, _ in enumerate(wavelengths):
        ratio = graybody_exitances[index]/blackbody_exitances[index]
        ratios.append(ratio)
    
    
    graph_exitance_vs_wavelength_at_temp(wavelengths, blackbody_exitances, temp_kelvin)
    
    graph_blackbody_and_graybody_vs_wavelength_at_temp(wavelengths, blackbody_exitances, graybody_exitances, temp_kelvin)
    
    graph_ratios(wavelengths, ratios, temp_kelvin)    
    
if __name__ == '__main__':
    my_gec = GraybodyEmissivityCalculator()
#     my_gec.set_emissivity_from_csv("../data/evansite_emissivity.csv")
    my_gec.set_constant_emissivity(0.7)
    

#     get_blackbody_and_graybody_and_ratios_and_graph_them(my_gec, start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin) 
    
    # Check every temperature from 2500 through 6000 in increments of 100K
    start_temp_kelvin = 5000
    stop_temp_kelvin = 6000
    temp_step_kelvin = 10
#     calculate_and_graph_total_power_for_temp_range(my_gec, start_temp_kelvin, stop_temp_kelvin, temp_step_kelvin)
    
    
    start_wavelength_um = decimal.Decimal(1.0)
    stop_wavelength_um = decimal.Decimal(2.0)
    wavelength_step_um = decimal.Decimal(0.01)
    
#     temps_kelvins = list(range(480,580,1))
#     powers_for_temps = []
#     
#     for temp_kelvin in temps_kelvins:
#         temp_kelvin = decimal.Decimal(temp_kelvin)
#         wavelengths, blackbody_exitances, graybody_exitances = get_blackbody_and_graybody_exitances(my_gec, start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin)
#         power_in_band = my_gec.numerically_integrate_curve(wavelengths, graybody_exitances)
#         powers_for_temps.append(power_in_band)
#         print(f"Calculated power in band for temp {temp_kelvin} K")
#   
#     graph_power_vs_temp(temps_kelvins, powers_for_temps)
    
    temp_kelvin = 1500
    
    
    wavelengths, blackbody_exitances, graybody_exitances = get_blackbody_and_graybody_exitances(my_gec, start_wavelength_um, stop_wavelength_um, wavelength_step_um, temp_kelvin)
    graph_exitance_vs_wavelength_at_temp(wavelengths, blackbody_exitances, temp_kelvin)
    print(my_gec.numerically_integrate_curve(wavelengths, graybody_exitances))
    
    one_exit = float(my_gec.calculate_blackbody_exitance_at_temp_and_wavelength(1.0, temp_kelvin))
    two_exit = float(my_gec.calculate_blackbody_exitance_at_temp_and_wavelength(2.0, temp_kelvin))
    ratio = one_exit/two_exit
    print(f"blackbody exitance at 1 um: {one_exit}")
    print(f"blackbody exitance at 2 um: {two_exit}")
    print(f"ratio: {ratio}")
    
    plt.show()
    
    
    
    