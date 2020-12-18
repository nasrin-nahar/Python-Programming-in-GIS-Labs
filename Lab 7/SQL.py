#Name: Nasrin Nahar
#Date: 10.18.20
#This code prints list of the names of the airports for which the SQL expression is true
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"TOT_ENP" > 100000')
for row in cursor:
    print row[0]
del row
del cursor