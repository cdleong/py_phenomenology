'''
Created on Oct 6, 2018

@author: cdleong
'''
import math
import numpy as np
import matplotlib.pyplot as plt

def irradiance_on_aperture_from_point_source(distance_r_meters, intensity_watts_per_steradian, theta_r_degrees):
    # E = (I/R^2)*cos
    theta_r_radians = math.radians(theta_r_degrees)
    irradiance_watts_per_sq_m = math.cos(theta_r_radians)*intensity_watts_per_steradian/(distance_r_meters**2)
    return irradiance_watts_per_sq_m


if __name__ == '__main__':
    
    # Testing irradiance_on_aperture_from_point_source
    angles = np.arange(0,180,0.1)
    intensity_watts_per_steradian = 100.00
    distance_r_meters = 10.0
    
    # Testing vs angle
    irradiance_at_angle = []
    for theta_r_degrees in angles: 
        irradiance = irradiance_on_aperture_from_point_source(distance_r_meters, intensity_watts_per_steradian, theta_r_degrees)
        print(irradiance)
        irradiance_at_angle.append((theta_r_degrees, irradiance))
        
    plt.figure()
    plt.title(f"irradiance vs angle, intensity={intensity_watts_per_steradian} W/sr, distance={distance_r_meters}")
    plt.xlabel('angle (degrees)')
    plt.ylabel('irradiance (watts per sr)')
    x_values, y_values = zip(*irradiance_at_angle)
    plt.scatter(x_values, y_values)
    
    
    # Testing vs distance    
    plt.figure()
    
    theta_r_degrees = 0.0
    distances_r_meters = np.arange(0,10.0, 0.1)
    irradiance_at_distance = []
    for distance_r_meters in distances_r_meters:
        irradiance = irradiance_on_aperture_from_point_source(distance_r_meters, intensity_watts_per_steradian, theta_r_degrees)
        irradiance_at_distance.append((distance_r_meters, irradiance))
        
    
    plt.title(f"irradiance vs distance, theta_r = {theta_r_degrees} degrees, intensity = intensity={intensity_watts_per_steradian} W/sr")
    plt.xlabel('distance (m)')
    plt.ylabel('irradiance (watts per sr)')
    x_values, y_values = zip(*irradiance_at_distance)
#     plt.scatter(x_values, y_values)
    plt.semilogy(x_values, y_values)
    
    
    
    
    plt.show()