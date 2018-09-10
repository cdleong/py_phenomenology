import logging
import numpy as np
import itertools
import decimal
decimal.getcontext().prec = 100
import pyphenom_physical_constants as ppc

class Atom(object):
    '''
    classdocs
    '''
    

    def __init__(self, name, energy_levels_ev):
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
        
        self.name=name
        
        
        self.energy_levels_ev = [decimal.Decimal(item) for item in energy_levels_ev]
        self.energy_levels_ev.sort()
        
        self.energy_deltas_ev = self.calculate_possible_energy_deltas_ev(self.energy_levels_ev)
        self.possible_photon_wavelengths_um = self.calculate_possible_photon_wavelengths_um(self.energy_deltas_ev)
        
        
    def calculate_possible_energy_deltas_ev(self, energy_levels_ev):
        
        
        print(f"Calculating possible deltas for energy levels {energy_levels_ev} eV")
        
        energy_level_combinations = itertools.combinations(energy_levels_ev, 2)
        print(energy_level_combinations)
        
        energy_deltas = []
        for index, energy_level_combination in enumerate(energy_level_combinations):
            delta_ev = max(energy_level_combination) - min(energy_level_combination)
#             self.logger.debug(f"index: {index}, energy (eV): {energy_level_combination}, delta (eV): {delta_ev}")
            energy_deltas.append(delta_ev)
            
        return energy_deltas
             
    def calculate_possible_photon_wavelengths_um(self, energy_deltas_ev):
        wavelengths_um = []
        for delta_ev in energy_deltas_ev:
            wavelength_um = self.calculate_photon_wavelength_for_delta(delta_ev)
            self.logger.debug(f"for delta={delta_ev:.5f} eV, wavelength is: {wavelength_um:.5f} um")
            wavelengths_um.append(wavelength_um)
            
        return wavelengths_um
        
        
    def calculate_photon_wavelength_for_delta(self, delta_ev):
        wavelength_um = (ppc.PLANCK_CONSTANT_EV_SECONDS*ppc.SPEED_OF_LIGHT_MICRONS_PER_SECOND)/delta_ev
        return wavelength_um
    
    def get_energy_level_at_principle_quantum_number(self, principle_quantum_number):
        return self.energy_levels_ev[principle_quantum_number-1] #TODO: more elegant solution
    
    def get_energy_delta_for_transition(self, start_level_principle_quantum_number, stop_level_principle_quantum_number):
        start_level_energy_ev = self.get_energy_level_at_principle_quantum_number(start_level_principle_quantum_number)
        stop_level_energy_ev = self.get_energy_level_at_principle_quantum_number(stop_level_principle_quantum_number)
        return stop_level_energy_ev - start_level_energy_ev
        

def calculate_approximate_electronic_energy_level_of_hydrogen(principle_quantum_number):
    energy_level = -13.6/principle_quantum_number**2
    return energy_level
    

def main():
#     energy_levels_ev = [-13.6, -3.4, -1.51, 0] # Hydrogen from slides
    energy_levels_ev = [-15.0, -3.75, -1.67, -0.94, -0.6] # mystery atom from HW problem IV-3


    energy_levels_ev = [decimal.Decimal(energy_level_ev) for energy_level_ev in energy_levels_ev]
    my_atom = Atom("Atom from HW problem IV-3",energy_levels_ev)
    
    energy_deltas_ev = my_atom.energy_deltas_ev
    energy_deltas_ev = [float(item) for item in energy_deltas_ev]
#     energy_deltas_ev.sort(reverse=True)
    my_atom.logger.info(energy_deltas_ev)
    
    possible_photon_wavelengths_um = my_atom.possible_photon_wavelengths_um
    possible_photon_wavelengths_nanometers = [float(item)*1000 for item in possible_photon_wavelengths_um]
    possible_photon_wavelengths_nanometers = [round(item, 2) for item in possible_photon_wavelengths_nanometers]
    possible_photon_wavelengths_nanometers.sort()
#     possible_photon_wavelengths_nanometers.sort()
    print(f"Possible photon wavelengths for {my_atom.name} (nm): {possible_photon_wavelengths_nanometers}")
    
    principle_quantum_numbers = list(range(1, 5)) # Should give me 1 through 4
    hydrogen_electronic_energy_levels = []
    for principle_quantum_number in principle_quantum_numbers:
        hydrogen_electronic_energy_level = calculate_approximate_electronic_energy_level_of_hydrogen(principle_quantum_number)
        hydrogen_electronic_energy_levels.append(hydrogen_electronic_energy_level)
        
    
    print(f"{principle_quantum_numbers}")
    print(f"{[float(item) for item in hydrogen_electronic_energy_levels]}")
    
    hydrogen_atom = Atom("Hydrogen",hydrogen_electronic_energy_levels)
    
    hydrogen_1_to_4_transition_energy_ev = hydrogen_atom.get_energy_delta_for_transition(1, 4)
    print(round(hydrogen_1_to_4_transition_energy_ev, 2))
    
    hydrogen_1_to_4_transition_photon_wavelength = hydrogen_atom.calculate_photon_wavelength_for_delta(hydrogen_1_to_4_transition_energy_ev)
    print(round(hydrogen_1_to_4_transition_photon_wavelength,5))
    
#     for i in range(1,4): 
#         relaxing_delta_ev = abs(hydrogen_atom.get_energy_delta_for_transition(4,i))
#         relaxing_wavelength_um = hydrogen_atom.calculate_photon_wavelength_for_delta(relaxing_delta_ev)
#         relaxing_wavelength_nm = relaxing_wavelength_um * 10**3
#         print(f"""Relaxing from principle quantum number 4 to {i}: 
#         delta = ~{relaxing_delta_ev:.2f} eV, 
#         wavelength = ~{relaxing_wavelength_um:.2f} um or {relaxing_wavelength_nm:.2f} nm""")
    
    
    for i in range(4, 0, -1):        
        for j in range(i-1, 0, -1):
            relaxing_delta_ev = hydrogen_atom.get_energy_delta_for_transition(i,j)
            relaxing_wavelength_um = hydrogen_atom.calculate_photon_wavelength_for_delta(abs(relaxing_delta_ev))
            relaxing_wavelength_nm = relaxing_wavelength_um * 10**3
            energy_level_ev_start = hydrogen_atom.get_energy_level_at_principle_quantum_number(i)
            energy_level_ev_end = hydrogen_atom.get_energy_level_at_principle_quantum_number(j)
            print(f"""Relaxing from principle quantum number {i} ({energy_level_ev_start:.2f} eV) to {j} ({energy_level_ev_end:.2f} eV): 
            delta = ~{relaxing_delta_ev:.2f} eV, 
            wavelength = ~{relaxing_wavelength_um:.2f} um or {relaxing_wavelength_nm:.2f} nm""")
    
    
if __name__ == "__main__":
    main()    