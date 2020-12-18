import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    myremap = RemapValue([[41,1], [42,2], [43,3]])
    outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
    outreclass.save("lc_recl")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
        
    

   