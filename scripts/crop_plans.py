#!/usr/bin/env python3
"""Crop each source presentation image down to just the floor-plan drawing.
Source layout (4096x2896): title top-left, logo top-right, plan drawing left-center,
old data panel right. We keep only the plan drawing (left region, below title band)."""
import os
import numpy as np
from PIL import Image

SRC = "assets/plans"
OUT = "assets/plans_crop"
os.makedirs(OUT, exist_ok=True)

# region of interest (fractions): exclude top title band and right data panel
ROI_X1, ROI_Y0, ROI_Y1 = 0.49, 0.155, 0.99
PAD = 0.012  # padding as fraction of width


def crop_plan(path, out):
    im = Image.open(path).convert("RGB")
    W, H = im.size
    arr = np.asarray(im)
    x1 = int(W * ROI_X1)
    y0, y1 = int(H * ROI_Y0), int(H * ROI_Y1)
    roi = arr[y0:y1, 0:x1]
    # content = not near-white
    gray = roi.min(axis=2)
    mask = gray < 232
    ys, xs = np.where(mask)
    if len(xs) == 0:
        im.save(out); return im.size
    pad = int(W * PAD)
    left = max(0, xs.min() - pad)
    right = min(x1, xs.max() + pad)
    top = max(0, y0 + ys.min() - pad)
    bot = min(H, y0 + ys.max() + pad)
    crop = im.crop((left, top, right, bot))
    crop.save(out, "PNG")
    return crop.size


if __name__ == "__main__":
    import sys
    names = sys.argv[1:] or [f for f in os.listdir(SRC) if f.endswith(".png") and f != "test.png"]
    for nm in names:
        sz = crop_plan(os.path.join(SRC, nm), os.path.join(OUT, nm))
        print(nm, "->", sz)
