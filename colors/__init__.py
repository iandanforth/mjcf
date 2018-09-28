from math import ceil
from .viridis import viridis # NoQA
from .plasma import plasma # NoQA
from .inferno import inferno # NoQA
from .magma import magma # NoQA


def get_rgb(colorscale, val):
    assert 0 <= val and val <= 1
    num_colors = len(colorscale)

    index = int(ceil(val * num_colors)) - 1

    return colorscale[index]
