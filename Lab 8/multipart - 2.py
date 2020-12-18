#Name: Nasrin Nahar
#Date: 10.21.20
#This code prints whether each feature in the Hawaii features class is multipart or single part and also prints the number of parts for every multipart feature

import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
    if row[1].isMultipart:
        print("Feature {0} is multipart and has {1} parts.".format(row[0],str(row[1].partCount)))
    else:
        print("Feature {0} is single part.".format(row[0]))