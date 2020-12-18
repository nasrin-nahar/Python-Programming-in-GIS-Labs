#Name: Nasrin Nahar
#Date: 10.27.20
#This code creates an envelope polygon feature class for the Hawaii.shp feature class.
import arcpy
from arcpy import env
env.workspace = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise08"
inFeatures = "Hawaii.shp"
outFeatureClass = "Hawaii_envelope.shp"
arcpy.MinimumBoundingGeometry_management(inFeatures, outFeatureClass,"ENVELOPE", "NONE")
