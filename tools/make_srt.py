"""SRT completo de un vídeo largo (capítulos capN + pantalla final) y tiempos de los capítulos. uso: python3 tools/make_srt.py youtube/venus"""
import json, re, sys, glob, os
D = sys.argv[1].rstrip('/') + '/'
caps = sorted(glob.glob(D + 'cap*/video.html'), key=lambda p: int(re.search(r'cap(\d+)', p).group(1)))
def ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000); return f'{h:02}:{m:02}:{s:02},{ms:03}'
out, k, base = [], 1, 0.0
for p in caps:
    html = open(p).read(); dur = float(re.search(r'data-duration="([\d.]+)"', html).group(1)); off = float(re.search(r'const OFF = ([\d.]+)', html).group(1))
    ws = json.load(open(os.path.dirname(p) + '/voz.json')); ph = [[]]
    for j, w in enumerate(ws):
        cur = ph[-1]
        if cur and (len(cur) == 8 or len(' '.join(x['word'] for x in cur)) + len(w['word']) > 42 or w['start'] - ws[j - 1]['end'] > .3 or re.search(r'[.!?,:;…»]$', ws[j - 1]['word'])): ph.append([])
        ph[-1].append(w)
    for q in ph:
        out.append(f"{k}\n{ts(base + off + q[0]['start'])} --> {ts(base + off + q[-1]['end'] + .2)}\n{' '.join(x['word'] for x in q)}\n"); k += 1
    print(f'{int(base // 60)}:{int(base % 60):02d}', os.path.basename(os.path.dirname(p))); base += dur
open(D + 'subtitulos.srt', 'w').write('\n'.join(out)); print('total', round(base, 1), '+ pantalla final 20 s')
