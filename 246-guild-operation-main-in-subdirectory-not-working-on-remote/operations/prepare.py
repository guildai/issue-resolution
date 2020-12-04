relative_import = True

if relative_import:
    from . import road_segmentation
else:
    from operations import road_segmentation

print(road_segmentation.msg)
