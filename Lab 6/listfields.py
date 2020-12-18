import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise06"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
    print field.name + " " + field.type
