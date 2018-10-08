'''
Created on Oct 8, 2018

@author: cdleong
'''
import pandas as pd #also need xlrd

class atmo_calculator(object):
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


def hydrostatic_molecular_density_at_altitude(altitude):
    pass

def calculate_effective_scale_height():
    

if __name__ == '__main__':
       
    bob = atmo_calculator()
    print(atmo_calculator.standard_atmo_gas_names)
    for b in atmo_calculator.standard_atmo_gas_names:
        print(b)
    
    
    
    
    
    