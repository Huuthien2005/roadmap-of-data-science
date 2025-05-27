#import library
import numpy as np
import pandas as pd
import matplotlib as mpl

#Generate innitial temperature in 5 cities in 365 days  
rng=np.random.default_rng(seed=0)
temperature= rng.integers(-20,45,size=(5,365))
print("temperature in 365 past days in 5 different cities:\n")
for cities,days in enumerate(temperature):
    print(f"city {cities+1}: {days}")
    
#Find Hottest & Coldest Day for Each City
hottest= temperature.max()
print(f"hottest temperature in each day of 5 cities: {hottest}")
lowest=temperature.min()
print(f"Lowest temperature in each day of 5 cities: {lowest}")

#Calculate Average Temperature by City
city_avg=temperature.mean(axis=1)
print("average of temperature in each city: \n",city_avg)

# Detect Heatwaves
#using sliding window method

window_sliding=3 #range of window will sliding
thresrol=35#condition of temperature to calculate
i=0
count=0# count a number of 3-more day temperature higher than 35
window_counts=[]
while i<5:
    for day in range(len(temperature[i])-window_sliding+1):
        window=temperature[i][day:day+window_sliding]
        if(np.all(window>thresrol)):
            count+=1
    window_counts.append(count)
    i+=1
print("the number of heatwave in each cities: \n",window_counts)

# Find all days where a city's temperature dropped more than 15°C from the previous day.
i=0
cities_day_drop=[]
while i<5:
    days_drop=[]
    for day in range(len(temperature[i])-1):
        if temperature[i][day]-temperature[i][day+1]>=15:
            current_day=int(temperature[i][day])
            next_day=int(temperature[i][day+1])
            
            days_drop.append([current_day,next_day])
    cities_day_drop.append(days_drop)
    i+=1
print("list of the day of a city's temperature dropped more than 15°C from the previous day")
for city_index, drops in enumerate(cities_day_drop):
    print(f"City {city_index+1}: {drops}")

