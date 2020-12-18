#Name: Nasrin Nahar
#Date: 9.29.20
#This code performs the dissolve function on the aprk feature class with respect to park type
 
# Import system modules
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise05"
env.overwriteOutput = True
my_result=arcpy.Dissolve_management("parks.shp","Results\park_dissolve.shp","PARK_TYPE","","SINGLE_PART","DISSOLVE_LINES")
print my_result
