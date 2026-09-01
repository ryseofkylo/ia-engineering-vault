# -*- coding: utf-8 -*-
"""Regenera 90 — Glosario.md a partir de las fichas del índice analítico.

Corré:  python .obsidian/regenerar-glosario.py
"""
import os, io, re

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHAS = os.path.join(VAULT, "01 — Capítulo 1 · Fundamentos de LLMs", "07 — Índice analítico")

PARTES = [
    ("Parte I · Cómo el modelo recibe el texto", ["1.1", "1.2", "1.3", "1.4"]),
    ("Parte II · Qué hace el modelo con un contexto largo", ["1.5", "1.6"]),
    ("Parte III · Cómo el modelo elige cada palabra", ["1.7", "1.8", "1.9", "1.10"]),
    ("Parte IV · Cómo se fuerza la forma de la salida", ["1.11", "1.12", "1.13"]),
    ("Parte V · Dónde corre el modelo", ["1.14", "1.15", "1.16", "1.17", "1.18", "1.19"]),
]

RE_LINEA = re.compile(r"^> \*\*En una línea\.\*\*\s*(.+)$", re.M)
RE_SEC = re.compile(r'^seccion:\s*"([\d.]+)"', re.M)
RE_DES = re.compile(r"^\*\*Leer el desarrollo:\*\* \[\[([^\]]+)\]\]", re.M)

entradas = []
for f in sorted(os.listdir(FICHAS)):
    if not f.endswith(".md") or f == "sortspec.md":
        continue
    nombre = f[:-3]
    t = io.open(os.path.join(FICHAS, f), encoding="utf-8").read()
    linea = RE_LINEA.search(t)
    sec = RE_SEC.search(t)
    des = RE_DES.search(t)
    if not (linea and sec and des):
        print("!! ficha incompleta:", nombre)
        continue
    entradas.append((nombre, linea.group(1).strip(), sec.group(1), des.group(1)))

g = ["---", "tags:", "  - indice", "  - glosario", "---", "",
     "# Glosario", "",
     f"> Los {len(entradas)} términos del Capítulo 1, en una línea cada uno.",
     "> Es la hoja de repaso: si podés reconstruir la explicación completa a partir de su línea, entendiste el tema.",
     "> La columna **§** te lleva a la sección del libro donde se desarrolla.",
     "",
     "> [!note] Esta página se genera sola",
     "> Sale de la línea `En una línea` de cada ficha del índice analítico. Si querés cambiar una definición, cambiala en la ficha, no acá. El script está en `.obsidian/regenerar-glosario.py`.",
     "", "---", "",
     "## Por orden alfabético", "",
     "| Término | En una línea | § |", "|---|---|---|"]

for nombre, linea, sec, des in sorted(entradas, key=lambda e: e[0].lower()):
    limpia = linea.replace("|", "\\|")
    g.append(f"| [[{nombre}]] | {limpia} | [[{des}\\|§{sec}]] |")

g += ["", "---", "", "## Por orden de aparición en el libro", ""]

por_sec = {}
for nombre, linea, sec, des in entradas:
    por_sec.setdefault(sec, []).append((nombre, linea))

for titulo, secs in PARTES:
    g.append(f"### {titulo}")
    g.append("")
    for s in secs:
        for nombre, linea in sorted(por_sec.get(s, [])):
            g.append(f"- **[[{nombre}]]** *(§{s})* — {linea}")
    g.append("")

g += ["---", "",
      f"**{len(entradas)} términos.** Volver a [[1.0 — Presentación del capítulo]] · [[00 — Cómo leer este libro]]", ""]

destino = os.path.join(VAULT, "90 — Glosario.md")
with io.open(destino, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(g))
print("Glosario regenerado con", len(entradas), "términos")
