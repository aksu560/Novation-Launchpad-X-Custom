def xy_to_pad_coords(x, y):
    return y * 10 + x

def pad_coords_to_xy(coords):
    x = coords % 10
    y  = int(coords / 10)
    return (x, y)