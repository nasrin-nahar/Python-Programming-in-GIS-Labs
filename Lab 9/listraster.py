import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster