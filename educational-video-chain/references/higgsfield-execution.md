# Ejecución con Higgsfield MCP

Úsala en la Fase 8 cuando Higgsfield MCP esté conectado y el usuario quiera pasar del storyboard a la producción. Complementa a [production-checklist.md](production-checklist.md): aquella dice **qué** comprobar y cuándo pedir permiso; esta dice **cómo** dar las órdenes a Higgsfield, paso a paso.

Esta guía se escribió a partir de las descripciones de las herramientas de Higgsfield MCP. Las herramientas y los modelos cambian: antes de usarla, carga los esquemas reales de la sesión y, si algo no coincide, manda lo que diga el esquema.

## Índice

0. Configuración recomendada (modelos, voz y parámetros)
1. Principios
2. Mapa de herramientas
3. Flujo de ejecución (fases 0–7)
4. Ficha de producción por escena
5. Reglas de seguridad
6. Revisión de calidad
7. Mensajes de autorización
8. Registro de campo (qué funcionó y cuánto costó)

---

## 1. Principios

- **Nada que cueste créditos sin autorización explícita**, fase por fase. Pedir un presupuesto no es autorizar.
- **Gasta exactamente lo aprobado**: genera siempre a partir de la referencia del presupuesto (`quote_ref`), nunca reescribiendo los parámetros a mano.
- **Lo exacto se compone; lo atmosférico se genera.** Flechas, etiquetas y subtítulos no van en los prompts: se añaden en montaje.
- **Imagen antes que vídeo.** Primero se aprueban los fotogramas clave; después se animan usándolos como referencia. Así la geometría no cambia entre escenas.
- **Vertical siempre**: `aspect_ratio: "9:16"` explícito en cada imagen y vídeo. Algunos modelos usan 16:9 si no se indica.
- **Usa la configuración recomendada (sección 0)** salvo que el usuario prefiera otra. Cámbiala también si Higgsfield rechaza un modelo; en ese caso, busca alternativas con `models_explore` y avisa.

## 0. Configuración recomendada (probada con el plan gratuito de Higgsfield)

Esta configuración se probó en noviembre de 2026 con el plan gratuito de Higgsfield y produjo shorts completos por unos 100–130 créditos. Antes de la primera producción, pregunta una vez al usuario si quiere usarla tal cual o cambiar algún modelo o la voz; después úsala sin volver a preguntar. Comprueba con `models_explore get` que los modelos siguen en el catálogo:

| Uso | Modelo (`model`) | Parámetros que hay que enviar siempre | Coste real |
|---|---|---|---|
| **Imágenes** (hoja de referencia, fotogramas clave, ilustraciones, realista) | **Nano Banana 2** · `nano_banana_2` | `aspect_ratio: "9:16"`, `resolution: "2k"` (sale a 1536 × 2752), `use_unlim: false`. Para mantener la coherencia: `medias: [{"value": "<job_id de la imagen aprobada>", "role": "image_references"}]` | 2 cr por imagen a 2k (1,5 a 1k) |
| **Vídeo** (planos realistas, históricos o atmosféricos a partir de un fotograma) | **Wan 2.7** · `wan2_7` | `aspect_ratio: "9:16"`, `duration` en segundos enteros, `use_unlim: false`, `medias: [{"value": "<job_id del fotograma aprobado>", "role": "start_image"}]`. Prompt con **un solo** movimiento de cámara | 1,5 cr/s. Sale a 716 × 1284 (~720p), así que en montaje se amplía a 1080 × 1920 |
| **Voz** (locución por escena) | **Eleven v4** · `elevenlabs_v4` | `dialogue: [{"text": "<narración>", "voice_type": "preset", "voice_id": "b847bc29-f184-583a-8ad9-d1f1e16d1a60"}]` (voz **Dylan**), más `prompt` con el mismo texto (la herramienta lo exige) y `use_unlim: false`. Una petición por escena | ≈ 0,5–1,2 cr por escena según la longitud (6,75 cr las 8 escenas del ascensor) |
| **Escenas 3D** (mecanismo central) | **3D Jutsu alojado** · herramientas `scene_builder_3d_*` | Ver [visual-language.md](visual-language.md) §6 y `get_preset_instructions` `/3d-jutsu` | 0 cr para construir y renderizar |
| **Montaje** y **efectos de sonido** | `sandbox_exec` con [../scripts/montaje_dinamico.py](../scripts/montaje_dinamico.py) y [../scripts/sfx.sh](../scripts/sfx.sh) | Ver [dynamic-editing.md](dynamic-editing.md) | 0 cr |

Ejemplos de llamada (copiar y adaptar):

```json
// Imagen: generate_image_batch → requests[]
{"index": 31, "params": {"model": "nano_banana_2", "aspect_ratio": "9:16", "resolution": "2k", "use_unlim": false,
  "medias": [{"value": "<job_id hoja de referencia>", "role": "image_references"}],
  "prompt": "Same shaft, camera, style, colors and proportions as the reference image. ... No text, no labels, no arrows."}}

// Editar una imagen fallida (cuesta lo mismo y conserva el encuadre)
{"index": 131, "params": {"model": "nano_banana_2", "aspect_ratio": "9:16", "resolution": "2k", "use_unlim": false,
  "medias": [{"value": "<job_id imagen a corregir>", "role": "image_references"}],
  "prompt": "Edit this exact image, keep everything identical. Only change: ..."}}

// Vídeo: generate_video_batch → requests[]
{"index": 1, "params": {"model": "wan2_7", "aspect_ratio": "9:16", "duration": 6, "use_unlim": false,
  "medias": [{"value": "<job_id fotograma aprobado>", "role": "start_image"}],
  "prompt": "Static camera. <una acción, con dirección y causa>. Nothing else moves, no new objects, no text."}}

// Voz: generate_audio_batch → requests[]
{"index": 1, "params": {"model": "elevenlabs_v4", "use_unlim": false, "prompt": "<narración exacta>",
  "dialogue": [{"text": "<narración exacta>", "voice_type": "preset", "voice_id": "b847bc29-f184-583a-8ad9-d1f1e16d1a60"}]}}
```

Cómo trabajar con esta configuración:

- **Presupuesta igualmente** con `estimate_*_cost` usando estos mismos parámetros, y pide autorización por fase. Tener los modelos decididos no autoriza el gasto.
- **Plan gratuito: un trabajo a la vez.** Envía lotes y vuelve a mandar solo los rechazados con «Rate limit». Los rechazos no cobran.
- **Si `balance` no dice `free`** (el usuario tiene un plan de pago), mantén estos modelos salvo que quiera probar otros. Puedes ofrecerle modelos que el plan gratuito bloquea (por ejemplo, Kling para vídeo), pero solo como propuesta.
- **Si alguno de estos modelos se rechaza o desaparece del catálogo**, no lo sustituyas en silencio: busca con `models_explore`, presupuesta 2–3 alternativas y deja que el usuario elija.
- **Modelos que no sirven con el plan gratuito o para este uso** (comprobado en noviembre de 2026):
  - Rechazados por el plan («Requires basic plan or higher»): Seedream 4.5, GPT Image 2.6, Recraft v4.1 y Kling 3.0.
  - Z-Image funciona, pero su geometría es incoherente: descártalo para cortes técnicos.
  - ElevenLabs v3 no existe en el catálogo.

## 2. Mapa de herramientas

Los nombres llevan un prefijo propio de la sesión (`mcp__<id>__`). Si están diferidas, cárgalas con ToolSearch en una sola llamada.

| Paso | Herramienta | ¿Gasta? | Para qué |
|---|---|---|---|
| Saldo | `balance` | No | Créditos disponibles y plan |
| Modelos | `models_explore` (`recommend`, `get`) | No | Modelos de imagen, vídeo y audio; formatos, duraciones, parámetros, roles de referencia (`medias[].roles`) |
| Voces | `list_voices` | No | Voces disponibles con `voice_id`, `voice_type` y muestra (`preview_url`) |
| Destino | `get_preferences` | No | Saber si hay que crear un proyecto |
| Proyecto | `create_project` | No* | Solo si `auto_create_project` es true o el usuario lo pide |
| Presupuesto | `estimate_image_cost`, `estimate_video_cost`, `estimate_audio_cost` | No | Coste de cada petición; devuelve `quote_ref` |
| Imagen | `generate_image` · `generate_image_batch` (1–12) | **Sí** | Hoja de referencia y fotogramas clave |
| Vídeo | `generate_video` · `generate_video_batch` (1–12) | **Sí** | Animar fotogramas aprobados, planos atmosféricos |
| Voz | `generate_audio` · `generate_audio_batch` (1–12) | **Sí** | Locución por escena |
| Esperar | `jobs_wait` (≤12 trabajos, ≤15 s por llamada) | No | Estado y URL de los resultados por lotes |
| Mostrar | `show_generation_by_ids` (≤60) | No | Enseñar al usuario un lote terminado, una sola vez |
| Montaje | `sandbox_exec` | No (comprobado en noviembre de 2026; vuelve a comprobarlo con `balance`) | Entorno Linux remoto con ffmpeg, ImageMagick, sox, fuentes de subtítulos (Montserrat, Metropolis), faster-whisper |
| Subir resultado | `media_upload` + PUT + `media_confirm` | No* | Guardar en Higgsfield el vídeo montado |
| Mejoras | `upscale_image`, `upscale_video`, `reframe`, `remove_background` | **Sí** | Solo si hacen falta y se presupuestan aparte |
| Escenas 3D | `scene_builder_3d_*` (3D Jutsu) | No para construir y renderizar; **sí** para `generate_angles` y `generate_video` desde un render | Mecanismos exactos con cámara animada. Antes de usarlo, lee `get_preset_instructions` `/3d-jutsu` y pregunta una vez la ruta (alojado gratis / Blender Studio de pago / Blender local). Ver [visual-language.md](visual-language.md) §6 |

\* Sin coste según su descripción, pero crean cosas en la cuenta del usuario: explícalo antes.

`sandbox_exec`: su descripción no dice si consume créditos. Trátalo como gasto posible e inclúyelo en la autorización del montaje. Si el usuario quiere confirmarlo, compara `balance` antes y después de un comando trivial, con su permiso.

## 3. Flujo de ejecución

```
F0 Descubrir (gratis) → F1 Fichas (sin llamadas) → F2 Presupuesto (gratis)
 → [AUTORIZACIÓN A] F3 Imágenes clave → revisión y aprobación del usuario
 → [AUTORIZACIÓN B] F4 Vídeo → revisión
 → [AUTORIZACIÓN C] F5 Voz → revisión
 → [AUTORIZACIÓN D] F6 Montaje → F7 Entrega
```

El usuario puede autorizar varias fases a la vez («A y B, máximo 300 créditos»). Aun así, enseña los fotogramas clave antes de animarlos: rehacer una imagen cuesta mucho menos que rehacer un vídeo.

### F0 — Descubrir (solo lectura)

**Con la configuración por defecto (sección 0)**, F0 se reduce a cuatro pasos:
- `balance`: saldo y plan;
- `get_preferences`;
- comprobar con `models_explore get` que los modelos de la sección 0 siguen en el catálogo, y anotar sus duraciones y parámetros;
- cargar las herramientas.

No hace falta recomendar modelos ni elegir voz, porque ya están decididos. Los pasos 2–7 de abajo se aplican solo si el usuario quiere cambiar algo o si un modelo por defecto falla.

1. `balance` → saldo.
2. `models_explore` con `action: "recommend"` para cada tipo:
   - imagen: «ilustración técnica estilizada, vertical 9:16, corte transversal limpio, coherencia entre planos»;
   - vídeo: «imagen a vídeo, vertical 9:16, movimiento sencillo y controlado, mantener la geometría de la imagen de referencia»;
   - audio: «locución en español, voz cercana y clara, ritmo pausado».
3. `models_explore` con `action: "get"` para cada candidato: anota formatos, **duraciones admitidas**, parámetros y **roles de referencia**.
4. `list_voices` → `list_voices` no indica el idioma de cada voz: las voces preset son multilingües y hablan en el idioma del texto. Propón 2–3 voces y deja que el usuario las escuche (`preview_url`). **Pregunta qué voz y qué modelo de voz quiere antes de generar la locución**: es habitual que la elección cambie tras escuchar las muestras.
5. `get_preferences` → decide el destino (proyecto o ninguno).
6. **Comprueba el plan del usuario.** `balance` devuelve `subscription_plan_type`. Con el plan `free`, muchos modelos rechazan el envío con «Requires basic plan or higher», y `estimate_*_cost` **no lo detecta** (da precio igualmente). Antes de prometer un modelo:
   - Envía la primera petición real de la fase (por ejemplo, la hoja de referencia) y mira si se acepta. Un rechazo no cobra nada.
   - Si se rechaza, busca alternativas con `models_explore` (`list` por tipo) y presupuesta 3–4. Los modelos con `supports_unlim: true` suelen estar abiertos al plan gratuito, aunque no siempre.
   - Puedes probar varios modelos en un mismo lote con la misma petición: el coste es pequeño y además sirve para comparar resultados. Hazlo solo dentro del máximo que haya aprobado el usuario.
   - Explica al usuario qué modelos han funcionado y cuáles no, y no cambies de modelo sin decírselo.
7. **Límite de un trabajo simultáneo** (plan gratuito): los lotes devuelven «Rate limit reached: max 1 concurrent job(s)» en parte de sus elementos. Los rechazados no cobran: guarda los `job_id` aceptados, espera con `jobs_wait` y vuelve a enviar **solo** los rechazados. A veces se aceptan 2–4 por lote, y las imágenes y vídeos aceptados quedan en cola y se procesan de uno en uno.

Resultado: la tabla de herramientas de [production-checklist.md](production-checklist.md), con los datos reales.

### F1 — Fichas de producción

Convierte cada escena del storyboard en una o varias fichas (sección 4). Reglas:

- **Un plano del storyboard = una petición**, salvo los planos que son solo gráficos (flechas, etiquetas), que se hacen en montaje.
- Duración del clip = la duración admitida igual o inmediatamente superior a la del plano. Se recorta en montaje y **se presupuesta con la duración generada**, no con la del plano.
- Planos técnicos (cortes, mecanismos): **escena 3D construida y renderizada** (3D Jutsu) si está disponible: piezas exactas, movimiento real y cámara animada, sin coste de créditos. Si no, imagen fija + animación en montaje. No pidas al vídeo generativo que «explique» un mecanismo.
- Cada ficha indica su tratamiento visual, su movimiento de cámara (uno, con motivo) y su elemento explicativo (ver [visual-language.md](visual-language.md)). En vídeo generado, el movimiento de cámara va en el prompt («slow push-in», «camera rises vertically following…»).
- Planos atmosféricos (lluvia, viento, paisaje): vídeo a partir del fotograma clave.

### F2 — Presupuesto

1. Para cada ficha, llama a `estimate_image_cost` / `estimate_video_cost` / `estimate_audio_cost` con los mismos `params` que usarás al generar (incluidos `aspect_ratio`, `duration` y `medias` si ya existen).
   - En vídeos de imagen a vídeo, la imagen aún no existe: presupuesta sin `medias` y vuelve a presupuestar antes de generar.
2. Guarda el `quote_ref` de cada ficha.
3. Presenta la tabla por escena: coste base y reserva de reintentos por separado, más los totales por fase (A imágenes, B vídeo, C voz, D montaje).
4. Si el total supera el saldo, dilo y propón recortes (menos planos generados, más animación en montaje).

### F3 — Imágenes clave (tras la autorización A)

1. Primero, **una sola imagen**: la hoja de referencia del sistema (vista canónica principal), con `generate_image`. Enséñala y pide aprobación: fija estilo, colores y proporciones.
2. Después, los fotogramas clave con `generate_image_batch` (≤12 por lote), cada uno con `params: {"ref": "<quote_ref>"}` e `index` = número de plano.
   - Si el modelo acepta referencias, pasa la hoja aprobada en `medias` (rol según `models_explore`) para mantener la coherencia.
3. `jobs_wait` en grupos de ≤12 hasta que todos terminen (si `all_terminal` es false, espera `poll_after_seconds`).
4. `show_generation_by_ids` una vez con todo el lote.
5. Revisión de calidad (sección 6). **Descarga y mira cada imagen**: no apruebes por el prompt. Los que fallen se rehacen contra la reserva de reintentos; avisa antes de superarla.
   - **Corrige editando, no regenerando**: pasa la imagen fallida como referencia (`medias`, rol de referencia del modelo) con un prompt «Edita esta imagen exacta, mantén todo igual. Solo cambia: …». Conserva encuadre y estilo y cuesta lo mismo que una imagen.
   - Para un estado nuevo de una escena ya aprobada (por ejemplo, la misma escena con la cuerda gastada), edita a partir del fotograma aprobado, no desde cero. Así se mantiene la acumulación de piezas.
   - Errores típicos vistos en cortes técnicos:
     - la cuerda o el cable sigue por debajo del objeto que cuelga, hasta el suelo;
     - piezas que flotan despegadas del conjunto (por ejemplo, pinzas a media altura del raíl en lugar de bajo la cabina);
     - un «primer plano» que en realidad omite las piezas ya instaladas;
     - el objeto colgado no aparece en la posición pedida (abajo o arriba).
   - Algunos modelos baratos producen geometrías incoherentes (cuerdas que atraviesan objetos, contrapeso pegado a la cabina): descártalos para cortes técnicos aunque sean muy baratos.
6. **El usuario aprueba los fotogramas** antes de pasar a vídeo.

### F4 — Vídeo (tras la autorización B)

1. Vuelve a presupuestar cada ficha ya con `medias: [{"value": "<job_id del fotograma aprobado>", "role": "<rol de imagen inicial del modelo>"}]` y usa el nuevo `quote_ref`.
2. `generate_video_batch` (≤12 por lote) con `aspect_ratio: "9:16"` y la duración admitida.
3. `jobs_wait` → `show_generation_by_ids` → revisión de calidad.
4. Si un clip deforma el objeto, prueba primero con un prompt de movimiento más simple; si sigue fallando, pasa ese plano a animación en montaje.

### F5 — Voz (tras la autorización C)

1. Una petición por escena con `generate_audio_batch`: el texto es la **narración exacta** de la ficha.
2. Misma voz (`voice_id` + `voice_type`) y mismos parámetros en todas las escenas, para que suene igual.
3. **Genera una escena de prueba** y mide su duración antes de generar las demás. Ajusta la velocidad si el modelo lo admite (en Seed Audio, `speech_rate: 20` ≈ 15 % más rápido).
4. Mide cada audio (con `ffprobe`) y **recorta los silencios** como se explica en [dynamic-editing.md](dynamic-editing.md). En el montaje, la línea de tiempo se adapta a la voz; no recortes palabras.
5. **Parámetros según el modelo**: no todos usan `prompt` y `voice_id` sueltos.
   - Los modelos de ElevenLabs (`elevenlabs_v4`, `elevenlabs_v4_turbo`) piden `dialogue: [{"text", "voice_type", "voice_id"}]`. Pon también `prompt` con el mismo texto, porque la herramienta lo exige.
   - `text2speech_v2` usa `variant` (elevenlabs, minimax, seed_speech…).
   - Lee siempre `models_explore get`.
6. **Si el usuario pide un modelo o una versión que no está en el catálogo** (por ejemplo, «ElevenLabs v3»), no lo sustituyas en silencio: enséñale las alternativas reales con su precio y deja que elija.
7. **Presupuesta todas las escenas**, no solo la primera. El coste de voz depende de la longitud del texto: en el ejemplo, un presupuesto hecho con la primera escena (0,46 cr) se convirtió en 6,75 cr para las 8.
8. No puedes escuchar el audio: pide al usuario que revise el acento y la pronunciación de los términos clave.

### F6 — Montaje (tras la autorización D)

**El estilo de montaje por defecto es el dinámico**: planos cada 2–4 s, transiciones, animaciones, efectos de sonido y ningún silencio. Sigue [dynamic-editing.md](dynamic-editing.md) y parte de [../scripts/montaje_dinamico.py](../scripts/montaje_dinamico.py) y [../scripts/sfx.sh](../scripts/sfx.sh). Los pasos de abajo son la base técnica.

Funcionamiento del sandbox (comprobado):
- **No se observó coste en créditos** al montar (saldo igual antes y después). Aun así, compruébalo con `balance` la primera vez.
- Los renders largos van con `background: true`. Consulta el estado con comandos de **`sleep` ≤ 45 s**: con esperas de 90–100 s el conector devolvió «server isn't responding». Ejecuta Python con `-u`, o el log saldrá vacío hasta el final.
- El sandbox puede reemplazarse entre llamadas (cambia el `sandbox_id`). `/home/user` se conserva, pero comprueba que los archivos siguen ahí antes de seguir.
- Si un paso falla a mitad de un script, guarda los planos ya renderizados y sáltalos al relanzar (comprueba si existe el archivo), para no repetir minutos de render.
- Revisa los fotogramas con `image_paths` (≤ 512 KiB). Para ver un clip, junta 4 fotogramas en una tira con `hstack`.

En `sandbox_exec` (comandos de ≤120 s; los largos con `background: true` y consultando el log):

1. Descarga los resultados con `curl` desde las URL de los trabajos terminados.
2. Recorta cada clip a la duración de su plano (`ffmpeg -ss/-t`) y escálalo a 1080 × 1920.
3. Planos solo gráficos: créalos con ImageMagick (PNG) y anímalos con ffmpeg (desplazamiento, aparición).
4. Superpón flechas y etiquetas (PNG con transparencia) según la ficha, **dentro de la zona segura** (y 288–1536, x < 950).
5. Subtítulos: genera un `.ass` con la narración troceada del storyboard (Montserrat, blancos con borde, 2 líneas como máximo, y 1150–1536). Si hace falta ajustar los tiempos, transcribe la voz con faster-whisper.
6. Une los clips en orden, añade la voz y, si se aprobó, música suave a volumen bajo.
7. Exporta en H.264, 1080 × 1920, 30 fps, AAC; duración ≤ 70 s.
8. Saca 4 fotogramas de control y revísalos con `image_paths`.
9. Para guardarlo en Higgsfield: `media_upload` **antes** del comando que crea el archivo final, añade el `curl -f -X PUT` al final de ese mismo comando, y `media_confirm` solo si devuelve HTTP 200.

Si el usuario prefiere montar en su editor, entrega los clips, la voz, los PNG de las etiquetas y el `.ass`, con una lista de montaje por tiempos.

### F7 — Entrega

- Vídeo final (o paquete para su editor). Para llevarlo al equipo del usuario: `media_upload`, PUT desde el sandbox (HTTP 200) y `media_confirm`. Después `curl` de la URL devuelta a la carpeta del usuario y `SendUserFile` con `display: "render"`.
- Guarda también localmente los fotogramas, clips y voces aprobados (`fotogramas/`, `clips/`, `voz/`) y un documento del proyecto con todos los `job_id`, tiempos y gasto por fase. Cada revisión del usuario es una versión nueva (`_v2`, `_v3`…): no sobrescribas la anterior.
- Tabla de gasto real por fase frente al presupuesto (vuelve a llamar a `balance`).
- Lista de los planos que se rehicieron y por qué.

## 4. Ficha de producción por escena

Una por plano generado. Guárdalas juntas en un JSON (por ejemplo `produccion.json`) para poder pasarlas por referencia.

```json
{
  "index": 51,
  "escena": "E5",
  "plano": "5a",
  "tiempo": "0:32–0:34.5",
  "tipo": "imagen",
  "modelo": "<id de models_explore>",
  "params": {
    "model": "<id>",
    "aspect_ratio": "9:16",
    "prompt": "…",
    "medias": [{"value": "<job_id de la hoja de referencia>", "role": "<rol>"}]
  },
  "duracion_generada_s": null,
  "duracion_plano_s": 2.5,
  "quote_ref": "<del presupuesto>",
  "coste_base": 0,
  "reintentos_previstos": 2,
  "montaje": ["etiqueta 'dentro' y 'fuera'", "subtítulo: «Así que pones dos telas.»"],
  "job_id": null,
  "estado": "pendiente | generado | aprobado | rehacer"
}
```

`index`: escena × 10 + plano (5a → 51, 5b → 52…), para que el orden sobreviva a los lotes.

### Cómo escribir el prompt

En este orden y en lenguaje espacial explícito:

1. **Encuadre**: «vertical 9:16, corte frontal de una tienda en forma de A, triángulo centrado, vértice en el tercio superior».
2. **Piezas y posición**: cada pieza de la hoja de referencia que se ve, con su color y dónde está respecto a las demás.
3. **Estado**: cómo está todo en ese instante (vídeo: estado inicial → acción → estado final, con dirección y causa).
4. **Estilo**: el de la hoja aprobada («ilustración 3D estilizada, colores planos, sin fotorrealismo, fondo azul noche»).
5. **Evitar**: posiciones incorrectas habituales, piezas que no existen todavía, texto, flechas, logotipos, marcas de agua.

En vídeo, pide **un solo movimiento sencillo** por clip. Los cambios de escena se hacen con cortes, no dentro del clip.

## 5. Reglas de seguridad

- **Tiempo de espera agotado al enviar**: el trabajo puede haberse creado. **No lo reenvíes**: guarda los `job_id` que tengas y consulta con `jobs_wait` antes de repetir nada.
- **Lote con fallos parciales**: reintenta solo los elementos fallidos, nunca el lote entero.
- **Generaciones gratuitas (`use_unlim`)**: no lo indiques. Si Higgsfield devuelve `unlim_choice`, no se ha generado nada: pregunta al usuario si usar sus generaciones gratuitas o sus créditos, y repite con su respuesta. `use_free_gens` solo si el usuario lo pide.
- **`count`**: 1 por petición. Las variantes multiplican el coste; pídelas solo si el usuario quiere elegir entre varias.
- **Máximo aprobado**: lleva la suma de lo gastado; si el siguiente reintento lo supera, para y pregunta.
- **Presupuesto que cambia**: si al volver a presupuestar (F4) el coste sube más de un 10 % respecto a lo aprobado, avisa antes de generar.
- **Identificadores**: nunca inventes `job_id`, `media_id`, `folder_id` ni `quote_ref`. Reutiliza un mismo `folder_id` en toda la conversación.
- **Proyecto**: no lo crees salvo que `get_preferences` diga `auto_create_project: true` o el usuario lo pida. Si lo creas, una sola vez.
- **Herramientas no relacionadas**: no uses publicación (TikTok, `publish_*`), anuncios, webs ni GPU de alquiler. Publicar requiere un permiso aparte.
- **`recovery_tool` o `adjustments`** en una respuesta: aplícalos. Si cambian algo que el usuario aprobó (duración, formato, modelo), díselo.

## 6. Revisión de calidad

Para cada resultado, antes de aprobarlo:

- [ ] Vertical 9:16 de verdad (no horizontal con bandas).
- [ ] Piezas en la posición de la hoja de referencia; ninguna pieza de etapas futuras.
- [ ] Proporciones y colores iguales que en planos anteriores.
- [ ] Movimiento con la dirección y la causa de la ficha.
- [ ] Lo importante, dentro de la zona segura.
- [ ] Sin texto inventado, logotipos, marcas de agua, manos o caras deformadas.
- [ ] Nada que contradiga la tabla de rigor (por ejemplo, agua entrando por donde no entra).

Un resultado que falla un punto de precisión se rehace aunque sea bonito.

## 7. Mensajes de autorización

Antes de cada fase de gasto, un mensaje así (en el idioma del usuario):

> **Fase B · Vídeo** — 9 clips verticales de 5 s con `<modelo>`, a partir de los fotogramas aprobados.
> Coste base: **X créditos**. Reserva de reintentos: **Y créditos**. Máximo: **X + Y**.
> Saldo actual: **Z créditos**.
> ¿Autorizas generar esta fase con ese máximo?

No generes hasta recibir un sí que se refiera a esa fase (o a un conjunto de fases que la incluya) y a ese importe.

Si al ejecutar una fase aprobada hay que cambiar de modelo (por ejemplo, porque el plan lo rechaza) y el coste sigue dentro del máximo aprobado, sigue adelante y díselo al usuario. Si el coste o la calidad cambian mucho (más caro, menos resolución), pregunta antes.

## 8. Registro de campo (noviembre de 2026, plan gratuito)

Es una referencia con fecha; vuelve a comprobarla en cada producción.

| Tipo | Funcionó con plan gratuito | Rechazado («Requires basic plan or higher») | Notas |
|---|---|---|---|
| Imagen | `nano_banana_2` (se ejecuta como nano_banana_flash): 1,5 cr a 1k, 2 cr a 2k (1536 × 2752) con referencia. Buena coherencia técnica y edita bien a partir de una imagen. · `z_image` (0,15 cr): geometría incoherente, descartado | `seedream_v4_5`, `gpt_image_2_6`, `recraft_v4_1` | Pide `resolution: "2k"` para no tener que ampliar |
| Vídeo | `wan2_7`: 1,5 cr/s, imagen inicial con rol `start_image`, salida 716 × 1284 (~720p), sigue bien el movimiento pedido | `kling3_0` | `kling_4_0_flash` tenía el mismo precio, pero no se probó. Seedance 2.0/2.5 cuesta 3–7 cr/s |
| Voz | `seed_audio` (≈ 0,8 cr por escena; `speech_rate`) · `elevenlabs_v4` (≈ 0,5–1,2 cr por escena según longitud; usa `dialogue`) | — | ElevenLabs v3 no existe en el catálogo. Alternativas: `elevenlabs_v4`, `elevenlabs_v4_turbo`, `text2speech_v2` con `variant: "elevenlabs"` |
| Montaje | `sandbox_exec`: 0 créditos | — | Límite de un trabajo simultáneo en las generaciones |

Gasto real del short de ejemplo (8 escenas, 70 → 54 s): imágenes 39,65 · vídeo 40,5 · voces 6,5 + 5,9 + 6,75 · montaje 0 → **99,3 créditos**.
