#Name: Nasrin Nahar
#Date: 10.18.20
#This code creates a new fearure class based on specific selection criteria
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise07"
infc = "airports.shp"
outfc = "Results/airports_anchorage.shp"
delimitedField = arcpy.AddFieldDelimiters(infc,"COUNTY")
arcpy.Select_analysis(infc, outfc, delimitedField + " ='Anchorage Borough'")
