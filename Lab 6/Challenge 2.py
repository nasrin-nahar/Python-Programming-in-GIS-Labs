#Name: Nasrin Nahar
#Date: 10.11.20
#This code reads all the feature classes in the specified workspace and copies only the polygon feature classes to a new geodatabase file
geodatabase.
import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise06"
arcpy.CreateFileGDB_management("D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise06/Results", "Ch2.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    if fcdescribe.shapeType == "Polygon":
        arcpy.CopyFeatures_management(fc, "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise06/Results/Ch2.gdb/" + fcdescribe.basename)
        