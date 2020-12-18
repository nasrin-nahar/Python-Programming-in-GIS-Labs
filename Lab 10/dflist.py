import arcpy
mxd = "D:/BU Masters/Fall 2020/Programming in GIS/Programming in GIS Lab data/Programming in GIS Lab data/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
    print df.name
del mapdoc
del listdf