#import the necessary libraries
import geopandas as gpd
import matplotlib.pyplot as plt

#read the data from a shapefile 
file_pathshapefile = r"C:\Users\pasat\OneDrive\Υπολογιστής\Geoinformation_Science\geoscripting\udemy\geopandas\data\Raptor_Nests.shp"
raptors = gpd.read_file(file_pathshapefile)

#reading the data from a geojson file 
file_pathgeojson = r"C:\Users\pasat\OneDrive\Υπολογιστής\Geoinformation_Science\geoscripting\udemy\geopandas\data\wildlife_buowl.geojson"
raptors_json = gpd.read_file(file_pathgeojson)


#check the info of the data with the info method.You can see the number of the rows and columns, the data type, the number of NULL data
print(raptors.info())


#view the first 5 rows of the data
print(raptors.head())
#view the last 5 rows of the data with tail method
print(raptors.tail(5))


#check the crs of the coordinate system 
print(raptors.crs)

#view the map with the colors determined by the column recentspec adding a legend also and configuring the size of the plot with the figsize 
raptors.plot(column = "recentstat", legend = True, figsize = (10,10))
plt.show()

#interacting with geojson file, check the info of the data 
print(raptors_json.info())

#check the 5 first rows for the geojson file
print(raptors_json.head())

#check the last 5 rows for the geojson file
print(raptors_json.tail(5))

#check also the coordinate system of the geojson file
print(raptors_json.crs)

#plot the map of the geosjon file determined by a column named habitat you can do the same with your data
raptors_json.plot(column = "recentstatus", legend = True, figsize = (10,10))
plt.show()