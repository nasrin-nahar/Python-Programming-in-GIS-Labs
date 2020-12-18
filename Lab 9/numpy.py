import arcpy, scipy
from arcpy.sa import *
inRaster = arcpy.Raster( "C:/raster/myraster" )
my_array = RasterToNumPyArray( inRaster )
outarray = scipy.<module>.<function>( my_array )
outraster = NumPyArrayToRaster( outarray )
outraster.save( "C:/raster/result" )





   