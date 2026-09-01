# -*- coding: utf-8 -*-
"""Verificación de coherencia de la bóveda-libro.

Corré:  python .obsidian/verificar-boveda.py
"""
import os, io, re, sys, collections

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = os.path.join(VAULT, "01 — Capítulo 1 · Fundamentos de LLMs")
FICHAS = os.path.join(CAP, "07 — Índice analítico")

# Orden canónico del libro
SECCIONES = [
    "1.0 — Presentación del capítulo",
    "1.1 — El modelo no lee texto, lee números",
    "1.2 — Byte Pair Encoding",
    "1.3 — Tokenizers reales y el costo de cada token",
    "1.4 — La ventana de contexto",
    "1.5 — Lost in the Middle",
    "1.6 — Por qué pasa y qué hacer al respecto",
    "1.7 — Logits, softmax y azar",
    "1.8 — Temperature",
    "1.9 — Top-k y top-p",
    "1.10 — Logprobs, parada y test time compute",
    "1.11 — Del texto libre al dato",
    "1.12 — Las cuatro estrategias",
    "1.13 — Constrained decoding",
    "1.14 — Local o API",
    "1.15 — Precisión numérica y la idea de cuantizar",
    "1.16 — El mecanismo de la cuantización",
    "1.17 — Elegir un modelo",
    "1.18 — VRAM, KV cache y offload",
    "1.19 — Ollama en la práctica",
    "1.20 — Trabajo práctico",
    "1.21 — Laboratorio",
    "1.22 — Autoevaluación",
]

problemas = []


def fallo(cat, msg):
    problemas.append((cat, msg))


# ---------------------------------------------------------------- inventario
notas = {}
for raiz, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        if f.endswith(".md"):
            nombre = os.path.splitext(f)[0]
            if nombre == "sortspec":
                continue
            if nombre in notas:
                fallo("duplicado", f"nombre repetido: {nombre}")
            notas[nombre] = os.path.join(raiz, f)

print(f"Notas de contenido: {len(notas)}")

# Acepta [[Nota]], [[Nota#Ancla]], [[Nota|alias]] y [[Nota\|alias]] (pipe escapado en tablas)
LINK = re.compile(r"\[\[([^\]\|#\\]+?)(?:\\?#([^\]\|\\]+))?(?:\\?\|[^\]]*)?\]\]")

entrantes = collections.Counter()
salientes = collections.Counter()
anclas = []
total_links = 0

for nombre, ruta in sorted(notas.items()):
    texto = io.open(ruta, encoding="utf-8").read()
    limpio = re.sub(r"(?s)```.*?```", "", texto)
    limpio = re.sub(r"`[^`\n]*`", "", limpio)
    for m in LINK.finditer(limpio):
        destino = m.group(1).strip()
        ancla = (m.group(2) or "").strip()
        salientes[nombre] += 1
        total_links += 1
        if destino not in notas:
            fallo("enlace roto", f"{nombre} → [[{destino}]]")
        else:
            entrantes[destino] += 1
            if ancla:
                anclas.append((nombre, destino, ancla))

for origen, destino, ancla in anclas:
    t = io.open(notas[destino], encoding="utf-8").read()
    encabezados = [h.strip() for h in re.findall(r"^#{1,6}\s+(.+)$", t, re.M)]
    if ancla not in encabezados:
        fallo("ancla rota", f"{origen} → [[{destino}#{ancla}]]")

for n in notas:
    if entrantes[n] == 0:
        fallo("huérfana", n)
    if salientes[n] == 0:
        fallo("sin salientes", n)

# ------------------------------------------------- cadena de navegación
NAV_SIG = re.compile(r"\*\*Siguiente →\*\*\s*\[\[([^\]\|]+)")
NAV_ANT = re.compile(r"\*\*← Anterior\*\*\s*\[\[([^\]\|]+)")

for i, sec in enumerate(SECCIONES):
    if sec not in notas:
        fallo("sección faltante", sec)
        continue
    t = io.open(notas[sec], encoding="utf-8").read()

    if not re.search(r"^# " + re.escape(sec.split(" — ")[1]), t, re.M) \
       and not re.search(r"^# ", t, re.M):
        fallo("sin H1", sec)

    ms = NAV_SIG.search(t)
    ma = NAV_ANT.search(t)

    if i + 1 < len(SECCIONES):
        esperado = SECCIONES[i + 1]
        if not ms:
            fallo("nav", f"{sec}: falta 'Siguiente →'")
        elif ms.group(1).strip() != esperado:
            fallo("nav", f"{sec}: Siguiente apunta a '{ms.group(1).strip()}', se esperaba '{esperado}'")
    if i > 0:
        esperado = SECCIONES[i - 1]
        if not ma:
            fallo("nav", f"{sec}: falta '← Anterior'")
        elif ma.group(1).strip() != esperado:
            fallo("nav", f"{sec}: Anterior apunta a '{ma.group(1).strip()}', se esperaba '{esperado}'")

# secciones de contenido (1.1–1.19) deben tener resumen
for sec in SECCIONES[1:20]:
    if sec in notas:
        t = io.open(notas[sec], encoding="utf-8").read()
        if "## Resumen de la sección" not in t:
            fallo("estructura", f"{sec}: sin 'Resumen de la sección'")
        if "## Errores frecuentes" not in t:
            fallo("estructura", f"{sec}: sin 'Errores frecuentes'")
        if "**Términos de esta sección**" not in t:
            fallo("estructura", f"{sec}: sin línea de términos")

# ------------------------------------------------------------- fichas
RE_LINEA = re.compile(r"^> \*\*En una línea\.\*\*\s*(.+)$", re.M)
RE_DES = re.compile(r"^\*\*Leer el desarrollo:\*\* \[\[([^\]]+)\]\]", re.M)

fichas = sorted(f[:-3] for f in os.listdir(FICHAS) if f.endswith(".md") and f != "sortspec.md")
print(f"Fichas del índice analítico: {len(fichas)}")

for nombre in fichas:
    t = io.open(os.path.join(FICHAS, nombre + ".md"), encoding="utf-8").read()
    if not RE_LINEA.search(t):
        fallo("ficha", f"{nombre}: sin 'En una línea'")
    if not re.search(r"^# " + re.escape(nombre) + r"\s*$", t, re.M):
        fallo("ficha", f"{nombre}: el H1 no coincide con el nombre del archivo")
    if not re.search(r'^seccion:\s*"[\d.]+"', t, re.M):
        fallo("ficha", f"{nombre}: sin campo 'seccion' en el frontmatter")
    m = RE_DES.search(t)
    if not m:
        fallo("ficha", f"{nombre}: sin 'Leer el desarrollo'")
    elif m.group(1).strip() not in SECCIONES:
        fallo("ficha", f"{nombre}: apunta a una sección inexistente: {m.group(1)}")

# ------------------------------------------------------------ sortspec
RE_SPEC = re.compile(r"^sorting-spec: \|\n((?:  .+\n)+)", re.M)
specs = 0
for raiz, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    if "sortspec.md" not in files:
        continue
    specs += 1
    ruta = os.path.join(raiz, "sortspec.md")
    t = io.open(ruta, encoding="utf-8").read()
    m = RE_SPEC.search(t)
    if not m:
        fallo("sortspec", f"{ruta}: no se pudo leer la lista")
        continue
    presentes = {os.path.splitext(x)[0] for x in os.listdir(raiz)}
    for linea in m.group(1).splitlines():
        item = linea.strip()
        if not item or item.startswith("target-folder:"):
            continue
        if item not in presentes:
            fallo("sortspec", f"{os.path.relpath(raiz, VAULT)}: '{item}' no existe en la carpeta")

print(f"Archivos sortspec: {specs}")

# ------------------------------------------------- restos de la versión vieja
RESTOS = ["Etapa 1 —", "Etapa 2 —", "Lectura 1 —", "Lectura 2 —",
          "02 — Conceptos", "01 — Lecturas", "03 — Práctica",
          "Revisión del Capítulo", "Bibliografía verificada", "Empezá acá"]
for nombre, ruta in notas.items():
    t = io.open(ruta, encoding="utf-8").read()
    for r in RESTOS:
        if r in t:
            fallo("resto viejo", f"{nombre}: contiene '{r}'")

# ------------------------------------------------------------- informe
print()
print(f"Enlaces internos: {total_links}  ·  promedio por nota: {total_links/max(len(notas),1):.1f}")
print()
if problemas:
    por_cat = collections.defaultdict(list)
    for cat, msg in problemas:
        por_cat[cat].append(msg)
    for cat in sorted(por_cat):
        print(f"=== {cat.upper()} ({len(por_cat[cat])}) ===")
        for msg in por_cat[cat]:
            print("   ", msg)
        print()
    print(f"TOTAL DE PROBLEMAS: {len(problemas)}")
    sys.exit(1)
else:
    print("Sin problemas: 0 enlaces rotos, 0 anclas rotas, 0 huérfanas,")
    print("cadena de navegación completa, fichas y sortspec consistentes.")
