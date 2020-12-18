#Name: Nasrin Nahar
#Date: 10.19.20
#This code prints a pair of x,y coordinates for each vertex in each feature in the river feature class

import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
fc = "rivers.shp"
cursor = arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"]))
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    for point in row[1].getPart(0):
        print("{0}, {1}".format(point.X, point.Y))