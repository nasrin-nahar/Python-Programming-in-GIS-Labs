import arcpy
mxd = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
dataset = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise10/Austin/base.shp"
spatialref = arcpy.Describe(dataset).spatialReference
extent = arcpy.Describe(dataset).extent
for df in arcpy.mapping.ListDataFrames(mapdoc):
    df.spatialReference = spatialref
    df.panToExtent(extent)
    df.scale = 15000
mapdoc.save()
del mapdoc