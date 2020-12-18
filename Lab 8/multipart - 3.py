#Name: Nasrin Nahar
#Date: 10.21.20
#This code prints prints the part number, followed by pairs of x,y coordinates of the vertices of Hawaii feature class
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    partnum = 0
    for part in row[1]:
        print("Part {0}: ".format(partnum))
        for point in part:
            print("{0}, {1}".format(point.X, point.Y))
        partnum += 1