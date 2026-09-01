---
tags:
  - ficha
  - capitulo-1
seccion: "1.18"
---

# Offload a CPU

> **En una línea.** Cuando el modelo no entra entero en la VRAM, el motor de inferencia deja algunas capas en la RAM del sistema y las procesa la CPU: funciona, pero puede ser entre 5 y 10 veces más lento.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.18 — VRAM, KV cache y offload|§1.18]]**
> y también se lo trata en [[1.19 — Ollama en la práctica|§1.19]].

---

## La idea, en corto

Un modelo son capas. Si no entran todas en la GPU, se cargan las que entren y el resto queda en RAM. Cada token generado tiene que atravesar **todas** las capas, así que en cada paso el cómputo salta de la GPU a la CPU y vuelve.

Ese salto es carísimo. La VRAM de una GPU moderna tiene un ancho de banda de cientos de GB/s; la RAM del sistema, mucho menos; y el bus PCIe entre las dos es otro cuello. Una sola capa en CPU puede dominar el tiempo total.

## Conectado con

[[VRAM]] · [[KV cache]] · [[Ollama]] · [[Cuantización]] · [[Compute capability]] · [[Modelo grande cuantizado vs modelo chico completo]]

---

**Leer el desarrollo:** [[1.18 — VRAM, KV cache y offload]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
