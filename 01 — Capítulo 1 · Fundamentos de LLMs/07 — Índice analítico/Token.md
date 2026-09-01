---
tags:
  - ficha
  - capitulo-1
seccion: "1.1"
---

# Token

> **En una línea.** Un token es la unidad mínima que el modelo procesa: un número entero que representa un pedacito de texto, que puede ser una palabra, un fragmento de palabra, un signo o un espacio.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.1 — El modelo no lee texto, lee números|§1.1]]**
> y también se lo trata en [[1.2 — Byte Pair Encoding|§1.2]].

---

## La idea, en corto

El modelo de lenguaje **no ve letras ni palabras**. Ve una lista de números enteros.

Antes de que el texto llegue al modelo, un componente separado —el *tokenizer*— lo corta en pedazos y reemplaza cada pedazo por su número en un diccionario fijo llamado vocabulario. `"Hola mundo"` puede convertirse en `[15496, 2159]`. El modelo trabaja con esos dos números y con nada más. Cuando responde, produce números, y el tokenizer los traduce de vuelta a texto.

## Conectado con

[[Byte Pair Encoding (BPE)]] · [[Vocabulario y vocab size]] · [[UTF-8 y por qué el modelo no ve letras]] · [[Ventana de contexto]] · [[Costo por token]] · [[Patologías de la tokenización]]

---

**Leer el desarrollo:** [[1.1 — El modelo no lee texto, lee números]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
