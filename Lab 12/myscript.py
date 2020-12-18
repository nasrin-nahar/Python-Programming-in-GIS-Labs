import arcpy
import list
arcpy.env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise12"
fields = list.listfieldnames("streets.shp")
print fields