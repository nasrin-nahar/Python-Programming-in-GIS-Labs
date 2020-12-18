#Name: Nasrin Nahar
#Date: 9.29.20
#This code runs the Add XY Features tool on the hospitals feature class.

import arcpy
from arcpy import env
env.workspace= "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise05"
env.overwriteOutput=True
prjFile = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise05/facilities.prj"
spatial_ref = arcpy.SpatialReference(prjFile)
my_result=arcpy.DefineProjection_management("hospitals.shp", spatial_ref)

print my_result
