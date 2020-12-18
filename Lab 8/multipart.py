#Name: Nasrin Nahar
#Date: 10.21.20
#This code prints whether each feature in the dams features class is multipart or single part

import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise08"
fc = "dams.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
    if row[1].isMultipart:
        print("Feature {0} is multipart.".format(row[0]))
    else:
        print("Feature {0} is single part.".format(row[0]))