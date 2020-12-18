import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
f1raster = arcpy.Raster( "C:/raster/factor1" )
f2raster = arcpy.Raster( "C:/raster/factor2" )
f3raster = arcpy.Raster( "C:/raster/factor3" )
outraster = ( f1 + f2 + f3 ) / 3
outraster.save( "C:/raster/final" )
        
    

   