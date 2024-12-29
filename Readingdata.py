#import the necessary libraries
import geopandas as gpd
import matplotlib.pyplot as plt

#read the data from a shapefile 
file_path = r"C:\Users\pasat\OneDrive\Υπολογιστής\Geoinformation_Science\geoscripting\udemy\geopandas\data\Raptor_Nests.shp"
raptors = gpd.read_file(file_path)

#reading the data from a geojason file 
file_path2 = r"C:\Users\pasat\OneDrive\Υπολογιστής\Geoinformation_Science\geoscripting\udemy\geopandas\data\wildlife_buowl.geojson.shp"

#view the first 5 rows of the data
print(raptors.head())
#view the last 5 rows of the data with tail method
print(raptors.tail(5))

#check the info of the data with the info method
print(raptors.info())

#check the crs of the coordinate system 
print(raptors.crs)

#view the map with the colors determined by the column recentspec adding a legend also and zooming with the figsize 
raptors.plot(column = "recentstat", legend = True, figsize = (10,10))
plt.show()