#Name: Nasrin Nahar
#Date: 10.18.20
#This code creates buffer around airport and seaplane base at specific distance
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
env.overwriteOutput = True
fc = "airports.shp"
infc1="Results/airports_only.shp"
infc2="Results/seaplane_base_only.shp"
outfc1= "Results/airports_buffer.shp"
outfc2= "Results/seaplane_base_buffer.shp"
delimitedField = arcpy.AddFieldDelimiters(infc,"FEATURE")
arcpy.Select_analysis(fc,infc1, delimitedField + " ='Airport'")
arcpy.Buffer_analysis(infc1, outfc1, "15000 METERS")

delimitedField = arcpy.AddFieldDelimiters(infc,"FEATURE")
arcpy.Select_analysis(fc,infc2, delimitedField + " ='Seaplane Base'")
arcpy.Buffer_analysis(infc2, outfc2, "7500 METERS")


