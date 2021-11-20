from PIL import Image
import numpy as np
from numpy import ndarray


def put_grey_mosaic_filter(img: Image, mosaic_size: int = 10, grey_gradation: int = 50) -> Image:
    img_pixels = np.array(img)
    img_height = len(img_pixels)
    img_width = len(img_pixels[1])
    for i in range(0, img_height, mosaic_size):
        for j in range(0, img_width, mosaic_size):
            avg_color = get_average_color_for_quadrant(img_pixels, i, j, mosaic_size)
            put_grey_in_quadrant(img_pixels,
                                 i, j,
                                 avg_color,
                                 mosaic_size,
                                 grey_gradation)

    result_image = Image.fromarray(img_pixels)
    return result_image


def get_average_color_for_quadrant(img_pixels: ndarray,
                                   start_width: int,
                                   start_height: int,
                                   mosaic_size: int) -> int:
    avg_color = 0

    (right_height_bound, right_width_bound) = find_right_bounds_for_image_processing(img_pixels,
                                                                                     start_width,
                                                                                     start_height,
                                                                                     mosaic_size)

    for n in range(start_height, right_height_bound):
        for k in range(start_width, right_width_bound):
            pixel = img_pixels[n][k]
            avg_color += int(np.average(pixel))
    avg_color //= mosaic_size * mosaic_size
    return avg_color


def find_right_bounds_for_image_processing(img_pixels: ndarray,
                                           start_width: int,
                                           start_height: int,
                                           mosaic_size: int) -> tuple:
    img_height = len(img_pixels)
    img_width = len(img_pixels[1])

    right_height_bound = start_height + mosaic_size

    if start_height + mosaic_size >= img_height:
        right_height_bound -= (start_height + mosaic_size) % img_height

    right_width_bound = start_width + mosaic_size

    if start_width + mosaic_size >= img_width:
        right_width_bound -= (start_width + mosaic_size) % img_width

    return right_height_bound, right_width_bound


def put_grey_in_quadrant(img_pixels: ndarray,
                         start_width: int,
                         start_height: int,
                         avg_color: int,
                         mosaic_size: int,
                         grey_gradation: int) -> None:
    (right_height_bound, right_width_bound) = find_right_bounds_for_image_processing(img_pixels,
                                                                                     start_width,
                                                                                     start_height,
                                                                                     mosaic_size)

    for n in range(start_height, right_height_bound):
        for k in range(start_width, right_width_bound):
            img_pixels[n][k] = \
                [avg_color // grey_gradation * grey_gradation] * len(img_pixels[n][k])
