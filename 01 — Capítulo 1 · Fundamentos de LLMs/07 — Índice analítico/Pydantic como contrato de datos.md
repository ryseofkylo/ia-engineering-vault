---
tags:
  - ficha
  - capitulo-1
seccion: "1.12"
---

# Pydantic como contrato de datos

> **En una línea.** Pydantic es una librería de Python que valida que un dato tenga la forma esperada; con un LLM cumple tres funciones a la vez: define el esquema que le pedís, valida lo que vuelve, y te da tipado real en el código.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.12 — Las cuatro estrategias|§1.12]]**
> y también se lo trata en [[1.11 — Del texto libre al dato|§1.11]].

---

## La idea, en corto

class RespuestaSQL(BaseModel):
    sql: str = Field(description="La consulta T-SQL, sin markdown ni backticks")
    explicacion: str = Field(description="Qué hace la query, en una oración")
    tablas_usadas: list[str] = Field(description="Nombres de las tablas referenciadas")
```

1. **Genera el esquema.** `RespuestaSQL.model_json_schema()` produce el JSON Schema que le mandás al modelo. Las `description` de cada campo **son parte del prompt**: escribilas con el mismo cuidado que escribirías una instrucción.
2. **Valida la vuelta.** `RespuestaSQL(**datos)` levanta `ValidationError` si falta un campo, si un tipo no coincide, o si falla una regla tuya.
3. **Tipa tu código.** A partir de ahí trabajás con un objeto, no con un diccionario. El IDE te autocompleta y los errores aparecen antes.

## Conectado con

[[Salida estructurada]] · [[Cómo se fuerza un formato]] · [[JSON mode]] · [[Function calling]] · [[Reintentos con validación]] · [[Alucinación]]

---

**Leer el desarrollo:** [[1.12 — Las cuatro estrategias]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
