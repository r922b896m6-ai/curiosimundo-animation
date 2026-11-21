"""Generador de cortos verticales de CURIOSIMUNDO (1080×1920, givemotion), con escenas 16:9 en una banda central.
Títulos arriba (T), subtítulos palabra a palabra abajo, tarjeta final con la portada del vídeo largo.
En el JS: W('palabra', n), S.id (inicio de escena), D (duración); band(z) da un <svg> 1920×1080 dentro de la banda.
"""
import json, os, re, subprocess
def norm(s): return re.sub(r'[^\w]', '', s.lower())

def corto(d, title, libs, scenes, titles, js, promo_word, promo_title, music, tail=1.4, hits=(), final=None):
    d = d.rstrip('/') + '/'
    words = json.load(open(d + 'voz.json'))
    def W(w, k=1):
        c = 0
        for x in words:
            if norm(x['word']) == norm(w):
                c += 1
                if c == k: return x['start']
        raise KeyError(f'{d}: palabra no encontrada {w} #{k}')
    A = lambda a: a if isinstance(a, (int, float)) else (W(*a) if isinstance(a, tuple) else W(a))
    dur = round(words[-1]['end'] + tail, 2)
    st = [(sid, round(0 if i == 0 else A(a) - .3, 2)) for i, (sid, a) in enumerate(scenes)] + [('promo', round(A(promo_word) - .3, 2))]
    for i in range(1, len(st)):
        assert st[i][1] > st[i - 1][1] + .5, f'escena {st[i][0]} fuera de orden'
    secs = '\n'.join(f'<section class="scene" id="{sid}" data-start="{t}" data-duration="{round((st[i + 1][1] + .1 if i + 1 < len(st) else dur) - t, 2)}"></section>' for i, (sid, t) in enumerate(st))
    S = '{' + ', '.join(f'{sid}: {t}' for sid, t in st) + '}'
    T = '[' + ', '.join(f"[{round(A(a) - .15, 2) if a != 0 else 0}, '{h}']" for a, h in titles) + f", [{st[-1][1]}, '']]"
    html = f'''<!doctype html>
<!-- {title} (TikTok, 9:16, {dur} s). Dato con número en el fotograma 0. -->
<html data-width="1080" data-height="1920" data-fps="30" data-duration="{dur}" data-safe-zone="reels">
<head><link rel="stylesheet" href="lib/cm.css"><script src="lib/cm.js"></script>{''.join(f'<script src="lib/{l}"></script>' for l in libs)}
<style>
  body {{ background: radial-gradient(1200px 1400px at 50% 40%, #1565C0, #0B2A5B 75%); }}
  .ttl {{ position:absolute; left:40px; right:40px; top:250px; height:290px; display:flex; align-items:center; justify-content:center; text-align:center; z-index:5;
         font: 400 118px/.92 'Bebas Neue'; text-shadow: 0 10px 40px rgb(0 0 0 / .6); opacity:0; }}
  .ttl em {{ font-style:normal; color:#FFD23F; }}
  #frame {{ position:absolute; left:0; top:556px; width:1080px; height:616px; border-top:4px solid #FFD23F; border-bottom:4px solid #FFD23F; z-index:3; pointer-events:none; }}
  #vcaps {{ position:absolute; inset:0; z-index:8; pointer-events:none; }}
  .vc {{ position:absolute; left:50px; right:50px; top:1240px; text-align:center; isolation:isolate; font: 850 86px/1.1 Inter; letter-spacing:-.02em; }}
  .vc .w {{ display:inline-block; padding:0 .14em; --hl:0; position:relative; color: color-mix(in oklab, #0B2A5B calc(var(--hl) * 100%), #fff);
           text-shadow: 0 5px 0 rgb(0 10 40 / calc(.7 - var(--hl) * .7)), 0 8px 30px rgb(0 0 0 / calc(.5 - var(--hl) * .5)); }}
  .vc .pl {{ position:absolute; left:0; top:.02em; height:1.08em; border-radius:.22em; z-index:-1; background:#FFD23F; }}
  #promo {{ z-index: 6; }}
</style></head>
<body>
<audio src="voz.mp3"></audio>
<audio src="musica.mp3" data-volume="0.5" data-duck="0.45" data-fade-out="1"></audio>
<audio src="sfx.mp3" data-volume="0.6"></audio>
{secs}
<div id="frame"></div><div id="titles"></div><div id="vcaps"></div>
<script>
const D = {dur}, S = {S};
gm.wait(fetch('voz.json').then(r => r.json()).then(words => {{
  const W = CM.W(words, 0), G = {{ global: true }}, tl = gm.timeline(null, G), $ = id => document.getElementById(id), mk = CM.mk;
  const sv = (id, bg) => {{ const s = mk('svg', {{ viewBox: '0 0 1080 1920', width: 1080, height: 1920, style: 'position:absolute;inset:0' }}, $(id)); CM.defs(s); if (bg) $(id).style.background = bg; return s; }};
  const band = (z, y = 560) => mk('svg', {{ x: 0, y, width: 1080, height: 608, viewBox: '0 0 1920 1080', preserveAspectRatio: 'xMidYMid slice' }}, z);
  const scene = (id, bg) => {{ const z = sv(id, bg || 'radial-gradient(1200px 1400px at 50% 40%, #1565C0, #0B2A5B 75%)'); return band(z); }};
  const shake = (el, at, a = 14) => tl.to(el, {{ x: a, duration: .06 }}, at).to(el, {{ x: -a, duration: .08 }}, at + .06).to(el, {{ x: 0, duration: .1 }}, at + .14);
  const T = {T};
  T.forEach(([at, html], i) => {{ const h = Object.assign(document.createElement('div'), {{ className: 'ttl', innerHTML: '<div>' + html + '</div>' }}); $('titles').append(h); if (!html) return;
    const end = T[i + 1] ? T[i + 1][0] : 99;
    if (at === 0) {{ h.style.opacity = 1; tl.fromTo(h, {{ scale: 1.15 }}, {{ scale: 1, duration: .5, ease: 'expo.out' }}, 0); }}
    else tl.fromTo(h, {{ opacity: 0, y: 90, scale: 1.2, filter: 'blur(10px)' }}, {{ opacity: 1, y: 0, scale: 1, filter: 'blur(0px)', duration: .3, ease: 'expo.out' }}, at);
    tl.to(h, {{ opacity: 0, y: -80, duration: .18, ease: 'power2.in' }}, end - .18); }});
  Object.keys(S).slice(1).forEach(id => tl.from($(id), {{ opacity: 0, duration: .2 }}, S[id]));
{js}
  /* promo */
  const pr = $('promo'); pr.style.background = 'radial-gradient(1200px 1400px at 50% 40%, #1d2a5a, #050a1a 75%)';
  pr.innerHTML = `<div style="position:absolute;left:0;right:0;top:250px;text-align:center;font:400 104px/.95 'Bebas Neue'">{promo_title}</div>
    <div id="card" style="position:absolute;left:90px;width:900px;top:560px;height:506px;border-radius:26px;overflow:hidden;box-shadow:0 30px 80px rgb(0 0 0 / .6);border:6px solid #fff">
      <img src="portada-youtube.png" style="width:100%;height:100%;object-fit:cover"><div style="position:absolute;left:50%;top:50%;width:170px;height:120px;margin:-60px 0 0 -85px;background:#E5484D;border-radius:30px"></div>
      <div style="position:absolute;left:50%;top:50%;margin:-32px 0 0 -18px;border-left:62px solid #fff;border-top:34px solid transparent;border-bottom:34px solid transparent"></div></div>`;
  tl.from(pr.children[0], {{ y: 60, opacity: 0, duration: .4, ease: 'expo.out' }}, S.promo + .1).from('#card', {{ scale: .6, opacity: 0, duration: .5, ease: 'back.out(1.6)' }}, S.promo + .3)
    .to('#card', {{ scale: 1.04, duration: .5, ease: 'sine.inOut', yoyo: true, repeat: 6 }}, S.promo + 1);
  {{FINAL}}
  /* subtítulos verticales palabra a palabra */
  const ws = words.map(w => ({{ text: w.word, start: w.start, end: w.end }})), ph = [[]];
  ws.forEach((w, i) => {{ const cur = ph.at(-1), prev = ws[i - 1];
    if (cur.length && (cur.length === 3 || cur.map(x => x.text).join(' ').length + w.text.length > 16 || w.start - prev.end > .28 || /[.!?,:…]$/.test(prev.text) || /^¿/.test(w.text))) ph.push([]);
    ph.at(-1).push(w); }});
  const ct = gm.timeline(null, G), els = ph.map(p => {{ const el = document.createElement('div'); el.className = 'vc'; el.innerHTML = '<i class="pl"></i>' + p.map(w => `<span class="w">${{w.text}}</span>`).join(' '); $('vcaps').append(el); return el; }});
  return document.fonts.ready.then(() => ph.forEach((p, k) => {{
    const el = els[k], sp = el.querySelectorAll('.w'), pl = el.querySelector('.pl'), nx = ph[k + 1], bx = i => ({{ x: sp[i].offsetLeft, width: sp[i].offsetWidth }});
    ct.fromTo(pl, {{ ...bx(0), scale: .5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: .16, ease: 'back.out(2)' }}, p[0].start - .04);
    p.forEach((w, i) => {{ ct.fromTo(sp[i], {{ opacity: 0, y: 40, scale: .6 }}, {{ opacity: 1, y: 0, scale: 1, duration: .22, ease: 'back.out(2.4)' }}, w.start - .06);
      if (i) ct.to(pl, {{ ...bx(i), duration: .1, ease: 'power3.out' }}, w.start - .08);
      ct.to(sp[i], {{ '--hl': 1, duration: .05 }}, w.start - .03).to(sp[i], {{ '--hl': 0, duration: .05 }}, p[i + 1] ? p[i + 1].start - .08 : Math.min(w.end + .3, nx ? nx[0].start - .2 : 99)); }});
    ct.to(el, {{ opacity: 0, duration: .12 }}, nx ? nx[0].start - .18 : p.at(-1).end + .7);
  }}));
}}));
</script>
</body>
</html>
'''
    fin = ''
    if final:
        fa = round(A(final[0]) - .3, 2)
        fin = f"const fq = document.createElement('div'); fq.style.cssText = \"position:absolute;left:0;right:0;top:250px;text-align:center;font:400 104px/.95 'Bebas Neue'\"; fq.innerHTML = '{final[1]}'; pr.append(fq); tl.to(pr.children[0], {{ opacity: 0, y: -40, duration: .2 }}, {fa}).from(fq, {{ opacity: 0, scale: 1.3, duration: .35, ease: 'expo.out' }}, {fa + .1});"
    html = html.replace('{FINAL}', fin)
    open(d + 'video.html', 'w').write(html)
    secm = [[round(a if isinstance(a, (int, float)) else A(a), 2), round(b if isinstance(b, (int, float)) else A(b), 2), k] for a, b, k in music]
    secm[-1][1] = dur
    au = {'dur': dur, 'sec': secm, 'hits': [round(A(h) - .05, 2) for h in hits] + [0.0]}
    new = json.dumps(au)
    if not os.path.exists(d + 'musica.mp3') or not os.path.exists(d + 'audio.json') or open(d + 'audio.json').read() != new:
        open(d + 'audio.json', 'w').write(new)
        root = os.path.dirname(os.path.abspath(__file__))
        subprocess.run(['python3', root + '/musica_historia.py', d], check=True, capture_output=True)
        for k in ('musica', 'sfx'):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', d + k + '.wav', '-b:a', '192k', d + k + '.mp3'], check=True); os.remove(d + k + '.wav')
    print(d, dur)
