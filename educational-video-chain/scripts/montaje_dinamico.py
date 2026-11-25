"""
Montaje dinámico para shorts verticales (1080 × 1920) en el sandbox de Higgsfield.
Probado en noviembre de 2026 con el short del ascensor (v2 y v3). Coste en créditos: 0.

Qué hace:
  1. Ajusta la línea de tiempo a la VOZ: cada escena dura lo que su voz + GAP (sin silencios).
  2. Corta los planos en los límites de frase, uno cada 2-4 s.
  3. Imágenes fijas: zoom continuo (zoompan) y temblor opcional en los impactos.
     Clips: se ajustan a la duración y entran con un golpe de zoom.
  4. Une los planos con transiciones xfade de T segundos (offset = suma de duraciones objetivo).
  5. Subtítulos ASS con aparición, palabras clave {entre llaves} en amarillo,
     rótulos con rebote y flechas vectoriales animadas (\\move).
  6. Mezcla voz (loudnorm) + efectos (scripts/sfx.sh): whoosh en cada corte y efectos por evento.

Antes de usarlo:
  - Prepara la voz limpia: voz/t{i}.wav (ver recorte de silencios en references/dynamic-editing.md).
  - Rellena CHUNKS (narración por frases), SHOTS (planos), LABELS, ARROWS y FX.
  - Las posiciones (x, y) son de la esquina superior izquierda del rótulo en 1080 × 1920.
    Compruébalas con fotogramas de control: el zoom desplaza un poco las piezas.
  - Lánzalo con background:true y consulta el log en llamadas de ≤45 s (las esperas largas cortan el conector).
"""
import subprocess, os

W, H, FPS = 1080, 1920, 30
T = 0.25      # duración de cada transición
GAP = 0.12    # aire entre escenas (≤0,15 s: el usuario no quiere silencios)
LEAD = 0.05   # la voz entra 0,05 s después del inicio de la escena
VOZ = "voz/t{i}.wav"
SFX = "sfx/{n}.wav"
OUT = "out/short.mp4"
FONTDIR = "/usr/share/fonts/truetype/higgsfield"   # Montserrat ExtraBold, Metropolis

# ---------------------------------------------------------------- contenido (EJEMPLO: ascensor)
CHUNKS = {
 1: ["Quieres subir cinco pisos sin escaleras.", "Cuelgas una caja de una cuerda y tiras."],
 2: ["Pero con gente dentro, pesa demasiado."],
 3: ["Así que cuelgas un bloque pesado al otro lado:", "el {contrapeso}.", "Cuando la caja sube, él baja.",
     "Ahora basta un {motor} pequeño arriba."],
 # ...
}

def run(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2500:]); raise SystemExit(c)

def dur(p):
    return float(subprocess.check_output(
        f"ffprobe -v error -show_entries format=duration -of csv=p=0 {p}", shell=True))

clean = lambda s: s.replace("{", "").replace("}", "")
N = len(CHUNKS)
vd = {i: dur(VOZ.format(i=i)) for i in CHUNKS}

# Línea de tiempo guiada por la voz
S, D, t = {}, {}, 0.0
for i in sorted(CHUNKS):
    S[i] = t; D[i] = LEAD + vd[i] + GAP; t += D[i]
TOTAL = sum(D.values())

# Reparto de cada frase según su número de caracteres
ct = {}
for i, cs in CHUNKS.items():
    tot = sum(len(clean(c)) for c in cs); x = S[i] + LEAD; ct[i] = []
    for c in cs:
        d = vd[i] * len(clean(c)) / tot; ct[i].append((x, x + d)); x += d
def at(i, k):  # inicio de la frase k relativo al inicio de la escena i
    return ct[i][k][0] - S[i]
end = lambda i: S[i] + D[i]

# ---------------------------------------------------------------- planos (EJEMPLO)
SHOTS = []
def still(img, d, zoom=0.06, zx=0.5, zy=0.5, shake=None):
    SHOTS.append(("img", img, d, zoom, zx, zy, shake))
def clip(src, d):
    SHOTS.append(("clip", src, d))
clip("v/E1.mp4", D[1])
still("f/2a.png", D[2], 0.05, 0.35, 0.55, shake=(0.25, 0.9))
b = at(3, 2); still("f/3a.png", b, 0.07, 0.6, 0.45); still("f/3b.png", D[3] - b, 0.05, 0.5, 0.4)
# ... la suma de duraciones de los planos debe ser igual a TOTAL

TRANS = ["slideup", "zoomin", "slideleft", "wipeup", "smoothup", "slideright", "circleopen", "fadeblack"]

# ---------------------------------------------------------------- render de planos
os.makedirs("tmp", exist_ok=True); os.makedirs("out", exist_ok=True)
files = []
for k, s in enumerate(SHOTS):
    d = s[2] + (T if k < len(SHOTS) - 1 else 0); n = int(round(d * FPS)); out = f"tmp/p{k:02d}.mp4"
    if s[0] == "img":
        _, img, _, zoom, zx, zy, shake = s
        zp = (f"scale={int(W*1.2)}:-2,zoompan=z='1+{zoom}*on/{n}':x='iw*{zx}-(iw/zoom/2)':"
              f"y='ih*{zy}-(ih/zoom/2)':d={n}:s={int(W*1.04)}x{int(H*1.04)}:fps={FPS}")
        if shake:
            a, bb = shake
            cx = f"(iw-{W})/2+if(between(t,{a},{bb}),14*sin(t*55),0)"
            cy = f"(ih-{H})/2+if(between(t,{a},{bb}),10*cos(t*47),0)"
        else:
            cx, cy = f"(iw-{W})/2", f"(ih-{H})/2"
        run(f"ffmpeg -y -loop 1 -i {img} -vf \"{zp},crop={W}:{H}:'{cx}':'{cy}',format=yuv420p\" "
            f"-frames:v {n} -c:v libx264 -preset veryfast -crf 18 {out}")
    else:
        src = s[1]; f = d / dur(src)
        vf = (f"setpts={f:.4f}*PTS,fps={FPS},scale={W}:-2,crop={W}:{H},"
              f"scale=w='{W}*(1+0.12*max(0,1-t/0.35))':h=-2:eval=frame,crop={W}:{H},format=yuv420p")
        run(f"ffmpeg -y -i {src} -an -vf \"{vf}\" -frames:v {n} -c:v libx264 -preset veryfast -crf 18 {out}")
    files.append(out)

ins = " ".join(f"-i {f}" for f in files); fc = []; last = "[0:v]"; acc = 0
for k in range(1, len(files)):
    acc += SHOTS[k-1][2]
    fc.append(f"{last}[{k}:v]xfade=transition={TRANS[(k-1)%len(TRANS)]}:duration={T}:offset={acc:.3f}[x{k}]")
    last = f"[x{k}]"
run(f"ffmpeg -y {ins} -filter_complex \"{';'.join(fc)}\" -map {last} -c:v libx264 -preset veryfast "
    f"-crf 18 -pix_fmt yuv420p tmp/video.mp4")
cuts, acc = [], 0
for s in SHOTS[:-1]:
    acc += s[2]; cuts.append(acc)

# ---------------------------------------------------------------- audio
FX = [("whoosh", c - 0.18, 0.55) for c in cuts]
FX += [("creak", S[1] + 1.6, 0.6), ("thud", S[2] + 0.25, 0.9), ("pop", S[3] + at(3, 1), 0.8)]  # EJEMPLO
FX = [f for f in FX if f[1] >= 0]

parts = [f"[{j}]adelay={int((S[i]+LEAD)*1000)}|{int((S[i]+LEAD)*1000)}[v{j}]" for j, i in enumerate(sorted(CHUNKS))]
run(f"ffmpeg -y {' '.join('-i '+VOZ.format(i=i) for i in sorted(CHUNKS))} -filter_complex "
    f"\"{';'.join(parts)};{''.join(f'[v{j}]' for j in range(N))}amix=inputs={N}:normalize=0,apad,"
    f"atrim=0:{TOTAL:.3f},loudnorm=I=-15:TP=-2[o]\" -map [o] -ar 48000 -ac 2 tmp/voz.wav")
parts = [f"[{j}]volume={v},adelay={int(tt*1000)}|{int(tt*1000)}[f{j}]" for j, (n, tt, v) in enumerate(FX)]
run(f"ffmpeg -y {' '.join('-i '+SFX.format(n=n) for n,_,_ in FX)} -filter_complex "
    f"\"{';'.join(parts)};{''.join(f'[f{j}]' for j in range(len(FX)))}amix=inputs={len(FX)}:normalize=0,"
    f"apad,atrim=0:{TOTAL:.3f}[o]\" -map [o] -ar 48000 -ac 2 tmp/sfx.wav")
run("ffmpeg -y -i tmp/voz.wav -i tmp/sfx.wav -filter_complex "
    "\"[1]volume=0.45[s];[0][s]amix=inputs=2:normalize=0,alimiter=limit=0.89[o]\" -map [o] -ar 48000 tmp/mix.wav")

# ---------------------------------------------------------------- ASS: subtítulos, rótulos y flechas
def ts(x):
    x = max(0, x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
YEL, WHT = "{\\c&H00D7FF&}", "{\\c&HFFFFFF&}"
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
"[V4+ Styles]",
"Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
# Subtítulo: blanco con borde negro, abajo dentro de la zona segura (MarginV 430 → y ≈ 1340-1530)
"Style: Sub,Montserrat ExtraBold,70,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,1,0,0,0,100,100,0,0,1,7,3,2,90,150,430,1",
# Rótulo: texto oscuro sobre caja blanca
"Style: Lab,Montserrat ExtraBold,54,&H003A2A1E,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,1,0,0,0,100,100,0,0,3,14,0,5,0,0,0,1",
# Rótulo de alerta: blanco sobre rojo
"Style: Red,Montserrat ExtraBold,58,&H00FFFFFF,&H00FFFFFF,&H003D26D7,&H003D26D7,1,0,0,0,100,100,0,0,3,14,0,5,0,0,0,1",
# Rótulo histórico: crema sobre marrón
"Style: Sep,Montserrat ExtraBold,52,&H00C8E6F4,&H00FFFFFF,&H001A2A3B,&H001A2A3B,1,0,0,0,100,100,0,0,3,14,0,5,0,0,0,1",
"Style: Arr,Arial,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,4,0,7,0,0,0,1", "",
"[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
POP = "{\\fscx30\\fscy30\\t(0,140,\\fscx112\\fscy112)\\t(140,240,\\fscx100\\fscy100)}"
for i, cs in CHUNKS.items():
    for k, c in enumerate(cs):
        a, b = ct[i][k]; txt = c.replace("{", YEL).replace("}", WHT)
        ass.append(f"Dialogue: 0,{ts(a)},{ts(b+0.05)},Sub,,0,0,0,,{{\\fscx85\\fscy85\\t(0,110,\\fscx100\\fscy100)}}{txt}")
def lab(style, text, x, y, a, b, size=54):
    cx = x + 0.31*size*len(text) + 16; cy = y + size/2 + 16
    ass.append(f"Dialogue: 1,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos({cx:.0f},{cy:.0f})\\fad(0,120)}}{POP}{text}")
DOWN = "m 0 0 l 44 0 l 44 70 l 80 70 l 22 140 l -36 70 l 0 70"
UP = "m 22 0 l 80 70 l 44 70 l 44 140 l 0 140 l 0 70 l -36 70"
def arrow(shape, x1, y1, x2, y2, a, b, col="&H3D26D7&"):   # rojo por defecto; "&HFFFFFF&" = blanco
    ass.append(f"Dialogue: 2,{ts(a)},{ts(b)},Arr,,0,0,0,,{{\\an7\\move({x1},{y1},{x2},{y2})\\1c{col}"
               f"\\3c&H000000&\\bord4\\fad(80,80)\\p1}}{shape}{{\\p0}}")
# EJEMPLO
lab("Red", "PESO", 515, 1180, S[2] + 0.2, end(2)); arrow(DOWN, 720, 1060, 720, 1120, S[2] + 0.25, end(2))
lab("Lab", "contrapeso", 470, 600, S[3] + at(3, 1), S[3] + at(3, 2))
open("tmp/subs.ass", "w").write("\n".join(ass) + "\n")

run(f"ffmpeg -y -i tmp/video.mp4 -i tmp/mix.wav -vf \"ass=tmp/subs.ass:fontsdir={FONTDIR}\" -map 0:v -map 1:a "
    f"-c:v libx264 -preset medium -crf 19 -r 30 -c:a aac -b:a 192k -t {TOTAL:.3f} -movflags +faststart {OUT}")
print("TOTAL", round(TOTAL, 2), "final", dur(OUT))
print("escenas", {i: (round(S[i], 2), round(D[i], 2)) for i in S})
# Comprobación obligatoria de silencios: no debe salir ningún hueco ≥ 0,3 s
r = subprocess.run(f"ffmpeg -nostats -i {OUT} -af silencedetect=n=-40dB:d=0.3 -f null -",
                   shell=True, capture_output=True, text=True)
print("huecos >= 0,3 s:", r.stderr.count("silence_end"))
