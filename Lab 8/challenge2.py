#Name: Nasrin Nahar
#Date: 10.27.20
#This code determines the perimeter ( in meters ) and area ( in square meters ) of each of the individual islands of the Hawaii.shp feature class

import arcpy
from arcpy import env
env.workspace = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_single.shp"
arcpy.MultipartToSinglepart_management(fc,newfc)
spatialref=arcpy.Describe(newfc).spatialReference
unit=spatialref.linearUnitName
cursor=arcpy.da.SearchCursor(newfc,["SHAPE@"])
for row in cursor:
    print (" Feature {0):Area{1} square {2} and Perimeter {3} {4}".format(row[1],row[0].area, unit,row[0].length,unit))
del cursor          
           
           




