---
tags:
  - ficha
  - capitulo-1
seccion: "1.12"
---

# Function calling

> **En una línea.** Es describirle al modelo un conjunto de funciones con sus parámetros, para que en vez de contestar texto devuelva "quiero llamar a esta función con estos argumentos" — y de paso es la forma más práctica de obtener salida estructurada.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.12 — Las cuatro estrategias|§1.12]]**

---

## La idea, en corto

Le pasás a la API una lista de funciones disponibles, cada una con nombre, descripción y un esquema JSON de sus parámetros. El modelo decide si corresponde llamar a alguna y devuelve el nombre más los argumentos, ya con la forma correcta.

**El modelo no ejecuta nada.** Sólo dice qué habría que ejecutar. La ejecución la hacés vos, y ese es un límite de seguridad importante.

## Conectado con

[[Cómo se fuerza un formato]] · [[JSON mode]] · [[Pydantic como contrato de datos]] · [[Salida estructurada]] · [[Constrained decoding]]

---

**Leer el desarrollo:** [[1.12 — Las cuatro estrategias]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
