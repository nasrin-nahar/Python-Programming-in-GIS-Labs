#Name: Nasrin Nahar
#Date: 10.27.20
#This code creates a new polygon feature class containing asingle ( square ) polygon with some specified coordinates

import arcpy, fileinput, string, os
from arcpy import env
env.overwriteOutput = True
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"

infile = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise08/Polygon_coordinates.txt"
fc = "Results/polygon.shp"
outpath = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
arcpy.CreateFeatureclass_management( outpath, fc, "Polygon" )
cursor = arcpy.da.InsertCursor( fc, ["SHAPE@"] )
array = arcpy.Array()
point = arcpy.Point( )
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
