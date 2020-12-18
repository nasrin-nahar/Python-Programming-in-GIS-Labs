import arcpy
from arcpy import env
out_path = "D:\BU Masters\Fall 2020\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
env.workspace = out_path
rasterlist = arcpy.ListRasters()
arcpy.CreatePersonalGDB_management(out_path + "/Results", "myrasters.gdb")
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    rname = desc.baseName
    outraster = out_path + "/Results/myrasters.gdb/" + rname
    arcpy.CopyRaster_management(raster,outraster)