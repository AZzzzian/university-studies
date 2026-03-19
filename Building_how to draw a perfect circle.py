import math
"""
Draw an ASCII circle with aspect-ratio correction and light supersampling so it
looks rounder on typical terminals. "x" draws the outline, "#" marks the center.
"""


def draw_circle(radius, aspect_ratio=0.46, thickness=0.35):
    """Render a circle; tweak aspect_ratio to match your font (width/height)."""
    # Sample four sub-points per cell to reduce blocky edges.
    samples = ((0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75))

    # Stretch x-range based on aspect ratio; extra margin avoids clipping.
    x_extent = int(math.ceil(radius / aspect_ratio)) + 1

    for y in range(-radius - 1, radius + 2):
        row_chars = []
        for x in range(-x_extent - 1, x_extent + 2):
            hits = 0
            for sx, sy in samples:
                dx = (x + sx) * aspect_ratio
                dy = y + sy
                distance = math.hypot(dx, dy)
                if radius - thickness <= distance <= radius + thickness:
                    hits += 1

            coverage = hits / len(samples)
            if coverage >= 0.5:
                row_chars.append("x")
            elif x == 0 and y == 0:
                row_chars.append("#")
            else:
                row_chars.append(" ")

        # Avoid extra spaces that can distort width; join directly.
        print("".join(row_chars))


if __name__ == "__main__":
    # Tune aspect_ratio to your font: try 0.45-0.5 if still tall/flat.
    draw_circle(5, aspect_ratio=0.46)
    draw_circle(10, aspect_ratio=0.46)
    draw_circle(20, aspect_ratio=0.46)












