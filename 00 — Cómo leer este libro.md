---
tags:
  - indice
---

# Cómo leer este libro

Esto es un **manual de AI Engineering** escrito para leerse de corrido, como un libro de facultad. Cada capítulo corresponde a una materia del plan de estudios, y está dividido en partes y secciones numeradas.

Si es la primera vez que lo abrís, leé esta página. Son tres minutos.

---

## La regla principal

> **No hace falta abrir ningún enlace externo. Nunca.**
>
> El contenido está acá adentro, desarrollado. Las fuentes de las que salió cada cosa están listadas en [[91 — Bibliografía]] por trazabilidad —para que sepas de dónde viene cada dato y puedas ir al original si algún día querés profundizar— pero **no son lectura obligatoria ni supuesta**.

Todo lo que necesitás saber está escrito en las secciones.

---

## Cómo se lee

**De corrido, en orden.** Empezás por la presentación del capítulo y seguís §1.1, §1.2, §1.3… Cada sección termina con un pie de navegación:

| | |
|---|---|
| **← Anterior** | **Siguiente →** |

Un clic por sección. No hay que volver al índice cada vez.

**Cada sección es autosuficiente.** Tiene su explicación completa, sus ejemplos, su código, sus errores frecuentes y un resumen numerado al final. Cuando una sección menciona otra —"como vimos en §1.3"— es una referencia, no una interrupción: podés seguir leyendo sin ir.

**Los términos del final son opcionales.** Cada sección cierra con una línea de *términos* que enlaza al índice analítico. Son fichas de consulta rápida, no lectura. **Mientras leés, ignoralos.**

---

## Anatomía de un capítulo

```
Capítulo N · <materia del plan>
│
├── 1.0 — Presentación del capítulo    ← índice, arco y qué vas a saber hacer
│
├── Parte I ·   secciones 1.1 – 1.4    ← el libro: lectura continua
├── Parte II ·  secciones 1.5 – 1.6
├── Parte III · secciones 1.7 – 1.10
├── Parte IV ·  secciones 1.11 – 1.13
├── Parte V ·   secciones 1.14 – 1.19
│
├── Cierre ·    secciones 1.20 – 1.22  ← trabajo práctico, laboratorio, autoevaluación
│
└── Índice analítico                   ← fichas de consulta + la red del grafo
```

**Las partes agrupan secciones por tema.** Dentro de cada capítulo la numeración es continua, así que §1.14 es la sección 14 del capítulo 1, esté en la parte que esté.

---

## Las dos formas de usar esto

| | El libro | La red |
|---|---|---|
| **Dónde está** | Las secciones numeradas | Vista de grafo (`Ctrl+G`) |
| **Para qué** | Aprender algo nuevo | Ubicar algo que ya sabés |
| **Cómo se recorre** | De arriba hacia abajo, con "Siguiente" | Saltando entre términos conectados |
| **Qué contiene** | El desarrollo completo | Fichas cortas que apuntan a su sección |

El **índice analítico** es lo que alimenta el grafo. Cada ficha tiene la definición en una línea, la idea en corto, un enlace a la sección donde se desarrolla, y sus términos relacionados. Sirve para dos cosas: repasar sin releer, y navegar por asociación cuando ya conocés el terreno.

El [[90 — Glosario]] junta las 51 definiciones de una línea en una sola página, alfabéticamente y por orden de aparición.

---

## El método de estudio

1. **Leé la sección entera**, de corrido, sin abrir enlaces.
2. **Leé el resumen numerado del final.** Si algún punto no te resulta obvio, volvé a esa parte de la sección.
3. **Hacé el experimento correspondiente** de [[1.21 — Laboratorio]], si la sección tiene uno.
4. **Pasá a la siguiente.**

Al final del capítulo, [[1.22 — Autoevaluación]] tiene las preguntas que tenés que poder responder.

> **La regla para avanzar.** No avances por aburrimiento ni por ansiedad. Avanzá cuando podés **explicarle el tema a alguien que no sabe nada**. Si al explicarlo tenés que decir "y bueno, es medio mágico", esa parte no la entendiste todavía.

---

## Sobre el orden del panel izquierdo

El orden de las carpetas y las notas **no es alfabético**: está definido por archivos `sortspec.md` que lee el plugin **Custom File Explorer sorting**.

Si algún día ves todo desordenado, el plugin está suspendido: hacé clic en su ícono en la cinta lateral izquierda para reactivarlo. Los `sortspec.md` no son contenido — no los borres.

Como respaldo, el índice completo con enlaces está siempre en la presentación de cada capítulo.

---

## Capítulos

- **[[1.0 — Presentación del capítulo|Capítulo 1 · Fundamentos de LLMs]]** — cómo funciona por adentro el objeto con el que vas a trabajar todo el resto de la carrera. 22 secciones, 2–3 semanas.

Los capítulos siguientes —Prompting y context engineering, Evaluación y error analysis, RAG en profundidad, Diseño de agentes, Producción y observabilidad, Costo/latencia/seguridad— se agregan a medida que avanzás.

---

## Notas de servicio

- [[90 — Glosario]] — los 51 términos del capítulo 1, en una línea cada uno.
- [[91 — Bibliografía]] — de dónde salió cada cosa. Trazabilidad, no tarea.
- [[92 — Nota de edición]] — cómo está construido este libro, qué se verificó y qué quedó afuera.
