#!/usr/bin/env python3
"""Render the HTML/CSS for one A4-landscape floor-plan sheet (Датский квартал)."""
import os

FONTS_DIR = os.path.abspath("./fonts")


def fmt(x):
    """1.09 -> '1,09' | 60.5 -> '60,5' | 12.0 -> '12'"""
    s = f"{float(x):.2f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _ff(family, weight, fname):
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"font-style:normal;src:url('file://{FONTS_DIR}/{fname}');}}")


def build_css():
    faces = "".join([
        _ff("Playfair", 400, "PlayfairDisplay-Regular.ttf"),
        _ff("Playfair", 700, "PlayfairDisplay-Bold.ttf"),
        _ff("Playfair", 900, "PlayfairDisplay-Black.ttf"),
        _ff("Manrope", 400, "Manrope-Regular.ttf"),
        _ff("Manrope", 500, "Manrope-Medium.ttf"),
        _ff("Manrope", 600, "Manrope-SemiBold.ttf"),
        _ff("Manrope", 700, "Manrope-Bold.ttf"),
    ])
    return faces + """
@page { size: A4 landscape; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { background: #FFFFFF; font-family: 'Manrope', sans-serif; color: #2C2630; }

.sheet {
  width: 297mm; height: 210mm; display: flex; background: #FFFFFF;
  overflow: hidden; page-break-after: always; position: relative;
}
.sheet:last-child { page-break-after: auto; }

/* ── LEFT : plan area ── */
.plan { width: 57%; padding: 13mm 0 13mm 13mm; display: flex; }
.planframe {
  flex: 1; border: 1px solid #D9CFC0; background: #FFFFFF; border-radius: 1.5mm;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column; gap: 4mm; position: relative;
}
.planframe::before {
  content: ""; position: absolute; left: 6mm; top: 6mm; right: 6mm; bottom: 6mm;
  border: 1px solid #EFE9DF; border-radius: 1mm;
}
.plan-mark {
  font-family: 'Playfair'; font-weight: 700; font-size: 11pt; color: #A8895C;
  letter-spacing: 0.18em; text-transform: uppercase; z-index: 1;
}
.plan-hint {
  font-family: 'Manrope'; font-weight: 600; font-size: 8.5pt; color: #C9BEAE;
  text-align: center; max-width: 95mm; line-height: 1.65; z-index: 1;
}
.plan-hint small { display: block; margin-top: 2mm; font-weight: 500;
  font-size: 7pt; color: #D5CBBF; }
.plan-hint .acc { color: #A8895C; font-weight: 700; }

/* ── DIVIDER ── */
.divider { width: 1px; background: #D9CFC0; flex: none; }

/* ── RIGHT : data ── */
.data { width: 43%; padding: 13mm 13mm 9mm 11mm; display: flex; flex-direction: column;
  background: #FFFFFF; }

.wordmark { font-family: 'Playfair'; font-weight: 700; font-size: 13pt; color: #2C2630;
  letter-spacing: 0.06em; text-transform: uppercase; line-height: 1; }
.submark { font-family: 'Manrope'; font-weight: 700; font-size: 7pt; color: #52358B;
  letter-spacing: 0.35em; text-transform: uppercase; margin-top: 2.5mm; }
.head-rule { border: none; border-top: 1px solid #D9CFC0; margin: 4.5mm 0; }

.kv-title { font-family: 'Playfair'; font-weight: 900; font-size: 24pt; color: #2C2630;
  letter-spacing: -0.01em; text-transform: uppercase; line-height: 1; }
.kv-meta { font-family: 'Manrope'; font-weight: 400; font-size: 8pt; color: #8A8290;
  margin-top: 2mm; letter-spacing: 0.02em; }

.area { border-top: 1px solid #D9CFC0; border-bottom: 1px solid #D9CFC0;
  padding: 4mm 0; margin: 4.5mm 0; }
.area-big { display: flex; align-items: baseline; gap: 2mm; }
.area-num { font-family: 'Playfair'; font-weight: 900; font-size: 42pt; color: #2C2630;
  letter-spacing: -0.02em; line-height: 0.85; }
.area-unit { font-family: 'Playfair'; font-weight: 700; font-size: 13pt; color: #52358B; }
.area-lbl { font-family: 'Manrope'; font-weight: 500; font-size: 6.5pt; color: #52358B;
  letter-spacing: 0.14em; text-transform: uppercase; margin-top: 2mm; }
.area-sub { display: flex; align-items: center; gap: 5mm; margin-top: 3.5mm; }
.area-sub .val { font-family: 'Manrope'; font-weight: 700; font-size: 12pt; color: #2C2630;
  display: block; line-height: 1; }
.area-sub .lbl { font-family: 'Manrope'; font-weight: 400; font-size: 6.5pt; color: #8A8290;
  letter-spacing: 0.1em; text-transform: uppercase; margin-top: 1mm; display: block; }
.area-sep { width: 1px; height: 9mm; background: #D9CFC0; }

.chips { display: flex; flex-wrap: nowrap; gap: 7mm; margin-bottom: 4.5mm; }
.chip { display: flex; align-items: baseline; }
.chip .v { font-family: 'Playfair'; font-weight: 900; font-size: 13pt; color: #2C2630; }
.chip .l { font-family: 'Manrope'; font-weight: 500; font-size: 7pt; color: #8A8290;
  margin-left: 1.5mm; }

.exp-h { font-family: 'Manrope'; font-weight: 600; font-size: 7pt; color: #52358B;
  letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 2mm; }
.erow { display: flex; align-items: baseline; padding: 0.55mm 0; }
.erow .en { font-family: 'Manrope'; font-weight: 400; font-size: 9pt; color: #2C2630; }
.erow .dots { flex: 1; border-bottom: 1px dotted #CFC4B3; margin: 0 2mm; transform: translateY(-1mm); }
.erow .ea { font-family: 'Manrope'; font-weight: 600; font-size: 9pt; color: #2C2630;
  white-space: nowrap; }

.spacer { flex: 1; }
.bottom-rule { border: none; border-top: 1.4pt solid #2C2630; margin-top: 4mm; padding-top: 3mm; }
.disclaimer { font-family: 'Manrope'; font-weight: 600; font-size: 9pt; color: #52358B;
  letter-spacing: 0.01em; }
.footrow { margin-top: 4mm; }
.dev-name { font-family: 'Manrope'; font-weight: 600; font-size: 6.5pt; color: #2C2630;
  letter-spacing: 0.04em; }
.legal { font-family: 'Manrope'; font-weight: 400; font-size: 6pt; color: #8A8290;
  letter-spacing: 0.02em; line-height: 1.6; margin-top: 1mm; }
"""


SPAL = ["", "спальня", "спальни", "спальни", "спальни", "спален"]


def build_page(lot):
    obsh = round(lot["zhilaya"] + lot["terrace"], 2)
    beds = lot["bedrooms"]
    baths = lot["baths"]
    spal = SPAL[beds] if beds <= 5 else "спален"
    san = "санузел" if baths == 1 else "санузла"

    rooms_html = ""
    for name, area in lot["rooms"]:
        rooms_html += (
            f'<div class="erow"><span class="en">{name}</span>'
            f'<span class="dots"></span>'
            f'<span class="ea">{fmt(area)}&nbsp;м²</span></div>'
        )

    return f'''<div class="sheet">
  <div class="plan">
    <div class="planframe">
      <div class="plan-mark">Планировка квартиры</div>
      <div class="plan-hint">Вставьте изображение планировки
        <small>на этаже 2 квартиры — соседнюю приглушите,<br>акцент на&nbsp;<span class="acc">кв.&nbsp;№{lot["apt"]}</span></small>
      </div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="data">
    <div class="wordmark">Хрустальный&nbsp;парк</div>
    <div class="submark">Датский&nbsp;квартал</div>
    <hr class="head-rule">
    <div class="kv-title">Квартира&nbsp;№{lot["apt"]}</div>
    <div class="kv-meta">{lot["group"]} · {lot["floor"]} этаж</div>
    <div class="area">
      <div class="area-big">
        <span class="area-num">{fmt(obsh)}</span><span class="area-unit">м²</span>
      </div>
      <div class="area-lbl">Общая площадь · жилая&nbsp;+&nbsp;терраса</div>
      <div class="area-sub">
        <div><span class="val">{fmt(lot["zhilaya"])}&nbsp;м²</span><span class="lbl">жилая</span></div>
        <div class="area-sep"></div>
        <div><span class="val">{fmt(lot["terrace"])}&nbsp;м²</span><span class="lbl">терраса</span></div>
      </div>
    </div>
    <div class="chips">
      <div class="chip"><span class="v">{beds}</span><span class="l">{spal}</span></div>
      <div class="chip"><span class="v">{baths}</span><span class="l">{san}</span></div>
      <div class="chip"><span class="v">{fmt(lot["terrace"])}</span><span class="l">м²&nbsp;терраса</span></div>
    </div>
    <div class="exp-h">Экспликация помещений</div>
    {rooms_html}
    <div class="spacer"></div>
    <div class="bottom-rule">
      <div class="disclaimer">Цены и точные площади уточняйте у менеджера</div>
    </div>
    <div class="footrow">
      <div class="dev-name">Застройщик&nbsp;ООО&nbsp;СЗ «Хрустальный&nbsp;Девелопмент»</div>
      <div class="legal">ЖК «Хрустальный&nbsp;парк» · Датский&nbsp;квартал · 14&nbsp;км Байкальского&nbsp;тракта, Иркутск<br>
      Дом введён в эксплуатацию · ключи сразу · hrustalnipark.ru</div>
    </div>
  </div>
</div>'''


def build_html(lots):
    pages = "".join(build_page(L) for L in lots)
    css = build_css()
    return f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{pages}</body></html>"
