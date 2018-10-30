"""ECE 595 Computer problem CIV-2.

'SHORT-RANGE MISSILE LAUNCH ALTITUDE'
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d



dirname = os.path.dirname(__file__)


def load_data(event_data_file=dirname+"/../data/Formatted Event Data.xls",
              altitude_data_file=dirname+"/../data/Altitude Model.xls"):
    """Load excel files to pandas dataframes."""
    event_data_df = pd.read_excel(event_data_file)
    altitude_data_df = pd.read_excel(altitude_data_file)

    return event_data_df, altitude_data_df


def plot_df_altitude_vs_time(times_sec, altitudes_km, title="Altitude vs Time"):
    """Plot raw data from file."""
    keys = altitude_data_df.keys()
    print(keys)
    plt.figure()
#    plt.plot(times_sec, altitudes_km)
    plt.scatter(times_sec, altitudes_km)
    plt.title(title)
    plt.xlabel("Time after 'launch' (sec)")
    plt.ylabel("altitude (km)")


if __name__ == "__main__":
    event_data_df, altitude_data_df = load_data()

    units_row = 0
    print(altitude_data_df)
    altitude_data_df = altitude_data_df.drop([units_row])
    print(altitude_data_df)

    raw_altitudes_km = altitude_data_df["altitude"]

    raw_times_sec = altitude_data_df["time"]

    plot_df_altitude_vs_time(times_sec=raw_times_sec,
                             altitudes_km=raw_altitudes_km)

    raw_event_times_sec = event_data_df["TIME"]
    print(raw_event_times_sec.shape)
    print(type(raw_event_times_sec))
    print(raw_altitudes_km.shape)

    alt_km_interpolator = interp1d(raw_times_sec, raw_altitudes_km)

    raw_event_times_sec_greater_than_zero = [time for time in raw_event_times_sec if time > 0]
    linear_interpolated_altitudes_km = alt_km_interpolator(raw_event_times_sec_greater_than_zero)
    plot_df_altitude_vs_time(times_sec=raw_event_times_sec_greater_than_zero,
                             altitudes_km=linear_interpolated_altitudes_km,
                             title="Linear interpolated altitude vs time")

    plt.show()
