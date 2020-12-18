#Name: Nasrin Nahar
#Date: 10.11.20
#This code copies the shapefiels in the result folder
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    arcpy.CopyFeatures_management(fc, "D:/BU Masters/Fall 2020\Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise06/Results/" + fc)