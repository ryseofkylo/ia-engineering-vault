---
tags:
  - indice
  - glosario
---

# Glosario

> Los 51 términos del Capítulo 1, en una línea cada uno.
> Es la hoja de repaso: si podés reconstruir la explicación completa a partir de su línea, entendiste el tema.
> La columna **§** te lleva a la sección del libro donde se desarrolla.

> [!note] Esta página se genera sola
> Sale de la línea `En una línea` de cada ficha del índice analítico. Si querés cambiar una definición, cambiala en la ficha, no acá. El script está en `.obsidian/regenerar-glosario.py`.

---

## Por orden alfabético

| Término | En una línea | § |
|---|---|---|
| [[Alucinación]] | Es cuando el modelo produce contenido plausible pero falso, y no es un defecto separable: es la misma propiedad probabilística que le permite ser creativo, vista desde el otro lado. | [[1.7 — Logits, softmax y azar\|§1.7]] |
| [[Byte Pair Encoding (BPE)]] | BPE es el algoritmo que construye el vocabulario de un tokenizer: busca el par de símbolos consecutivos más frecuente, lo fusiona en un símbolo nuevo, y repite hasta llegar al tamaño de vocabulario deseado. | [[1.2 — Byte Pair Encoding\|§1.2]] |
| [[Closed-book y oracle como baselines]] | *Closed-book* es el modelo contestando sin ningún documento (el piso) y *oracle* es el modelo con únicamente el documento correcto (el techo): sin esas dos referencias, cualquier número de accuracy de tu sistema RAG es ininterpretable. | [[1.5 — Lost in the Middle\|§1.5]] |
| [[Compute capability]] | Es el número de versión que NVIDIA le asigna a la arquitectura de cada GPU, y determina qué operaciones soporta el hardware y si un motor de inferencia puede usarla. | [[1.18 — VRAM, KV cache y offload\|§1.18]] |
| [[Condición de parada]] | Es la regla que decide cuándo el modelo deja de generar: o llegó a un token especial de fin, o alcanzó el máximo de tokens que le permitiste. | [[1.10 — Logprobs, parada y test time compute\|§1.10]] |
| [[Constrained decoding]] | Es forzar el formato interviniendo en el sampling: en cada paso se enmascaran los logits de todos los tokens que romperían la gramática, así que generar algo inválido es literalmente imposible. | [[1.13 — Constrained decoding\|§1.13]] |
| [[Costo por token]] | Las APIs cobran por token de entrada y por token de salida a precios distintos, así que tu factura es una función directa de cómo el tokenizer parte tu texto — y en un modelo local el "costo" no es plata sino VRAM y latencia. | [[1.3 — Tokenizers reales y el costo de cada token\|§1.3]] |
| [[Cuantización]] | Es guardar los pesos del modelo con menos precisión numérica —por ejemplo 4 bits en vez de 16— para que ocupe menos memoria y corra más rápido, a cambio de un error chiquito que casi siempre no se nota. | [[1.15 — Precisión numérica y la idea de cuantizar\|§1.15]] |
| [[Cuantización afín]] | Es el método más común de cuantizar: mapear el rango real de valores float de un tensor al rango de enteros disponible, usando dos parámetros — `scale` (cuánto vale un escalón) y `zero-point` (qué entero representa el cero). | [[1.16 — El mecanismo de la cuantización\|§1.16]] |
| [[Cómo se fuerza un formato]] | Hay cuatro formas de lograr que el modelo devuelva el formato que querés, y se ordenan por la fuerza de la garantía: pedirlo, restringir la sintaxis, pasar un esquema, o hacer que lo inválido sea imposible de generar. | [[1.12 — Las cuatro estrategias\|§1.12]] |
| [[FP8]] | Es un tipo de 8 bits que conserva la estructura de punto flotante (signo, exponente, mantisa) en vez de ser un entero, y retiene más precisión que int8 en algunos escenarios — pero necesita hardware específico. | [[1.16 — El mecanismo de la cuantización\|§1.16]] |
| [[Function calling]] | Es describirle al modelo un conjunto de funciones con sus parámetros, para que en vez de contestar texto devuelva "quiero llamar a esta función con estos argumentos" — y de paso es la forma más práctica de obtener salida estructurada. | [[1.12 — Las cuatro estrategias\|§1.12]] |
| [[Granularidad de la cuantización]] | Es cuántos pesos comparten el mismo par de parámetros `scale` y `zero-point`: uno solo para todo el tensor (simple, impreciso) o uno por canal o por grupo de N pesos (más preciso, un poco más caro). | [[1.16 — El mecanismo de la cuantización\|§1.16]] |
| [[Greedy decoding y temperature 0]] | *Greedy decoding* es elegir siempre el token más probable, sin sortear; `temperature=0` es técnicamente eso mismo — un `argmax` sobre los logits. | [[1.8 — Temperature\|§1.8]] |
| [[Hugging Face Hub y transformers]] | El Hub es el repositorio donde vive la mayoría de los modelos abiertos, y `transformers` es la librería de Python que los carga, los cuantiza y los corre — con más control y más trabajo que Ollama. | [[1.17 — Elegir un modelo\|§1.17]] |
| [[JSON mode]] | Es una opción de la API que garantiza que la salida sea **JSON sintácticamente válido**, pero no garantiza absolutamente nada sobre qué campos tiene ni qué valores traen. | [[1.11 — Del texto libre al dato\|§1.11]] |
| [[KV cache]] | Es la memoria donde el modelo guarda los cálculos intermedios de todos los tokens ya procesados para no repetirlos en cada paso; crece linealmente con la ventana de contexto y es la razón número uno por la que un modelo que "debería entrar" no entra. | [[1.18 — VRAM, KV cache y offload\|§1.18]] |
| [[Logits y softmax]] | En cada paso de generación el modelo produce un *logit* —un número crudo, sin normalizar— por cada token del vocabulario, y softmax convierte ese vector de números en probabilidades que suman 1. | [[1.7 — Logits, softmax y azar\|§1.7]] |
| [[Logprobs]] | Son las probabilidades en escala logarítmica; se usan porque con vocabularios de ~100.000 tokens las probabilidades son tan chicas que se pierden por *underflow*, y porque en escala log las multiplicaciones se vuelven sumas. | [[1.10 — Logprobs, parada y test time compute\|§1.10]] |
| [[Lost in the middle]] | Es el hallazgo de que un modelo usa mucho mejor la información que está al principio o al final de su contexto que la que está en el medio: la curva de accuracy contra posición tiene forma de U. | [[1.5 — Lost in the Middle\|§1.5]] |
| [[Modelo grande cuantizado vs modelo chico completo]] | Con un presupuesto fijo de VRAM podés elegir un modelo grande muy cuantizado o uno chico en alta precisión; la respuesta habitual es el grande cuantizado, pero es una regla con excepciones y tu tarea puede ser una de ellas. | [[1.17 — Elegir un modelo\|§1.17]] |
| [[Modelos locales vs API]] | Correr el modelo en tu propia máquina en vez de llamar a una API de un tercero: cambiás comodidad y calidad máxima por privacidad del dato, costo fijo y control total sobre la generación. | [[1.14 — Local o API\|§1.14]] |
| [[Más contexto no es mejor]] | Meterle más documentos al modelo tiene rendimientos decrecientes que llegan rápido: el rendimiento del lector se satura mucho antes que el recall del retriever, así que a partir de cierto punto sólo estás pagando latencia y tokens. | [[1.6 — Por qué pasa y qué hacer al respecto\|§1.6]] |
| [[No determinismo del LLM]] | El mismo prompt puede producir respuestas distintas, porque el modelo genera una distribución de probabilidad y alguien sortea de ella — y aun eliminando el sorteo quedan otras fuentes de variación. | [[1.7 — Logits, softmax y azar\|§1.7]] |
| [[Offload a CPU]] | Cuando el modelo no entra entero en la VRAM, el motor de inferencia deja algunas capas en la RAM del sistema y las procesa la CPU: funciona, pero puede ser entre 5 y 10 veces más lento. | [[1.18 — VRAM, KV cache y offload\|§1.18]] |
| [[Ollama]] | Es la forma más simple de correr modelos abiertos en tu máquina: descarga, cuantización y servidor con API compatible con OpenAI, todo resuelto por vos. | [[1.19 — Ollama en la práctica\|§1.19]] |
| [[Patologías de la tokenización]] | La mayoría de los comportamientos raros de un LLM —no sabe deletrear, se equivoca en aritmética simple, se rompe con la indentación de Python— tienen una sola causa común: cómo el tokenizer partió el texto. | [[1.3 — Tokenizers reales y el costo de cada token\|§1.3]] |
| [[Perplexity]] | Es una medida de la incertidumbre de un modelo de lenguaje al predecir la palabra siguiente: más baja es mejor, y se usa como termómetro barato del daño que causó una cuantización. | [[1.15 — Precisión numérica y la idea de cuantizar\|§1.15]] |
| [[Pesos abiertos vs open source]] | *Open weights* significa que podés descargar y correr los pesos del modelo; *open source* significaría además tener el código y los datos de entrenamiento — y casi ningún modelo "abierto" famoso cumple lo segundo. | [[1.14 — Local o API\|§1.14]] |
| [[Pre-tokenización por regex]] | Antes de aplicar BPE, el texto se parte con una expresión regular en categorías (letras, números, puntuación, espacios) para prohibir fusiones que desperdiciarían vocabulario. | [[1.2 — Byte Pair Encoding\|§1.2]] |
| [[Precisión numérica]] | Es cuántos bits usás para guardar cada número del modelo; determina directamente cuánta memoria ocupa y cuánta precisión conservás. | [[1.15 — Precisión numérica y la idea de cuantizar\|§1.15]] |
| [[Primacy y recency bias]] | El modelo presta más atención al principio de su contexto (*primacy*) y al final (*recency*) que al medio; esos dos sesgos juntos son los que dibujan la curva en U. | [[1.5 — Lost in the Middle\|§1.5]] |
| [[PTQ y QAT]] | PTQ cuantiza el modelo **después** de entrenarlo (barato, es lo que vas a usar); QAT simula la cuantización **durante** el entrenamiento para que el modelo se adapte (mejor calidad, requiere reentrenar). | [[1.16 — El mecanismo de la cuantización\|§1.16]] |
| [[Pydantic como contrato de datos]] | Pydantic es una librería de Python que valida que un dato tenga la forma esperada; con un LLM cumple tres funciones a la vez: define el esquema que le pedís, valida lo que vuelve, y te da tipado real en el código. | [[1.12 — Las cuatro estrategias\|§1.12]] |
| [[Query-aware contextualization]] | Es poner la pregunta **antes y después** de los datos en vez de sólo después, para que un modelo decoder-only pueda tenerla en cuenta mientras procesa cada documento. | [[1.6 — Por qué pasa y qué hacer al respecto\|§1.6]] |
| [[Regex como máquina de estados finitos]] | Toda expresión regular equivale a una máquina de estados finitos, y eso es lo que permite saber, en cada paso de generación, exactamente qué tokens están permitidos y cuáles hay que prohibir. | [[1.13 — Constrained decoding\|§1.13]] |
| [[Reintentos con validación]] | Es el patrón de validar la respuesta y, si falla, volver a pedirla incluyendo el mensaje de error para que el modelo se corrija; es una red de seguridad efectiva y con un costo que hay que contar. | [[1.12 — Las cuatro estrategias\|§1.12]] |
| [[Reranking y truncado de la lista recuperada]] | Son las dos palancas para mitigar la degradación posicional: reordenar los documentos recuperados para empujar lo relevante hacia el principio, y recortar la lista cuando los últimos documentos no aportan. | [[1.6 — Por qué pasa y qué hacer al respecto\|§1.6]] |
| [[Salida estructurada]] | Es hacer que el modelo devuelva un dato con forma conocida —un objeto con campos definidos— en vez de texto libre, para que tu programa pueda consumirlo sin adivinar. | [[1.11 — Del texto libre al dato\|§1.11]] |
| [[Temperature]] | Temperature es un número por el que se **dividen los logits antes del softmax**: valores bajos agrandan la ventaja del token más probable (salida consistente y aburrida), valores altos la achican (salida creativa y riesgosa). | [[1.8 — Temperature\|§1.8]] |
| [[Test time compute]] | Es generar varias salidas para el mismo pedido y quedarse con la mejor, gastando más cómputo en el momento de la inferencia en vez de en el entrenamiento. | [[1.10 — Logprobs, parada y test time compute\|§1.10]] |
| [[tiktoken y SentencePiece]] | Son las dos familias de tokenizer que vas a encontrar: `tiktoken` (OpenAI) trabaja siempre sobre bytes UTF-8, y SentencePiece (Llama y buena parte del mundo abierto) trabaja primero sobre caracteres Unicode y cae a bytes sólo para los raros. | [[1.3 — Tokenizers reales y el costo de cada token\|§1.3]] |
| [[Token]] | Un token es la unidad mínima que el modelo procesa: un número entero que representa un pedacito de texto, que puede ser una palabra, un fragmento de palabra, un signo o un espacio. | [[1.1 — El modelo no lee texto, lee números\|§1.1]] |
| [[Tokens especiales]] | Son tokens que no salen del algoritmo BPE sino que se agregan a mano al vocabulario para marcar estructura: dónde empieza un documento, dónde termina un turno de conversación, dónde va un hueco a completar. | [[1.2 — Byte Pair Encoding\|§1.2]] |
| [[Top-k]] | Top-k se queda con los *k* tokens de logit más alto, descarta todo el resto, y sortea sólo entre esos: un corte de cantidad **fija**. | [[1.9 — Top-k y top-p\|§1.9]] |
| [[Top-p (nucleus sampling)]] | Top-p ordena los tokens por probabilidad, los va sumando hasta llegar al umbral *p*, y sortea sólo entre esos: un corte por **masa de probabilidad acumulada**, que se adapta solo a cada contexto. | [[1.9 — Top-k y top-p\|§1.9]] |
| [[UTF-8 y por qué el modelo no ve letras]] | El texto se convierte primero a bytes UTF-8 —256 valores posibles— y ese es el alfabeto inicial del tokenizer, porque garantiza que cualquier texto del mundo se pueda representar sin que nada quede "fuera del diccionario". | [[1.1 — El modelo no lee texto, lee números\|§1.1]] |
| [[Ventana de contexto]] | Es la cantidad máxima de tokens —entrada más salida— que el modelo puede tener en cuenta en una sola llamada; es un límite duro, contado en tokens y no en palabras. | [[1.4 — La ventana de contexto\|§1.4]] |
| [[Vocabulario y vocab size]] | El vocabulario es la lista completa de tokens que el modelo conoce, y su tamaño es una decisión de diseño con costos en las dos direcciones: chico da secuencias largas, grande da una capa de salida enorme. | [[1.2 — Byte Pair Encoding\|§1.2]] |
| [[VRAM]] | Es la memoria de tu placa de video, y es el límite duro que decide qué modelos podés correr: si el modelo más su contexto no entran, o no arranca o se parte con la CPU y se vuelve lentísimo. | [[1.18 — VRAM, KV cache y offload\|§1.18]] |
| [[Weight packing]] | Como el hardware no maneja datos de 4 bits en memoria, se empaquetan **dos valores int4 en un solo byte** — y la ganancia principal de int4 no es de cómputo sino de ancho de banda de memoria. | [[1.16 — El mecanismo de la cuantización\|§1.16]] |

---

## Por orden de aparición en el libro

### Parte I · Cómo el modelo recibe el texto

- **[[Token]]** *(§1.1)* — Un token es la unidad mínima que el modelo procesa: un número entero que representa un pedacito de texto, que puede ser una palabra, un fragmento de palabra, un signo o un espacio.
- **[[UTF-8 y por qué el modelo no ve letras]]** *(§1.1)* — El texto se convierte primero a bytes UTF-8 —256 valores posibles— y ese es el alfabeto inicial del tokenizer, porque garantiza que cualquier texto del mundo se pueda representar sin que nada quede "fuera del diccionario".
- **[[Byte Pair Encoding (BPE)]]** *(§1.2)* — BPE es el algoritmo que construye el vocabulario de un tokenizer: busca el par de símbolos consecutivos más frecuente, lo fusiona en un símbolo nuevo, y repite hasta llegar al tamaño de vocabulario deseado.
- **[[Pre-tokenización por regex]]** *(§1.2)* — Antes de aplicar BPE, el texto se parte con una expresión regular en categorías (letras, números, puntuación, espacios) para prohibir fusiones que desperdiciarían vocabulario.
- **[[Tokens especiales]]** *(§1.2)* — Son tokens que no salen del algoritmo BPE sino que se agregan a mano al vocabulario para marcar estructura: dónde empieza un documento, dónde termina un turno de conversación, dónde va un hueco a completar.
- **[[Vocabulario y vocab size]]** *(§1.2)* — El vocabulario es la lista completa de tokens que el modelo conoce, y su tamaño es una decisión de diseño con costos en las dos direcciones: chico da secuencias largas, grande da una capa de salida enorme.
- **[[Costo por token]]** *(§1.3)* — Las APIs cobran por token de entrada y por token de salida a precios distintos, así que tu factura es una función directa de cómo el tokenizer parte tu texto — y en un modelo local el "costo" no es plata sino VRAM y latencia.
- **[[Patologías de la tokenización]]** *(§1.3)* — La mayoría de los comportamientos raros de un LLM —no sabe deletrear, se equivoca en aritmética simple, se rompe con la indentación de Python— tienen una sola causa común: cómo el tokenizer partió el texto.
- **[[tiktoken y SentencePiece]]** *(§1.3)* — Son las dos familias de tokenizer que vas a encontrar: `tiktoken` (OpenAI) trabaja siempre sobre bytes UTF-8, y SentencePiece (Llama y buena parte del mundo abierto) trabaja primero sobre caracteres Unicode y cae a bytes sólo para los raros.
- **[[Ventana de contexto]]** *(§1.4)* — Es la cantidad máxima de tokens —entrada más salida— que el modelo puede tener en cuenta en una sola llamada; es un límite duro, contado en tokens y no en palabras.

### Parte II · Qué hace el modelo con un contexto largo

- **[[Closed-book y oracle como baselines]]** *(§1.5)* — *Closed-book* es el modelo contestando sin ningún documento (el piso) y *oracle* es el modelo con únicamente el documento correcto (el techo): sin esas dos referencias, cualquier número de accuracy de tu sistema RAG es ininterpretable.
- **[[Lost in the middle]]** *(§1.5)* — Es el hallazgo de que un modelo usa mucho mejor la información que está al principio o al final de su contexto que la que está en el medio: la curva de accuracy contra posición tiene forma de U.
- **[[Primacy y recency bias]]** *(§1.5)* — El modelo presta más atención al principio de su contexto (*primacy*) y al final (*recency*) que al medio; esos dos sesgos juntos son los que dibujan la curva en U.
- **[[Más contexto no es mejor]]** *(§1.6)* — Meterle más documentos al modelo tiene rendimientos decrecientes que llegan rápido: el rendimiento del lector se satura mucho antes que el recall del retriever, así que a partir de cierto punto sólo estás pagando latencia y tokens.
- **[[Query-aware contextualization]]** *(§1.6)* — Es poner la pregunta **antes y después** de los datos en vez de sólo después, para que un modelo decoder-only pueda tenerla en cuenta mientras procesa cada documento.
- **[[Reranking y truncado de la lista recuperada]]** *(§1.6)* — Son las dos palancas para mitigar la degradación posicional: reordenar los documentos recuperados para empujar lo relevante hacia el principio, y recortar la lista cuando los últimos documentos no aportan.

### Parte III · Cómo el modelo elige cada palabra

- **[[Alucinación]]** *(§1.7)* — Es cuando el modelo produce contenido plausible pero falso, y no es un defecto separable: es la misma propiedad probabilística que le permite ser creativo, vista desde el otro lado.
- **[[Logits y softmax]]** *(§1.7)* — En cada paso de generación el modelo produce un *logit* —un número crudo, sin normalizar— por cada token del vocabulario, y softmax convierte ese vector de números en probabilidades que suman 1.
- **[[No determinismo del LLM]]** *(§1.7)* — El mismo prompt puede producir respuestas distintas, porque el modelo genera una distribución de probabilidad y alguien sortea de ella — y aun eliminando el sorteo quedan otras fuentes de variación.
- **[[Greedy decoding y temperature 0]]** *(§1.8)* — *Greedy decoding* es elegir siempre el token más probable, sin sortear; `temperature=0` es técnicamente eso mismo — un `argmax` sobre los logits.
- **[[Temperature]]** *(§1.8)* — Temperature es un número por el que se **dividen los logits antes del softmax**: valores bajos agrandan la ventaja del token más probable (salida consistente y aburrida), valores altos la achican (salida creativa y riesgosa).
- **[[Top-k]]** *(§1.9)* — Top-k se queda con los *k* tokens de logit más alto, descarta todo el resto, y sortea sólo entre esos: un corte de cantidad **fija**.
- **[[Top-p (nucleus sampling)]]** *(§1.9)* — Top-p ordena los tokens por probabilidad, los va sumando hasta llegar al umbral *p*, y sortea sólo entre esos: un corte por **masa de probabilidad acumulada**, que se adapta solo a cada contexto.
- **[[Condición de parada]]** *(§1.10)* — Es la regla que decide cuándo el modelo deja de generar: o llegó a un token especial de fin, o alcanzó el máximo de tokens que le permitiste.
- **[[Logprobs]]** *(§1.10)* — Son las probabilidades en escala logarítmica; se usan porque con vocabularios de ~100.000 tokens las probabilidades son tan chicas que se pierden por *underflow*, y porque en escala log las multiplicaciones se vuelven sumas.
- **[[Test time compute]]** *(§1.10)* — Es generar varias salidas para el mismo pedido y quedarse con la mejor, gastando más cómputo en el momento de la inferencia en vez de en el entrenamiento.

### Parte IV · Cómo se fuerza la forma de la salida

- **[[JSON mode]]** *(§1.11)* — Es una opción de la API que garantiza que la salida sea **JSON sintácticamente válido**, pero no garantiza absolutamente nada sobre qué campos tiene ni qué valores traen.
- **[[Salida estructurada]]** *(§1.11)* — Es hacer que el modelo devuelva un dato con forma conocida —un objeto con campos definidos— en vez de texto libre, para que tu programa pueda consumirlo sin adivinar.
- **[[Cómo se fuerza un formato]]** *(§1.12)* — Hay cuatro formas de lograr que el modelo devuelva el formato que querés, y se ordenan por la fuerza de la garantía: pedirlo, restringir la sintaxis, pasar un esquema, o hacer que lo inválido sea imposible de generar.
- **[[Function calling]]** *(§1.12)* — Es describirle al modelo un conjunto de funciones con sus parámetros, para que en vez de contestar texto devuelva "quiero llamar a esta función con estos argumentos" — y de paso es la forma más práctica de obtener salida estructurada.
- **[[Pydantic como contrato de datos]]** *(§1.12)* — Pydantic es una librería de Python que valida que un dato tenga la forma esperada; con un LLM cumple tres funciones a la vez: define el esquema que le pedís, valida lo que vuelve, y te da tipado real en el código.
- **[[Reintentos con validación]]** *(§1.12)* — Es el patrón de validar la respuesta y, si falla, volver a pedirla incluyendo el mensaje de error para que el modelo se corrija; es una red de seguridad efectiva y con un costo que hay que contar.
- **[[Constrained decoding]]** *(§1.13)* — Es forzar el formato interviniendo en el sampling: en cada paso se enmascaran los logits de todos los tokens que romperían la gramática, así que generar algo inválido es literalmente imposible.
- **[[Regex como máquina de estados finitos]]** *(§1.13)* — Toda expresión regular equivale a una máquina de estados finitos, y eso es lo que permite saber, en cada paso de generación, exactamente qué tokens están permitidos y cuáles hay que prohibir.

### Parte V · Dónde corre el modelo

- **[[Modelos locales vs API]]** *(§1.14)* — Correr el modelo en tu propia máquina en vez de llamar a una API de un tercero: cambiás comodidad y calidad máxima por privacidad del dato, costo fijo y control total sobre la generación.
- **[[Pesos abiertos vs open source]]** *(§1.14)* — *Open weights* significa que podés descargar y correr los pesos del modelo; *open source* significaría además tener el código y los datos de entrenamiento — y casi ningún modelo "abierto" famoso cumple lo segundo.
- **[[Cuantización]]** *(§1.15)* — Es guardar los pesos del modelo con menos precisión numérica —por ejemplo 4 bits en vez de 16— para que ocupe menos memoria y corra más rápido, a cambio de un error chiquito que casi siempre no se nota.
- **[[Perplexity]]** *(§1.15)* — Es una medida de la incertidumbre de un modelo de lenguaje al predecir la palabra siguiente: más baja es mejor, y se usa como termómetro barato del daño que causó una cuantización.
- **[[Precisión numérica]]** *(§1.15)* — Es cuántos bits usás para guardar cada número del modelo; determina directamente cuánta memoria ocupa y cuánta precisión conservás.
- **[[Cuantización afín]]** *(§1.16)* — Es el método más común de cuantizar: mapear el rango real de valores float de un tensor al rango de enteros disponible, usando dos parámetros — `scale` (cuánto vale un escalón) y `zero-point` (qué entero representa el cero).
- **[[FP8]]** *(§1.16)* — Es un tipo de 8 bits que conserva la estructura de punto flotante (signo, exponente, mantisa) en vez de ser un entero, y retiene más precisión que int8 en algunos escenarios — pero necesita hardware específico.
- **[[Granularidad de la cuantización]]** *(§1.16)* — Es cuántos pesos comparten el mismo par de parámetros `scale` y `zero-point`: uno solo para todo el tensor (simple, impreciso) o uno por canal o por grupo de N pesos (más preciso, un poco más caro).
- **[[PTQ y QAT]]** *(§1.16)* — PTQ cuantiza el modelo **después** de entrenarlo (barato, es lo que vas a usar); QAT simula la cuantización **durante** el entrenamiento para que el modelo se adapte (mejor calidad, requiere reentrenar).
- **[[Weight packing]]** *(§1.16)* — Como el hardware no maneja datos de 4 bits en memoria, se empaquetan **dos valores int4 en un solo byte** — y la ganancia principal de int4 no es de cómputo sino de ancho de banda de memoria.
- **[[Hugging Face Hub y transformers]]** *(§1.17)* — El Hub es el repositorio donde vive la mayoría de los modelos abiertos, y `transformers` es la librería de Python que los carga, los cuantiza y los corre — con más control y más trabajo que Ollama.
- **[[Modelo grande cuantizado vs modelo chico completo]]** *(§1.17)* — Con un presupuesto fijo de VRAM podés elegir un modelo grande muy cuantizado o uno chico en alta precisión; la respuesta habitual es el grande cuantizado, pero es una regla con excepciones y tu tarea puede ser una de ellas.
- **[[Compute capability]]** *(§1.18)* — Es el número de versión que NVIDIA le asigna a la arquitectura de cada GPU, y determina qué operaciones soporta el hardware y si un motor de inferencia puede usarla.
- **[[KV cache]]** *(§1.18)* — Es la memoria donde el modelo guarda los cálculos intermedios de todos los tokens ya procesados para no repetirlos en cada paso; crece linealmente con la ventana de contexto y es la razón número uno por la que un modelo que "debería entrar" no entra.
- **[[Offload a CPU]]** *(§1.18)* — Cuando el modelo no entra entero en la VRAM, el motor de inferencia deja algunas capas en la RAM del sistema y las procesa la CPU: funciona, pero puede ser entre 5 y 10 veces más lento.
- **[[VRAM]]** *(§1.18)* — Es la memoria de tu placa de video, y es el límite duro que decide qué modelos podés correr: si el modelo más su contexto no entran, o no arranca o se parte con la CPU y se vuelve lentísimo.
- **[[Ollama]]** *(§1.19)* — Es la forma más simple de correr modelos abiertos en tu máquina: descarga, cuantización y servidor con API compatible con OpenAI, todo resuelto por vos.

---

**51 términos.** Volver a [[1.0 — Presentación del capítulo]] · [[00 — Cómo leer este libro]]
