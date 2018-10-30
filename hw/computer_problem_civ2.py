"""ECE 595 Computer problem CIV-2.

'SHORT-RANGE MISSILE LAUNCH ALTITUDE'
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from mpl_toolkits.mplot3d import Axes3D
import geopy
import math
from geopy import distance

dirname = os.path.dirname(__file__)


def load_data(event_data_file=dirname+"/../data/Formatted Event Data.xls",
              altitude_data_file=dirname+"/../data/Altitude Model.xls"):
    """Load excel files to pandas dataframes."""
    event_data_df = pd.read_excel(event_data_file)
    altitude_data_df = pd.read_excel(altitude_data_file)

    return event_data_df, altitude_data_df


def plot_df_altitude_vs_time(times_sec, altitudes_km, title="Altitude vs Time"):
    """Plot raw data from file."""
    plt.figure()
#    plt.plot(times_sec, altitudes_km)
    plt.scatter(times_sec, altitudes_km)
    plt.title(title)
    plt.xlabel("Time after 'launch' (sec)")
    plt.ylabel("altitude (km)")


def plot_lla_three_d(xs, ys, zs, title="Lat/Lon/Altitude"):
    """Plot in 3d! Awesome."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(xs, ys, zs, c='r')
    ax.plot(xs, ys, zs, c='r')
    plt.title(title)
    ax.set_xlabel('Lat (deg)')
    ax.set_ylabel('Lon (deg)')
    ax.set_zlabel('Alt (km)')


if __name__ == "__main__":
    event_data_df, altitude_data_df = load_data()

    units_row = 0
#    print(altitude_data_df)
    altitude_data_df = altitude_data_df.drop([units_row])
#    print(altitude_data_df)

    raw_altitudes_km = altitude_data_df["altitude"]

    raw_times_sec = altitude_data_df["time"]

    plot_df_altitude_vs_time(times_sec=raw_times_sec,
                             altitudes_km=raw_altitudes_km)

    raw_event_times_sec = event_data_df["TIME"]
#    print(raw_event_times_sec.shape)
#    print(type(raw_event_times_sec))
#    print(raw_altitudes_km.shape)

    alt_km_interpolator = interp1d(raw_times_sec, raw_altitudes_km)

    raw_event_times_sec_greater_than_zero = [time for time in raw_event_times_sec if time > 0]
    linear_interpolated_altitudes_km = alt_km_interpolator(raw_event_times_sec_greater_than_zero)
    plot_df_altitude_vs_time(times_sec=raw_event_times_sec_greater_than_zero,
                             altitudes_km=linear_interpolated_altitudes_km,
                             title="Linear interpolated altitude vs time")

    # convert to float64
    altitude_data_df['time'] = altitude_data_df['time'].apply(float)
    merged_df = pd.merge_ordered(event_data_df,
                                altitude_data_df,
                                how = 'outer',
                                left_on = 'TIME',
                                right_on = 'time')

    pandas_interpolated_altitudes_km = merged_df["altitude"].interpolate("quadratic")
    plot_df_altitude_vs_time(times_sec=merged_df["TIME"].interpolate("quadratic"),
                             altitudes_km=pandas_interpolated_altitudes_km,
                             title="Pandas-interpolated altitude vs time")

    merged_df['TIME'] = merged_df['TIME'].apply(float)
    merged_df['LATITUDE'] = merged_df['LATITUDE'].apply(float)
    merged_df['LONGITUDE'] = merged_df['LONGITUDE'].apply(float)
    merged_df['altitude'] = merged_df['altitude'].apply(float)
    ts = merged_df['TIME'].interpolate("quadratic")
    xs = merged_df['LATITUDE'].interpolate("quadratic")
    ys = merged_df['LONGITUDE'].interpolate("quadratic")
    zs = merged_df['altitude'].interpolate("quadratic")
    plot_lla_three_d(xs, ys, zs)

    print("Lat lon alt time")
    index = 0
    zipped = zip(xs, ys, zs, ts)
    N = 10
    for x, y, z, t in zipped:
        print("{3}, {0:8.2f}, {1:8.2f}, {2:8.2f}, {4:8.2f}".format(x,y,z,index,t))


    moving_average_xs = np.convolve(xs, np.ones((N,))/N, mode='valid')
    moving_average_ys = np.convolve(ys, np.ones((N,))/N, mode='valid')
    moving_average_zs = np.convolve(zs, np.ones((N,))/N, mode='valid')
    plot_lla_three_d(moving_average_xs,
                     moving_average_ys,
                     moving_average_zs,
                     title="LLA plot, but with moving average of each coord")

    start_point = geopy.point.Point(40.001, -119.001, 0.00)
    zipped = zip(ts, xs, ys, zs)
    distances_km = []
    times_for_distances = []
    for t, x, y, z in zipped:
        if (not math.isnan(t)
            and not math.isnan(x)
            and not math.isnan(y)
            and not math.isnan(z)):
            current_point = geopy.point.Point(x, y, z)
            distance_km = distance.distance(start_point, current_point).km
            print(f"at time {t} distance is {distance_km} km")
            times_for_distances.append(t)
            distances_km.append(distance_km)


    plt.figure()
#    plt.plot(times_sec, altitudes_km)
    plt.scatter(times_for_distances, distances_km)
    plt.title("3d distance vs time")
    plt.xlabel("Time after 'launch' (sec)")
    plt.ylabel("3d distance (km)")


    plt.show()
