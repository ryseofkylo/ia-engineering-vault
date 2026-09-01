---
tags:
  - ficha
  - capitulo-1
seccion: "1.11"
---

# Salida estructurada

> **En una línea.** Es hacer que el modelo devuelva un dato con forma conocida —un objeto con campos definidos— en vez de texto libre, para que tu programa pueda consumirlo sin adivinar.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.11 — Del texto libre al dato|§1.11]]**
> y también se lo trata en [[1.12 — Las cuatro estrategias|§1.12]].

---

## La idea, en corto

Un LLM devuelve texto. Tu programa necesita datos. Entre esas dos cosas hay un abismo, y la salida estructurada es el puente.

1. **Tareas cuya salida tiene una gramática obligatoria.** Text-to-SQL, text-to-regex, clasificación. La salida tiene que ser sintácticamente válida o no sirve para nada.
2. **Salidas que otra parte de la aplicación tiene que parsear.** Querés la descripción, no `"Acá tenés la descripción:"` ni `"Como modelo de lenguaje, no puedo..."`.

## Conectado con

[[Cómo se fuerza un formato]] · [[JSON mode]] · [[Function calling]] · [[Constrained decoding]] · [[Pydantic como contrato de datos]] · [[Reintentos con validación]]

---

**Leer el desarrollo:** [[1.11 — Del texto libre al dato]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
