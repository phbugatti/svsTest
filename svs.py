import openslide as ps

image = ps.OpenSlide('imageTest.svs')

print(image.properties)
print(image.dimensions, image.level_dimensions)

#imagethumb = image.get_thumbnail((500,500))

#imagethumb.show()

imageRGB = image.read_region((0, 0), 1, image.level_dimensions[1])

imageRGB.show()



