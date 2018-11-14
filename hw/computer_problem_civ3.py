"""ECE 595 Computer problem CIV-3.

'SHORT-RANGE MISSILE LAUNCH ATMOSPHERIC TRANSMISSION'
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import seaborn as sns
from sklearn.metrics import mean_squared_error
from pyphenom import atmosphere
sns.set()

dirname = os.path.dirname(__file__)


def load_data(event_data_file=dirname + "/../data/Formatted Event Data.xls",
              altitude_data_file=dirname + "/../data/Altitude Model.xls",
              atmo_trans_file=dirname + "/../data/Transmission from Altitude to Space.xls"):
    """Load excel files to pandas dataframes."""
    event_data_df = pd.read_excel(event_data_file)
    print("loaded event data")
    print(event_data_df)

    altitude_data_df = pd.read_excel(altitude_data_file)
    units_row = 0

    # drop units row
    altitude_data_df = altitude_data_df.drop([units_row])

    # fix the datatypes
    altitude_data_df['time'] = altitude_data_df['time'].apply(float)
    altitude_data_df['altitude'] = altitude_data_df['altitude'].apply(float)

    print("loaded altitude data")
    print(altitude_data_df)

    atmo_trans_df = pd.read_excel(atmo_trans_file)
    print("loaded atmo transmission data")
    print(atmo_trans_df)

    return event_data_df, altitude_data_df, atmo_trans_df


def graph_atmo_trans_df(atmo_trans_df):
    """graphing."""
    plt.figure()
    plt.title("Atmo Trans With Altitude")
    plt.xlabel("Transmission factor")
    plt.ylabel("Altitude(km)")
    plt.plot(atmo_trans_df["TRANSMISSION"],
             atmo_trans_df["ALTITUDE"])


def find_best_fit(x, y, deg):

    coefs = poly.polyfit(x, y, deg)
    ffit = poly.Polynomial(coefs)
    return ffit


def find_best_fit_for_atmo_transmission(atmo_trans_df, deg=4):

    x = atmo_trans_df["ALTITUDE"]
    y = atmo_trans_df["TRANSMISSION"]
    atmo_ffit = find_best_fit(x, y, deg)

    # test it out
    x_new = np.arange(min(x), max(x), 0.1)
    plt.figure()
    plt.title("Best-fit curve, 0.1 km increments, poynomial degree={}".format(deg))
    plt.plot(atmo_ffit(x_new), x_new)
    plt.xlabel("Transmission factor")
    plt.ylabel("Altitude(km)")

    return atmo_ffit


def graph_alt_vs_time(time_sec, alt_km, title):
    plt.figure()
    plt.title(title)
    plt.plot(time_sec, alt_km)
    plt.xlabel("Transmission factor")
    plt.ylabel("Altitude(km)")


def find_best_fit_for_altitude(altitude_data_df, deg=10):
    # graph old
    x = altitude_data_df["time"]
    y = altitude_data_df["altitude"]
    graph_alt_vs_time(x, y, "Old Altitude Data")

    alt_ffit = find_best_fit(x, y, deg=deg)

    # test it out
    x_new = np.arange(min(x), max(x), 0.01)

    graph_alt_vs_time(x_new, alt_ffit(x_new),
                      "Best-fit altitude data, deg={}".format(deg))

    return alt_ffit


def find_best_args_for_atf_function(atmo_trans_df):

    x = atmo_trans_df["ALTITUDE"]
    actual_transmission = atmo_trans_df["TRANSMISSION"]

    # we have a value that's really low
    # we have a value that's really high
    # we have a number of values to try
    number_of_values_to_try = 100

    # original guesses
    really_low = -30
    really_high = -5

    # we got a value around 10^-30, so let's bracket it a bit
    really_low = -40
    really_high = -20
    possible_sigmas = np.logspace(really_low, really_high, number_of_values_to_try)

    # we got 5.0941380148163644e-30, so let's bracket even further
    really_low = -31
    really_high = -29
    possible_sigmas = np.logspace(really_low, really_high, number_of_values_to_try)

    # original guess
    really_low = -1  # 10^-1 is 0.1 km
    really_high = 4  # 10^4 is 10000 km

    #updated guess, since our last value was around 5.7
    really_low = -1
    really_high = 1
    possible_scale_heights_km = np.logspace(really_low, really_high, number_of_values_to_try)

    # second guess was around 6.280291441834256, let's get even closer
    possible_scale_heights_km = np.linspace(5, 7, number_of_values_to_try)

    results = []
    # O(scary). Twould be better to do a search or gradient descent or such
    for sigma in possible_sigmas:
        for scale_height_km in possible_scale_heights_km:
            calculated_transmissions = []
            for alt_km in atmo_trans_df["ALTITUDE"]:
                transmission_factor = atmosphere.calculate_atmospheric_transmission_factor_to_space(alt_km, sigma, scale_height_km)

                calculated_transmissions.append(transmission_factor)

            mse = mean_squared_error(calculated_transmissions, actual_transmission)

            results_tuple = (mse, sigma, scale_height_km)
            results.append(results_tuple)


    lowest_mse = 10e10000
    lowest_result = None
    for result in results:
        mse = result[0]
        if mse < lowest_mse:
            lowest_result = result
            lowest_mse = mse


    if lowest_result:
        print("BEST")
        print(lowest_result)

        sigma = lowest_result[1]
        scale_height_km = lowest_result[2]

        calculated_transmission_factors = []
        for alt_km in atmo_trans_df["ALTITUDE"]:
            transmission_factor = atmosphere.calculate_atmospheric_transmission_factor_to_space(alt_km, sigma, scale_height_km)
            calculated_transmission_factors.append(transmission_factor)

        plt.figure()
        plt.title("actual and calculated transmission factor vs height, sigma={0}, scale_height_km={1}".format(sigma, scale_height_km))
        plt.plot(actual_transmission, atmo_trans_df["ALTITUDE"],)
        plt.plot(calculated_transmission_factors, atmo_trans_df["ALTITUDE"])
        plt.xlabel("transmission factor")
        plt.ylabel("altitude(km)")


        return sigma, scale_height_km


def calculate_vert_transmission_for_rocker_heights()

if __name__ == "__main__":
    event_data_df, altitude_data_df, atmo_trans_df = load_data()

    graph_atmo_trans_df(atmo_trans_df)

    atmo_ffit = find_best_fit_for_atmo_transmission(atmo_trans_df)

    alt_ffit = find_best_fit_for_altitude(altitude_data_df)
    find_best_args_for_atf_function(atmo_trans_df)
    plt.show()
