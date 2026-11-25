# Storyboard y precisión visual

Úsala en la Fase 7. Una escena es buena si un espectador **sin sonido** entiende qué está pasando, por qué y qué cambió.

Úsala junto con [visual-language.md](visual-language.md), que explica cómo elegir el tratamiento de cada escena (3D, ilustración, realista), los elementos explicativos, los movimientos de cámara y los detalles. Este archivo pone las reglas de precisión; aquel, la riqueza visual. Las dos cosas son obligatorias.

## 1. Primero: hoja de referencia del sistema

Antes de la primera escena, define el sistema una sola vez. Todas las escenas la respetan; así la geometría y la posición de los componentes no cambian entre planos (el fallo más habitual en vídeo generado con IA).

Contenido mínimo:

- **Vistas canónicas**: exterior lateral, corte longitudinal, corte transversal, planta (las que el tema necesite).
- **Ejes y orientación**: qué es delante/detrás, arriba/abajo, izquierda/derecha. Fija una dirección de avance en pantalla (p. ej. el vehículo siempre avanza hacia la derecha).
- **Tabla de componentes**:

| Componente | Ubicación en el conjunto | Forma y tamaño relativo | Visible desde fuera | Color/código visual | Aparece desde la etapa |
|---|---|---|---|---|---|

- **Código de colores fijo**: un color por fluido o tipo de elemento (p. ej. agua = azul, aire = blanco/gris claro, estructura resistente = gris oscuro, energía = amarillo, flecha de fuerza = rojo). No lo cambies a mitad del vídeo.
- **Proporciones**: relaciones de tamaño que deben mantenerse (p. ej. "la vela ocupa ~1/6 de la eslora").
- **Estado del sistema por etapa**: qué piezas existen ya en cada etapa (el sistema es acumulativo; no deben desaparecer piezas instaladas).

## 1b. Formato vertical 9:16 (estándar de la skill)

El vídeo se publica en Shorts, Reels y TikTok: lienzo **1080 × 1920**, duración **≤ 70 s**.

- **Zona segura**: deja libre ~15 % superior (nombre de cuenta, iconos) y ~20 % inferior (descripción, botones), y ~12 % del lado derecho (botones de like/comentar). Lo que el espectador tiene que ver para entender el mecanismo va en el centro.
- **Orienta el sistema en vertical** cuando sea posible: cortes de arriba abajo, objetos de pie, procesos que suben o bajan. Si el objeto es alargado en horizontal (un vehículo), muéstralo en diagonal, por partes con un plano de situación, o con la cámara recorriéndolo; no lo encojas para que quepa entero.
- **Un solo foco por plano**: en pantalla pequeña no caben dos mecanismos a la vez. Evita pantallas divididas en horizontal; si comparas, divide arriba/abajo.
- **Planos más cerrados** que en horizontal; el detalle importante debe ocupar al menos 1/3 de la pantalla.
- **Subtítulos obligatorios** (mucha gente ve sin sonido): letra grande, 2 líneas como máximo, dentro de la zona segura, en el tercio central-inferior. No deben tapar la pieza que se explica.
- **Etiquetas en pantalla** en palabras sencillas (las mismas que usa la locución), de 1–3 palabras.
- **Ritmo**: cambio visual cada 2–4 s; el gancho visual en el primer segundo.
- **Hoja de referencia en vertical**: define las vistas canónicas ya en 9:16 para que todas las escenas compartan encuadre.

## 2. Ficha de escena (obligatoria)

```
ESCENA [n] — [título corto]                          Etapa del mapa: [#]
Duración: [s]          Tiempo: [mm:ss–mm:ss]
Narración exacta: «…»
Subtítulo / texto en pantalla: [texto y posición dentro de la zona segura]

Elementos visibles:
  - [componente]: [descripción física: forma, material, tamaño relativo]
    Ubicación: [posición respecto al conjunto y a otros componentes]
Estado inicial: [cómo está todo al empezar la escena]
Acción / movimiento: [qué se mueve]
  Dirección: [hacia dónde, con referencia a los ejes de la hoja]
  Causa: [qué fuerza/mecanismo lo provoca]
Estado final: [cómo queda]
Tratamiento visual: [3D técnico | ilustración 2D | realista | histórico | motion graphics] (ver visual-language.md §1)
Planos: [lista de planos de 2–4 s con su tipo: contexto / mecanismo / detalle / consecuencia]
Encuadre y cámara: [vista canónica usada, tamaño de plano; composición 9:16]
  Movimiento de cámara: [tipo (push-in, pull-out, órbita, grúa vertical, tracking, tilt, snap zoom, whip, rack focus, fija)]
    Inicio → fin: [encuadre inicial → encuadre final, en segundos]
    Motivo: [qué guía: seguir la pieza, revelar escala, entrar en el detalle…]
Elementos explicativos: [uno principal (máx. 2): corte, rayos X, despiece, flecha de fuerza/flujo, partículas,
  resaltado, lupa, comparación de escala, fantasma, antes/después, etiqueta con línea guía, indicador]
  Aparece/desaparece: [en qué palabra de la narración]
Plano detalle: [pieza en macro y qué rasgo se ve: ranura, diente, trenzado, desgaste…]
Detalles de verosimilitud: [materiales, micro-movimientos (polvo, chispas, vibración) con su efecto de sonido]
Ayudas visuales: [flechas (qué representan), etiquetas (texto exacto), transparencias, cortes]
El espectador debe comprender: [una frase]
Continuidad: [qué hereda de escenas anteriores; qué no puede cambiar]
Técnica recomendada: [ver sección 4]
Riesgos de precisión: [qué podría salir mal al generarla y cómo evitarlo]
```

"Narración exacta" debe coincidir palabra por palabra con el guion, para que el montaje sea directo.

## 3. Reglas de precisión

1. **Ubicación correcta**: cada componente está donde está en la realidad. Si se simplifica, se simplifica la forma, nunca la posición.
2. **Conexiones correctas**: si A alimenta a B, la conexión se ve o se insinúa; no aparecen conexiones que no existen.
3. **Mecanismos reales**: lo que se mueve, se mueve como en la realidad y por la causa real (el agua entra *por abajo* porque el aire sale *por arriba*; no "porque sí").
4. **Interior vs exterior**: distingue siempre qué está dentro de qué. Usa corte o transparencia cuando la pieza esté oculta; nunca la dibujes "flotando" visible a través de una pared opaca.
5. **Geometría estable**: proporciones, número de piezas y orientación no cambian entre escenas salvo que la historia lo exija (y entonces se muestra el cambio).
6. **Flechas con significado único**: una flecha = una magnitud (flujo, fuerza, movimiento). Leyenda constante. No más de 2–3 tipos por escena.
7. **Etiquetas mínimas**: 1–3 palabras, solo la primera vez que aparece una pieza o cuando cambia de estado.
8. **Escala honesta**: si exageras una escala para que se vea (p. ej. la compresión de un casco), indícalo en pantalla ("exagerado").
9. **Precisión antes que espectáculo**: si una toma espectacular contradice el mecanismo, se descarta.
10. **Acumulación visible**: las soluciones anteriores siguen presentes en las escenas siguientes.

## 4. Técnica visual recomendada

| Necesidad | Técnica | Nota para generación con IA |
|---|---|---|
| Mostrar mecanismo interno con exactitud | **Escena 3D construida** (corte, transparencia, despiece) con cámara animada | Primera opción si hay herramienta 3D (por ejemplo, Higgsfield 3D Jutsu, que es gratuito de construir y renderizar). La IA de vídeo suele fallar en cortes técnicos; sin 3D, genera fotogramas fijos y anima en montaje |
| Mostrar volumen o cómo encajan las piezas | Órbita 3D o despiece animado | Solo con 3D construido; no lo pidas a un vídeo generado |
| Seguir un movimiento vertical | Grúa vertical que acompaña a la pieza | En 3D, fotogramas clave de cámara; en montaje, desplazamiento sobre una imagen alta |
| Flujo de fluidos | Corte + partículas o niveles de color | Mejor animación 2D/motion graphics que vídeo generativo |
| Contexto real y escala | Plano exterior realista | Vídeo generativo o imagen + movimiento de cámara |
| Fuerzas y presiones | Flechas superpuestas sobre corte | Siempre en postproducción, nunca dentro del prompt |
| Comparar antes/después | Pantalla dividida o fundido sobre el mismo encuadre | Mismo encuadre y semilla/referencia para coherencia |
| Paso del tiempo / condición nueva | Cambio de luz, rótulo de hora, clima | Útil para retos tipo B |
| Detalle humano | Plano realista de personas | Revisa manos, uniformes y equipamiento contra referencias |

Regla práctica: **lo que tiene que ser exacto se dibuja o se compone; lo que tiene que ser atmosférico se genera.**

## 5. Prompts para generación

Cuando el alcance incluya producción, añade a cada ficha un bloque de prompt:

- Describe la vista canónica y la posición de cada componente en lenguaje espacial explícito ("tanque en forma de anillo entre el casco interior y el exterior, en la mitad inferior").
- Indica estilo, iluminación y paleta de la hoja de referencia.
- Añade negativos: piezas que no deben aparecer, posiciones incorrectas habituales.
- Usa imagen de referencia (fotograma clave aprobado) para mantener coherencia entre escenas.
- Deja fuera del prompt texto, flechas y etiquetas: se añaden en montaje.

## 6. Comprobación final del storyboard

- [ ] Existe hoja de referencia y todas las escenas la respetan.
- [ ] Cada etapa del mapa tiene al menos una escena con su prueba visual.
- [ ] Ninguna escena es "genérica" (intercambiable con otra frase del guion).
- [ ] Los componentes ocultos se muestran con corte o transparencia.
- [ ] Dirección de movimiento y causa indicadas en cada escena con acción.
- [ ] La suma de duraciones coincide con la duración del guion y no supera 70 s.
- [ ] Todo lo importante está dentro de la zona segura vertical; subtítulos en cada escena con locución.
- [ ] Narración exacta coincide con el guion.
- [ ] El vídeo combina al menos 3 tratamientos visuales y el mecanismo central va en 3D (o se justifica por qué no).
- [ ] Cada etapa tiene un plano de mecanismo y, en conjunto, hay un plano detalle por etapa.
- [ ] Cada movimiento de cámara tiene motivo, hay uno por plano y la cámara está quieta mientras se explica un detalle fino.
- [ ] Cada escena tiene un elemento explicativo principal que aparece cuando la locución lo nombra.
- [ ] Ver [visual-language.md](visual-language.md) para el catálogo completo.
