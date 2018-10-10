'''
Created on Oct 8, 2018

@author: cdleong
'''
import pandas as pd #also need xlrd
import math
import pyphenom_physical_constants

APPROXIMATE_MEAN_MOLECULAR_MASS_OF_EARTH_ATMOSPHERE_KG = 4.79*10**-26

class Atmosphere(object):
    standard_atmo_gas_names = "N2    O2    H2O    CO2    O3    N2O    CO    CH4    NO    SO2    NO2    NH3    HNO3    OH    HF    HCL    HBR    HI    CLO    OCS    H2CO    HOCL    HCN    CH3CL    H2O2    C2H2    C2H6    PH3".split()
    def __init__(self, file_path="../data/Atmosphere Model.xls"):
        self.file_path = file_path
        self.atmo_df = self.load_standard_atmo()
        self.molecular_mass_df = self.load_molecular_mass() 
        

    def load_molecular_mass(self):
        sheet_name = "Molecular Mass"
        molecular_mass_df = pd.read_excel(self.file_path,sheet_name=sheet_name)
        print(f"loaded columns {molecular_mass_df.keys()} from sheet {sheet_name}")
        return molecular_mass_df
        
        
         
    def load_standard_atmo(self):
        # read standard atmo sheet
        sheet_name = "US STANDARD ATMOSPHERE"
        
        #The _second_ row is the header row
        header_row = 1
        
        standard_atmo_df = pd.read_excel(self.file_path,sheet_name=sheet_name, header=header_row)
        
        
        # delete the units row
        units_row = standard_atmo_df.index[0]
        standard_atmo_df = standard_atmo_df.drop(units_row)
        
#         print(standard_atmo_df)
        return standard_atmo_df


def hydrostatic_molecular_density_at_altitude(altitude_meters, 
                                              scale_height=None):
    n_zero = pyphenom_physical_constants.LOSCHMIDTS_NUMBER
    
    # If scale height not given, calculate with default settings
    if not scale_height:
        scale_height = calculate_isothermal_atmo_scale_height_meters()

    exponent_term = -altitude_meters/scale_height
    molecular_density_at_altitude = n_zero*math.pow(math.e, exponent_term)
    return molecular_density_at_altitude
    

def calculate_isothermal_atmo_scale_height_meters(temp_kelvin=pyphenom_physical_constants.APPROXIMATE_TEMPERATURE_OF_EARTH_KELVINS, # avg temperature of Earth, Earth stuff 
                                           mean_molecular_mass_kg=APPROXIMATE_MEAN_MOLECULAR_MASS_OF_EARTH_ATMOSPHERE_KG):
    """assuming isothermal and using an estimated mean molecular mass"""
    
    k_b = float(pyphenom_physical_constants.BOLTZMANN_CONSTANT) # J/K
    
    g = pyphenom_physical_constants.GRAVITY_ON_EARTH   # meters per second per second
    scale_height_m = k_b*temp_kelvin/(mean_molecular_mass_kg*g) # meters
    return scale_height_m


if __name__ == '__main__':
       
#     bob = Atmosphere()
#     print(Atmosphere.standard_atmo_gas_names)
#     for b in Atmosphere.standard_atmo_gas_names:
#         print(b)
        
    # test molecular density at altitude
    scale_height_m = calculate_isothermal_atmo_scale_height_meters()
    print(f"isothermal atmosphere scale height: {scale_height_m}")
    print(f"Internet says we should get about 8km for Earth's atmosphere")
    
    sea_level_density = hydrostatic_molecular_density_at_altitude(0, scale_height_m)
    scale_height_density = hydrostatic_molecular_density_at_altitude(scale_height_m, scale_height_m)
    ratio = scale_height_density/sea_level_density
    one_over_e = 1/math.e
    print(f"at alt= 0, molecular density is {sea_level_density}")
    print(f"at alt= {scale_height_m} meters, molecular density is {scale_height_density}")
    print(f"1/e is: {one_over_e}, scale_height_density/sea_level_density is {ratio}")
    
        
        
    
    
    
    
    
    
    