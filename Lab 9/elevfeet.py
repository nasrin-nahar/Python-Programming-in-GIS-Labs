import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="D:\BU Masters\Fall 2020\Programming in GIS\Programming in GIS Lab data\Programming in GIS Lab data\Exercise09"
slope = Slope(elevraster)
goodslope = slope < 20
goodelev = elevraster < 2000
goodfinal = goodslope & goodelev
goodfinal.save("final")
        
    

   