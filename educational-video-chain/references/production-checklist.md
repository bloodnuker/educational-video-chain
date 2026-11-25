# Checklist de producción con IA (Higgsfield MCP u otras)

Úsala en la Fase 8. Su propósito es preparar la producción **sin gastar nada** hasta que el usuario lo autorice expresamente.

Para dar las órdenes concretas a Higgsfield MCP (herramientas, orden de llamadas, fichas por plano, montaje), sigue [higgsfield-execution.md](higgsfield-execution.md).

## 1. Regla de gasto

- No ejecutes ninguna generación, render, upscale, voz, lipsync ni acción que consuma créditos sin autorización explícita del usuario **para ese gasto**.
- "¿Cuánto costaría?", "prepárame la producción", "hazme el presupuesto" **no** son autorizaciones.
- Una autorización válida nombra qué se genera y acepta un importe (o un máximo). Ejemplo: "Adelante con las escenas 1–4, máximo 200 créditos".
- Antes de ejecutar, repite: qué se va a generar, con qué modelo, coste estimado y saldo disponible si la herramienta lo informa. Respeta el máximo; si un reintento lo superaría, para y pregunta.
- Las llamadas de solo lectura (listar modelos, consultar precios o saldo) sí se pueden hacer, siempre que la herramienta indique que no cobran. Si no estás seguro de que una llamada sea gratuita, pregunta antes.

## 2. Descubrimiento de herramientas (no supongas)

1. Lista las herramientas MCP realmente disponibles en la sesión (busca las del proveedor, p. ej. nombres que contengan `higgsfield`). Si están diferidas, cárgalas primero.
2. Para cada herramienta, lee su esquema y descripción y anota:

| Herramienta | Tipo (imagen/vídeo/voz/montaje/otra) | Modelos | Duraciones admitidas | Resoluciones / relaciones de aspecto | ¿Genera audio? | Entrada (texto, imagen de referencia, vídeo) | Coste (créditos) | Fuente del coste |
|---|---|---|---|---|---|---|---|---|

3. Comprueba que cada modelo admite **relación de aspecto 9:16** (o 1080 × 1920). Si no la admite, no lo asignes a escenas finales: generar en horizontal y recortar suele dejar fuera lo importante.
4. Si existe una herramienta para listar modelos, precios o saldo, úsala (solo lectura).
5. **Fuente del coste**: "devuelto por la herramienta", "descripción de la herramienta" o "estimación no verificada". Nunca presentes como real un precio que solo viste en la web del proveedor.
   - Que un modelo tenga presupuesto no significa que el plan del usuario lo permita. Márcalo como «sin probar con este plan» hasta que una petición real se acepte (ver la sección F0 de higgsfield-execution.md).
   - Presupuesta la voz con todas las escenas: el coste crece con la longitud del texto.
6. Lo que aparece en la web del proveedor pero no en la sesión **no existe** a efectos del plan. Puedes mencionarlo como "no disponible en esta sesión".
7. Si no hay herramientas de generación conectadas, dilo claramente y entrega el plan con columnas de coste vacías o marcadas como "pendiente de conectar".

## 3. Clasificación de operaciones

Separa siempre:

- **Imagen**: fotogramas clave, hoja de referencia, fondos.
- **Vídeo**: animación de fotogramas, planos generados (texto→vídeo, imagen→vídeo).
- **Voz**: locución (TTS), clonación de voz si existe y está autorizada. Por defecto, **Eleven v4 con la voz Dylan** (ver higgsfield-execution.md §0). Solo si el usuario quiere cambiarla, propón 2–3 voces con su muestra. Los silencios se eliminan en montaje (ver [dynamic-editing.md](dynamic-editing.md)).
- **Subtítulos**: obligatorios en vertical; indica si se generan con una herramienta o en montaje.
- **Montaje y edición**: unión de clips, rótulos, flechas, subtítulos animados y **efectos de sonido**. El estilo por defecto es **dinámico y sin silencios** ([dynamic-editing.md](dynamic-editing.md)). Indica si se hace con una herramienta de la sesión o fuera (editor del usuario).
- **Operaciones adicionales**: upscale, interpolación, lipsync, eliminación de fondo, extensión de clip.

## 4. Asignación por escena

Para cada escena del storyboard decide la técnica según la sección 4 de [storyboard-visual-accuracy.md](storyboard-visual-accuracy.md):

- Escenas técnicas (cortes, mecanismos, flujos): imagen de referencia + animación en montaje, o motion graphics. Evita depender del vídeo generativo para la exactitud.
- Escenas atmosféricas o de contexto: vídeo generativo.
- Ajusta la duración del clip a las duraciones que el modelo admite de verdad (si admite 5 y 10 s, una escena de 7 s se genera a 10 y se recorta, y se presupuesta a 10).

## 5. Presupuesto

Tabla por escena:

| Escena | Operación | Herramienta/modelo | Parámetros (duración, resolución) | Unidades | Coste unitario | Coste base | Reintentos previstos | Coste reintentos | Fuente del precio |
|---|---|---|---|---|---|---|---|---|---|

Reglas:

- **Coste base** = una generación satisfactoria por operación.
- **Reserva de reintentos** separada, no sumada al base. Referencia orientativa (ajústala si hay datos del usuario): imagen técnica ×2, vídeo de mecanismo ×2–3, vídeo atmosférico ×1, voz ×0,5.
- Total = base + reserva, mostrados por separado y sumados.
- Añade locución (por minuto o por carácter, según la herramienta) y montaje si consume créditos.
- Indica supuestos y lo que no está incluido.

## 6. Paquete de producción (entregable)

- Hoja de referencia del sistema y fotogramas clave a generar primero (aprobación antes de animar).
- Prompts por escena (ver sección 5 de storyboard-visual-accuracy.md) con negativos y referencia.
- Texto de locución final con marcas de tiempo y pronunciación de términos técnicos.
- Lista de rótulos, flechas y etiquetas para montaje.
- Orden de ejecución recomendado: referencia → fotogramas clave → aprobación del usuario → animación → voz → montaje.
- Presupuesto (sección 5) y petición de autorización explícita.

## 7. Control de calidad tras cada generación (si se autoriza)

- ¿Los componentes están en su sitio según la hoja de referencia?
- ¿Las proporciones y la orientación coinciden con escenas anteriores?
- ¿El movimiento tiene la dirección y causa correctas?
- ¿Hay artefactos (piezas duplicadas, texto inventado, manos, uniformes erróneos)?
- Si falla, cuenta el reintento contra la reserva y avisa antes de superarla.
