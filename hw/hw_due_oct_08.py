'''
Created on Oct 7, 2018

@author: cdleong
'''
import radiometry
import numpy as np
import math
import matplotlib.pyplot as plt
from solid_angles import calculate_area_subtended_by_fov
import atmosphere

def vii_7():
    x_meters = 10.0
    intensity_watts_per_steradian = 100.0
    h_meters_values = np.arange(0.1, 10.0, 0.1)
    
    
    # find irradiance at different distances
    irradiances_at_distances = []
    for h_meters in h_meters_values:
        distance_r_meters = math.hypot(x_meters, h_meters)
        cosine_theta_r = x_meters/h_meters        
        theta_r_degrees = math.degrees(math.atan(cosine_theta_r))
        
    
        irradiance_watts_per_sq_m = radiometry.irradiance_on_aperture_from_point_source(distance_r_meters, intensity_watts_per_steradian, theta_r_degrees)
        e_at_h = (h_meters, irradiance_watts_per_sq_m)
        irradiances_at_distances.append(e_at_h)
        print(f"at h = {h_meters}:, \n\tr = {distance_r_meters}, \n\ttheta_r_degrees = {theta_r_degrees}, and irradiance = {irradiance_watts_per_sq_m}")

    x_values, y_values = zip(*irradiances_at_distances)
    
    # find the max
    max_irradiance = max(y_values)
    max_irradiance_index = y_values.index(max_irradiance)
    print(f"max irradiance: {max_irradiance}")
    max_irradiance_h = x_values[max_irradiance_index]
    print(f"max irradiance h: {max_irradiance_h}")
    
    print(max_irradiance_index)
    print(np.argmax(irradiances_at_distances, 0)) # experimenting with argmax. 
    print(irradiances_at_distances[max_irradiance_index]) # this works also 
    
    
    # Graph the calculations    
    plt.figure()    
    plt.title(f"irradiance vs distance h, intensity={intensity_watts_per_steradian} W/sr, x = 10m")
    plt.xlabel('h (m)')
    plt.ylabel('irradiance (watts per sr)')
    
    plt.scatter(x_values, y_values)
#     plt.semilogy(x_values, y_values)    
    plt.show()
    

def vii_9():
    pass

def vii_10_a():
    
    radius_of_earth_km = 6371
    radius_of_satellite_km = 0.5 / 1000
    altitude_of_satellite_km = 200
    
    xlim = 20000
    ylim = 10000
    
    fig, ax = plt.subplots()    
    patches = []
    
    
    # Plot the Earth
    earth_x = xlim/2
    earth_y = 0
    earth_circle = plt.Circle((earth_x,earth_y), radius_of_earth_km, color='DarkBlue')

    # Plot the Sat
    sat_x = 10000
    sat_y = radius_of_earth_km+altitude_of_satellite_km
    how_big_to_draw_satellite = radius_of_satellite_km*1
    sat_circle = plt.Circle((sat_x, sat_y), how_big_to_draw_satellite, color="DarkGray")
    sat_circle.set_color("DarkGray")
    
    # Optionally, make a nice circle around the satellite, touching the ground
    sensor_circle = plt.Circle((sat_x, sat_y), altitude_of_satellite_km, edgecolor = "Black", fill = False)
    
    
    # draw a line from the sat to the ground
    ground_right_below_sat_x = sat_x
    ground_right_below_sat_y = radius_of_earth_km    
    ground_sat_line = plt.Line2D([sat_x, ground_right_below_sat_x], [sat_y, ground_right_below_sat_y], color="Black")

    ##############################
    # Draw a line at 45 degrees

    # given length of side we want
    length_desired = 400 # right into the Earth please
    
    # and angle...
    angle_desired_degrees = 45
    angle_desire_rad = math.radians(angle_desired_degrees)
    
    # new x, new_y = 
    delta_x = length_desired*math.cos(angle_desire_rad)
    delta_y = length_desired*math.sin(angle_desire_rad)
    
    new_x = sat_x + delta_x
    new_y = sat_y - delta_y
    
    sat_target_line = plt.Line2D([sat_x, new_x], [sat_y, new_y], color="Red")
    
    
    ######################################################
    # Atmosphere circle
    atm_x = earth_x
    atm_y = earth_y
    
    # Karman line: 100km
    karman_line = 100
    atm_radius = radius_of_earth_km + karman_line
    atm_circle = plt.Circle((atm_x, atm_y), atm_radius, edgecolor = "Blue", fill = False)

    # add artists
    ax.add_artist(earth_circle)
    ax.add_artist(sat_circle)
#     ax.add_artist(sensor_circle)
    ax.add_artist(ground_sat_line)
    ax.add_artist(sat_target_line)
    ax.add_artist(atm_circle)
    
    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)
#     ax.set_facecolor("Black")
    
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.title("Earth and Satellite, to scale, with sensor-target line and Karman line")
    
    plt.xlabel('km')
    plt.ylabel('km')
    
    # calculate distance, given values gleaned from plot
    target_x = 10203
    target_y = 6368
    dist = math.hypot(target_x - sat_x, target_y - sat_y)
    print(f"sat-target distance: {dist}")
    
    # calculate distance, given values gleaned from plot
    hit_atmo_x = 10100
    hit_atmo_y = 6470
    atmo_dist = math.hypot(target_x - hit_atmo_x, target_y - hit_atmo_y)
    print(f"the sensor has to look through: {atmo_dist} km of atmo")
    
    
    plt.show()


def vii_10_b():
    sat_target_distance_km = 287.0853531617383  # from part a
    distance_r_meters = sat_target_distance_km*1000  # 1000 meters per kilometer
    fov_sr = 0.004
    source_area_sq_m = calculate_area_subtended_by_fov(distance_r_meters, fov_sr)
    source_area_sq_km = source_area_sq_m / 1e6
    print(f"The source area is {source_area_sq_m} square meters, or {source_area_sq_km} square km")

def c_iii_1():
    sa = atmosphere.Atmosphere()
    
    
    altitudes_km = []
    molecular_densities_per_cubic_cm = []
    pressures = []
    sums_of_ppms = []
    for index, row in sa.atmo_df.iterrows():
        alt_km = row["ALT"]
        density_inv_cubic_cm = row["DENSITY"]
        pressure_millbar = row["PRES"]
        
        altitudes_km.append(alt_km)
        molecular_densities_per_cubic_cm.append(density_inv_cubic_cm)
        pressures.append(pressure_millbar)
        
        sum_of_ppm = 0.0
        
        for gas_name in atmosphere.Atmosphere.standard_atmo_gas_names:
            gas_ppm = row[gas_name]
            print(f"    at alt {alt_km}, {gas_name} has {gas_ppm} ppm")
            sum_of_ppm = sum_of_ppm + gas_ppm

        percent_of_million = sum_of_ppm/1000000
        sums_of_ppms.append(sum_of_ppm)
        print(f"at altitude {alt_km}, density is {density_inv_cubic_cm}, pressure is {pressure_millbar} mb, sum of ppm figures is {sum_of_ppm}, or {percent_of_million} fraction")
        
    plt.figure()
    plt.title("Molecular density vs altitude, US Standard Atmo")    
    plt.scatter(molecular_densities_per_cubic_cm, altitudes_km)    
    plt.xlabel('molecular density per cubic centimeter')    
    plt.ylabel('altitude, km')
     
     
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
    
    plt.figure()
    plt.title("sum of ppms/one million vs altitude")    
    plt.xlabel('% of one million')   
    plt.ylabel('altitude, km')
    percent_values = [(x/1000000)*100 for x in sums_of_ppms]
    plt.plot(percent_values, altitudes_km)
    
    
    
        
    plt.show()
    plt.title("Molecular density vs altitude, US Standard Atmo")    


if __name__ == '__main__':
    print("hello world")
#     vii_7()
#     vii_10_a()
#     vii_10_b()
    c_iii_1()
    
    
    
    