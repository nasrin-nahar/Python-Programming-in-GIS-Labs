import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
elev = arcpy.Raster("elevation")
lc = arcpy.Raster("landcover.tif")
slope = Slope(elev)
aspect = Aspect(elev)
goodslope = ((slope > 5) & (slope < 20))
goodaspect = ((aspect > 150) & (aspect < 270))
goodland = ((lc == 41) | (lc == 42) | (lc ==43))
outraster = (goodslope & goodaspect & goodland)
outraster.save("D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise09/Results/final")
arcpy.CheckInExtension("Spatial")
