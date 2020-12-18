#Name: Nasrin Nahar
#Date: 10.18.20
#This code adds a text field to a specific feature class called and populates that field with YES and NO values, depending on the value of the FEATURE field.
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
env.overwriteOutput = True
fc = "Results/roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 10)
delimfield = arcpy.AddFieldDelimiters(fc, "FEATURE")

cursor1 = arcpy.da.UpdateCursor(fc,["FERRY"],delimfield + " = 'Ferry Crossing'")
for row in cursor1:
    row[0] = "Yes"
    cursor1.updateRow(row)
del row
del cursor1

cursor2 = arcpy.da.UpdateCursor(fc,["FERRY"],delimfield + "<>'Ferry Crossing'")
for row in cursor2:
    row[0] = "No"
    cursor2.updateRow(row)
del row
del cursor2


