# educational-video-chain

Skill para crear vídeos educativos narrativos **verticales (9:16) de hasta 70 segundos** para Shorts, Reels y TikTok, pensados para **todas las edades**, que explican cómo se construye, evoluciona o funciona un objeto, máquina, estructura o sistema mediante una cadena de **problemas reales y soluciones progresivas**.

El espectador parte de la versión más ingenua de una idea ("haces un agujero y lo tapas con tablas") y la acompaña hasta un sistema que funciona, aprendiendo cada concepto en el momento en que la historia lo necesita.

## Qué hace

| Fase | Resultado |
|---|---|
| 1. Encargo | Tema, audiencia, plataforma, duración, tono, alcance |
| 2. Premisa | Versión básica, objetivo final y criterio de éxito |
| 3. Investigación | Mecanismos y problemas documentados, con fuentes |
| 4. Mapa narrativo | Tabla de etapas problema → solución, tipo A/B |
| 5. Validación | Puntuación con la rúbrica y correcciones |
| 6. Guion | Español conversacional, ajustado a la duración |
| 7. Storyboard | Hoja de referencia + fichas de escena técnicamente precisas |
| 8. Producción | Inventario real de herramientas MCP y presupuesto en créditos, sin gastar |

Se detiene en el alcance pedido: *ideación* (hasta el mapa validado), *preproducción* (hasta storyboard y presupuesto) o *producción* (solo con autorización explícita de gasto).

## Estándar de formato y tono

| | |
|---|---|
| Formato | Vertical 9:16, 1080 × 1920, con subtítulos |
| Duración | Máximo 70 s (≈ 155–160 palabras) |
| Lenguaje | Sencillo, para todas las edades; 1–2 términos técnicos como mucho, explicados |
| Tono | Cercano, segunda persona, claro. Sin humor |
| Lenguaje visual | Escenas 3D para el mecanismo, ilustraciones y planos realistas, elementos explicativos (cortes, rayos X, despiece, flechas, lupa), movimientos de cámara con motivo, un plano detalle por etapa |
| Montaje | Dinámico y sin silencios: un plano cada 2–4 s, transiciones, animaciones, efectos de sonido |

Si un tema no cabe en 70 s, la skill reduce el objetivo o propone una serie de vídeos, en lugar de acelerar la locución.

## Dos patrones narrativos

- **A — Cadena de consecuencias**: la solución anterior provoca el siguiente problema.
- **B — Evolución por condiciones de uso**: el problema surge porque cambia algo (hora, clima, tiempo, uso, desgaste, personas, límites físicos).

Un buen vídeo combina ambos y nunca inventa causalidad.

## Estructura

```
educational-video-chain/
├── SKILL.md                                  Instrucciones principales y flujo
├── README.md                                 Este archivo
├── references/
│   ├── causal-progression-rubric.md          Rúbrica (12 criterios) para validar el mapa
│   ├── research-guidelines.md                Jerarquía de fuentes, etiquetas de verificación, reglas anti-drama
│   ├── storyboard-visual-accuracy.md         Hoja de referencia, ficha de escena, reglas de precisión
│   ├── visual-language.md                    Escenas 3D, ilustraciones, elementos explicativos, cámara y detalles
│   ├── production-checklist.md               Descubrimiento de herramientas, presupuesto, regla de gasto
│   ├── higgsfield-execution.md               Órdenes paso a paso a Higgsfield MCP: fichas, lotes, montaje, seguridad, registro de campo
│   └── dynamic-editing.md                    Montaje dinámico: cero silencios, ritmo, animaciones ASS, efectos de sonido
└── scripts/
    ├── montaje_dinamico.py                   Montaje completo en el sandbox de Higgsfield (plantilla probada)
    └── sfx.sh                                Efectos de sonido sintetizados con sox
```

## Instalación

**Claude Code (escritorio o terminal)**

1. Descomprime el ZIP.
2. Copia la carpeta `educational-video-chain/` en `~/.claude/skills/` (en Windows: `%USERPROFILE%\.claude\skills\`).
3. Abre una sesión nueva de Claude Code y pide, por ejemplo: «Quiero un short sobre cómo funciona un ascensor».

**Claude (claude.ai o app de escritorio)**

1. Activa las skills en *Configuración → Capacidades*.
2. Sube el archivo ZIP en la sección de skills.

## Requisitos

- **Fases 1–7** (idea, investigación, mapa narrativo, guion y storyboard): no necesitan nada más.
- **Fase 8, producción**: necesita el conector **Higgsfield MCP** con una cuenta de Higgsfield. Generar imágenes, vídeo y voz gasta **créditos de tu cuenta**. La skill presupuesta cada fase y no gasta nada sin tu autorización explícita. Un short completo costó entre 100 y 130 créditos en las pruebas (noviembre de 2026; los precios pueden cambiar).

## Ejemplos de uso

- «Quiero un short sobre cómo funciona un ascensor.»
- «Hazme el mapa narrativo de un reel sobre cómo se construye una casa en un árbol.»
- «Prepara el storyboard y el presupuesto en Higgsfield para el vídeo del submarino. No generes nada aún.»

## Garantías

- No inventa problemas, cifras ni peligros; marca simplificaciones y datos no públicos.
- No asume funciones de herramientas que no estén realmente disponibles en la sesión.
- No consume créditos sin autorización explícita; una estimación no es una autorización. Con Higgsfield, cada fase (imágenes, vídeo, voz, montaje) se autoriza por separado y se genera exactamente lo presupuestado.
