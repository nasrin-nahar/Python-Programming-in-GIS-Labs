#Name: Nasrin Nahar
#Date: 10.19.20
#This code prints the total length of all the river segments with units


import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
fc = "rivers.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for row in cursor:
    length = length + row[0]
units = arcpy.Describe(fc).spatialReference.linearUnitName
print str(length) + " " + units