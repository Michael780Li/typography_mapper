import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import pandas as pd

print('This is a python app that reads a document and outputs a typography map')
Long = []
Lat = []
Elev = []

# excel file info
# location of data file
# to location of excel data file
file_Location = r'C:\Users\Michael\Desktop\Typography python\data.xlsx'
sheet_name = 'Sheet1'  # change to data sheet name

# read coordinates from excel file
data = pd.read_excel(
    file_Location, sheet_name=sheet_name)
Long = data['x'].values.tolist()
Lat = data['y'].values.tolist()
Elev = data['z'].values.tolist()

# resolution of map
pts = 500

# produces evenly spaced points between max and min coordinates

rangeX = np.linspace(np.min(Lat), np.max(Lat), pts)
rangeY = np.linspace(np.min(Long), np.max(Long), pts)
rangeZ = np.linspace(np.min(Elev), np.max(Elev), pts)

[Xg, Yg] = np.meshgrid(rangeX, rangeY)

Zg = griddata((Long, Lat), Elev, (Xg, Yg), method='linear')

Xg = np.matrix.flatten(Xg)  # Gridded longitude
Yg = np.matrix.flatten(Yg)  # Gridded latitude
Zg = np.matrix.flatten(Zg)  # Gridded elevation

plt.scatter(Xg, Yg, 1, Zg)

plt.colorbar(label='Elevation [m]')
plt.title('Typography')
plt.xlabel('Longitude [°]')
plt.ylabel('Latitude [°]')
plt.show()
