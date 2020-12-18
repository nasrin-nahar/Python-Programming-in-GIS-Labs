#Name: Nasrin Nahar
#Date: 10.11.20
#This code creates a new geodatabase file and copies the shapefiels in that geodatabase with basename
import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise06"
arcpy.CreateFileGDB_management("D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise06/Results","NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise06/Results/NM.gdb/" + fcdesc.basename)    