#Name: Nasrin Nahar
#Date: 10.18.20
#This code apply search cursor to print specific values of a feature class

import arcpy
from arcpy import env
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["NAME"])
for row in cursor:
    print "Airport name = {0}".format(row[0])
    