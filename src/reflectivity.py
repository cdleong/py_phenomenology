'''
Created on Sep 23, 2018

@author: cdleong
'''
import math

class SmoothDielectricSurface(object):
    '''
    classdocs
    n_t is self inde
    n_i is air
    theta_i is incident angle
    theta_t is transmission angle
    '''


    def __init__(self, index_of_refraction):
        '''
        Constructor
        '''
        self.index_of_refraction = index_of_refraction
        

    def get_reflection_angle(self, incidence_angle_degrees):
        return incidence_angle_degrees
    
    def get_transmission_angle_degrees(self, incidence_angle_degrees, other_medium_index_of_refraction=1.00):
        #snell's law, solved for angle of transmission
        # see https://www.omnicalculator.com/physics/snells-law for checking        
        incidence_angle_radians = math.radians(incidence_angle_degrees)
        answer = math.asin((other_medium_index_of_refraction*math.sin(incidence_angle_radians))/self.index_of_refraction)
        answer = math.degrees(answer)
        return answer
        

    def get_transverse_magnetic_light(self, incidence_angle_degrees, transmission_angle_degrees, other_medium_index_of_refraction=1.00):
        incidence_angle_radians = math.radians(incidence_angle_degrees)
        transmission_angle_radians = math.radians(transmission_angle_degrees)
                
        a = self.index_of_refraction * math.cos(incidence_angle_radians)
        b = other_medium_index_of_refraction * math.cos(transmission_angle_radians)
        numerator = -a + b 
        denominator = a + b
        fraction = numerator/denominator
        return fraction**2
        
         
    def get_transverse_electric_light(self, incidence_angle_degrees, transmission_angle_degrees, other_medium_index_of_refraction=1.00):
        incidence_angle_radians = math.radians(incidence_angle_degrees)
        transmission_angle_radians = math.radians(transmission_angle_degrees)
        a = other_medium_index_of_refraction*math.cos(incidence_angle_radians)
        b = self.index_of_refraction * math.cos(transmission_angle_radians)
        numerator = a - b
        denominator = a + b
        fraction = numerator/denominator
        return fraction**2
        
                
    def get_reflected_light(self, incidence_angle_degrees, other_medium_index_of_refraction=1.00):
        transmission_angle_degrees = self.get_transmission_angle_degrees(incidence_angle_degrees, other_medium_index_of_refraction)
        transverse_electric = self.get_transverse_electric_light(incidence_angle_degrees, transmission_angle_degrees, other_medium_index_of_refraction)
        transverse_magnetic =self.get_transverse_magnetic_light(incidence_angle_degrees, transmission_angle_degrees, other_medium_index_of_refraction)
        
        return transverse_electric, transverse_magnetic 
    
    def get_degree_of_polarization(self, incidence_angle_degrees, other_medium_index_of_refraction=1.00):
        transverse_electric, transverse_magnetic = self.get_reflected_light(incidence_angle_degrees, other_medium_index_of_refraction)
        return (transverse_electric - transverse_magnetic)/(transverse_electric + transverse_magnetic)

if __name__ == "__main__":
    glass = SmoothDielectricSurface(1.5)
    hood_surface = SmoothDielectricSurface(2.45)
    other_medium_index_of_refraction = 1.00
    incidence_angle_degrees = 30
    transverse_electric, transverse_magnetic = hood_surface.get_reflected_light(incidence_angle_degrees, other_medium_index_of_refraction)
    degree_of_polarization = hood_surface.get_degree_of_polarization(incidence_angle_degrees, other_medium_index_of_refraction)
    
    print(f"transverse_electric: {transverse_electric}")
    print(f"transverse_magnetic: {transverse_magnetic}")
    print(f"all reflected light: {transverse_magnetic+transverse_electric}")
    print(f"degree_of_polarization: {degree_of_polarization}")
    
    print(glass.get_degree_of_polarization(0))
    print(glass.get_degree_of_polarization(10))
    print(glass.get_degree_of_polarization(56.1))