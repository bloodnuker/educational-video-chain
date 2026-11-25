# Lenguaje visual: escenas 3D, ilustraciones, elementos explicativos, cámara y detalles

Úsala en la Fase 7 (storyboard) y en la Fase 8 (producción). Es un estándar de la skill: los vídeos deben combinar **escenas 3D, ilustraciones, elementos explicativos, movimientos de cámara y detalles**, sin perder la precisión técnica de [storyboard-visual-accuracy.md](storyboard-visual-accuracy.md).

Lección del primer short (ascensor): las escenas técnicas eran fotogramas fijos con zoom, y el movimiento clave (la caja sube mientras el contrapeso baja) se resolvió con un fundido. Lo correcto era una **escena 3D animada** con la cámara acompañando el movimiento. Las reglas de abajo existen para que eso no se repita.

---

## 1. Tratamiento visual por escena

Cada escena del storyboard declara **uno** de estos tratamientos según lo que tiene que explicar. Un vídeo bueno combina al menos tres.

| Tratamiento | Cuándo usarlo | Qué aporta | Cómo producirlo |
|---|---|---|---|
| **3D técnico** | Mecanismos con piezas que se mueven, volumen, posición relativa, recorridos | Movimiento real y exacto, cámara libre, cortes y transparencias coherentes | Escena 3D (sección 6): construida y renderizada, no generada |
| **Ilustración 2D** (plana, isométrica, línea, acuarela) | Ideas, comparaciones, el «antes» ingenuo, esquemas sencillos | Claridad y estilo propio; el ojo entiende rápido | Imagen generada con la hoja de estilo fija, o dibujo vectorial en montaje |
| **Realista** | Contexto, escala humana, el resultado final, el «para qué» | Credibilidad y conexión con lo cotidiano | Imagen o vídeo generado |
| **Histórico / grabado** | Recompensa final, origen del invento | Cambio de textura que marca el cierre | Imagen generada en estilo de época + animación simple |
| **Motion graphics** | Fuerzas, flujos, cifras, secuencias lógicas | Lo invisible se vuelve visible | Montaje (ASS, ffmpeg, ImageMagick) |

Reglas:

- **El mecanismo central del vídeo va en 3D técnico** siempre que haya una herramienta 3D disponible. Si no la hay, dilo y usa ilustración por fotogramas con la animación en montaje.
- **Mantén un estilo por tratamiento** en todo el vídeo: una sola paleta y un solo grosor de línea para la ilustración, y un solo material y una sola iluminación para el 3D. La hoja de referencia del sistema fija ambos.
- **Al cambiar de tratamiento** (por ejemplo, de ilustración a 3D) usa una transición motivada: un *match cut* sobre la misma pieza, o un zoom que entra en el objeto.

## 2. Elementos explicativos

Son las herramientas para que el espectador **vea la causa**, no solo el resultado. Elige el elemento por lo que debe entenderse.

| Elemento | Para qué | Ejemplo |
|---|---|---|
| **Corte** (sección) | Ver lo que hay dentro sin desmontar | Corte frontal del hueco del ascensor |
| **Rayos X / transparencia** | Ver una pieza oculta sin perder el exterior | La carcasa se vuelve translúcida y deja ver las pinzas |
| **Despiece animado** (*exploded view*) | Mostrar de qué partes se compone algo y cómo encajan | El freno se separa en mordaza, muelle y raíl, y vuelve a montarse |
| **Flecha de fuerza / flujo** | Peso, empuje, corriente, dirección | Flecha roja de peso; flechas blancas de sube y baja |
| **Partículas** | Aire, agua, calor, electricidad | Puntos que fluyen por un tubo |
| **Resaltado de pieza** (brillo, contorno, color) | Señalar de qué se habla en cada momento | El contrapeso se ilumina al nombrarlo |
| **Lupa / recuadro de detalle** | Detalle pequeño sin perder el contexto | Círculo ampliado de la cuerda gastada sobre el plano general |
| **Comparación de escala** | Tamaños o pesos que no se intuyen | El contrapeso al lado de cinco personas |
| **Fantasma / trazo de recorrido** | Movimiento ya ocurrido, trayectoria | Silueta semitransparente de la posición anterior de la caja |
| **Antes / después** (dividido arriba/abajo o fundido) | Efecto de una solución | Caja balanceándose frente a caja con raíles |
| **Etiqueta con línea guía** | Nombrar una pieza en una escena llena | «Pinzas» con una línea hasta la mordaza |
| **Indicador simple** (medidor, contador) | Una magnitud que cambia | Aguja de velocidad que pasa a rojo antes de frenar |

Reglas:

- **Un elemento explicativo principal por plano.** Como mucho, dos: por ejemplo, un resaltado y una flecha.
- El elemento **aparece cuando la locución lo nombra** y se va al pasar a otra idea.
- El código de colores es el de la hoja de referencia: rojo para fuerza o peligro, blanco para movimiento, amarillo para la palabra clave, y uno por fluido.
- Simplificación honesta: si exageras algo para que se vea, escribe «exagerado» o «simplificado» en pantalla.

## 3. Movimientos de cámara

Cada movimiento debe tener **un motivo**: si no lo tiene, cámara fija.

| Movimiento | Motivo | Uso típico en estos vídeos |
|---|---|---|
| **Acercamiento** (*push-in*) | Dirigir la atención, entrar en el detalle | De la caja entera a las pinzas |
| **Alejamiento** (*pull-out*) | Revelar el contexto o la escala | De la cuerda gastada al edificio entero |
| **Órbita** | Mostrar volumen y posición relativa en 3D | Girar 45° alrededor del freno para ver cómo abraza el raíl |
| **Grúa vertical** (*pedestal*) | Seguir un movimiento vertical. **Ideal en 9:16** | La cámara sube junto a la cabina |
| **Travelling lateral** (*tracking*) | Seguir un objeto que se desplaza | Seguir el contrapeso mientras baja |
| **Panorámica vertical** (*tilt*) | Recorrer algo alto sin cortar | Del foso a la polea en un solo plano |
| **Zoom brusco** (*snap zoom*) | Golpe de énfasis, sorpresa | «¿Y si la cuerda se rompe?» |
| **Barrido rápido** (*whip pan*) | Transición con energía entre dos espacios | Del hueco al rellano |
| **Cambio de foco** (*rack focus*) | Pasar la atención de una pieza a otra en el mismo plano | De la mano en el botón a la puerta |
| **Cámara fija** | Mecanismos finos que necesitan quietud | Las pinzas mordiendo el raíl |
| **Plano subjetivo** (POV) | Poner al espectador en la situación | Ver el hueco vacío desde la puerta |

Reglas:

- **Un movimiento por plano.** No combines órbita y acercamiento en el mismo plano.
- **En vertical, prioriza los movimientos verticales** (grúa, tilt): aprovechan la pantalla alta.
- **La cámara no se mueve mientras se explica un detalle fino.** Primero se mueve, luego se queda quieta para explicar.
- Duración: entre 1,5 y 4 s, con aceleración y frenada suaves (*ease in/out*). La única excepción son los movimientos de énfasis (zoom brusco, barrido rápido).
- En 3D, la trayectoria de cámara se anima con fotogramas clave. En vídeo generado, se pide en el prompt con un solo movimiento: «slow push-in», «slow orbit left 30 degrees», «camera rises vertically following the cabin». En imágenes fijas, se simula en montaje con zoom, desplazamiento y temblor.
- Evita el plano inclinado (*dutch angle*) y los giros de 360°: marean y no explican nada.

## 4. Detalles

Los detalles hacen que el vídeo parezca cuidado y premian a quien mira con atención.

- **Un plano detalle (macro) por etapa**, centrado en la pieza que resuelve el problema: la ranura de la polea, el diente de la mordaza, el gancho del cierre.
- **Materiales creíbles**: hormigón con poro, acero con reflejo suave y algo de desgaste, cuerda con trenzado visible, tornillos en las uniones. En ilustración, una textura sutil coherente con el estilo.
- **Micro-movimientos**: polvo en el choque, chispas al frenar, vibración del motor, el cable que se tensa. Son breves y van con su efecto de sonido.
- **Detalles humanos**: manos que pulsan o tiran, personas con proporciones correctas y sin rasgos deformados. Revisa manos y caras en cada imagen generada.
- **Continuidad de detalles**: una pieza que aparece desgastada sigue igual hasta que se repara; los tornillos no aparecen ni desaparecen entre planos.
- **Detalle de recompensa**: un elemento pequeño y verdadero que se descubre en el último plano, ligado a la recompensa final.
- **No inventes detalles técnicos** para decorar: si un componente no existe en la realidad, no se dibuja, aunque quede bonito.

## 5. Patrón de ritmo por etapa

Úsalo como base y varíalo para que no resulte mecánico.

```
contexto (plano general, ilustración o realista)
 → mecanismo (3D técnico con corte/transparencia y movimiento de cámara motivado)
 → detalle (macro de la pieza clave, cámara fija, elemento explicativo)
 → consecuencia (vuelta al plano general o antes/después)
```

En un short de ≤ 70 s con 4–6 etapas no caben los cuatro planos en todas: alterna. Por ejemplo, en una etapa mecanismo + detalle y en la siguiente contexto + mecanismo. Cada etapa tiene al menos un plano de mecanismo, y el vídeo completo tiene al menos 3 tratamientos visuales distintos.

## 6. Cómo producir cada cosa

Descubre siempre las herramientas reales de la sesión; no supongas.

**Escenas 3D:**
- **Higgsfield 3D Jutsu** (herramientas `scene_builder_3d_*`). Antes de usarlo, lee `get_preset_instructions` con `{"preset": "/3d-jutsu"}` y sus referencias (`scene-building`, `composition-modeling`, `lookdev-lighting`, `animation-audit`).
  - Construir, editar y **renderizar no consume créditos**, según sus instrucciones (noviembre de 2026). Solo cuesta pasar un render por IA con `generate_angles` o `generate_video`.
  - Las escenas se construyen con Python (`bpy`). Renderiza con EEVEE y publica PNG o MP4 (H.264) como artefactos: hasta 8 por operación, con un límite de unos 5 min por operación. Usa resolución y muestras bajas.
  - Solo importa modelos de su catálogo: no admite mallas propias ni generadas. Para piezas técnicas, constrúyelas con formas simples, que además salen más exactas.
  - Hay otras dos rutas: Blender Studio (GPU de alquiler, cobra por segundo) y el Blender del propio usuario (`/scene-builder`). **Pregunta una vez qué ruta prefiere el usuario**, recomendando la gratuita, como piden las instrucciones de 3D Jutsu.
  - Nombra los objetos por su función (`HERO_cabina`, `ENV_hueco`, `CAM_main`, `LGT_key`). Coloca la cámara de entrega en 9:16 (por ejemplo, 1080 × 1920 al 50 %) y anima la cámara con fotogramas clave.
  - Renderiza un fotograma de prueba, míralo y corrige antes del render final.
- Ventaja: el 3D garantiza que las piezas estén en su sitio y se muevan como en la realidad, que es justo donde fallan las imágenes y vídeos generados.

**Ilustraciones:** imagen generada con una hoja de estilo aprobada como referencia. Para dar movimiento, edita a partir de la imagen aprobada (estados distintos con el mismo encuadre) y anima en montaje.

**Realista e histórico:** imagen generada → vídeo a partir de esa imagen, con **un** movimiento de cámara en el prompt.

**Elementos explicativos y cámara simulada:** en montaje. Ver [dynamic-editing.md](dynamic-editing.md).
- Flechas, resaltados, etiquetas con línea guía e indicadores se hacen con ASS (dibujo vectorial, `\move`, `\t`).
- La lupa es un recorte ampliado y circular superpuesto con `overlay` en ffmpeg.
- Los fantasmas y las comparaciones de escala se hacen con capas semitransparentes.

**Presupuesto:** el 3D alojado no tiene coste de créditos, pero sí tiempo: unos minutos por render. Inclúyelo en el plan y avisa de la ruta y de su coste antes de empezar.
