---
name: educational-video-chain
description: Desarrolla vídeos educativos narrativos verticales (Shorts, Reels, TikTok; máximo 70 s; para todas las edades) que explican cómo se construye, evoluciona o funciona un objeto, máquina, estructura o sistema mediante una cadena de problemas reales y soluciones progresivas (desde la versión más básica hasta el sistema funcional). Cubre ideación, investigación factual, mapa narrativo, guion en español, storyboard técnicamente preciso (escenas 3D, ilustraciones, elementos explicativos, movimientos de cámara y detalles), preparación de producción con IA (por ejemplo Higgsfield MCP) con presupuesto en créditos, y montaje dinámico sin silencios con efectos de sonido. Úsala siempre que el usuario quiera un vídeo, reel, short, guion o storyboard divulgativo del tipo "cómo funciona X", "cómo se construye X", "por qué X es así", "de un agujero a un búnker", aunque no mencione la palabra "skill" ni "cadena", y también cuando pida preparar o presupuestar la producción de ese tipo de vídeo con herramientas de IA.
---

# educational-video-chain

Convierte un tema técnico en una **historia de construcción y resolución de problemas**. El espectador acompaña una idea sencilla desde su versión más ingenua hasta un sistema que funciona, y aprende porque necesita entender qué falló, cómo se resolvió y qué hizo falta después.

Lo que esta skill NO produce: una clase, un tutorial paso a paso, ni una lista de componentes ("el submarino tiene tanques, hélice, periscopio…"). Si el resultado se puede reordenar sin perder sentido, es una lista, no una cadena.

Prioridades, en este orden: **narrativa → rigor factual → claridad visual → producción**. La IA generativa es una herramienta de producción, nunca el centro de la historia.

---

## El motor narrativo

Cada etapa avanza el sistema un paso y abre el siguiente:

```
estado actual → acción o condición → problema real → por qué importa
→ solución tangible → nueva capacidad → siguiente reto
```

El siguiente reto puede llegar por dos vías, y un buen vídeo **combina ambas**:

- **Patrón A — Cadena de consecuencias.** La solución anterior revela una vulnerabilidad nueva. (Cubres el agujero con hormigón → ya no hay ventilación → añades un conducto → entra agua por el conducto…)
- **Patrón B — Evolución por condiciones de uso.** El problema no lo causa la solución anterior, sino algo que cambia: hora del día, clima, paso del tiempo, nueva forma de uso, mantenimiento o desgaste, comportamiento de personas o animales, un límite físico no considerado. (El gallinero funciona… hasta que llega la noche, luego el invierno, luego un depredador.)

Solo existe causalidad donde realmente la hay. Forzar un "y por eso…" que no es cierto es un error factual, no un recurso narrativo. Cuando el problema viene de una condición nueva, dilo así: "Todo bien… hasta que se hace de noche."

### Arco general (orientativo, no plantilla)

1. Premisa sencilla que cualquiera imagina.
2. Primera versión, la más básica posible.
3. Problema real: algo falla, falta o no basta.
4. Consecuencia: por qué importa.
5. Solución tangible: se construye, añade, modifica o reemplaza algo visible.
6. Nueva capacidad.
7. Nueva dificultad (consecuencia o nueva condición).
8. Repetir hasta completar el sistema.
9. Resultado: el sistema cumple el objetivo definido al principio.
10. Recompensa final: dato curioso, consecuencia inesperada o detalle humano.

El número de etapas depende del tema y de la duración (ver tabla de duración más abajo).

---

## Flujo de trabajo

Trabaja por fases y no saltes la validación. Indica al usuario en qué fase estás cuando entregues algo.

### Fase 1 — Comprender el encargo

Extrae del mensaje: tema, objetivo del vídeo, audiencia, plataforma, duración, tono, restricciones y **alcance** (ideación · preproducción · producción).

Si falta un dato imprescindible, pregunta **solo por ese dato**. Para lo demás usa valores por defecto razonables y decláralos:

| Dato | Por defecto |
|---|---|
| Audiencia | Personas de **todas las edades** (niños, adultos y mayores), sin formación técnica |
| Plataforma | **Vertical 9:16** para Shorts, Reels y TikTok (1080 × 1920) |
| Duración | 60–70 s, **máximo 70 s** |
| Tono | Cercano, en segunda persona (tú), claro y sereno. **Sin humor** |
| Alcance | Preproducción (mapa + guion + storyboard), sin generar nada |
| Lenguaje visual | Mezcla de escenas 3D (mecanismo central), ilustraciones y planos realistas; elementos explicativos; movimientos de cámara con motivo; un plano detalle por etapa |
| Montaje (si se produce) | Dinámico: un plano cada 2–4 s, transiciones, rótulos, flechas y subtítulos animados, efectos de sonido, **sin silencios** (ningún hueco de 0,3 s o más) |
| Modelos Higgsfield (si se produce) | Imágenes: **Nano Banana 2** (`nano_banana_2`, 9:16, 2k) · Vídeo: **Wan 2.7** (`wan2_7`, 9:16, `start_image`) · Voz: **Eleven v4** (`elevenlabs_v4`) con la voz **Dylan** · 3D: **3D Jutsu** alojado · Montaje: `sandbox_exec`. Parámetros y ejemplos en [references/higgsfield-execution.md](references/higgsfield-execution.md) §0 |

Estos valores son el estándar de la skill, no solo sugerencias: formato vertical, máximo 70 s, lenguaje para todas las edades y tono sin humor. Cámbialos únicamente si el usuario lo pide de forma explícita en ese encargo.

**Si el tema no cabe en 70 s**, no aceleres la locución ni comprimas explicaciones: elige un objetivo más pequeño (p. ej. «cómo baja y sube un submarino» en lugar de «cómo funciona un submarino») o propón una serie de varios vídeos, cada uno con su propia cadena completa.

El alcance importa porque determina dónde te detienes: *ideación* termina en el mapa validado; *preproducción* en el storyboard y el presupuesto; *producción* requiere autorización explícita de gasto (Fase 8).

### Fase 2 — Definir la premisa

Responde tres preguntas antes de investigar a fondo:

- ¿Qué intentamos construir o conseguir? (objetivo en una frase, con verbo)
- ¿Cuál es la versión más básica e ingenua? (algo que el espectador pueda imaginar en un segundo: "un agujero cubierto con tablas", "soltar gallinas en el patio", "una caja de acero cerrada")
- ¿Qué significa que finalmente funcione? (criterio de éxito observable; es el final del vídeo)

Una buena premisa es visual, concreta y ligeramente ingenua: invita a pensar "eso no puede ser tan fácil".

### Fase 3 — Investigar

Lee **[references/research-guidelines.md](references/research-guidelines.md)** antes de empezar. Resumen operativo:

- Entiende el funcionamiento real antes de buscar problemas.
- Busca problemas **documentados** de construcción, operación y mantenimiento (manuales, normativa, accidentes investigados, fuentes técnicas e institucionales).
- Verifica cada mecanismo, material, cifra y ubicación de componente que vaya a aparecer en pantalla.
- Separa hechos documentados de simplificaciones didácticas, y marca las simplificaciones.
- Nunca inventes averías, peligros ni cifras para crear drama.

Si el tema no da para suficientes problemas reales, **no rellenes**: propón otro enfoque (otro punto de partida, otra escala, otro ángulo histórico) y explica por qué.

### Fase 4 — Construir el mapa narrativo

Antes de escribir una sola frase de guion, construye el mapa. Una fila por etapa:

| # | Estado actual | Acción o condición | Problema | Consecuencia | Solución | Nueva capacidad | Siguiente reto (y por qué) | Aprendizaje | Prueba visual | Tipo (A/B) | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|---|

- **Tipo**: A si el reto nace de la solución anterior; B si nace de una condición nueva. Indicar el tipo te obliga a no fingir causalidad.
- **Prueba visual**: la imagen concreta que demuestra lo ocurrido (no "plano del submarino", sino "corte longitudinal: el agua entra por las aberturas inferiores del tanque mientras el aire sale por la válvula superior").
- **Fuente**: referencia corta a lo que respalda el problema y la solución.

Acompaña el mapa con una **justificación del orden**: por qué cada etapa va donde va (dependencia causal, momento temporal, o escalado de complejidad).

### Fase 5 — Validar el mapa

Evalúa el mapa con **[references/causal-progression-rubric.md](references/causal-progression-rubric.md)**. Entrega la puntuación y los cambios hechos. Si algún criterio bloqueante falla (problemas inventados, causalidad falsa, solución no tangible, la historia es una lista), corrige el mapa y vuelve a puntuar antes de seguir.

En alcance *ideación*, detente aquí.

### Fase 6 — Escribir el guion

- Español natural y conversacional, como se habla, no como se escribe un informe.
- **Lenguaje para todas las edades**: lo tiene que entender un niño de 10 años y no debe aburrir a un adulto. Ver la sección «Lenguaje sencillo» más abajo.
- **Tono**: cercano y en segunda persona («pones», «te das cuenta»). Sin chistes, ironía, juegos de palabras ni exageraciones cómicas: la curiosidad la crea el problema, no la broma.
- Empieza con una acción o la premisa, nunca con "Hoy vamos a ver…" o una definición.
- Integra la explicación técnica en el momento en que la historia la necesita, y en una frase si es posible.
- Evita enumeraciones y bloques enciclopédicos; si dices tres cosas seguidas sin que pase nada, sobra algo.
- La fórmula "haces X → pasa Y → necesitas Z" es útil, pero varía la entrada: una pregunta, un cambio de hora, un cambio de tiempo, una observación concreta.
- **Gancho en los primeros 2–3 segundos**: la premisa y su primer fallo deben llegar enseguida; en vertical el espectador decide muy pronto si se queda.
- Termina cuando el sistema cumple el objetivo definido en la Fase 2, más la recompensa final. No añadas resumen ni moraleja.

Ajusta la densidad a la duración. Para que lo sigan todas las edades, usa **≈ 2,2–2,3 palabras por segundo** y no superes 2,5 en ninguna escena:

| Duración | Palabras aprox. | Etapas problema→solución |
|---|---|---|
| 30 s | 65–70 | 3 |
| 45 s | 100–105 | 4 |
| 60 s | 135–140 | 5–6 |
| 70 s (máximo) | 155–160 | 6–7 |

Si el mapa tiene más etapas de las que caben, fusiona o elimina las de menor aprendizaje; nunca comprimas una explicación hasta volverla falsa. Comprueba el recuento de palabras al terminar: es fácil pasarse.

#### Lenguaje sencillo

- Frases cortas: idealmente menos de 15 palabras, una idea por frase.
- Palabras de uso diario. Describe lo que pasa en lugar de nombrarlo con el término técnico: «tu aliento se convierte en gotitas» antes que «condensación»; «el agua empuja hacia arriba» antes que «empuje hidrostático».
- Como mucho 1–2 términos técnicos por vídeo, solo si el espectador los va a necesitar, y explicados en la misma frase con una comparación cotidiana.
- Sin siglas, fórmulas, unidades raras ni cifras innecesarias. Si una cifra ayuda, redondéala y compárala con algo conocido.
- Sin referencias que solo entienda un adulto (marcas, historia, cultura de internet) ni contenido que pueda asustar a un niño sin necesidad.
- La simplificación no puede volverse falsa: si una palabra sencilla cambia el significado, busca otra o añade media frase. Anota la simplificación en la tabla de rigor.
- Prueba final: lee el guion en voz alta y marca cada palabra que un niño de 10 años no usaría. Sustitúyela o explícala.

### Fase 7 — Storyboard

Esta fase pesa tanto como el guion. Lee **[references/storyboard-visual-accuracy.md](references/storyboard-visual-accuracy.md)** antes de escribir la primera escena: contiene la ficha de escena obligatoria, la hoja de referencia del sistema (geometría y ubicación fija de componentes) y las reglas de precisión.

Principio rector: **cada escena debe entenderse sin sonido**. En vertical esto es aún más importante, porque mucha gente ve estos vídeos sin audio: los subtítulos son obligatorios y la imagen tiene que bastar.

El formato es **vertical 9:16**: compón cada escena para esa pantalla (ver la sección «Formato vertical» de la referencia). Si una escena solo "acompaña" la narración (un plano bonito genérico), rehazla para que *muestre* el mecanismo, la causa y el efecto.

Antes de la primera escena, crea la **hoja de referencia del sistema** (vistas, componentes, posiciones, colores codificados). Todas las escenas deben respetarla para que la geometría no cambie entre planos.

Lee también **[references/visual-language.md](references/visual-language.md)**. El storyboard debe combinar:

- **Escenas 3D**: el mecanismo central va en 3D construido, con cortes, transparencias o despiece.
- **Ilustraciones** y planos realistas, con al menos 3 tratamientos visuales en el vídeo.
- **Elementos explicativos**: uno principal por plano, que aparece cuando la locución lo nombra.
- **Movimientos de cámara** con motivo, uno por plano, preferiblemente verticales en 9:16.
- **Detalles**: un plano detalle (macro) por etapa, materiales creíbles y micro-movimientos con su efecto de sonido.

La ficha de escena tiene campos para cada uno de estos puntos.

### Fase 8 — Preparación y ejecución de producción

Lee **[references/production-checklist.md](references/production-checklist.md)**. Puntos no negociables:

- **Descubre las herramientas reales de la sesión** (Higgsfield MCP u otras) listando sus funciones y parámetros; no asumas que algo existe porque aparece en la web del proveedor. Si no hay herramientas de generación conectadas, dilo y entrega el plan de producción sin ellas.
- Separa imagen, vídeo, voz, montaje y operaciones adicionales (upscale, lipsync, etc.).
- Presupuesto por escena y total, con **coste base** y **reserva de reintentos** por separado. Indica de dónde sale cada precio (respuesta de la herramienta, documentación de la sesión o estimación marcada como tal).
- **No inicies ninguna generación, render ni acción que consuma créditos sin autorización explícita** del usuario para ese gasto concreto. Pedir una estimación no es autorizar la producción. Si el usuario autoriza, confirma el importe máximo y respétalo.

**Si Higgsfield MCP está conectado**, sigue **[references/higgsfield-execution.md](references/higgsfield-execution.md)** para dar las órdenes: qué herramienta usar en cada paso, fichas de producción por plano, presupuesto con `quote_ref`, generación por lotes (imágenes clave → aprobación → vídeo → voz), montaje con `sandbox_exec` y reglas de seguridad. Cada fase de gasto (imágenes, vídeo, voz, montaje) necesita su propia autorización, salvo que el usuario apruebe varias a la vez con un máximo. Su sección 8 recoge qué modelos funcionaron con el plan gratuito y cuánto costó un short completo.

Antes de producir, comprueba también:

- **El plan del usuario limita los modelos.** El presupuesto no lo detecta: verifica con la primera petición real (un rechazo no cobra) y avisa si cambias de modelo.
- **Modelos y voz:** parte de la configuración recomendada (Nano Banana 2, Wan 2.7, Eleven v4 con la voz Dylan, 3D Jutsu). Antes de la primera producción, pregunta una vez al usuario si quiere usarla o cambiar algún modelo o la voz, y después no vuelvas a preguntar. Cámbiala también si un modelo falla o no está disponible en su plan. Si pide uno que no está en el catálogo, enséñale las alternativas reales con su precio.
- **Montaje:** el estándar es **dinámico y sin silencios**. Sigue **[references/dynamic-editing.md](references/dynamic-editing.md)** y los scripts de [scripts/](scripts/):
  - la línea de tiempo se ajusta a la voz real y ningún hueco llega a 0,3 s;
  - un plano cada 2–4 s, con transiciones;
  - rótulos, flechas y subtítulos animados, con las palabras clave en amarillo;
  - efectos de sonido.

  El vídeo puede quedar por debajo de la duración del guion; no rellenes con pausas.

---

## Formato de entrega

Entrega en el orden de las fases y solo hasta el alcance pedido:

1. **Encargo** (datos y supuestos por defecto).
2. **Premisa** · **Objetivo final** · **Criterio de éxito**.
3. **Mapa narrativo** (tabla) + **justificación del orden**.
4. **Mecanismos a verificar** y estado de verificación (verificado / simplificación declarada / pendiente).
5. **Evaluación con la rúbrica** y correcciones.
6. **Guion** (con tiempos).
7. **Hoja de referencia del sistema** + **storyboard** (fichas de escena).
8. **Plan de producción y presupuesto** (sin ejecutar).
9. **Fuentes**.

Si el usuario pide solo una parte ("solo el guion"), haz igualmente las fases previas de forma interna y entrega un mapa abreviado: el guion depende de que la cadena sea correcta.

---

## Señales de que vas por mal camino

- El mapa se lee como el índice de un manual ("1. Casco. 2. Tanques. 3. Motor.").
- Todos los retos son tipo A (cadena forzada) o todos tipo B (sucesión de catástrofes externas sin evolución del sistema).
- Una solución no se ve: "se mejora el sistema" en lugar de "se añade una válvula en la parte superior del tanque".
- Aparece una cifra sin fuente o un peligro que no encuentras documentado.
- El final llega porque se acabó el tiempo, no porque el sistema cumple el objetivo.
- Una escena del storyboard podría ilustrar cualquier frase del guion.
- El guion necesita más de 70 s, o va a más de 2,5 palabras por segundo.
- Aparecen palabras que un niño de 10 años no entendería sin explicación, o hay chistes y frases irónicas.
- Una escena está compuesta en horizontal y «recortada» a vertical, dejando lo importante fuera de la zona segura.
- El montaje deja silencios de 0,3 s o más, mantiene un mismo plano fijo más de 4 s o no tiene efectos de sonido.
- Un rótulo o una flecha tapa el subtítulo o a las personas.
- Has aprobado un fotograma sin descargarlo y mirarlo, o has prometido un modelo sin comprobar que el plan del usuario lo permite.
- Un movimiento mecánico clave se resuelve con un fundido entre dos imágenes fijas en lugar de una animación (3D o capas).
- Todo el vídeo tiene el mismo tratamiento visual, no hay planos detalle o la cámara se mueve sin motivo.
