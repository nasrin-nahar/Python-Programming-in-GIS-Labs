#Name: Nasrin Nahar
#Date: 10.11.20
#This code prints the name of each feature class and the geometry type of that feature class
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print"{0} is a {1} feature class".format(fcdescribe.basename,fcdescribe.shapeType)
    
    
    