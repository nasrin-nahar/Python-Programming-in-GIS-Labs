#Name: Nasrin Nahar
#Date: 10.18.20
#This code apply insert cursor to insert a row

import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
fc = "Results/airports.shp"
cursor = arcpy.da.InsertCursor(fc, "NAME")
cursor.insertRow(["New Airport"])
del cursor