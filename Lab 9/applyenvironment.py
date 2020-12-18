import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
elevfeet = arcpy.Raster( "C:/raster/elevation" )
elevmeter = elevfeet * 0.3048
env.cellsize = 30
env.mask = "C:/raster/studyarea.shp"
elevrasterclip = ApplyEnvironment( elevmeter )
elevrasterclip.save( "C:/raster/dem30_m" )





   