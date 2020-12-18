import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise11"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    desc = arcpy.Describe(fc)
    print desc.basename + ": " + desc.shapeType