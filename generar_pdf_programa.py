# -*- coding: utf-8 -*-
"""
Genera Programa_General_VI_CIGESTUR_2026.pdf (A4) a partir de la página publicada,
usando su hoja de estilos de impresión. Ejecutar tras publicar index.html en GitHub Pages.

Uso: python generar_pdf_programa.py [url]
"""
import os
import sys
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "https://leogallardo97-bit.github.io/cigestur-2026-programa-general/"
DST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Programa_General_VI_CIGESTUR_2026.pdf")

FOOTER = """<div style="width:100%;font-family:Arial,sans-serif;font-size:7.5pt;color:#5c5c6b;
 padding:0 12mm;display:flex;justify-content:space-between;">
 <span>VI CIGESTUR 2026 · Programa General · Universidad de Córdoba · congresogestionturisticadelpatrimonio.com</span>
 <span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>"""

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page()
    pg.goto(URL, wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.evaluate("[...document.images].every(i => i.complete)")
    pg.emulate_media(media="print")
    pg.pdf(path=DST, format="A4", print_background=True, prefer_css_page_size=True,
           display_header_footer=True, header_template="<div></div>", footer_template=FOOTER,
           margin={"top": "14mm", "bottom": "16mm", "left": "12mm", "right": "12mm"})
    b.close()
print(DST)
