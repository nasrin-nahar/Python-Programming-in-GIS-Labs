#Name: Nasrin Nahar
#Date: 9.29.20
#This code performs the centroid function on the park feature

import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise05"
in_features = "parks.shp"
out_featureclass = "Results/parks_centroid.shp"
if arcpy.ProductInfo() == "ArcInfo":
    arcpy.FeatureToPoint_management(in_features, out_featureclass)
else:
    print "An ArcInfo license is not available."

    
