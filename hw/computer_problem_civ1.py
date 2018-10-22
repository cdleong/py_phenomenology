'''
Created on Oct 20, 2018

@author: cdleong
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import colorline



def load_data(file_path="../data/Formatted Event Data.xls"):
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
    

def main():
    event_data_df = load_data()
    print(event_data_df.keys())
    
    # part A
    plot_time_vs_intensity(event_data_df)
    
    # part B
    plot_lat_and_lon(event_data_df)
    

    
    plt.show()




if __name__ == '__main__':
    main()