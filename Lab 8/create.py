#Name: Nasrin Nahar
#Date: 10.21.20
#This code creates a new empty polyline feature class with the coordinates in a text file

import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
env.overwriteOutput = True
outpath = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
newfc = "Results/newpolyline.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
infile = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise08/coordinates.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor