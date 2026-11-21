"""Generador de capítulos para vídeos largos de CURIOSIMUNDO (16:9, givemotion).

Cada capítulo: capN/guion.txt + voz.json (tools/producir.sh) → capN/video.html, audio.json, musica.mp3, sfx.mp3.
Las escenas se anclan a palabras de la narración: ('id', 'palabra') o ('id', ('palabra', n)) o ('id', segundos).
En el JS: W('palabra', n) da el segundo en el vídeo, S.id el inicio de la escena, D la duración del capítulo.
"""
import json, os, re, subprocess, unicodedata

def norm(s): return re.sub(r'[^\w]', '', s.lower())

class Project:
    def __init__(self, d, title, libs, common='', music=True):
        self.d, self.title, self.libs, self.common = d.rstrip('/') + '/', title, libs, common

    def page(self, n, desc, scenes, js, off=4, tail=1.6, card=None, mood='tension', hits=(), extra_audio=None, last_mood=None):
        cd = f'{self.d}cap{n}/'
        words = json.load(open(cd + 'voz.json'))
        def W(w, k=1):
            c = 0
            for x in words:
                if norm(x['word']) == norm(w):
                    c += 1
                    if c == k: return x['start'] + off
            raise KeyError(f'cap{n}: palabra no encontrada {w} #{k}')
        dur = round(off + words[-1]['end'] + tail, 2)
        st = []
        for i, (sid, a) in enumerate(scenes):
            if i == 0: t = max(0, off - .4)
            elif isinstance(a, (int, float)): t = a
            elif isinstance(a, tuple): t = W(*a) - .35
            else: t = W(a) - .35
            if st and t <= st[-1][1] + .5: raise ValueError(f'cap{n}: la escena {sid} ({t:.2f}) no va después de {st[-1][0]} ({st[-1][1]})')
            st.append((sid, round(t, 2)))
        secs = []
        for i, (sid, t) in enumerate(st):
            e = st[i + 1][1] + .1 if i + 1 < len(st) else dur
            secs.append(f'<section class="scene" id="{sid}" data-start="{t}" data-duration="{round(e - t, 2)}"></section>')
        S = '{' + ', '.join(f'{sid}: {t}' for sid, t in st) + '}'
        cardjs = f"CM.card($('cards'), tl, {card[0]}, '{card[1]}', '{card[2]}', 0, {off});" if card else ''
        libs = ''.join(f'<script src="lib/{l}"></script>' for l in self.libs)
        html = f'''<!doctype html>
<!-- {self.title} · Capítulo {n} · {desc} -->
<html data-width="1920" data-height="1080" data-fps="30" data-duration="{dur}">
<head><link rel="stylesheet" href="lib/cm.css"><script src="lib/cm.js"></script>{libs}</head>
<body>
<audio src="voz.mp3" data-start="{off}"></audio>
<audio src="musica.mp3" data-volume="0.5" data-duck="0.4" data-fade-out="1"></audio>
<audio src="sfx.mp3" data-volume="0.55"></audio>
{chr(10).join(secs)}
<div class="vig"></div><div id="heads"></div><div id="cards"></div><div id="caps"></div>
<script>
const OFF = {off}, D = {dur}, S = {S};
gm.wait(fetch('voz.json').then(r => r.json()).then(words => {{
  const W = CM.W(words, OFF), G = {{ global: true }}, tl = gm.timeline(null, G), H = document.getElementById('heads'), $ = id => document.getElementById(id), mk = CM.mk;
{self.common}
  {cardjs}
{js}
  return CM.captions(words, OFF);
}}));
</script>
</body>
</html>
'''
        open(cd + 'video.html', 'w').write(html)
        sec = ([[0, off, 'card']] if card else []) + [[off if card else 0, dur, mood]]
        if last_mood:
            sec[-1][1] = round(dur - 6, 2); sec.append([round(dur - 6, 2), dur, last_mood])
        A = {'dur': dur, 'sec': sec, 'hits': [round(W(*((h,) if isinstance(h, str) else h)) - .05, 2) for h in hits]}
        if extra_audio: A.update(extra_audio(W))
        A['sec'] = [[a, min(b, dur), k] for a, b, k in A['sec'] if a < dur]
        new = json.dumps(A)
        if not os.path.exists(cd + 'musica.mp3') or open(cd + 'audio.json').read() != new if os.path.exists(cd + 'audio.json') else True:
            open(cd + 'audio.json', 'w').write(new)
            root = os.path.dirname(os.path.abspath(__file__))
            subprocess.run(['python3', root + '/musica_historia.py', cd], check=True, capture_output=True)
            for k in ('musica', 'sfx'):
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', cd + k + '.wav', '-b:a', '192k', cd + k + '.mp3'], check=True); os.remove(cd + k + '.wav')
        print(f'cap{n}', dur)
        return dur
