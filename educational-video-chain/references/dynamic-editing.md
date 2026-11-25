# Montaje dinámico, sin silencios y con efectos de sonido

Úsala en la Fase 8 (montaje). Es el **estándar de la skill**: un primer montaje con huecos entre escenas resultó lento y con silencios. No vuelvas al montaje «plano por escena con huecos» salvo que el usuario lo pida.

Implementación probada: [../scripts/montaje_dinamico.py](../scripts/montaje_dinamico.py) (montaje) y [../scripts/sfx.sh](../scripts/sfx.sh) (efectos). Ambos se ejecutan en el sandbox de Higgsfield (`sandbox_exec`), que tiene ffmpeg, sox, ImageMagick y las fuentes Montserrat y Metropolis. Montar no ha consumido créditos (saldo comprobado antes y después).

## 1. Cero silencios: la línea de tiempo la manda la voz

El primer montaje se hizo con huecos fijos de storyboard (2,2–2,3 palabras/s y la voz dentro). Quedaban silencios de 1–1,5 s, y el usuario pidió que no hubiera ninguno.

Reglas:

1. **Limpia cada audio** antes de montar:
   ```bash
   ffmpeg -i E{i}.wav -af "silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.03,areverse,\
   silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.05,areverse,\
   silenceremove=stop_periods=-1:stop_duration=0.25:stop_threshold=-42dB" -ar 48000 -ac 2 t{i}.wav
   ```
   Esto quita el silencio del principio y del final y limita las pausas internas a 0,25 s.
2. **Duración de escena = 0,05 s + voz + 0,12 s.** Los tiempos del storyboard son orientativos: en el montaje final se ajustan los planos a la voz, no al revés.
3. **El vídeo dura lo que dure la voz.** Puede quedar por debajo de lo previsto (70 → 54–56 s en el ejemplo); está bien. El máximo de 70 s sigue vigente.
4. **No alargues el final** para un efecto (aplauso, campanilla): termina justo después de la última frase, o sube el efecto para que no se perciba hueco.
5. **Verifica siempre** en el archivo final:
   ```bash
   ffmpeg -nostats -i final.mp4 -af silencedetect=n=-40dB:d=0.3 -f null - 2>&1 | grep silence_end
   ```
   El resultado debe estar vacío: ningún hueco de 0,3 s o más. Comunica al usuario el hueco más largo medido.

## 2. Ritmo visual

- **Un plano cada 2–4 s**, cortado en los **límites de frase** de la narración: reparte el tiempo de cada frase en proporción a sus caracteres dentro de la voz real de la escena.
- **Transiciones de 0,25 s** con `xfade` y variadas: `slideup`, `zoomin`, `slideleft`, `wipeup`, `smoothup`, `slideright`, `circleopen` y `fadeblack` al final. Con transiciones encadenadas, renderiza cada plano con +T s (salvo el último) y usa `offset = suma de las duraciones objetivo anteriores`. Así la duración total no cambia.
- **Imágenes fijas siempre en movimiento**: `zoompan` del 5–14 % hacia el punto que importa (por ejemplo, la cuerda gastada).
- **Temblor de cámara** (desplazamiento con seno en `crop`, ±14 px) en los impactos: peso, choque, frenazo.
- **Clips de vídeo**: ajusta su velocidad a la duración del plano (`setpts`) y haz que entren con un golpe de zoom (1,12 → 1 en 0,35 s).
- Si una escena técnica tiene dos fotogramas (antes/después), divídela en dos planos con transición; no los mantengas como un único plano largo.

## 3. Animaciones (todas en un único archivo ASS)

- **Subtítulos**: Montserrat ExtraBold 70, blancos con borde negro, 2 líneas como máximo, abajo dentro de la zona segura (`MarginV` 430). Aparecen con una pequeña escala (85 % → 100 % en 110 ms). Las **palabras clave van en amarillo**: márcalas entre llaves en el texto de la frase.
- **Rótulos** con rebote (`\fscx30 → 112 → 100` en 240 ms), en caja blanca. Hay variantes roja (alerta, «PESO») y sepia (histórico). Usa 1–3 palabras, iguales a las de la locución.
- **Flechas vectoriales** (`\p1`) con `\move`: roja para fuerza o peligro, blanca para movimiento. Indican sentido (sube/baja) durante la frase que lo dice.
- **Comprobación**: ningún rótulo ni flecha puede tapar el subtítulo (franja y ≈ 1340–1530) ni a las personas o piezas clave. En el ejemplo, «PESO» encima de la caja tapaba a las personas y una flecha pisaba el subtítulo: se movieron.

## 4. Efectos de sonido

Sintetízalos con [../scripts/sfx.sh](../scripts/sfx.sh). No cuestan créditos y no dependen de licencias.

| Evento | Efecto | Volumen relativo |
|---|---|---|
| Cada transición | whoosh (empieza 0,18 s antes del corte) | 0,55 |
| Aparece un rótulo | pop | 0,8 |
| Peso, choque, golpe | thud | 0,6–0,9 |
| Cuerda, madera | creak | 0,6–0,7 |
| Motor | motor | 0,9 |
| Metal que muerde, frenazo | screech + thud | 0,9 |
| Botón, pestillo | click | 1,0 |
| Llegada | ding | 0,8 |
| Corte de cuerda | snap | 1,0 |
| Celebración | applause (sintético y flojo: volumen 1,8) | 1,8 |

La mezcla final es: voz con `loudnorm I=-15`, efectos al 45 % y `alimiter 0.89`. La voz siempre tiene que entenderse por encima de los efectos.

Avisa al usuario de que los efectos son sintéticos y sencillos. Si quiere más calidad, ofrece un modelo de audio de efectos de la sesión, con su presupuesto aparte.

## 5. Revisión antes de entregar

- [ ] Hueco más largo < 0,3 s (con `silencedetect`).
- [ ] 8 fotogramas de control (`hstack` de 4 + 4, enviados con `image_paths`): rótulos sobre la pieza correcta, sin tapar el subtítulo.
- [ ] 1080 × 1920, 30 fps, ≤ 70 s, con audio AAC.
- [ ] Para entregar: `media_upload`, PUT desde el sandbox (HTTP 200) y `media_confirm`. Después descarga la URL a la carpeta del usuario y envíala con SendUserFile.
- [ ] Conserva las versiones anteriores (`_v2`, `_v3`…) y anota los cambios en el documento del proyecto.
