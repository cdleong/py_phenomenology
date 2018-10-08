'''
Created on Sep 25, 2018

@author: cdleong
'''

import math

def calculate_exact_round_fov(cone_angle_alpha_radians):
    return 2*math.pi*(1-math.cos(cone_angle_alpha_radians/2))
    
def calculate_approx_round_fov(cone_angle_alpha_radians): 
    cone_angle_alpha_radians_squared = cone_angle_alpha_radians**2
    return (math.pi*cone_angle_alpha_radians_squared)/4   

def calculate_approx_square_fov(theta_one_rad, theta_two_rad):
    return theta_one_rad*theta_two_rad

def calculate_approx_cone_angle_given_symmetric_solid_angle(solid_angle_steradians):
    return math.sqrt((4 * solid_angle_steradians)/math.pi)