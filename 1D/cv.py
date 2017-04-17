# this is Tze How's code, I just cleaned it up a little

from SimpleCV import Color, Image

FILTERS = {
    'red':   (127,9,27),
    'blue':  (0,97,126),
    'green': (18,140,67)
}

def filter_to_point(filter, imgname):
    img = Image(imgname)

    zones = img.colorDistance(filter).invert()
    blobs = zones.binarize(230)

    blobs.findBlobs().draw(color=Color.BLACK, width=20)
    blobs.save('blobs.bmp')
    blobs_img = Image('blobs.bmp').invert()

    points = blobs_img.findBlobs(minsize=100).coordinates()
    return list(points[0])

def get_points(imgname):
    return {key: filter_to_point(filter, imgname) for key, filter in FILTERS.iteritems()}
