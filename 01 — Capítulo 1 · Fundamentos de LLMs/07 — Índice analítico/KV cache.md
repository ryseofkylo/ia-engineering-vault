---
tags:
  - ficha
  - capitulo-1
seccion: "1.18"
---

# KV cache

> **En una línea.** Es la memoria donde el modelo guarda los cálculos intermedios de todos los tokens ya procesados para no repetirlos en cada paso; crece linealmente con la ventana de contexto y es la razón número uno por la que un modelo que "debería entrar" no entra.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.18 — VRAM, KV cache y offload|§1.18]]**
> y también se lo trata en [[1.4 — La ventana de contexto|§1.4]].

---

## La idea, en corto

Un modelo autorregresivo genera token por token. Sin cache, para generar el token 500 tendría que recalcular la atención sobre los 499 anteriores desde cero, en cada paso. Sería absurdamente lento.

La solución: guardar, para cada token ya procesado y para cada capa, sus vectores **Key** y **Value**. Eso es el KV cache. Con él, cada token nuevo sólo calcula lo suyo y consulta el cache.

## Conectado con

[[VRAM]] · [[Offload a CPU]] · [[Ventana de contexto]] · [[Ollama]] · [[Más contexto no es mejor]] · [[Modelo grande cuantizado vs modelo chico completo]]

---

**Leer el desarrollo:** [[1.18 — VRAM, KV cache y offload]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
