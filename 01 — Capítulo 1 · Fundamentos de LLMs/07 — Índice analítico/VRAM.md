---
tags:
  - ficha
  - capitulo-1
seccion: "1.18"
---

# VRAM

> **En una línea.** Es la memoria de tu placa de video, y es el límite duro que decide qué modelos podés correr: si el modelo más su contexto no entran, o no arranca o se parte con la CPU y se vuelve lentísimo.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.18 — VRAM, KV cache y offload|§1.18]]**
> y también se lo trata en [[1.15 — Precisión numérica y la idea de cuantizar|§1.15]].

---

## La idea, en corto

**2. [[KV cache]].** Crece con la ventana de contexto y con la cantidad de pedidos en paralelo. Es la parte que la gente olvida.

**3. Activaciones y buffers.** Los valores intermedios de cada capa. Relativamente chicos en inferencia.

## Conectado con

[[KV cache]] · [[Offload a CPU]] · [[Cuantización]] · [[Precisión numérica]] · [[Ollama]] · [[Compute capability]] · [[Modelo grande cuantizado vs modelo chico completo]] · [[Ventana de contexto]]

---

**Leer el desarrollo:** [[1.18 — VRAM, KV cache y offload]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
