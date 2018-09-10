'''
Created on Sep 9, 2018

@author: cdleong
'''
import decimal
# CONSTANTS
FIRST_RADIATION_CONSTANT = decimal.Decimal(3.742*10.0**8)  # W*um^4*m^-2
SECOND_RADIATION_CONSTANT = decimal.Decimal(1.438*10.0**4)  # um*K
C_1 = FIRST_RADIATION_CONSTANT
C_2 = SECOND_RADIATION_CONSTANT
SPEED_OF_LIGHT_MICRONS_PER_SECOND =  decimal.Decimal(2.998*10.0**8*10.0**6) # speed of light in micrometers per second
C = SPEED_OF_LIGHT_MICRONS_PER_SECOND
PLANCK_CONSTANT_JOULES_SECONDS = decimal.Decimal(6.63*10.0**-34) # aka "h", J *S 
H = PLANCK_CONSTANT_JOULES_SECONDS
PLANCK_CONSTANT_EV_SECONDS = decimal.Decimal(4.135667*10**-15)
STEFAN_BOLTZMANN_CONSTANT = decimal.Decimal(5.67*10**-8) # AKA sigma_b, W*m^-2*K^-4


