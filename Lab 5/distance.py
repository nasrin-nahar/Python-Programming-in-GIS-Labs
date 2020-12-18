#Name: Nasrin Nahar
#Date: 9.29.20
#This code calcualtes euclidean distance of bike route feature class and checks availability of Spatial Analyst license in ArcGIS desktop
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise05"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    out_distance = arcpy.sa.EucDistance("bike_routes.shp", cell_size =  100)
    out_distance.save ("D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise05/Results/bike_dist")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."