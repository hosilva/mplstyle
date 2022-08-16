import numpy as np

maths_colours = np.array([
    [0.368417, 0.506779, 0.709798],
    [0.880722, 0.611041, 0.142051],
    [0.560181, 0.691569, 0.194885],
    [0.922526, 0.385626, 0.209179],
    [0.528488, 0.470624, 0.701351],
    [0.772079, 0.431554, 0.102387],
    [0.363898, 0.618501, 0.782349],
    [1, 0.75, 0],
    [0.647624, 0.37816, 0.614037]
    ])

i = 1

for colours in maths_colours:
    rgb = ( colours * 255 ).astype(int)
    hex_string = "#" + hex(rgb[0])[-2:] + hex(rgb[1])[-2:] + hex(rgb[2])[-2:]
    hex_string_no_x = hex_string.replace("x","0")
    print("colour_0" + str(i) + " = " + hex_string_no_x)
    i+=1
