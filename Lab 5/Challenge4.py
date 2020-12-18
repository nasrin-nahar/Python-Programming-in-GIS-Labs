#Name: Nasrin Nahar
#Date: 9.29.20
#This code checks the availbility of ArcGIS 3D Analyst,ArcGIS Network Analyst and ArcGIS Spatial Analyst extension license
import arcpy
from arcpy import env
env.workspace= "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise05"
print("The following extensions are available:")
extensions = ["3D", "Network", "Spatial"]
for ex in extensions:
    if arcpy.CheckExtension(ex) == "Available":
        print "ArcGIS {0} Analyst".format(ex)
        
    
    