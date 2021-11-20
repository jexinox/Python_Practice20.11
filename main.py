from PIL import Image

import filter

inp_file = input("Input image name to put filter on: ")
inp_img = Image.open(inp_file)

mosaic_size = int(input("Input mosaic size: "))
grey_gradation = int(input("Input grey gradation: "))

res = filter.put_grey_mosaic_filter(inp_img, mosaic_size, grey_gradation)
res.save("res.jpg")
print("Result saved to res.jpg")