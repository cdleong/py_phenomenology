'''
Created on Oct 20, 2018

@author: cdleong
'''
import os
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from pyphenom import colorline



from shapely.geometry import Point
from shapely.geometry import shape

dirname = os.path.dirname(__file__)

def load_data(file_path=dirname+"/../data/Formatted Event Data.xls"):
    event_data_df = pd.read_excel(file_path)
    return event_data_df


def plot_time_vs_intensity(event_data_df):
    intensities = event_data_df["INTENSITY"]
    times = event_data_df["TIME"]

    plt.figure()
    plt.plot(times, intensities)
    plt.title("Intensity vs time of event")
    plt.xlabel("Time after 'launch' in seconds")
    plt.ylabel("Intensity (arbitrary sensor units)")


def plot_lat_and_lon(event_data_df):
    lats = event_data_df["LATITUDE"]
    lons = event_data_df["LONGITUDE"]

    plt.figure()
    plt.plot(lons, lats)

    plt.figure()
#     fig, axes = plt.subplots()
    colorline.colorline(lons, lats, cmap="copper")
    plt.xlim(lons.min()-0.01, lons.max()+0.01)
    plt.ylim(lats.min()-0.01, lats.max()+0.01)

    plt.grid(True)


    event_data_df['Coordinates'] = list(zip(event_data_df.LONGITUDE, event_data_df.LATITUDE))
    event_data_df['Coordinates'] = event_data_df['Coordinates'].apply(Point)
    gdf = geopandas.GeoDataFrame(event_data_df, geometry='Coordinates')

    nevada = geopandas.read_file(dirname+"/../data/cb_2017_32_tract_500k.shp")

    ax = nevada.plot()
    ax = nevada.plot(color='white', edgecolor='black')

    gdf.plot(ax=ax, color='red')









def convert_coords_to_ground_track(event_data_df):
    # References:
    # http://ryan-m-cooper.com/blog/gps-points-to-line-segments.html
    # https://gis.stackexchange.com/questions/202190/turn-a-geodataframe-of-x-y-coordinates-into-linestrings-using-groupby
    # https://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html
    lats = event_data_df["LATITUDE"]
    lons = event_data_df["LONGITUDE"]



    origin = (lats[0], lons[0])
    print(f"Origin: {origin}")

    coords = zip(lats, lons)
    diff_from_origin = []
    for coord in coords:
        diff = (coord[0] - origin[0], coord[1]-origin[1])


#         diff_km = geopy.distance.vincenty(origin, coord)
#         print(coord, diff, diff_km)

def main():
    event_data_df = load_data()
    print(event_data_df.keys())

    # part A
#     plot_time_vs_intensity(event_data_df)

    # part B
    plot_lat_and_lon(event_data_df)

    # part C
#     convert_coords_to_ground_track(event_data_df)
#
#     world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
#
#     print(world.keys())
#     print(world.name)
#     world.plot()
#
#     world[world.name == "United States"].plot()
#     print(world[world.name == "United States"].name.keys())
#     print("Hello world")
# #     print(geopandas.datasets.available)
# #
#     nevada = geopandas.read_file("../data/nevada_administrative.shp")
# #     nevada.plot()
#
#     states = geopandas.read_file("../data/cb_2017_us_state_5m.shx")
# #     states.plot()
#
#
    plt.show()





if __name__ == '__main__':
    main()
