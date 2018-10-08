'''
Created on Oct 7, 2018

@author: cdleong
'''
import radiometry
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib

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

def vii_10():
    
    radius_of_earth_km = 6371
    radius_of_satellite_km = 0.5 / 1000
    altitude_of_satellite_km = 200
    
    xlim = 20000
    ylim = 20000
    
    fig, ax = plt.subplots()    
    patches = []
    
    earth_x = xlim/2
    earth_y = 0
    earth_circle = plt.Circle((earth_x,earth_y), radius_of_earth_km, color='DarkBlue')

    
    sat_x = 10000
    sat_y = radius_of_earth_km+altitude_of_satellite_km
    sat_circle = plt.Circle((sat_x, sat_y), radius_of_satellite_km, color="DarkGray")
    sat_circle.set_color("DarkGray")

    ax.add_artist(earth_circle)
    ax.add_artist(sat_circle)
    
    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)
#     ax.set_facecolor("Black")
    
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.title("The situation")
    plt.show()


if __name__ == '__main__':
#     vii_7()
    vii_10()