#!/usr/bin/env python3
"""Download Playfair Display + Manrope variable fonts and instantiate static weights."""
import os, urllib.request, ssl
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

FONTS = "./fonts"
os.makedirs(FONTS, exist_ok=True)
ctx = ssl.create_default_context()

SOURCES = {
    "Playfair": "https://github.com/google/fonts/raw/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf",
    "Manrope":  "https://github.com/google/fonts/raw/main/ofl/manrope/Manrope%5Bwght%5D.ttf",
}

def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print("cached", dest); return
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    print("downloaded", dest, len(data))

def instance(var_path, wght, out_path):
    f = TTFont(var_path)
    instantiateVariableFont(f, {"wght": wght}, inplace=True)
    f.save(out_path)
    print("instanced", out_path, wght)

var = {}
for fam, url in SOURCES.items():
    p = os.path.join(FONTS, f"{fam}-VAR.ttf")
    download(url, p)
    var[fam] = p

# Playfair: 400, 700, 900
for w, name in [(400, "Regular"), (700, "Bold"), (900, "Black")]:
    instance(var["Playfair"], w, os.path.join(FONTS, f"PlayfairDisplay-{name}.ttf"))
# Manrope: 400, 500, 600, 700
for w, name in [(400, "Regular"), (500, "Medium"), (600, "SemiBold"), (700, "Bold")]:
    instance(var["Manrope"], w, os.path.join(FONTS, f"Manrope-{name}.ttf"))

print("FONTS DONE")
