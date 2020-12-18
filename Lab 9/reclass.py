import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    myremap = RemapRange([[1000,2000,1], [2000,3000,2], [3000,4000,3]])
    outreclass = Reclassify("elevation", "VALUE", myremap)
    outreclass.save("elev_recl")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
        
    

   