---
tags:
  - ficha
  - capitulo-1
seccion: "1.1"
---

# UTF-8 y por qué el modelo no ve letras

> **En una línea.** El texto se convierte primero a bytes UTF-8 —256 valores posibles— y ese es el alfabeto inicial del tokenizer, porque garantiza que cualquier texto del mundo se pueda representar sin que nada quede "fuera del diccionario".

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.1 — El modelo no lee texto, lee números|§1.1]]**

---

## La idea, en corto

1. **Caracteres Unicode.** Cada carácter del mundo tiene un número (*code point*). La `á` es U+00E1. Hay más de 150.000 asignados.
2. **Bytes UTF-8.** La codificación que convierte esos code points en bytes. Es de largo variable: **de 1 a 4 bytes** por carácter. Los caracteres ASCII ocupan 1 byte; la `á` ocupa 2; un emoji puede ocupar 4.
3. **Tokens.** Lo que produce BPE fusionando bytes.

¿Por qué arrancar en bytes y no en caracteres? Por una razón de garantía: **hay exactamente 256 valores de byte posibles**, así que si el vocabulario inicial son esos 256, ningún texto puede contener algo irrepresentable. Nunca vas a tener un carácter "desconocido". Si arrancaras desde caracteres Unicode, tu vocabulario base tendría que ser gigante o dejar cosas afuera.

## Conectado con

[[Token]] · [[Byte Pair Encoding (BPE)]] · [[Vocabulario y vocab size]] · [[Patologías de la tokenización]] · [[tiktoken y SentencePiece]]

---

**Leer el desarrollo:** [[1.1 — El modelo no lee texto, lee números]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
