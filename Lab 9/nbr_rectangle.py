import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
mynbr = NbrRectangle( 5, 5, "CELL" )
outraster = FocalStatistics( "landuse", mynbr, "VARIETY" )
outraster.save( "C:/raster/lu_var" )





   