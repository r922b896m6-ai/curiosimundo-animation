#!/usr/bin/env bash
# Flujo reutilizable CURIOSIMUNDO: guion.txt → narración IA (voz.mp3 + tiempos) → subtítulos (SRT + escenas.md)
# uso: tools/producir.sh produccion/01-pulpo [voz]
#   voz por defecto: es-MX-JorgeNeural (otras: es-MX-DaliaNeural, es-ES-AlvaroNeural, es-US-AlonsoNeural)
set -euo pipefail
DIR="${1:?indica la carpeta del vídeo, p. ej. produccion/01-pulpo}"
VOICE="${2:-es-MX-JorgeNeural}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 -c "import edge_tts" 2>/dev/null || pip install -q edge-tts
cd "$DIR"
python3 "$ROOT/tools/tts_seg.py" guion.txt "$VOICE" voz
rm -rf voz_parts
python3 "$ROOT/tools/subtitulos.py" .
echo "listo: $DIR/voz.mp3, voz.json, subtitulos.srt, escenas.md"
