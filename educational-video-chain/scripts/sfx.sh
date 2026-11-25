#!/usr/bin/env bash
# Efectos de sonido sintetizados con sox (sin coste de créditos).
# Uso en el sandbox de Higgsfield: bash sfx.sh <carpeta_destino>
# Probado en noviembre de 2026. Cada comando va por separado: si uno falla, los demás se crean igual.
set -u
D="${1:-sfx}"; mkdir -p "$D"; cd "$D"
R="-r 48000 -c 2"
sox -n $R whoosh.wav  synth 0.45 pinknoise fade q 0.15 0.45 0.25 sinc 300-3500 gain -6          # transiciones
sox -n $R pop.wav     synth 0.09 sine 900:300 fade 0 0.09 0.06 gain -8                          # aparición de rótulos
sox -n $R click.wav   synth 0.03 square 2200 fade 0 0.03 0.025 gain -14                         # botón, pestillo
sox -n $R thud.wav    synth 0.35 sine 70:40 fade 0 0.35 0.3 gain -3                             # golpe, peso, choque
sox -n $R screech.wav synth 0.6 sawtooth 2400:1800 tremolo 40 60 sinc 1500-6000 fade 0.02 0.6 0.25 gain -18  # metal que muerde
sox -n $R creak.wav   synth 0.8 brownnoise tremolo 9 60 sinc 200-1500 fade 0.05 0.8 0.3 gain -10  # cuerda, madera
sox -n $R motor.wav   synth 1.6 sawtooth 110 lowpass 900 tremolo 25 20 fade 0.2 1.6 0.4 gain -20  # zumbido de motor
sox -n $R d1.wav synth 0.5 sine 1318 fade 0 0.5 0.45 gain -12
sox -n $R d2.wav synth 0.7 sine 1046 fade 0 0.7 0.65 gain -12
sox d1.wav d2.wav ding.wav && rm -f d1.wav d2.wav                                                # llegada
sox -n $R snap.wav    synth 0.12 whitenoise sinc 1000-8000 fade 0 0.12 0.1 gain -6              # corte seco
# Aplauso: ráfagas cortas de ruido mezcladas. Suena flojo: súbelo (volumen ~1,8) o termina el vídeo justo después.
# Los temporales llevan el prefijo "tmpclap_": no uses "c*.wav", que borraría click.wav y creak.wav.
for i in $(seq 1 25); do sox -n $R tmpclap_$i.wav synth 0.03 whitenoise sinc 800-6000 fade 0 0.03 0.02 gain -$((14+RANDOM%8)) pad 0.$((RANDOM%9))$((RANDOM%9)) 0; done
sox -m tmpclap_*.wav tmpclap_mix.wav && sox tmpclap_mix.wav tmpclap_mix.wav tmpclap_mix.wav tmpclap_mix.wav applause.wav && rm -f tmpclap_*.wav
for f in *.wav; do printf "%s %s\n" "$f" "$(soxi -D "$f")"; done
