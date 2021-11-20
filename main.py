from PIL import Image

import filter

inp_file = "img2.jpg"  # input("Input image name to put filter on: ")
inp_img = Image.open(inp_file)

mosaic_size = 10  # int(input("Input mosaic size: "))
grey_gradation = 50  # int(input("Input grey gradation: "))

res = filter.put_grey_mosaic_filter(inp_img, mosaic_size, grey_gradation)
res.save("res.jpg")
print("Result saved to res.jpg")