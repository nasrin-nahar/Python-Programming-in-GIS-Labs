import arcpy
from arcpy import env
env.workspace = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise10"
mxd = arcpy.mapping.MapDocument("D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)
for dframe in dflist:
    if dframe.name <> "Parks":
        arcpy.mapping.AddLayer(dframe, lyr)
mxd.save()
del mxd