__author__ = "730761420"


def get_coords(xs: str, ys: str) -> None:
    xindx: int = 0
    while xindx < len(xs):
        yindx: int = 0
        while yindx < len(ys):
            print((xs[xindx]) + (ys[yindx]))
            yindx += 1
        xindx += 1
