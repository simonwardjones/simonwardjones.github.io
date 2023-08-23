import math


colours = [
    "rgb(252, 254, 7)",
    "rgb(252, 143, 9)",
    "rgb(252, 91, 9)",
    "rgb(252, 44, 8)",
    "rgb(198, 6, 9)",
    "rgb(145, 6, 89)",
    "rgb(89, 6, 90)",
    "rgb(8, 6, 88)",
    "rgb(13, 50, 144)",
    "rgb(8, 91, 90)",
    "rgb(47, 141, 11)",
    "rgb(88, 200, 0)",
]


def get_arcs():
    # cx = centre x
    # sx = start x
    # fx = finish x
    cx, cy = 50, 50
    r = 30
    n = len(colours)
    paths = []
    sw = 12  # stroke width
    for i, colour in enumerate(colours):
        start_angle = (i / n) * 2 * math.pi
        end_angle = ((i + 1) / n) * 2 * math.pi
        sx = cx + math.sin(start_angle) * r
        sy = cy - math.cos(start_angle) * r
        xr = 0  # x-axis rotation
        laf = 0  # large arc flag
        sf = 1  # sweep flag
        fx = cx + math.sin(end_angle) * r
        fy = cy - math.cos(end_angle) * r
        path = f"""<path
d='M {sx:.4f} {sy:.4f} A {r:.4f} {r:.4f} {xr} {laf} {sf} {fx:.4f} {fy:.4f}'
stroke='{colour}'
stroke-width='{sw}'/>""".replace(
            "\n", " "
        )
        print(path)


def get_circles():
    cx, cy = 50, 50
    r = 30
    offset = -90  # start at 12 o'clock
    n = len(colours)
    circumference = 2 * math.pi * r
    seg = circumference / n
    sw = 30 # stroke width
    buffer = seg * n  # longer than remainder of circumference
    for i, colour in enumerate(colours):
        rotate = f"rotate({offset + (i/n) * 360} {cx} {cy})"
        start_angle = (i / n) * 2 * math.pi
        circle = f"""<circle class="circleComponent"
r="{r}" cx="{cx}" cy="{cy}" stroke="{colour}"
transform="{rotate}"
stroke-dasharray="{seg} {buffer}"
stroke-width="{sw}"
fill="none"/>
            """.replace(
            "\n", " "
        )
        print(circle)


def get_colour_gradient():
    n = len(colours)
    for i, colour in enumerate(colours):
        colour_from, colour_to = (i / n) * 360, ((i + 1) / n) * 360
        print(f"{colour:<18} {colour_from}deg {colour_to}deg,")


if __name__ == "__main__":
    get_arcs()
    get_circles()
    get_colour_gradient()
