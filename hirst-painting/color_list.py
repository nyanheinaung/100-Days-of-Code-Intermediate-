import colorgram


def extract_color(img):

    colors = colorgram.extract(img, 30)
    color_list = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_list.append(new_color)

    return color_list
