"""ECE 595 Computer problem CIV-2.

'SHORT-RANGE MISSILE LAUNCH ALTITUDE'
"""

import os
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from pyphenom import colorline


from shapely.geometry import Point
from shapely.geometry import shape

dirname = os.path.dirname(__file__)


def load_data(event_data_file=dirname+"/../data/Formatted Event Data.xls",
              altitude_data_file=dirname+"/../data/Altitude Model.xls"):
    """Load excel files to pandas dataframes."""
    event_data_df = pd.read_excel(event_data_file)
    altitude_data_df = pd.read_excel(altitude_data_file)

    return event_data_df, altitude_data_df


def plot_df_altitude_vs_time(times_sec, altitudes_km):
    """Plot raw data from file."""
    keys = altitude_data_df.keys()
    print(keys)
    plt.figure()
    plt.plot(times_sec, altitudes_km)
    plt.title("Altitude vs Time")
    plt.xlabel("Time after 'launch' (sec)")
    plt.ylabel("altitude (km)")


if __name__ == "__main__":
    event_data_df, altitude_data_df = load_data()

    row_actual_data_starts = 1

    raw_altitudes_km = altitude_data_df["altitude"]
    raw_altitudes_km = raw_altitudes_km[row_actual_data_starts:]

    raw_times_sec = altitude_data_df["time"]
    raw_times_sec = raw_times_sec[row_actual_data_starts:]

    plot_df_altitude_vs_time(times_sec=raw_times_sec,
                             altitudes_km=raw_altitudes_km)
    plt.show()
