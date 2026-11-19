"""Une la narración de los 8 capítulos en un solo SRT para YouTube (subtitulos.srt) y calcula los capítulos."""
import json, re, subprocess
DUR = []; OFF = [0, 4, 4, 4, 4, 4, 4]
for i in range(7):
    DUR.append(float(re.search(r'data-duration="([\d.]+)"', open(f'cap{i}/video.html').read()).group(1)))
def ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000); return f'{h:02}:{m:02}:{s:02},{ms:03}'
out, k, base = [], 1, 0.0
for i in range(7):
    ws = json.load(open(f'cap{i}/voz.json')); ph = [[]]
    for j, w in enumerate(ws):
        cur = ph[-1]
        if cur and (len(cur) == 8 or len(' '.join(x['word'] for x in cur)) + len(w['word']) > 42 or w['start'] - ws[j - 1]['end'] > .3 or re.search(r'[.!?,:;…»]$', ws[j - 1]['word'])): ph.append([])
        ph[-1].append(w)
    for p in ph:
        a = base + OFF[i] + p[0]['start']; b = base + OFF[i] + p[-1]['end'] + .2
        out.append(f"{k}\n{ts(a)} --> {ts(b)}\n{' '.join(x['word'] for x in p)}\n"); k += 1
    base += DUR[i]
open('subtitulos.srt', 'w').write('\n'.join(out))
t = 0
for i, d in enumerate(DUR): print(f'{int(t // 60)}:{int(t % 60):02d}', i); t += d
print('total', round(t, 1))
