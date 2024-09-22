import numpy as np
import csv
from scipy.interpolate import interpn

readfile = "tas_annual.csv"
writefile = 'fixed_data.csv'
australia_only = True
precision = 20
#lon_ratio = 2 if not australia_only else int((155-111)/(45-11))

array = np.loadtxt(readfile, delimiter=",")

lats, lons = array.shape

latitudes = np.linspace(start=-90, stop=90, num=lats, endpoint=True)
longitudes = np.linspace(start=0, stop=360, num=lons, endpoint=True)

points = (latitudes, longitudes)
values = array


new_lats = np.linspace(start=-90, stop=90, num=lats*precision, endpoint=True)
new_lons = np.linspace(start=0, stop=360, num=lons*precision, endpoint=True)

coords = np.array(np.meshgrid(new_lats,new_lons)).transpose([1,2,0])
#print(coords)

interpolation = interpn(points, values, coords)
interpolation = interpolation.transpose([1, 0])



with open(writefile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["lat", "lon", "temp-change"])

    for i in range(len(new_lats)):
        for j in range(len(new_lons)):
            if not australia_only or (-45 <= new_lats[i] <= -11 and 111 <= new_lons[j] <= 155):
                writer.writerow([new_lats[i], new_lons[j], interpolation[i, j]])


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
