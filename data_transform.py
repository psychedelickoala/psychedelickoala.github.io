import numpy as np
import csv
from scipy.interpolate import interpn

readfile = "tas_annual.csv"
writefile = 'fixed_data.csv'
australia_only = True
precision = 1
lon_ratio = 2 if not australia_only else int((155-111)/(45-11))

array = np.loadtxt(readfile, delimiter=",")

lats, lons = array.shape

latitudes = np.linspace(start=-90, stop=90, num=lats*precision, endpoint=True)
longitudes = np.linspace(start=0, stop=360, num=(lons*precision*lon_ratio), endpoint=False)

points = (latitudes, longitudes)
values = array
point = np.array([[[0.01, 15.67], [5.89, 13.21]], [[7.89, 15.67], [0.00, 13.21]]])

interpolation = interpn(points, values, point)
print(interpolation)


"""

with open(writefile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["lat", "lon", "temp-change"])

    for i in range(len(latitudes)):
        for j in range(len(longitudes)):
            if not australia_only or (-45 <= latitudes[i] <= -11 and 111 <= longitudes[j] <= 155):
                writer.writerow([latitudes[i], longitudes[j], get_value(i, j)])
"""

# cemetery
"""
    i_min, j_min = i//precision, j//(precision*lon_ratio)
    i_max, j_max = i_min + 1, j_min + 1
    if i_max >= lats:
        i_max =  i_min
    if j_max >= lons:
        j_max =  j_min
    
    ll, lr, ul, ur = array[i_min, j_min], array[i_min, j_max], array[i_max, j_min], array[i_max, j_max]
    h_frac = (i%precision)/precision
    v_frac = (j%(lon_ratio*precision))/(lon_ratio*precision)
    return (h_frac*ll + (1-h_frac)*lr)*v_frac + (h_frac*ul + (1-h_frac)*ur)*(1-v_frac)


"""
