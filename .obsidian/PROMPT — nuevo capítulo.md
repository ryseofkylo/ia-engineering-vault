# PROMPT REUTILIZABLE — Agregar un capítulo al manual de AI Engineering

> Copiá todo lo que está debajo de la línea, completá el bloque **A COMPLETAR** y pegalo en una conversación nueva.
> Guardado acá para no ensuciar el libro. Este archivo no aparece en el explorador de Obsidian.

---

Necesito que agregues un capítulo nuevo a mi manual de AI Engineering, siguiendo **exactamente** el mismo criterio y la misma estructura que el Capítulo 1, que ya está terminado.

## A COMPLETAR

- **Capítulo:** <N>
- **Materia del plan:** <MX — nombre de la materia>
- **Duración y correlativas:** <lo que dice el plan>
- **Unidades del plan** (pegar textual el bloque de la materia desde `C:\Users\Matias\Downloads\plan-estudio.html`):

```
<pegar acá las unidades, el trabajo práctico y el criterio de aprobación>
```

- **Fuentes** (los links de los que hay que extraer el conocimiento):

```
1. <url>
2. <url>
3. <url>
...
```

## Antes de escribir nada

**Leé el Capítulo 1 que ya está hecho** en `C:\Users\Matias\Documents\IA Engineering\01 — Capítulo 1 · Fundamentos de LLMs\`. Es el modelo a imitar: mirá al menos `1.0 — Presentación del capítulo`, dos secciones de contenido completas y tres fichas del índice analítico. Todo lo que sigue en este prompt describe lo que vas a ver ahí; si algo se contradice, gana lo que está escrito en el Capítulo 1.

## El principio de diseño, que es lo más importante

**El libro reemplaza a las fuentes. No las acompaña.**

Yo **no voy a abrir los links**. El objetivo es que el conocimiento que hay en ellos quede trasladado y desarrollado adentro de las notas, de forma que no necesite nada más. Nada de "mirá el video", "leé la sección 2 del paper", "hacé las lecciones 5 y 6". La bibliografía existe sólo por trazabilidad, y tiene que decirlo explícitamente.

Corolarios que no se negocian:

1. **Lectura sostenida.** Secciones largas (1.200–2.500 palabras) en prosa continua, no en viñetas. Se lee como un manual de facultad, de corrido.
2. **Cada sección es autosuficiente.** Las referencias cruzadas ("como vimos en §N.3") son referencias, no interrupciones: se puede seguir leyendo sin ir.
3. **Los enlaces a fichas van SÓLO en una línea al final**, nunca en medio del texto. Tener que saltar a las fichas para encontrar la sustancia es exactamente el error que ya corregimos una vez.
4. **Nada de "etapa" ni "lectura" como rótulo estructural.** Son **secciones** numeradas §N.M.
5. **Todo aterriza en mis sistemas reales**, no en ejemplos de juguete.

## Estructura obligatoria

```
01 — Capítulo N · <materia>/
    N.0 — Presentación del capítulo.md         ← índice con enlaces, arco, qué vas a saber hacer
    01 — Parte I · <tema>/     §N.1 …
    02 — Parte II · <tema>/
    03 — Parte III · <tema>/
    04 — Parte IV · <tema>/                    ← 4 a 6 partes según el material
    05 — Parte V · <tema>/
    06 — Cierre/
        N.20 — Trabajo práctico.md
        N.21 — Laboratorio.md
        N.22 — Autoevaluación.md
    07 — Índice analítico/                     ← las fichas: una por concepto
    sortspec.md                                ← uno por carpeta
```

- **Numeración continua dentro del capítulo**: §N.14 es la sección 14 aunque esté en la Parte V.
- Apuntá a **18–25 secciones** de contenido más las 3 de cierre.
- Las partes agrupan por tema y le dan al panel izquierdo forma de índice de libro.

## Anatomía de cada sección de contenido

En este orden, siempre:

1. **H1** `# N.M · Título`
2. **Apertura** de 2–4 párrafos que sitúan el tema y dicen por qué esta sección va acá.
3. **Desarrollo en prosa** con subtítulos `##`, ejemplos trabajados, tablas y código real.
4. **`## Cómo se ve esto en <mi sistema>`** — la bajada concreta y accionable.
5. **`## Errores frecuentes`** — en negrita el error, después la explicación.
6. **`## Resumen de la sección`** — lista numerada de 6 a 9 puntos.
7. **Línea de términos**: `**Términos de esta sección**: [[Ficha]] · [[Ficha]] …`
8. **Pie de navegación**, tabla de dos columnas:

```
| | |
|---|---|
| **← Anterior** [[N.M-1 — …]] | **Siguiente →** [[N.M+1 — …]] |
```

Usá callouts `> [!warning]`, `> [!important]`, `> [!note]` para lo que no se puede pasar por alto. Diagramas ASCII cuando aclaren un mecanismo.

## Las fichas del índice analítico

Una por concepto atómico. **No son lectura: son consulta y son lo que dibuja el grafo.** Estructura:

```markdown
---
tags:
  - ficha
  - capitulo-N
seccion: "N.M"
---

# <Término>

> **En una línea.** <definición de una sola oración; de acá sale el glosario>

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[N.M — …|§N.M]]**
> y también se lo trata en [[…|§N.K]].

---

## La idea, en corto

<2–3 párrafos, no más>

## Conectado con

[[Otra ficha]] · [[Otra ficha]] · …

---

**Leer el desarrollo:** [[N.M — …]] · **Índice del capítulo:** [[N.0 — Presentación del capítulo]]
```

## El procedimiento

1. **Investigá las fuentes de verdad.** Traelas con WebFetch. **No escribas de memoria.** Si un resumen automático parece flojo o sospechoso, bajá el PDF o el HTML original y leelo — en el Capítulo 1, el resumen del abstract de un paper listaba modelos que el paper no había evaluado, y sólo se detectó yendo al PDF.
2. **Diseñá el arco** antes de escribir: agrupá las fuentes en 4–6 partes que sigan el recorrido natural del tema.
3. **Ordená pedagógicamente**, siguiendo el orden de las unidades del plan de estudios, no el orden en que yo pegué los links. Si cambia, documentalo en la nota de edición con la razón concreta de cada movimiento y una tabla de equivalencia con mi numeración original.
4. **Escribí sección por sección**, completas, sin dejar esqueletos para después.
5. **Generá las fichas** del índice analítico.
6. **Escribí los `sortspec.md`** de cada carpeta.
7. **Regenerá el glosario** — hay que extender `.obsidian/regenerar-glosario.py` para que cubra el capítulo nuevo.
8. **Verificá** con `.obsidian/verificar-boveda.py` — hay que extenderlo con las secciones del capítulo nuevo. Tiene que dar **cero problemas**.
9. **Auditá la cobertura fuente por fuente**: por cada link, listá los conceptos, números y términos que aporta y comprobá con un grep que **todos** estén en el libro. Reportame la tabla de cobertura. Si falta algo, cerralo.

## Criterios de calidad (tienen que dar todos)

- 0 enlaces rotos, 0 anclas a encabezados inexistentes, 0 notas huérfanas.
- Cadena de navegación completa: el "Siguiente" de cada sección apunta a la que sigue y el "Anterior" a la previa.
- 0 enlaces a fichas fuera de la línea de términos.
- 0 frases que manden a las fuentes.
- Cobertura 100 % en la auditoría fuente por fuente.
- Cada sección de contenido entre 1.200 y 2.500 palabras.

## Cómo escribir

- **Español rioplatense**, de vos. Explicado para que lo entienda alguien que no sabe nada del tema, sin ser condescendiente.
- **Precisión sobre entusiasmo.** Los números van con su fuente y su contexto; si un dato es de 2023 y puede no aplicar hoy, decilo.
- **Marcá lo inferido.** Si algo no se pudo verificar en fuente primaria, decilo en el texto.
- Cuando una técnica funcione en un benchmark y no necesariamente en mi tarea, decilo explícitamente y mandame a medirlo.

## Mi contexto técnico (para los ejemplos)

- **`schema-rag`** (Supercanal): RAG sobre el esquema de una base SQL Server/Synapse para generar text-to-SQL. ~778 objetos, ~14.232 columnas. ChromaDB + sentence-transformers. Indexa datos de clientes reales (campos como `CLIENTENRO`, `CONTRATONRO`), y por eso la privacidad del dato es el argumento de peso para correr modelos locales.
- **`LiftIQ`**: segundo sistema con LLM.
- **Hardware**: RTX 5070 Ti, 16 GB de VRAM, compute capability 12.0 (Blackwell).
- Ya traigo SQL y Python con soltura. No arranco de cero: no repitas fundamentos de programación.

## Al terminar

Reportame:
- Estructura final y cantidad de secciones, fichas y palabras.
- La tabla de cobertura fuente por fuente.
- El resultado de la verificación mecánica.
- Qué queda pendiente que dependa de mí (mis datos, mis mediciones).
- Si reordenaste las fuentes, la tabla de equivalencia con mi numeración original.

**No me preguntes si empezás: empezá.** Si hay una decisión de diseño ambigua, tomala vos y explicámela después.
