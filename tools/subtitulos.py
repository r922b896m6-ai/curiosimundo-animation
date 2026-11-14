"""Genera subtítulos sincronizados a partir de la narración IA.

Entrada (en la carpeta del vídeo):
  guion.txt  líneas "rate|pitch|pausa|texto"; cada línea de narración es una ESCENA
  voz.json   tiempos por palabra creados por tools/tts_seg.py

Salida:
  subtitulos.srt   subtítulos por frases cortas (máx. 3 palabras / 17 caracteres), listos para CapCut o TikTok
  escenas.md       tabla por escena: tiempo de inicio y fin, narración y subtítulos con su tiempo

uso: python3 tools/subtitulos.py produccion/01-pulpo
"""
import json, re, sys, pathlib

d = pathlib.Path(sys.argv[1])
words = json.load(open(d / 'voz.json'))
lines = [l.rstrip('\n').split('|', 3)[3] for l in open(d / 'guion.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
norm = lambda s: re.sub(r'[^\wáéíóúüñ]', '', s.lower())

# assign words to scenes (one scene per script line)
scenes, i = [], 0
for n, text in enumerate(lines, 1):
    k = len([t for t in text.split() if norm(t)])
    scenes.append({'n': n, 'text': text, 'words': words[i:i + k]}); i += k
assert i == len(words), 'el guion y voz.json no coinciden: vuelve a generar la voz'

def phrases(ws):
    out = [[]]
    for j, w in enumerate(ws):
        cur = out[-1]
        if cur:
            prev = ws[j - 1]
            if (len(cur) == 3 or len(' '.join(x['word'] for x in cur)) + len(w['word']) > 17
                    or w['start'] - prev['end'] > .28 or re.search(r'[.!?,:;…»]$', prev['word']) or w['word'][0] in '¿¡«'):
                out.append([])
        out[-1].append(w)
    return [p for p in out if p]

def ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'

allp = [p for sc in scenes for p in phrases(sc['words'])]
nxt = {id(p): (allp[k + 1][0]['start'] if k + 1 < len(allp) else 1e9) for k, p in enumerate(allp)}
srt, md, idx = [], ['| Escena | Tiempo | Narración | Subtítulos |', '|---|---|---|---|'], 1
for sc in scenes:
    ps = [p for p in allp if p[0] in sc['words']]; chunks = []
    for p in ps:
        a, b = p[0]['start'], min(p[-1]['end'] + .15, nxt[id(p)] - .02)
        txt = ' '.join(x['word'] for x in p)
        srt.append(f'{idx}\n{ts(a)} --> {ts(b)}\n{txt}\n'); idx += 1
        chunks.append(f'`{a:.1f}s` {txt}')
    t0, t1 = sc['words'][0]['start'], sc['words'][-1]['end']
    md.append(f"| {sc['n']} | {t0:.1f}–{t1:.1f} s | {sc['text']} | {'<br>'.join(chunks)} |")

(d / 'subtitulos.srt').write_text('\n'.join(srt), encoding='utf-8')
(d / 'escenas.md').write_text('# Escenas con tiempos y subtítulos (generado)\n\n' + '\n'.join(md) + '\n', encoding='utf-8')
print(f'{len(scenes)} escenas, {idx - 1} subtítulos, {words[-1]["end"]:.1f} s de narración')
