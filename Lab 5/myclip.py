#Name: Nasrin Nahar
#Date: 9.29.20
#This code performs the clip function on the bike routes feature with respect to the park feature and return the last tool message
import arcpy
from arcpy import env
env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise05"
env.overwriteOutput = True
newclip = arcpy.Clip_analysis("bike_routes.shp", "parks.shp",
"Results/bike_Clip.shp")
fCount = arcpy.GetCount_management("Results/bike_Clip.shp")
msgCount = newclip.messageCount
print newclip.getMessage(msgCount-1)