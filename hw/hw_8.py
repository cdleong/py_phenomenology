'''
Created on Sep 25, 2018

@author: cdleong
'''
import math
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from pyphenom import solid_angles

def vi_1_a():
    angles = [5, 10, 20, 50, 100, 180]
    for angle in angles:
        cone_angle_alpha_radians = math.radians(angle)
        approx_angle = solid_angles.calculate_approx_round_fov(cone_angle_alpha_radians)
        exact_angle = solid_angles.calculate_exact_round_fov(cone_angle_alpha_radians)
        print(f"For angle {angle} degrees... \n\t approx solid angle is {approx_angle} steradians, \n\t exact angle is {exact_angle} steradians")    
    
def vi_1_b():
    denominators = [1, 2, 4, 10, 100, 1000]
    for denom in denominators:
        solid_angle_steradians = math.pi/denom
        interior_cone_angle = solid_angles.calculate_approx_cone_angle_given_symmetric_solid_angle(solid_angle_steradians)
        print(f"for symmetrical solid angle cone pi/{denom} (which works out to {solid_angle_steradians})...")
        print(f"\t the interior cone angle is: {interior_cone_angle} rad")
    


if __name__ == '__main__':
#     vi_1_a()
    
    vi_1_b()
