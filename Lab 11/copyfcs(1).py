import arcpy, os
from arcpy import env
try:
    env.workspace = "D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise11"
    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        desc = arcpy.Describe(fc)
        arcpy.CopyFeatures_management(fc, os.path.join("Results/mydata.mdb", desc.basename))
except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "There has been a nontool error."    