import numpy as np
import csv
from scipy.interpolate import interpn

# add 19 for end year
files = {
    "15": 2015,
    "20": 2020,
    "25": 2025,
    "30": 2030,
    "35": 2035,
    "40": 2040,
    "45": 2045,
    "50": 2050,
    "55": 2055,
    "60": 2060,
    "65": 2065,
    "70": 2070,
    "75": 2075,
    "80": 2080
}

readfile = "assignment-2/temp-data/tas_annual_15.csv"
writefile = 'assignment-2/temp-data/processed_tas_annual.csv'
australia_only = True
aus_lats = (-45, -9)
aus_lons = (110, 156)

array = np.loadtxt(readfile, delimiter=",")

lats, lons = array.shape

latitudes = np.linspace(start=-90, stop=90, num=lats, endpoint=True)
longitudes = np.linspace(start=0, stop=360, num=lons, endpoint=True)

points = (latitudes, longitudes)
values = array


new_lats = np.linspace(start=-90, stop=90, num=lats*4, endpoint=True)
new_lons = np.linspace(start=0, stop=360, num=lons*7, endpoint=True)

coords = np.array(np.meshgrid(new_lats,new_lons)).transpose([1,2,0])

interpolation = interpn(points, values, coords)
interpolation = interpolation.transpose([1, 0])



with open(writefile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["lat", "lon", "temp-change"])

    for i in range(len(new_lats)):
        for j in range(len(new_lons)):
            if not australia_only or (aus_lats[0] <= new_lats[i] <= aus_lats[1] and aus_lons[0] <= new_lons[j] <= aus_lons[1]):
                writer.writerow([np.round(new_lats[i], 3), np.round(new_lons[j], 3), np.round(interpolation[i, j], 3)])
