#Name: Nasrin Nahar
#Date: 10.11.20
#This code print the feature class list of the shapefiles in the specified workspace
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise06"
fclist = arcpy.ListFeatureClasses()
print fclist