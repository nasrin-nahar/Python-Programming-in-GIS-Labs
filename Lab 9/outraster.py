import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
outraster = arcpy.sa.Slope("Elevation")
outraster.save("slope")