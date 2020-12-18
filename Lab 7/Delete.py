#Name: Nasrin Nahar
#Date: 10.18.20
#This code apply update cursor to delete rows based on specific criteria
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
fc = "Results/airports.shp"
cursor = arcpy.da.UpdateCursor(fc, ["TOT_ENP"])
for row in cursor:
    if row[0] < 100000:
        cursor.deleteRow()
del row
del cursor