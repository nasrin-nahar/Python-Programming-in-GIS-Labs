#Name: Nasrin Nahar
#Date: 10.18.20
#This code validates the table and field names before running a operation
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
fc = "Results/airports.shp"
newfield = "NEW?*&$"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)

import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
fc = "Results/airports.shp"
newfield = "NEW CODE"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
fieldlist = arcpy.ListFields(fc)
fieldnames = []
for field in fieldlist:
    fieldnames.append(field.name)
    if fieldname not in fieldnames:
        arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)
        print "New field has been added."
    else:
        print "Field name already exists."
