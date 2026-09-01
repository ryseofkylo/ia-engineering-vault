---
tags:
  - ficha
  - capitulo-1
seccion: "1.15"
---

# Cuantización

> **En una línea.** Es guardar los pesos del modelo con menos precisión numérica —por ejemplo 4 bits en vez de 16— para que ocupe menos memoria y corra más rápido, a cambio de un error chiquito que casi siempre no se nota.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.15 — Precisión numérica y la idea de cuantizar|§1.15]]**
> y también se lo trata en [[1.16 — El mecanismo de la cuantización|§1.16]].

---

## La idea, en corto

La analogía más clara es ésta: cuando te preguntan la hora, contestás **"10:21"**. No contestás "10:21, 18 segundos, 700 milisegundos y 3 nanosegundos". Tenés la precisión disponible y elegís tirarla, porque para la función que cumple la respuesta el resto es ruido caro de transmitir.

Con los pesos de un modelo pasa lo mismo. Están guardados con mucha precisión, y para que el modelo funcione no hace falta tanta.

## Conectado con

[[Precisión numérica]] · [[Cuantización afín]] · [[Granularidad de la cuantización]] · [[PTQ y QAT]] · [[Weight packing]] · [[FP8]] · [[Perplexity]] · [[Modelo grande cuantizado vs modelo chico completo]] · [[VRAM]]

---

**Leer el desarrollo:** [[1.15 — Precisión numérica y la idea de cuantizar]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
