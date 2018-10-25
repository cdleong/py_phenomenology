'''
Created on Oct 9, 2018

@author: cdleong
'''
import matplotlib.pyplot as plt
import numpy as np
from pyphenom import atmosphere


def c_iii_1_a(molecular_densities_per_cubic_cm, altitudes_km):
    plt.figure()
    plt.title("US Standard Atmo density vs altitude")    
    plt.plot(molecular_densities_per_cubic_cm, altitudes_km)    
    plt.xlabel('molecular density per cubic centimeter')    
    plt.ylabel('altitude, km')
    
    scale_height_m = atmosphere.calculate_isothermal_atmo_scale_height_meters(temp_kelvin=300)
    hydrostatic_densities_per_cubic_centimeter = []
    for altitude_km in altitudes_km:
        altitude_meters = altitude_km * 1000
        hydrostatic_density_per_cubic_meter = atmosphere.hydrostatic_molecular_density_at_altitude_per_cubic_meter(altitude_meters, scale_height_m)
        hydrostatic_density_per_cubic_centimeter = hydrostatic_density_per_cubic_meter / 10**6
        print(f"at altitude = {altitude_meters}, hydrostatic_density_per_cubic_centimeter is {hydrostatic_density_per_cubic_centimeter}")
        
        hydrostatic_densities_per_cubic_centimeter.append(hydrostatic_density_per_cubic_centimeter)
    
    plt.figure()
    plt.title("Hydrostatic density vs altitude")    
    plt.plot(hydrostatic_densities_per_cubic_centimeter, altitudes_km)
    plt.xlabel('molecular density per cubic centimeter')    
    plt.ylabel('altitude, km')  
    
    plt.figure()
    plt.title("Hydrostatic and US Standard Atmo densities, vs altitude")    
    plt.plot(molecular_densities_per_cubic_cm, altitudes_km, label="Standard Atmo")    
    plt.plot(hydrostatic_densities_per_cubic_centimeter, altitudes_km, label="Hydrostatic")
    plt.xlabel('molecular density per cubic centimeter')    
    plt.ylabel('altitude, km')    
    plt.legend()
    


def c_iii_1_b(molecular_densities_per_cubic_cm, pressures, altitudes_km):
    plt.figure()
    plt.title("Pressure vs density")
    plt.plot(pressures, molecular_densities_per_cubic_cm)
    plt.xlabel('pressure, millibars')
    plt.ylabel('molecular density per cubic centimeter')
     
    fig, ax1 = plt.subplots()
    plt.title("Pressure and density vs alt")
    plt.ylabel('altitude, km')
     
    ax1.set_xlabel("molecular density per cubic centimeter")
    ax1.plot(molecular_densities_per_cubic_cm, altitudes_km, color='b')
     
    ax2 = ax1.twiny()
    ax2.set_xlabel("pressure milllibars")
    ax2.plot(pressures, altitudes_km, color='r')
#     fig.tight_layout()    

def c_iii_1_c(sums_of_ppms, dict_of_lists_of_percents_for_each_gas,  altitudes_km):
    
    plt.figure()
    plt.title("sum of ppms/one million vs altitude")    
    plt.xlabel('% of one million')   
    plt.ylabel('altitude, km')
    percent_values = [(x/1000000)*100 for x in sums_of_ppms]
    plt.plot(percent_values, altitudes_km)    
    
    
    

    
     
    
    fig, ax = plt.subplots()
    plt.title("Stacked Area Chart, because it looks cool!") 
    x_values = altitudes_km
    y_values = []
    y_labels = []
    
    

    for gas_name in dict_of_lists_of_percents_for_each_gas:
        list_of_values_for_gas = dict_of_lists_of_percents_for_each_gas[gas_name]
        print(f"GAS NAME: {gas_name}")
        print(f"{list_of_values_for_gas}")
        print(f"{len(list_of_values_for_gas)}")
        
        
        y_values.append(list_of_values_for_gas)
        y_labels.append(gas_name)

         
    zipped_lists = list(zip(y_labels, y_values))
    print(zipped_lists)
    
    for item in zipped_lists:
        print(item[0])
        print(item[1][0])
        
    print()
    zipped_lists= sorted(zipped_lists, key=lambda x: x[1][0], reverse=True)
    
    
    for item in zipped_lists:
        print(item[0])
        print(item[1][0])
        

    y_labels, y_values  = zip(*zipped_lists)
    y_values = list(y_values)
    ax.stackplot(x_values, y_values, labels=y_labels)
    plt.legend(loc='upper right')
    plt.ylabel('Proportion of 1 million parts')   
    plt.xlabel('altitude, km')


    

    

def c_iii_1():
    sa = atmosphere.Atmosphere()
    
    
    altitudes_km = []
    molecular_densities_per_cubic_cm = []
    pressures = []
    sums_of_ppms = []
    dict_of_lists_of_percents_for_each_gas = {}
    one_million = 1000000
    for _, row in sa.atmo_df.iterrows():
        
        alt_km = row["ALT"]
        density_inv_cubic_cm = row["DENSITY"]
        pressure_millbar = row["PRES"]
        
        
        
        altitudes_km.append(alt_km)
        molecular_densities_per_cubic_cm.append(density_inv_cubic_cm)
        pressures.append(pressure_millbar)
        
        sum_of_ppm = 0.0
        
        for gas_name in atmosphere.Atmosphere.standard_atmo_gas_names:
            
            if gas_name not in dict_of_lists_of_percents_for_each_gas:
                dict_of_lists_of_percents_for_each_gas[gas_name] = []
                
            gas_ppm = row[gas_name]
            
            sum_of_ppm = sum_of_ppm + gas_ppm

            # calculate percentage for each gas:
            gas_percentage = gas_ppm/one_million
            
            
            dict_of_lists_of_percents_for_each_gas[gas_name].append(gas_percentage)
            print(f"    at alt {alt_km}, {gas_name} has {gas_ppm} ppm, which is {gas_percentage*100} percent of 1 million")
            
        
        percent_of_million = sum_of_ppm/one_million
        sums_of_ppms.append(sum_of_ppm)
        print(f"at altitude {alt_km}, density is {density_inv_cubic_cm}, pressure is {pressure_millbar} mb, sum of ppm figures is {sum_of_ppm}, or {percent_of_million} fraction")
        
        
        
        
    
#     c_iii_1_a(molecular_densities_per_cubic_cm, altitudes_km)
     
     
#     c_iii_1_b(molecular_densities_per_cubic_cm, pressures, altitudes_km)

    c_iii_1_c(sums_of_ppms, dict_of_lists_of_percents_for_each_gas, altitudes_km)

    

    plt.show()



if __name__ == '__main__':
    c_iii_1()
