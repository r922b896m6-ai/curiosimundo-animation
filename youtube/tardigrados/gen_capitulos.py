D='/home/user/curiosimundo-animation/youtube/tardigrados/'
COMMON = r'''
  const svgOf = (id, bg) => { const s = CM.svgIn($(id)); if (bg) $(id).style.background = bg; return s; };
  const fadeIn = ids => ids.forEach(id => tl.from($(id), { opacity: 0, duration: .3 }, +$(id).dataset.start));
  const big = (id, html, top, at, extra = '', end) => { const t = CM.text($(id), 'big', html, top, extra); tl.from(t, { scale: 1.3, opacity: 0, duration: .4, ease: 'expo.out' }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; };
  const mid = (id, html, top, at, extra = '', end) => { const t = CM.text($(id), 'mid', html, top, extra); tl.from(t, { y: 20, opacity: 0, duration: .35 }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; };
  /* walking bear in a wrapper (safe for tweens) */
  const bearAt = (s, x, y, sc = 1, dir = 1, walk = 0, opts = {}) => { const w = mk('g', {}, s), b = TD.bear(w, opts); b.g.setAttribute('transform', `translate(${x} ${y}) scale(${sc * dir} ${sc})`); return { w, b, x, y, sc, dir, walk }; };
  const walkers = (sec, list, t0) => gm.onFrame($(sec), (l, info) => list.forEach(o => { const t = info.time; o.b.setWalk(t, o.walk ? 1 : .25); if (o.walk) o.b.g.setAttribute('transform', `translate(${o.x + o.dir * (t - t0) * o.walk} ${o.y}) scale(${o.sc * o.dir} ${o.sc})`); }));
  const thermo = (s, x, y, h = 600) => { const g = mk('g', {}, s); mk('rect', { x: x - 40, y: y - h, width: 80, height: h, rx: 40, fill: '#e8eef4', stroke: '#9aa7b8', 'stroke-width': 8 }, g); mk('circle', { cx: x, cy: y + 40, r: 70, fill: '#e8eef4', stroke: '#9aa7b8', 'stroke-width': 8 }, g);
    const bulb = mk('circle', { cx: x, cy: y + 40, r: 52, fill: '#E5484D' }, g), col = mk('rect', { x: x - 22, y: y - h / 2, width: 44, height: h / 2 + 20, rx: 22, fill: '#E5484D' }, g); return { g, set: (k, c) => { col.setAttribute('y', y - h * k); col.setAttribute('height', h * k + 20); col.setAttribute('fill', c); bulb.setAttribute('fill', c); } }; };
  const bar = (s, x, y, w, h, col, label, sub) => { const g = mk('g', {}, s), r = mk('rect', { x, y, width: w, height: h, rx: 14, fill: col }, g); const t = mk('text', { x: x - 30, y: y + h / 2 + 18, 'text-anchor': 'end', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#fff' }, g); t.textContent = label;
    if (sub) { const u = mk('text', { x: x + w + 24, y: y + h / 2 + 18, 'font-family': 'Bebas Neue', 'font-size': 64, fill: col }, g); u.textContent = sub; } return { g, r }; };
  const virusDot = (s, x, y, r) => mk('circle', { cx: x, cy: y, r, fill: '#c94a4a' }, s);
'''
def page(n, dur, desc, secs, js, off=4):
    sec='\n'.join(f'<section class="scene" id="{i}" data-start="{s}" data-duration="{round(e-s+.1,2)}"></section>' for i,s,e in secs)
    html=f'''<!doctype html>
<!-- Tardígrados · Capítulo {n} · {desc} -->
<html data-width="1920" data-height="1080" data-fps="30" data-duration="{dur}">
<head><link rel="stylesheet" href="lib/cm.css"><script src="lib/cm.js"></script><script src="lib/td.js"></script></head>
<body>
<audio src="voz.mp3" data-start="{off}"></audio>
<audio src="musica.mp3" data-volume="0.5" data-duck="0.4" data-fade-out="1"></audio>
<audio src="sfx.mp3" data-volume="0.5"></audio>
{sec}
<div class="vig"></div><div id="heads"></div><div id="cards"></div><div id="caps"></div>
<script>
const OFF = {off};
gm.wait(fetch('voz.json').then(r => r.json()).then(words => {{
  const W = CM.W(words, OFF), G = {{ global: true }}, tl = gm.timeline(null, G), H = document.getElementById('heads'), $ = id => document.getElementById(id), mk = CM.mk;
{COMMON}
{js}
  return CM.captions(words, OFF);
}}));
</script>
</body>
</html>
'''
    open(D+f'cap{n}/video.html','w').write(html)

SCOPE_BG = "'#0b0f14'"
# ---------- CAP 0
page(0, 17.5, 'Introducción.', [('s0',0,10.1),('t',9.8,17.5)], r'''
  const z = svgOf('s0', '#0b0f14'), inner = TD.scope(z, 960, 560, 470); const b = bearAt(inner, 560, 760, 1.15, 1, 60); walkers('s0', [b], 0);
  tl.fromTo(z, { scale: 1.15 }, { scale: 1, duration: 10, ease: 'none', transformOrigin: '50% 50%' }, 0);
  const tags = [['VACÍO', 'vacío', 200, 220], ['−272 °C', 'frío', 1480, 260], ['RADIACIÓN', 'radiación', 1460, 780]].map(([t, w, x, y]) => { const d = CM.text($('s0'), 'big', t, y, `font-size:90px;left:${x - 300}px;right:auto;width:600px`); tl.from(d, { scale: 1.6, opacity: 0, duration: .3, ease: 'expo.out' }, W(w) - .2); return d; });
  const mm = CM.text($('s0'), 'big', '&lt; <em>1 MM</em>', 860, 'font-size:120px;left:60px;right:auto;width:600px'); tl.from(mm, { scale: 1.6, opacity: 0, duration: .3, ease: 'expo.out' }, W('milímetro') - .3);
  const t = $('t'); t.style.background = 'radial-gradient(1200px 800px at 50% 45%, #2f6a3a, #0a1a10 75%)';
  t.innerHTML = '<div class="mid" style="top:250px;color:#FFD23F">CURIOSIMUNDO PRESENTA</div><div class="big" style="top:330px;font-size:200px">EL <em>TARDÍGRADO</em></div><div class="mid" style="top:600px">el animal más resistente del mundo</div>';
  const [p, h, s] = t.children; tl.from(t, { opacity: 0, duration: .4 }, 9.8).from(p, { y: 20, opacity: 0, duration: .4 }, 10.0).from(h, { scale: 1.3, opacity: 0, filter: 'blur(16px)', duration: .8, ease: 'expo.out' }, 10.2)
    .to(h, { scale: 1.05, duration: 6, ease: 'sine.inOut' }, 11.0).from(s, { y: 30, opacity: 0, duration: .4 }, W('animal') - .3);
''', off=0)

# ---------- CAP 1
page(1, 85.1, '¿Qué es un tardígrado? Goeze 1773, Spallanzani, anatomía, parentesco, 1.300 especies, dónde viven, cómo verlos.',
 [('goeze',3.6,17.1),('name',17.0,28.7),('anat',28.6,46.4),('fam',46.3,55.5),('world',55.4,67.2),('water',67.1,74.9),('home',74.8,85.1)], r'''
  CM.card($('cards'), tl, 1, '1773', 'EL OSO DE AGUA', 0, 4);
  const zg = svgOf('goeze', 'linear-gradient(#3a2a1e, #1a120c)'); mk('rect', { y: 760, width: 1920, height: 320, fill: '#5a3e26' }, zg);
  const mic = mk('g', { transform: 'translate(1260 760)' }, zg); mk('rect', { x: -110, y: -20, width: 220, height: 20, fill: '#b8862a' }, mic); mk('rect', { x: -14, y: -320, width: 28, height: 300, fill: '#c9962a' }, mic); mk('rect', { x: -40, y: -380, width: 80, height: 70, rx: 10, fill: '#d8a83a' }, mic); mk('rect', { x: -60, y: -120, width: 120, height: 14, fill: '#8a6a2a' }, mic);
  const cand = mk('g', {}, zg); mk('rect', { x: 1560, y: 640, width: 30, height: 120, fill: '#efe7d2' }, cand); const fl = mk('ellipse', { cx: 1575, cy: 625, rx: 12, ry: 26, fill: '#ffc86a' }, cand); mk('circle', { cx: 1575, cy: 625, r: 120, fill: 'rgb(255 190 90 / .12)' }, cand);
  CM.civil(zg, 1000, 940, 2.6, '#2a2a34'); gm.onFrame($('goeze'), (l, i) => fl.setAttribute('ry', 26 * (1 + Math.sin(i.time * 9) * .1)));
  const bub = mk('g', {}, zg); mk('circle', { cx: 520, cy: 470, r: 300, fill: '#d8e6c8', stroke: '#1a2028', 'stroke-width': 18 }, bub); const gb = bearAt(bub, 400, 600, .8, 1, 40); walkers('goeze', [gb], 12);
  tl.from(bub, { scale: 0, opacity: 0, duration: .5, ease: 'back.out(1.6)', transformOrigin: '520px 470px' }, W('increíble') - .4);
  CM.head(H, tl, '<em>1773</em>', 'Johann August Ephraim Goeze, naturalista alemán', 4.4, 17.0);
  big('goeze', '«PEQUEÑO <em>OSO DE AGUA</em>»', 120, W('pequeño') - .4, 'font-size:100px');
  const zn = svgOf('name', '#0b0f14'), inn = TD.scope(zn, 960, 560, 460); const nb = bearAt(inn, 520, 760, 1.1, 1, 25); walkers('name', [nb], 17.0);
  CM.head(H, tl, '<em>TARDÍGRADO</em>', '«el que camina despacio» · Lazzaro Spallanzani, 1776', 20.0, 28.5);
  const za = svgOf('anat', 'linear-gradient(#e8efe0, #c9d8b8)'); const ab = bearAt(za, 900, 820, 1.7, 1, 0); walkers('anat', [ab], 0);
  const lab = (txt, x1, y1, x2, y2, at) => { const g = mk('g', {}, za); mk('line', { x1, y1, x2, y2, stroke: '#1a2a1a', 'stroke-width': 5 }, g); mk('circle', { cx: x1, cy: y1, r: 10, fill: '#1a2a1a' }, g); const t = mk('text', { x: x2, y: y2 - 14, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#1a2a1a' }, g); t.textContent = txt; tl.from(g, { opacity: 0, duration: .3 }, at); };
  lab('8 PATAS', 650, 740, 420, 520, W('ocho') - .2); lab('GARRAS', 1105, 930, 1500, 800, W('garras') - .2); lab('BOCA EN TUBO', 1310, 615, 1560, 420, W('boca') - .2);
  const sc = mk('g', {}, za); mk('rect', { x: 120, y: 960, width: 300, height: 14, fill: '#1a2a1a' }, sc); const st = mk('text', { x: 270, y: 940, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 56, fill: '#1a2a1a' }, sc); st.textContent = '&lt; 1 MM'; st.textContent = '< 1 MM'; tl.from(sc, { opacity: 0, duration: .3 }, W('milímetro') - .3);
  CM.head(H, tl, '<em>ANATOMÍA</em>', 'menos de 1 mm · se alimenta de musgos y algas', 29.1, 46.2);
  const zf = svgOf('fam', 'linear-gradient(#efe7d2, #d9cfb4)'); const node = (txt, x, y, col) => { const g = mk('g', {}, zf); mk('rect', { x: x - 230, y: y - 60, width: 460, height: 120, rx: 24, fill: col }, g); const t = mk('text', { x, y: y + 22, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 60, fill: '#fff' }, g); t.textContent = txt; return g; };
  mk('path', { d: 'M960 380 L960 520 M420 520 L1500 520 M420 520 L420 600 M960 520 L960 600 M1500 520 L1500 600', stroke: '#5a4a3a', 'stroke-width': 8, fill: 'none' }, zf);
  const n0 = node('PANARTRÓPODOS', 960, 320, '#5a4a3a'), n1 = node('TARDÍGRADOS', 420, 660, '#2f8f5a'), n2 = node('ARTRÓPODOS', 960, 660, '#2f6fcf'), n3 = node('GUSANOS ATERCIOPELADOS', 1500, 660, '#8a5a36');
  n3.querySelector('rect').setAttribute('width', 560); n3.querySelector('rect').setAttribute('x', 1220);
  tl.from([n0, n1], { opacity: 0, y: 20, duration: .3, stagger: .2 }, 46.8).from(n2, { opacity: 0, y: 20, duration: .3 }, W('artrópodos') - .2).from(n3, { opacity: 0, y: 20, duration: .3 }, W('gusanos') - .2);
  CM.head(H, tl, 'SU <em>FAMILIA</em>', 'parientes de insectos, arañas y gusanos aterciopelados', 46.8, 55.3);
  const zw = svgOf('world', '#0e1a12'); const tiles = [['MONTAÑAS', '#7d8fa8', 'montañas'], ['FONDO DEL MAR', '#1d4f7a', 'fondo'], ['ANTÁRTIDA', '#cfe0ef', 'antártida…'], ['TU TEJADO', '#5e8f3e', 'tejado']];
  tiles.forEach(([t, c, w], i) => { const g = mk('g', {}, zw), x = 60 + i * 460; mk('rect', { x, y: 420, width: 420, height: 420, rx: 24, fill: c }, g); TD.moss(g, x + 210, 840, .8, 10);
    const bb = bearAt(g, x + 210, 760, .45, 1, 0); const tt = mk('text', { x: x + 210, y: 500, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 56, fill: i === 2 ? '#1a2a3a' : '#fff' }, g); tt.textContent = t; tl.from(g, { opacity: 0, y: 40, duration: .35 }, W(w) - .3); });
  big('world', 'UNAS <em>1.300</em> ESPECIES', 150, W('trescientas') - .4, 'font-size:120px');
  const zr = svgOf('water', 'linear-gradient(#9cc4e6, #e8efe0)'); TD.moss(zr, 960, 1100, 6, 26); const film = mk('rect', { x: 0, y: 640, width: 1920, height: 60, fill: 'rgb(120 190 255 / .35)' }, zr);
  const wb = bearAt(zr, 300, 720, .8, 1, 120); walkers('water', [wb], 67.1); CM.head(H, tl, 'UNA CAPA DE <em>AGUA</em>', 'la necesitan para estar activos', 67.6, 74.7);
  tl.to(film, { opacity: 0, duration: 1.5 }, W('desaparece') - .5);
  const zh = svgOf('home', '#10151c'); const jar = mk('g', {}, zh); mk('rect', { x: 260, y: 520, width: 260, height: 340, rx: 30, fill: 'rgb(150 200 255 / .3)', stroke: '#cfe0ef', 'stroke-width': 8 }, jar); TD.moss(jar, 390, 840, 1.2, 12);
  const ins = TD.scope(zh, 1300, 560, 360); const hb = bearAt(ins, 1120, 740, .9, 1, 40); walkers('home', [hb], 74.8);
  const steps = mid('home', 'MUSGO + AGUA + <b>MICROSCOPIO</b>', 140, W('microscopio', 2) - .3);
  CM.head(H, tl, 'BÚSCALOS EN <em>CASA</em>', 'en el musgo remojado', 75.2, 85.0);
  fadeIn(['name', 'anat', 'fam', 'world', 'water', 'home']);
''')

# ---------- CAP 2
page(2, 71.1, 'La criptobiosis: el tonel, 95 % de agua fuera, metabolismo casi cero, vidrio de azúcares y proteínas, el despertar, otros que lo hacen.',
 [('dry',3.6,18.3),('pct',18.2,28.4),('crypto',28.3,31.9),('glass',31.8,48.2),('wake',48.1,59.3),('others',59.2,71.1)], r'''
  CM.card($('cards'), tl, 2, 'EL TRUCO', 'CRIPTOBIOSIS', 0, 4);
  const zd = svgOf('dry', 'linear-gradient(#9cc4e6, #e8efe0)'); const moss = TD.moss(zd, 960, 1120, 6, 26); const bw = mk('g', {}, zd), tw = mk('g', {}, zd);
  const bb = TD.bear(bw); bb.g.setAttribute('transform', 'translate(900 760) scale(1.3)'); const tun = TD.tun(tw); tun.setAttribute('transform', 'translate(940 760) scale(1.3)');
  gm.onFrame($('dry'), (l, i) => bb.setWalk(i.time, .4));
  const dryOv = mk('rect', { width: 1920, height: 1080, fill: '#d8b47a', opacity: 0 }, zd); zd.insertBefore(dryOv, moss); tl.to(dryOv, { opacity: .85, duration: 2 }, 4.6).to(moss, { opacity: .45, duration: 2 }, 4.6);
  tl.to(bw, { opacity: 0, scale: .85, transformOrigin: '900px 600px', duration: .8 }, W('bolita') - .3).from(tw, { opacity: 0, scale: 1.2, transformOrigin: '940px 600px', duration: .8 }, W('bolita') - .3);
  CM.head(H, tl, 'CUANDO TODO <em>SE SECA</em>', 'recoge las patas y encoge la cabeza', 4.4, 13.9); CM.head(H, tl, 'EL <em>TONEL</em>', '«tun», en alemán', 14.1, 18.1);
  const zp = svgOf('pct', '#10151c'); const tank = mk('rect', { x: 260, y: 300, width: 220, height: 600, rx: 24, fill: 'none', stroke: '#9fb3c8', 'stroke-width': 8 }, zp); const wat = mk('rect', { x: 268, y: 308, width: 204, height: 584, rx: 18, fill: '#3f86b4' }, zp);
  tl.to(wat, { attr: { y: 870, height: 22 }, duration: 2.5, ease: 'power2.in' }, 18.8);
  const met = mk('path', { d: '', stroke: '#5bd08a', 'stroke-width': 8, fill: 'none' }, zp); gm.onFrame($('pct'), (l, i) => { const k = gm.clamp((i.time - 22.6) / 1.5); let d = 'M700 600'; for (let x = 0; x <= 1000; x += 20) d += ` L${700 + x} ${600 - Math.sin(x / 40 + i.time * 6) * 120 * (1 - k)}`; met.setAttribute('d', d); });
  big('pct', '–95 % <em>DE AGUA</em>', 150, W('noventa') - .3, 'font-size:110px;left:auto;right:80px;width:1100px'); mid('pct', 'metabolismo: <b>casi cero</b>', 800, W('metabolismo') - .2, 'left:auto;right:80px;width:1100px');
  CM.head(H, tl, 'VIDA EN <em>PAUSA</em>', '', 25.8, 28.2);
  const zc = $('crypto'); zc.style.background = 'radial-gradient(1200px 800px at 50% 45%, #2f6a3a, #0a1a10 75%)'; big('crypto', '<em>CRIPTOBIOSIS</em>', 380, 28.5, 'font-size:180px'); mid('crypto', '«vida escondida»', 620, W('vida') - .2);
  const zl = svgOf('glass', '#0e1622'); mk('circle', { cx: 960, cy: 560, r: 400, fill: '#1d2e44', stroke: '#9fb3c8', 'stroke-width': 8 }, zl);
  const mol = Array.from({ length: 60 }, (_, i) => mk('circle', { r: 10 + (i % 3) * 4, fill: i % 4 ? '#e8b92a' : '#5bd08a' }, zl)); const hexes = mk('g', { opacity: 0 }, zl);
  for (let r = 0; r < 9; r++) for (let c = 0; c < 9; c++) { const x = 640 + c * 80 + (r % 2) * 40, y = 240 + r * 80; if ((x - 960) ** 2 + (y - 560) ** 2 < 380 ** 2) mk('path', { d: `M${x} ${y - 40} l35 20 l0 40 l-35 20 l-35 -20 l0 -40z`, fill: 'rgb(160 220 255 / .18)', stroke: '#bfe6ff', 'stroke-width': 3 }, hexes); }
  const tG = W('vidrio') - .6; gm.onFrame($('glass'), (l, i) => { const t = i.time, k = gm.clamp((t - tG) / 1.2); mol.forEach((m, j) => { const a = j * 2.4 + t * (1 - k) * (1 + j % 3), rr = 60 + (j * 37) % 300; m.setAttribute('cx', 960 + Math.cos(a) * rr); m.setAttribute('cy', 560 + Math.sin(a * 1.3) * rr * .9); }); hexes.setAttribute('opacity', k); });
  CM.head(H, tl, '<em>AZÚCARES</em> Y PROTEÍNAS', 'que al secarse forman una especie de cristal', 32.3, 43.4); CM.head(H, tl, 'COMO <em>VIDRIO</em>', 'todo queda inmovilizado y protegido', 43.6, 48.0);
  const zk = svgOf('wake', 'linear-gradient(#7d8fa8, #c9d8e8)'); TD.moss(zk, 960, 1120, 6, 26); const drops = Array.from({ length: 50 }, (_, i) => mk('line', { stroke: '#cfe6ff', 'stroke-width': 4, opacity: .8 }, zk));
  const kt = mk('g', {}, zk), kb = mk('g', {}, zk); const ktun = TD.tun(kt); ktun.setAttribute('transform', 'translate(940 760) scale(1.3)'); const kbear = TD.bear(kb); kbear.g.setAttribute('transform', 'translate(900 760) scale(1.3)');
  tl.to(kt, { opacity: 0, duration: .8 }, W('hincha') - .3).from(kb, { opacity: 0, scale: .85, transformOrigin: '900px 600px', duration: .8 }, W('hincha') - .3);
  gm.onFrame($('wake'), (l, i) => { const t = i.time; drops.forEach((d, j) => { const x = (j * 97) % 1920, y = ((t * 900 + j * 211) % 1200) - 100; d.setAttribute('x1', x); d.setAttribute('y1', y); d.setAttribute('x2', x - 10); d.setAttribute('y2', y + 40); }); kbear.setWalk(t, t > 52 ? 1 : .2);
    if (t > 52) kbear.g.setAttribute('transform', `translate(${900 + (t - 52) * 70} 760) scale(1.3)`); });
  CM.head(H, tl, 'VUELVE EL <em>AGUA</em>', 'en minutos u horas, camina otra vez', 48.9, 56.4); big('wake', '<em>AÑOS</em> ESPERANDO', 160, W('años') - .3, 'font-size:110px');
  const zo = svgOf('others', 'linear-gradient(#efe7d2, #d9cfb4)'); [['SEMILLAS', 'semillas,', '#8a6a3a'], ['BACTERIAS', 'bacterias', '#2f6fcf'], ['ROTÍFEROS', 'rotíferos,', '#2f8f5a']].forEach(([t, w, c], i) => {
    const g = mk('g', {}, zo), x = 160 + i * 560; mk('rect', { x, y: 380, width: 480, height: 420, rx: 30, fill: c }, g); const tt = mk('text', { x: x + 240, y: 620, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 90, fill: '#fff' }, g); tt.textContent = t; tl.from(g, { opacity: 0, y: 40, duration: .35 }, W(w) - .3); });
  CM.head(H, tl, 'NO SON LOS <em>ÚNICOS</em>', 'pero pocos lo llevan tan lejos', 59.9, 71.0);
  fadeIn(['pct', 'crypto', 'glass', 'wake', 'others']);
''')

# ---------- CAP 3
page(3, 71.3, 'Los récords: frío (−272 °C), calor (80 °C una hora), radiación (×1.000), presión (+11.000 atm), 30 años congelados, matiz.',
 [('intro',3.6,10.5),('cold',10.4,20.0),('heat',19.9,29.7),('rad',29.6,40.1),('pres',40.0,48.1),('time',48.0,62.4),('note',62.3,71.3)], r'''
  CM.card($('cards'), tl, 3, 'AL LÍMITE', 'LOS RÉCORDS', 0, 4);
  const zi = svgOf('intro', 'radial-gradient(circle at 50% 70%, #3a3a46, #0a0a10 70%)'); const spot = mk('ellipse', { cx: 960, cy: 820, rx: 420, ry: 80, fill: 'rgb(255 255 220 / .18)' }, zi); const it = mk('g', {}, zi); const tu = TD.tun(it); tu.setAttribute('transform', 'translate(960 820) scale(1.4)');
  tl.fromTo(it, { scale: .7 }, { scale: 1, duration: 6, ease: 'none', transformOrigin: '960px 700px' }, 3.6); CM.head(H, tl, 'EN FORMA DE <em>TONEL</em>', 'pruebas que acabarían con casi cualquier ser vivo', 4.4, 10.3);
  const zc = svgOf('cold', 'linear-gradient(#0e2a4a, #6fa8d8)'); const th = thermo(zc, 360, 820); const fl = mk('g', {}, zc); mk('path', { d: 'M1100 300 L1100 820 Q1100 900 1180 900 L1460 900 Q1540 900 1540 820 L1540 300', fill: 'rgb(200 230 255 / .25)', stroke: '#cfe6ff', 'stroke-width': 8 }, fl);
  mk('rect', { x: 1108, y: 520, width: 424, height: 372, fill: 'rgb(160 210 255 / .4)' }, fl); const ct = mk('g', {}, fl); const ctun = TD.tun(ct); ctun.setAttribute('transform', 'translate(1320 800) scale(.9)');
  gm.onFrame($('cold'), (l, i) => { const k = gm.clamp((i.time - 10.8) / 4); th.set(.5 - k * .48, k > .5 ? '#5bc0ff' : '#E5484D'); });
  big('cold', '<em>−272 °C</em>', 160, W('doscientos') - .3, 'font-size:180px;left:520px;right:auto;width:1000px'); mid('cold', 'helio líquido: a <b>1 grado</b> del cero absoluto', 380, W('apenas') - .3, 'left:520px;right:auto;width:1000px');
  CM.head(H, tl, '<em>FRÍO</em>', '', 10.7, 19.8);
  const zh = svgOf('heat', 'linear-gradient(#e8a86a, #6a2a1a)'); const th2 = thermo(zh, 360, 820); gm.onFrame($('heat'), (l, i) => th2.set(.3 + gm.clamp((i.time - 20.3) / 3) * .55, '#E5484D'));
  const hb = mk('g', {}, zh); const ht = TD.tun(hb); ht.setAttribute('transform', 'translate(1300 800) scale(1)');
  big('heat', '<em>+80 °C</em> · 1 HORA', 160, W('ochenta') - .4, 'font-size:150px;left:520px;right:auto;width:1200px'); mid('heat', 'la <b>mitad</b> sobrevivió (en tonel)', 380, W('mitad') - .2, 'left:520px;right:auto;width:1200px');
  mid('heat', 'activos, <b>mucho más delicados</b>', 460, W('activos,') - .2, 'left:520px;right:auto;width:1200px'); CM.head(H, tl, '<em>CALOR</em>', '', 20.3, 29.5);
  const zr = svgOf('rad', '#10151c'); const b1 = bar(zr, 520, 400, 4, 120, '#E5484D', 'PERSONA', '≈5 GY'), b2 = bar(zr, 520, 640, 880, 120, '#5bd08a', 'TARDÍGRADO', '');
  b1.g.querySelectorAll('text')[1].textContent = '5 GY'; const lbl = mk('text', { x: 1420, y: 720, 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#5bd08a' }, zr); lbl.textContent = '3.000–5.000 GY';
  tl.from(b1.g, { opacity: 0, duration: .3 }, W('persona,') - .2).from(b2.r, { attr: { width: 0 }, duration: 1.2, ease: 'power2.out' }, W('soportan') - .3).from(lbl, { opacity: 0, duration: .3 }, W('soportan') + .6);
  big('rad', '× <em>1.000</em>', 160, W('veces') - .5, 'font-size:160px'); CM.head(H, tl, '<em>RADIACIÓN</em>', '', 30.2, 39.9);
  const zp = svgOf('pres', 'linear-gradient(#5a5f66, #2a2e34)'); const press = mk('g', {}, zp); mk('rect', { x: 760, y: 0, width: 400, height: 420, fill: '#8a9099' }, press); mk('rect', { x: 700, y: 420, width: 520, height: 60, fill: '#a8afb8' }, press);
  mk('rect', { x: 600, y: 860, width: 720, height: 80, fill: '#6a6e74' }, zp); const pt = mk('g', {}, zp); const pun = TD.tun(pt); pun.setAttribute('transform', 'translate(960 860) scale(.9)');
  tl.fromTo(press, { y: -200 }, { y: 220, duration: .6, ease: 'power3.in' }, W('impactos') - .4).to(press, { y: -200, duration: .6 }, W('impactos') + .6);
  big('pres', '<em>+11.000</em> VECES', 160, W('once') - .3, 'font-size:130px;left:auto;right:60px;width:700px'); mid('pres', 'la presión del aire', 320, W('aire') - .3, 'left:auto;right:60px;width:700px'); CM.head(H, tl, '<em>PRESIÓN</em>', '', 40.5, 47.9);
  const zt = svgOf('time', 'linear-gradient(#cfe0ef, #eef4f8)'); const ice = mk('rect', { x: 560, y: 360, width: 800, height: 520, rx: 40, fill: 'rgb(170 210 240 / .7)', stroke: '#fff', 'stroke-width': 10 }, zt); const im = TD.moss(zt, 960, 860, 3, 20);
  const tb1 = bearAt(zt, 820, 860, .5, 1, 0), tb2 = bearAt(zt, 1100, 860, .5, -1, 0); [tb1, tb2].forEach(o => o.w.style.opacity = 0); tl.to([tb1.w, tb2.w], { opacity: 1, duration: .6, stagger: .3 }, W('volvieron') - .3).to(ice, { opacity: .15, duration: 1 }, W('descongelaron') - .2);
  walkers('time', [tb1, tb2], 0); const eggs = mk('g', {}, zt); for (let i = 0; i < 5; i++) mk('ellipse', { cx: 1180 + i * 28, cy: 850, rx: 12, ry: 9, fill: '#f2e6c8', stroke: '#a88a5a', 'stroke-width': 2 }, eggs); tl.from(eggs, { opacity: 0, duration: .4 }, W('crías') - .2);
  big('time', 'UNOS <em>30 AÑOS</em> CONGELADOS', 230, W('treinta') - .4, 'font-size:110px'); CM.head(H, tl, 'EL <em>TIEMPO</em>', '2016 · musgo antártico', 48.4, 62.2);
  const zn = svgOf('note', 'linear-gradient(#efe7d2, #d9cfb4)'); const card = mk('g', {}, zn); mk('rect', { x: 460, y: 300, width: 1000, height: 480, rx: 20, fill: '#fffaf0', stroke: '#c9b48c', 'stroke-width': 6, transform: 'rotate(-2 960 540)' }, card);
  big('note', '<em>OJO</em>', 360, 62.6, 'font-size:150px;color:#c0392b'); mid('note', 'cada especie aguanta <span style="color:#c0392b">cosas distintas</span>', 560, W('especies') - .3, 'color:#3a2a1a');
  fadeIn(['cold', 'heat', 'rad', 'pres', 'time', 'note']);
''')

# ---------- CAP 4
page(4, 67.3, 'Al espacio: FOTON-M3 2007, 10 días de vacío y UV, 68 % reviven, crías, UV demasiado, Endeavour 2011 y la EEI.',
 [('q',3.6,7.7),('foton',7.6,28.9),('lab',28.8,43.3),('uv',43.2,54.1),('more',54.0,67.3)], r'''
  CM.card($('cards'), tl, 4, '2007', 'AL ESPACIO SIN TRAJE', 0, 4);
  const stars = s => { for (let i = 0; i < 90; i++) mk('circle', { cx: gm.random('x' + i) * 1920, cy: gm.random('y' + i) * 1080, r: 1 + gm.random('r' + i) * 2, fill: '#fff', opacity: .3 + gm.random('o' + i) * .6 }, s); };
  const zq = svgOf('q', 'linear-gradient(#0b1430, #3a6aa0)'); stars(zq); TD.moss(zq, 960, 1100, 5, 20); const qb = bearAt(zq, 860, 900, .9, 1, 0); walkers('q', [qb], 0); big('q', '?', 200, 4.4, 'font-size:240px;color:#FFD23F');
  const zf = svgOf('foton', '#030817'); stars(zf); mk('circle', { cx: 960, cy: 1900, r: 1100, fill: '#1e6fd0' }, zf); mk('circle', { cx: 960, cy: 1900, r: 1130, fill: 'none', stroke: 'rgb(159 208 255 / .4)', 'stroke-width': 30 }, zf);
  const cap = mk('g', {}, zf); mk('circle', { r: 120, fill: '#c9cdd4', stroke: '#7d838c', 'stroke-width': 8 }, cap); mk('rect', { x: -330, y: -30, width: 200, height: 60, fill: '#2f4f9a' }, cap); mk('rect', { x: 130, y: -30, width: 200, height: 60, fill: '#2f4f9a' }, cap);
  const tray = mk('g', {}, cap); mk('rect', { x: -90, y: 100, width: 180, height: 40, fill: '#5a5f66' }, tray); for (let i = 0; i < 5; i++) mk('ellipse', { cx: -64 + i * 32, cy: 112, rx: 12, ry: 8, fill: '#c9a07a' }, tray);
  const rays = mk('g', { opacity: 0 }, zf); for (let i = 0; i < 6; i++) mk('line', { x1: 1920, y1: 100 + i * 40, x2: 1200, y2: 400 + i * 30, stroke: '#FFD23F', 'stroke-width': 6, opacity: .6 }, rays);
  gm.onFrame($('foton'), (l, i) => { const t = i.time - 7.6; cap.setAttribute('transform', `translate(${300 + t * 50} ${420 + Math.sin(t * .5) * 30}) rotate(${t * 3})`); });
  tl.to(rays, { opacity: 1, duration: .5 }, W('luz') - .3); CM.head(H, tl, '<em>FOTON-M3</em>', 'septiembre de 2007 · satélite ruso con experimentos de la ESA', 8.0, 19.1);
  big('foton', '<em>10 DÍAS</em> EN EL VACÍO', 160, W('diez') - .3, 'font-size:120px', 23.3); mid('foton', '+ luz directa del Sol, <b>sin atmósfera</b>', 160, W('luz') - .3, 'font-size:46px');
  const zl = svgOf('lab', 'linear-gradient(#e8eef4, #c9d6e2)'); mk('ellipse', { cx: 960, cy: 720, rx: 620, ry: 200, fill: 'rgb(150 200 255 / .3)', stroke: '#9fb3c8', 'stroke-width': 8 }, zl);
  const lbs = [0, 1, 2, 3].map(i => bearAt(zl, 560 + i * 260, 760, .45, i % 2 ? -1 : 1, 0)); const lts = [0, 1, 2, 3].map(i => { const g = mk('g', {}, zl); const t = TD.tun(g); t.setAttribute('transform', `translate(${560 + i * 260} 760) scale(.45)`); return g; });
  lbs.forEach(o => o.w.style.opacity = 0); tl.to(lts, { opacity: 0, duration: .5, stagger: .2 }, W('revivieron') - .5).to(lbs.map(o => o.w), { opacity: 1, duration: .5, stagger: .2 }, W('revivieron') - .5); walkers('lab', lbs, 0);
  const eg = mk('g', {}, zl); for (let i = 0; i < 8; i++) mk('ellipse', { cx: 700 + i * 70, cy: 860, rx: 14, ry: 10, fill: '#f2e6c8', stroke: '#a88a5a', 'stroke-width': 2 }, eg); tl.from(eg, { opacity: 0, duration: .4 }, W('huevos') - .3);
  big('lab', '<em>+68 %</em> REVIVIERON', 160, W('sesenta') - .3, 'font-size:120px'); mid('lab', 'de los protegidos del sol · <b>en media hora</b>', 320, W('protegido') - .3); CM.head(H, tl, 'DE VUELTA, <em>AGUA</em>', '', 29.1, 43.1);
  const zu = svgOf('uv', '#14082a'); const uvr = mk('g', {}, zu); for (let i = 0; i < 10; i++) mk('line', { x1: 1920, y1: i * 60, x2: 700, y2: 500 + i * 20, stroke: '#b06aff', 'stroke-width': 8, opacity: .5 }, uvr);
  for (let i = 0; i < 4; i++) { const g = mk('g', {}, zu); const t = TD.tun(g); t.setAttribute('transform', `translate(${560 + i * 260} 800) scale(.45)`); }
  mid('uv', 'la luz <b>ultravioleta</b> del Sol: demasiado', 260, W('ultravioleta') - .3); CM.head(H, tl, 'LOS PRIMEROS <em>ANIMALES</em>', 'en sobrevivir a la exposición directa al espacio', W('primeros') - .4, 54.0);
  const zm = svgOf('more', '#030817'); stars(zm); const sh = mk('g', {}, zm); mk('path', { d: 'M0 0 L260 0 L320 30 L260 60 L0 60Z', fill: '#e8eef4' }, sh); mk('path', { d: 'M60 0 L160 -80 L200 0Z M60 60 L160 140 L200 60Z', fill: '#c9cdd4' }, sh); mk('path', { d: 'M20 0 L0 -60 L60 0Z', fill: '#c9cdd4' }, sh);
  const iss = mk('g', {}, zm); mk('rect', { x: -260, y: -10, width: 520, height: 20, fill: '#c9cdd4' }, iss); [-240, -140, 140, 240].forEach(x => mk('rect', { x: x - 40, y: -120, width: 80, height: 240, fill: '#2f4f9a' }, iss)); mk('rect', { x: -60, y: -40, width: 120, height: 80, fill: '#e8eef4' }, iss);
  gm.onFrame($('more'), (l, i) => { const t = i.time - 54.0; sh.setAttribute('transform', `translate(${-400 + t * 160} 380) rotate(-8)`); iss.setAttribute('transform', `translate(${2200 - Math.max(0, i.time - 60.4) * 260} 640)`); });
  CM.head(H, tl, '<em>ENDEAVOUR</em>', '2011 · último viaje del transbordador', 54.4, 60.8); CM.head(H, tl, 'ESTACIÓN ESPACIAL <em>INTERNACIONAL</em>', 'cómo se adaptan sin gravedad', 61.0, 67.1);
  fadeIn(['foton', 'lab', 'uv', 'more']);
''')

# ---------- CAP 5
page(5, 65.3, 'Tardígrados en la Luna: Beresheet (SpaceIL, 2019), biblioteca y tardígrados, choque, experimentos de impacto, sin agua no despertarán.',
 [('launch',3.6,17.3),('lib',17.2,24.6),('crash',24.5,33.4),('gun',33.3,47.2),('moon',47.1,65.3)], r'''
  CM.card($('cards'), tl, 5, '2019', 'TARDÍGRADOS EN LA LUNA', 0, 4);
  const stars = s => { for (let i = 0; i < 90; i++) mk('circle', { cx: gm.random('x' + i) * 1920, cy: gm.random('y' + i) * 1080, r: 1 + gm.random('r' + i) * 2, fill: '#fff', opacity: .3 + gm.random('o' + i) * .6 }, s); };
  const moonDisc = (s, x, y, r) => { mk('circle', { cx: x, cy: y, r, fill: '#cfcfc8' }, s); [[-.3, -.2, .18], [.25, .1, .14], [-.05, .35, .1], [.3, -.35, .08]].forEach(([a, b, c]) => mk('circle', { cx: x + a * r, cy: y + b * r, r: c * r, fill: '#b5b5ac' }, s)); };
  const zl = svgOf('launch', '#030817'); stars(zl); mk('circle', { cx: 300, cy: 860, r: 260, fill: '#1e6fd0' }, zl); moonDisc(zl, 1600, 260, 140);
  const path = mk('path', { d: 'M420 700 Q900 300 1480 300', stroke: '#FFD23F', 'stroke-width': 5, 'stroke-dasharray': '14 12', fill: 'none' }, zl); tl.from(path, { draw: 0, duration: 4, ease: 'power1.inOut' }, 5.0);
  const ship = mk('g', {}, zl); mk('path', { d: 'M-40 -20 L40 -20 L50 20 L-50 20Z', fill: '#d8dde6' }, ship); [-40, 40].forEach(x => mk('path', { d: `M${x} 20 L${x * 1.5} 60`, stroke: '#d8dde6', 'stroke-width': 6 }, ship));
  gm.onFrame($('launch'), (l, i) => { const k = gm.clamp((i.time - 5) / 4), x = (1 - k) ** 2 * 420 + 2 * (1 - k) * k * 900 + k * k * 1480, y = (1 - k) ** 2 * 700 + 2 * (1 - k) * k * 300 + k * k * 300; ship.setAttribute('transform', `translate(${x} ${y}) scale(1.2)`); });
  CM.head(H, tl, '<em>BERESHEET</em>', 'febrero de 2019 · nave israelí privada', 4.4, 10.9); CM.head(H, tl, '«EN EL <em>PRINCIPIO</em>»', 'construida por SpaceIL', 11.1, 17.1);
  const zb = svgOf('lib', '#10151c'); const disc = mk('g', {}, zb); mk('circle', { cx: 960, cy: 600, r: 300, fill: '#c9cdd4', stroke: '#8a9099', 'stroke-width': 8 }, disc); mk('circle', { cx: 960, cy: 600, r: 70, fill: '#10151c' }, disc);
  for (let i = 0; i < 40; i++) { const a = i * 0.7, r = 120 + (i * 13) % 160; mk('ellipse', { cx: 960 + Math.cos(a) * r, cy: 600 + Math.sin(a) * r, rx: 7, ry: 5, fill: '#a8784a' }, disc); }
  tl.fromTo(disc, { rotate: 0 }, { rotate: 40, duration: 7.4, ease: 'none', transformOrigin: '960px 600px' }, 17.2);
  big('lib', 'BIBLIOTECA <em>EN MINIATURA</em>', 120, W('biblioteca') - .3, 'font-size:100px'); mid('lib', '+ <b>miles de tardígrados</b> deshidratados', 960, W('miles') - .3);
  const zc = svgOf('crash', '#030817'); stars(zc); const ground = mk('path', { d: 'M0 820 Q480 780 960 820 T1920 810 L1920 1080 L0 1080Z', fill: '#9a9a92' }, zc); [[300, 900, 60], [1300, 920, 90], [1700, 860, 40]].forEach(([x, y, r]) => mk('ellipse', { cx: x, cy: y, rx: r, ry: r * .3, fill: '#7d7d76' }, zc));
  const lan = mk('g', {}, zc); mk('path', { d: 'M-50 -30 L50 -30 L60 20 L-60 20Z', fill: '#d8dde6' }, lan); [-50, 50].forEach(x => mk('path', { d: `M${x} 20 L${x * 1.5} 60`, stroke: '#d8dde6', 'stroke-width': 6 }, lan)); const fl = mk('path', { d: 'M-20 20 L0 90 L20 20Z', fill: '#ffb040' }, lan);
  const dust = mk('ellipse', { cx: 1100, cy: 820, rx: 0, ry: 0, fill: '#c9c9c0', opacity: .8 }, zc); const tOff = W('apagó') - .2, tHit = W('estrelló') - .1;
  gm.onFrame($('crash'), (l, i) => { const t = i.time, k = gm.clamp((t - 24.5) / (tHit - 24.5)); lan.setAttribute('transform', `translate(${700 + k * 400} ${200 + k * k * 600}) rotate(${t > tOff ? (t - tOff) * 20 : 0}) scale(1.4)`); fl.style.display = t < tOff ? '' : 'none'; lan.style.display = t < tHit ? '' : 'none';
    const d = gm.clamp((t - tHit) / 1.5); dust.setAttribute('rx', d * 320); dust.setAttribute('ry', d * 90); dust.setAttribute('opacity', .8 * (1 - d * .5)); });
  CM.head(H, tl, '11 DE ABRIL DE <em>2019</em>', 'un fallo apaga el motor principal', 24.9, 33.2);
  const zg = svgOf('gun', 'linear-gradient(#e8eef4, #c9d6e2)'); mk('rect', { x: 100, y: 500, width: 700, height: 80, rx: 20, fill: '#5a5f66' }, zg); mk('rect', { x: 1500, y: 360, width: 60, height: 360, fill: '#8a6a4a' }, zg);
  const proj = mk('circle', { r: 30, fill: '#c9a07a', stroke: '#8a6040', 'stroke-width': 5 }, zg); const flash = mk('circle', { cx: 1500, cy: 540, r: 0, fill: 'url(#cmFlash)' }, zg);
  gm.onFrame($('gun'), (l, i) => { const k = ((i.time - 37.5) * .8) % 1; proj.setAttribute('cx', 800 + k * 700); proj.setAttribute('cy', 540); proj.style.display = i.time > 37.5 ? '' : 'none'; flash.setAttribute('r', k > .9 ? 120 : 0); });
  mid('gun', 'cientos de m/s: <b>aguantaron</b>', 220, W('aguantaron') - .2, 'font-size:50px'); mid('gun', 'más rápido: <b>no</b>', 300, W('altas') - .6, 'font-size:50px'); CM.head(H, tl, '¿<em>SOBREVIVIERON</em>?', 'experimentos de impacto en laboratorio', 33.6, 47.0);
  const zm = svgOf('moon', '#030817'); stars(zm); mk('path', { d: 'M0 700 Q480 660 960 700 T1920 690 L1920 1080 L0 1080Z', fill: '#9a9a92' }, zm); mk('circle', { cx: 1600, cy: 220, r: 120, fill: '#1e6fd0' }, zm);
  for (let i = 0; i < 9; i++) { const g = mk('g', {}, zm); const t = TD.tun(g); t.setAttribute('transform', `translate(${200 + i * 190} ${820 + (i % 3) * 40}) scale(.3)`); }
  const ic = [['AGUA', 'agua'], ['AIRE', 'aire'], ['COMIDA', 'comida,']].map(([t, w], i) => { const d = CM.text($('moon'), 'big', `<span style="text-decoration:line-through;text-decoration-color:#E5484D;text-decoration-thickness:10px">${t}</span>`, 260, `font-size:110px;left:${160 + i * 560}px;right:auto;width:500px`); tl.from(d, { opacity: 0, scale: 1.4, duration: .3 }, W(w, w === 'agua' ? 1 : 1) - .2); return d; });
  tl.to(ic, { opacity: 0, duration: .3 }, 56.6); CM.head(H, tl, 'DORMIDOS <em>PARA SIEMPRE</em>', 'la Luna no está colonizada por osos de agua', 47.4, 65.1);
  fadeIn(['lib', 'crash', 'gun', 'moon']);
''')

# ---------- CAP 6
page(6, 56.7, 'El secreto en su ADN: Dsup (2016), células humanas, reparación del ADN, vacunas sin frío, astronautas.',
 [('dna',3.6,23.6),('cells',23.5,31.1),('rep',31.0,38.3),('vac',38.2,47.5),('astro',47.4,56.7)], r'''
  CM.card($('cards'), tl, 6, '2016', 'EL SECRETO EN SU ADN', 0, 4);
  const helix = (s, cx, cy, len, amp, ph) => { const g = mk('g', {}, s), a = mk('path', { stroke: '#5bc0ff', 'stroke-width': 10, fill: 'none' }, g), b = mk('path', { stroke: '#ff7aa8', 'stroke-width': 10, fill: 'none' }, g), rungs = Array.from({ length: 24 }, () => mk('line', { stroke: '#cfe0ef', 'stroke-width': 5, opacity: .7 }, g));
    const draw = t => { let da = '', db = ''; for (let x = 0; x <= len; x += 10) { const y1 = cy + Math.sin(x / 70 + t * ph) * amp, y2 = cy - Math.sin(x / 70 + t * ph) * amp; da += `${x ? 'L' : 'M'}${cx + x} ${y1} `; db += `${x ? 'L' : 'M'}${cx + x} ${y2} `; } a.setAttribute('d', da); b.setAttribute('d', db);
      rungs.forEach((r, i) => { const x = i * len / 24, y1 = cy + Math.sin(x / 70 + t * ph) * amp, y2 = cy - Math.sin(x / 70 + t * ph) * amp; r.setAttribute('x1', cx + x); r.setAttribute('x2', cx + x); r.setAttribute('y1', y1); r.setAttribute('y2', y2); }); }; return { g, draw }; };
  const zd = svgOf('dna', '#0b1220'); const h = helix(zd, 260, 600, 1400, 140, 1.2); const shield = mk('g', { opacity: 0 }, zd); for (let i = 0; i < 12; i++) mk('ellipse', { cx: 320 + i * 115, cy: 600, rx: 70, ry: 170, fill: 'rgb(255 210 63 / .35)', stroke: '#FFD23F', 'stroke-width': 5 }, shield);
  gm.onFrame($('dna'), (l, i) => h.draw(i.time)); tl.to(shield, { opacity: 1, duration: .8 }, W('envuelve') - .3);
  big('dna', '<em>DSUP</em>', 150, W('dsup') - .3, 'font-size:180px'); mid('dna', '«damage suppressor»: <b>supresora de daños</b>', 360, W('supresora') - .4);
  CM.head(H, tl, 'UNA PROTEÍNA <em>NUEVA</em>', '2016 · genoma de un tardígrado estudiado en Japón', 4.4, 15.5); CM.head(H, tl, 'UN <em>ESCUDO</em> PARA EL ADN', 'frente a la radiación', 19.6, 23.4);
  const zc = svgOf('cells', '#10151c'); const dish = (x, lab, n) => { const g = mk('g', {}, zc); mk('circle', { cx: x, cy: 540, r: 260, fill: 'rgb(150 200 255 / .15)', stroke: '#9fb3c8', 'stroke-width': 8 }, g);
    for (let i = 0; i < 14; i++) mk('circle', { cx: x - 200 + (i % 5) * 100, cy: 420 + Math.floor(i / 5) * 110, r: 34, fill: '#e8b9a8' }, g); for (let i = 0; i < n; i++) mk('path', { d: `M${x - 180 + (i * 67) % 360} ${400 + (i * 53) % 260} l24 24 m0 -24 l-24 24`, stroke: '#E5484D', 'stroke-width': 8 }, g);
    const t = mk('text', { x, y: 870, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#fff' }, g); t.textContent = lab; return g; };
  const d1 = dish(560, 'SIN DSUP', 12), d2 = dish(1360, 'CON DSUP', 3); tl.from(d2, { opacity: 0, duration: .4 }, W('sufrieron') - .3);
  CM.head(H, tl, 'CÉLULAS <em>HUMANAS</em> + DSUP', 'mucho menos daño por rayos X', 24.0, 30.9);
  const zr = svgOf('rep', '#0b1220'); const h2 = helix(zr, 260, 600, 1400, 120, 1); const gaps = [600, 1100].map(x => mk('rect', { x, y: 420, width: 60, height: 360, fill: '#0b1220' }, zr)); gm.onFrame($('rep'), (l, i) => h2.draw(i.time));
  tl.to(gaps, { opacity: 0, duration: .6, stagger: .5 }, W('reparan') - .2); CM.head(H, tl, 'REPARACIÓN <em>EXPRÉS</em>', 'activan genes que arreglan su ADN', 31.5, 38.1);
  const zv = svgOf('vac', 'linear-gradient(#e8eef4, #c9d6e2)'); const vial = mk('g', {}, zv); mk('rect', { x: 780, y: 360, width: 200, height: 420, rx: 30, fill: 'rgb(150 200 255 / .5)', stroke: '#6a8aa8', 'stroke-width': 8 }, vial); mk('rect', { x: 800, y: 300, width: 160, height: 70, fill: '#c0392b' }, vial);
  const snow = mk('g', {}, zv); mk('path', { d: 'M1300 400 v320 M1160 480 l280 160 M1160 640 l280 -160', stroke: '#5bc0ff', 'stroke-width': 18, 'stroke-linecap': 'round' }, snow); mk('path', { d: 'M1140 380 L1460 740', stroke: '#E5484D', 'stroke-width': 22 }, snow);
  tl.from(snow, { opacity: 0, scale: 1.3, transformOrigin: '1300px 560px', duration: .4 }, W('frío') - .3); CM.head(H, tl, '¿VACUNAS <em>SIN NEVERA</em>?', 'se estudian sus proteínas «de vidrio»', 38.6, 47.3);
  const za = svgOf('astro', '#030817'); for (let i = 0; i < 80; i++) mk('circle', { cx: gm.random('ax' + i) * 1920, cy: gm.random('ay' + i) * 1080, r: 1 + gm.random('ar' + i) * 2, fill: '#fff', opacity: .6 }, za); mk('circle', { cx: 1550, cy: 300, r: 110, fill: '#c8643a' }, za);
  const as = mk('g', { transform: 'translate(760 640)' }, za); mk('circle', { cy: -170, r: 70, fill: '#e8eef4' }, as); mk('ellipse', { cx: 10, cy: -170, rx: 46, ry: 36, fill: '#2a3a5a' }, as); mk('rect', { x: -80, y: -110, width: 160, height: 220, rx: 40, fill: '#e8eef4' }, as); mk('rect', { x: -70, y: 110, width: 60, height: 140, rx: 20, fill: '#e8eef4' }, as); mk('rect', { x: 10, y: 110, width: 60, height: 140, rx: 20, fill: '#e8eef4' }, as);
  const sh = mk('ellipse', { cx: 760, cy: 560, rx: 240, ry: 360, fill: 'rgb(255 210 63 / .18)', stroke: '#FFD23F', 'stroke-width': 5, opacity: 0 }, za); tl.to(sh, { opacity: 1, duration: .6 }, W('proteger') - .2);
  CM.head(H, tl, '¿Y LOS <em>ASTRONAUTAS</em>?', 'todavía estamos lejos', 47.8, 56.6);
  fadeIn(['cells', 'rep', 'vac', 'astro']);
''')

# ---------- CAP 7
page(7, 63.9, '¿Inmortales? No: frágiles activos, pausa, años en tonel, fósil en ámbar (16 Ma), estudio 2017 (muerte del Sol), musgo, pregunta final.',
 [('no',3.6,10.2),('frag',10.1,21.5),('wait',21.4,27.6),('fos',27.5,41.4),('sun',41.3,48.0),('moss',47.9,55.9),('end',55.8,63.9)], r'''
  CM.card($('cards'), tl, 7, 'LA VERDAD', '¿SON INMORTALES?', 0, 4);
  const zn = svgOf('no', 'radial-gradient(circle at 50% 60%, #2f3a4a, #0a0e14 70%)'); const nb = bearAt(zn, 860, 860, 1.3, 1, 0); walkers('no', [nb], 0); const crown = mk('path', { d: 'M780 520 L800 420 L860 480 L920 400 L980 480 L1040 420 L1060 520Z', fill: '#FFD23F' }, zn);
  const stamp = big('no', '<span style="color:#E5484D">NO</span>', 300, W('no') - .2, 'font-size:300px'); tl.to(crown, { opacity: 0, y: -60, duration: .4 }, W('no'));
  const zf = svgOf('frag', 'linear-gradient(#e8efe0, #c9d8b8)'); const fb = bearAt(zf, 600, 860, 1, 1, 0); walkers('frag', [fb], 0);
  const life = bar(zf, 1000, 520, 700, 90, '#5bd08a', '', ''); const lt = mk('text', { x: 1350, y: 490, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#1a2a1a' }, zf); lt.textContent = 'DE MESES A ~2 AÑOS'; lt.textContent = 'DE MESES A UN PAR DE AÑOS';
  tl.from(life.r, { attr: { width: 0 }, duration: 1 }, W('viven') - .2).from(lt, { opacity: 0, duration: .3 }, W('meses') - .2);
  CM.head(H, tl, 'ACTIVOS, <em>FRÁGILES</em>', 'el calor o una sequía mal llegada pueden matarlos', 10.5, 18.3); big('frag', 'SU SUPERPODER: <em>PAUSARSE</em>', 200, W('superpoder') - .3, 'font-size:110px');
  const zw = svgOf('wait', '#10151c'); const wt = mk('g', {}, zw); const wtun = TD.tun(wt); wtun.setAttribute('transform', 'translate(700 760) scale(1.2)'); const clk = mk('g', { transform: 'translate(1350 520)' }, zw); mk('circle', { r: 200, fill: '#e8eef4', stroke: '#9fb3c8', 'stroke-width': 12 }, clk);
  const hand = mk('line', { x1: 0, y1: 0, x2: 0, y2: -160, stroke: '#1a2a3a', 'stroke-width': 12, 'stroke-linecap': 'round' }, clk); gm.onFrame($('wait'), (l, i) => hand.setAttribute('transform', `rotate(${i.time * 540})`));
  CM.head(H, tl, '<em>AÑOS</em> EN PAUSA', 'su límite exacto aún no se conoce', 21.6, 27.4);
  const zo = svgOf('fos', 'linear-gradient(#3a2a1a, #1a120c)'); const amber = mk('g', {}, zo); mk('path', { d: 'M560 300 Q960 160 1360 320 Q1500 560 1300 820 Q960 940 600 820 Q420 560 560 300Z', fill: '#e89a2a', opacity: .85 }, amber); mk('path', { d: 'M640 360 Q900 260 1100 330', stroke: '#ffd88a', 'stroke-width': 18, fill: 'none', opacity: .6 }, amber);
  const ab = bearAt(amber, 900, 700, .7, 1, 0); ab.w.setAttribute('opacity', .75); tl.from(amber, { scale: .6, opacity: 0, duration: .6, ease: 'back.out(1.6)', transformOrigin: '960px 580px' }, 27.8);
  big('fos', '<em>16 MILLONES</em> DE AÑOS', 120, W('dieciséis') - .4, 'font-size:110px', 38.8); big('fos', 'ANTEPASADOS: <em>+500 MILLONES</em>', 120, W('quinientos') - .4, 'font-size:100px');
  CM.head(H, tl, 'SUPERVIVIENTES <em>ANTIGUOS</em>', 'fósiles en ámbar', 28.0, 36.5);
  const zs = svgOf('sun', '#030817'); const sun = mk('circle', { cx: 960, cy: 540, r: 160, fill: '#FFD23F' }, zs); mk('circle', { cx: 1650, cy: 760, r: 40, fill: '#1e6fd0' }, zs);
  tl.to(sun, { attr: { r: 520 }, fill: '#E5484D', duration: 5, ease: 'power1.in' }, 42.6); CM.head(H, tl, 'SOLO LA <em>MUERTE DEL SOL</em>', 'acabaría con todos · estudio de 2017', 41.6, 47.8);
  const zm = svgOf('moss', 'linear-gradient(#8a8f99, #5a5f66)'); for (let r = 0; r < 6; r++) for (let c = 0; c < 10; c++) mk('rect', { x: c * 196 + (r % 2) * 98, y: r * 190, width: 186, height: 180, fill: '#7d828c', stroke: '#6a6e76', 'stroke-width': 6 }, zm);
  const mg = mk('g', {}, zm); TD.moss(mg, 960, 1120, 7, 30); const tiny = [0, 1, 2, 3, 4].map(i => bearAt(zm, 300 + i * 340, 900 + (i % 2) * 60, .35, i % 2 ? -1 : 1, 0)); walkers('moss', tiny, 0);
  tl.fromTo(zm, { scale: 1 }, { scale: 1.25, duration: 8, ease: 'none', transformOrigin: '50% 80%' }, 47.9); CM.head(H, tl, 'MIRA EL <em>MUSGO</em>', 'puede haber miles de osos de agua esperando la lluvia', 48.2, 55.6);
  const end = document.createElement('div'); end.style.cssText = 'position:absolute;inset:0;z-index:6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;background:radial-gradient(1200px 800px at 50% 45%, #2f6a3a, #0a1a10 75%)';
  end.innerHTML = '<div style="font:400 120px/1 \'Bebas Neue\';text-align:center">¿QUÉ ANIMAL <span style="color:#FFD23F">SE LE ACERCA</span>?</div><div style="font:800 40px Inter;letter-spacing:.06em">CUÉNTAMELO EN LOS COMENTARIOS</div><div class="sub" style="margin-top:30px;padding:22px 60px;border-radius:16px;background:#d0312d;font:800 44px Inter;letter-spacing:.08em">SUSCRÍBETE</div><div style="margin-top:20px;font:400 90px Bebas Neue;letter-spacing:.14em">CURIOSI<span style="color:#FFD23F">MUNDO</span></div>';
  $('end').append(end);
  tl.from(end, { opacity: 0, duration: .5 }, W('qué') - .4).from(end.children[0], { scale: 1.2, opacity: 0, duration: .5, ease: 'expo.out' }, W('qué') - .3)
    .from(end.children[1], { y: 20, opacity: 0, duration: .3 }, W('cuéntamelo') - .2).from(end.children[2], { scale: 0, duration: .4, ease: 'back.out(2.5)' }, W('suscríbete') - .2)
    .to(end.children[2], { scale: 1.08, duration: .4, yoyo: true, repeat: 3, ease: 'sine.inOut' }, W('suscríbete') + .3).from(end.children[3], { y: 30, opacity: 0, letterSpacing: '.4em', duration: .7, ease: 'expo.out' }, W('curiosimundo') - .2);
  fadeIn(['frag', 'wait', 'fos', 'sun', 'moss']);
''')
