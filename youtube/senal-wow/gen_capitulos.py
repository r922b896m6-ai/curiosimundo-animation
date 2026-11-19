D='/home/user/curiosimundo-animation/youtube/senal-wow/'
COMMON = r'''
  const svgOf = (id, bg) => { const s = CM.svgIn($(id)); if (bg) $(id).style.background = bg; return s; };
  const fadeIn = ids => ids.forEach(id => tl.from($(id), { opacity: 0, duration: .3 }, +$(id).dataset.start));
  const big = (id, html, top, at, extra = '', end) => { const t = CM.text($(id), 'big', html, top, extra); tl.from(t, { scale: 1.3, opacity: 0, duration: .4, ease: 'expo.out' }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; };
  const mid = (id, html, top, at, extra = '', end) => { const t = CM.text($(id), 'mid', html, top, extra); tl.from(t, { y: 20, opacity: 0, duration: .35 }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; };
  const NIGHT = 'linear-gradient(#050a1a, #1d2a4a)';
  const dish = (s, x, y, sc = 1) => { const g = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s); mk('rect', { x: -10, y: -120, width: 20, height: 120, fill: '#8a96a4' }, g); mk('path', { d: 'M-120 -200 Q0 -60 120 -200 Q0 -150 -120 -200Z', fill: '#d8dde6', stroke: '#8a96a4', 'stroke-width': 4 }, g); mk('line', { x1: 0, y1: -150, x2: 0, y2: -250, stroke: '#8a96a4', 'stroke-width': 5 }, g); return g; };
  const waves = (s, x, y, n = 4, col = '#FFD23F') => Array.from({ length: n }, (_, i) => mk('circle', { cx: x, cy: y, r: 10, fill: 'none', stroke: col, 'stroke-width': 5 }, s));
  const pulse = (sec, ws, t0, period = 1.6, maxR = 300) => gm.onFrame($(sec), (l, info) => ws.forEach((c, i) => { const k = (((info.time - t0) / period) + i / ws.length) % 1; c.setAttribute('r', 10 + k * maxR); c.setAttribute('opacity', info.time < t0 ? 0 : 1 - k); }));
  const stamp = (id, txt, at, top = 420, col = '#E5484D') => { const t = CM.text($(id), 'big', `<span style="border:12px solid ${col};border-radius:20px;padding:0 40px;color:${col}">${txt}</span>`, top, 'font-size:150px;transform:rotate(-8deg)'); tl.from(t, { scale: 2, opacity: 0, duration: .3, ease: 'back.out(2)' }, at); return t; };
'''
def page(n, dur, desc, secs, js, off=4):
    sec='\n'.join(f'<section class="scene" id="{i}" data-start="{s}" data-duration="{round(e-s+.1,2)}"></section>' for i,s,e in secs)
    html=f'''<!doctype html>
<!-- La señal Wow! · Capítulo {n} · {desc} -->
<html data-width="1920" data-height="1080" data-fps="30" data-duration="{dur}">
<head><link rel="stylesheet" href="lib/cm.css"><script src="lib/cm.js"></script><script src="lib/wow.js"></script></head>
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

page(0, 19.0, 'Introducción.', [('s0',0,10.9),('t',10.6,19.0)], r'''
  $('s0').style.background = '#1a1612'; const p = WOW.printout($('s0'), { left: 560, top: 40, w: 800, h: 1000 }); p.ring.style.opacity = 0; p.wow.style.opacity = 0;
  tl.fromTo(p.d, { scale: 1.6 }, { scale: 1, duration: 10.6, ease: 'none', transformOrigin: '42% 50%' }, 0).to(p.ring, { opacity: 1, duration: .3 }, W('escribió') - .4).to(p.wow, { opacity: 1, duration: .3 }, W('wow!') - .2);
  const n = CM.text($('s0'), 'big', '<em>72</em> SEGUNDOS', 420, 'font-size:180px;text-shadow:0 10px 60px #000'); tl.fromTo(n, { scale: 1.2 }, { scale: 1, duration: .6, ease: 'expo.out' }, 0).to(n, { opacity: 0, duration: .3 }, 2.4);
  const y = CM.text($('s0'), 'big', '<em>1977</em>', 420, 'font-size:200px;text-shadow:0 10px 60px #000'); tl.from(y, { opacity: 0, scale: 1.3, duration: .4 }, 2.6).to(y, { opacity: 0, duration: .3 }, 4.6);
  const t = $('t'); t.style.background = 'radial-gradient(1200px 800px at 50% 45%, #1d2a5a, #050a1a 75%)';
  t.innerHTML = '<div class="mid" style="top:250px;color:#FFD23F">CURIOSIMUNDO PRESENTA</div><div class="big" style="top:330px;font-size:200px">LA SEÑAL <em>«WOW!»</em></div><div class="mid" style="top:600px">1977 · 72 segundos sin explicación</div>';
  const [a, h, s] = t.children; tl.from(t, { opacity: 0, duration: .4 }, 10.6).from(a, { y: 20, opacity: 0, duration: .4 }, 10.8).from(h, { scale: 1.3, opacity: 0, filter: 'blur(16px)', duration: .8, ease: 'expo.out' }, 11.0)
    .to(h, { scale: 1.05, duration: 7, ease: 'sine.inOut' }, 11.8).from(s, { y: 30, opacity: 0, duration: .4 }, W('casi') - .2);
''', off=0)

page(1, 53.7, 'La gran oreja: Big Ear, su forma, la Tierra que gira, SETI desde 1973, tiras de papel, el ruido.',
 [('ear',3.6,28.4),('seti',28.3,38.8),('print',38.7,53.7)], r'''
  CM.card($('cards'), tl, 1, 'OHIO', 'LA GRAN OREJA', 0, 4);
  const ze = svgOf('ear', 'linear-gradient(#050a1a, #2a3a5a 58%, #2f5a2a 58%)'); const st = mk('g', {}, ze); WOW.stars(st, 140, 3840, 600); const e = WOW.bigEar(ze);
  gm.onFrame($('ear'), (l, i) => st.setAttribute('transform', `translate(${-Math.max(0, i.time - 24.0) * 120} 0)`));
  tl.fromTo(ze, { scale: 1.25 }, { scale: 1, duration: 9, ease: 'power1.out', transformOrigin: '50% 70%' }, 3.6);
  CM.head(H, tl, '<em>BIG EAR</em>', 'la «gran oreja» · Universidad Estatal de Ohio', 4.4, 12.3); CM.head(H, tl, 'MÁS GRANDE QUE <em>3 CAMPOS</em> DE FÚTBOL', 'dos reflectores y un suelo de aluminio', 12.5, 20.9);
  CM.head(H, tl, 'NO SE <em>MOVÍA</em>', 'la rotación de la Tierra hacía pasar el cielo por delante', 21.1, 28.2);
  const zs = svgOf('seti', NIGHT); WOW.stars(zs, 160); dish(zs, 960, 1000, 1.6); const ws = waves(zs, 960, 640, 5, '#5bc0ff'); pulse('seti', ws, 29.0, 2, 420);
  big('seti', '<em>SETI</em>', 180, W('seti') - .3, 'font-size:180px'); mid('seti', 'búsqueda de <b>inteligencia extraterrestre</b>', 380, W('seti'));
  CM.head(H, tl, 'DESDE <em>1973</em>', 'buscando señales de otras civilizaciones', 28.6, 38.6);
  $('print').style.background = '#1a1612'; const p = WOW.printout($('print'), { left: 1000, top: 60, w: 800, h: 960 }); p.ring.style.display = 'none'; p.wow.style.display = 'none'; p.d.querySelectorAll('.wc').forEach(c => c.textContent = '1');
  tl.fromTo(p.d, { y: 900 }, { y: 0, duration: 1.5, ease: 'power2.out' }, 38.7).to(p.d, { y: -200, duration: 13, ease: 'none' }, 40.2);
  CM.head(H, tl, 'TIRAS DE <em>PAPEL</em>', 'números y letras, columna tras columna', 39.0, 47.0); CM.head(H, tl, 'SOLO <em>RUIDO</em>', 'unos y doses: el murmullo del universo', 47.2, 53.6);
  fadeIn(['seti', 'print']);
''')

page(2, 61.5, '6EQUJ5: 15 de agosto de 1977, Jerry Ehman, el círculo rojo y el Wow!, la escala, 30 veces el ruido, 72 segundos.',
 [('sky',3.6,13.0),('kit',12.9,20.5),('print',20.4,33.2),('curve',33.1,48.6),('pass',48.5,61.5)], r'''
  CM.card($('cards'), tl, 2, '15 · 8 · 1977', '6EQUJ5', 0, 4);
  const zs = svgOf('sky', NIGHT); WOW.stars(zs, 200); const sag = [[820, 520], [900, 460], [990, 470], [1060, 540], [980, 620], [880, 620], [1120, 430]].map(([x, y]) => mk('circle', { cx: x, cy: y, r: 9, fill: '#FFD23F' }, zs));
  const sl = mk('path', { d: 'M820 520 L900 460 L990 470 L1060 540 L980 620 L880 620 Z M990 470 L1120 430', stroke: '#FFD23F', 'stroke-width': 3, fill: 'none', opacity: .7 }, zs); tl.from(sl, { draw: 0, duration: 1.5 }, W('sagitario') - .5);
  big('sky', '<em>SAGITARIO</em>', 760, W('sagitario') - .3, 'font-size:110px'); CM.head(H, tl, '15 DE AGOSTO DE <em>1977</em>', '22:16 · Big Ear mira hacia Sagitario', 4.4, 12.8);
  const zk = svgOf('kit', 'linear-gradient(#5a4a3a, #2a2018)'); mk('rect', { x: 260, y: 640, width: 1400, height: 60, fill: '#8a6a4a' }, zk); mk('rect', { x: 320, y: 700, width: 30, height: 380, fill: '#6a4a2a' }, zk); mk('rect', { x: 1570, y: 700, width: 30, height: 380, fill: '#6a4a2a' }, zk);
  for (let i = 0; i < 5; i++) mk('rect', { x: 560 + i * 160, y: 580 - i * 6, width: 300, height: 70, fill: '#f4f1e6', stroke: '#c9c3b0', 'stroke-width': 3, transform: `rotate(${(i - 2) * 4} ${700 + i * 160} 620)` }, zk);
  mk('path', { d: 'M1500 200 L1500 380 M1420 380 L1580 380 L1540 300 L1460 300Z', stroke: '#3a3a3a', 'stroke-width': 8, fill: '#FFD23F' }, zk); CM.civil(zk, 1300, 640, 2.3, '#2a3a5a');
  CM.head(H, tl, '<em>JERRY EHMAN</em>', 'astrónomo voluntario · en la mesa de su cocina', 13.4, 20.3);
  $('print').style.background = '#1a1612'; const p = WOW.printout($('print'), { left: 560, top: 40, w: 800, h: 1000 }); p.ring.style.opacity = 0; p.wow.style.opacity = 0;
  const cells = p.d.querySelectorAll('.wc'); ['seis', 'e', 'q', 'u', 'j', 'cinco'].forEach((w, i) => tl.to(cells[i], { color: '#d0312d', duration: .15 }, W(w) - .1));
  tl.fromTo(p.d, { scale: 1.5 }, { scale: 1, duration: 3, ease: 'power2.inOut', transformOrigin: '42% 50%' }, 20.4).to(p.ring, { opacity: 1, duration: .3 }, W('rodeó') - .2).to(p.wow, { opacity: 1, duration: .3 }, W('wow!') - .3);
  const zc = svgOf('curve', '#0e1622'); const cv = WOW.curve(zc, 460, 860, 180, 15); tl.from(cv.bars, { attr: { height: 0, y: 860 }, duration: .4, stagger: .15 }, 33.6);
  mid('curve', '1 – 9, después <b>A – Z</b>', 160, W('letras') - .4, 'font-size:56px'); big('curve', 'U = UNAS <em>30 VECES</em> EL RUIDO', 250, W('treinta') - .4, 'font-size:96px');
  CM.head(H, tl, 'NO ERA UN <em>MENSAJE</em>', 'cada carácter mide la intensidad', 33.4, 41.6);
  const zp = svgOf('pass', NIGHT); const sky = mk('g', {}, zp); WOW.stars(sky, 260, 3840, 1080); const src = mk('circle', { cx: 0, cy: 380, r: 14, fill: '#FFD23F' }, sky);
  mk('path', { d: 'M760 1080 L900 300 L1020 300 L1160 1080Z', fill: 'rgb(91 192 255 / .14)', stroke: '#5bc0ff', 'stroke-width': 3 }, zp);
  const meter = mk('rect', { x: 1640, y: 900, width: 80, height: 0, fill: '#FFD23F' }, zp); mk('rect', { x: 1636, y: 300, width: 88, height: 604, fill: 'none', stroke: '#9fb3c8', 'stroke-width': 4 }, zp);
  gm.onFrame($('pass'), (l, i) => { const t = i.time - 49.0, x = 200 + t * 140; src.setAttribute('cx', x); const k = Math.exp(-(((x - 960) / 260) ** 2)); meter.setAttribute('height', 600 * k); meter.setAttribute('y', 900 - 600 * k); });
  big('pass', '<em>72</em> SEGUNDOS', 140, W('setenta') - .3, 'font-size:120px'); mid('pass', 'como si viniera de <b>más allá del sistema solar</b>', 280, W('lejos') - .4);
  fadeIn(['kit', 'print', 'curve', 'pass']);
''')

page(3, 53.0, 'Por qué es especial: 1420 MHz, el hidrógeno, Cocconi y Morrison (1959), banda protegida, señal estrecha, el mejor candidato.',
 [('spec',3.6,14.9),('fis',14.8,26.8),('prot',26.7,34.7),('narrow',34.6,46.1),('cand',46.0,53.0)], r'''
  CM.card($('cards'), tl, 3, '1420 MHz', 'POR QUÉ ES ESPECIAL', 0, 4);
  const zs = svgOf('spec', '#0e1622'); const sp = WOW.spectrum(zs, 200, 760, 1520); tl.from(sp.spike, { draw: 0, duration: .6 }, W('megahercios') - .4);
  const at = mk('g', {}, zs); mk('circle', { cx: 1560, cy: 260, r: 40, fill: '#E5484D' }, at); mk('circle', { cx: 1560, cy: 260, r: 120, fill: 'none', stroke: '#9fb3c8', 'stroke-width': 4 }, at); const el = mk('circle', { r: 16, fill: '#5bc0ff' }, at);
  gm.onFrame($('spec'), (l, i) => { el.setAttribute('cx', 1560 + Math.cos(i.time * 3) * 120); el.setAttribute('cy', 260 + Math.sin(i.time * 3) * 120); }); tl.from(at, { opacity: 0, duration: .4 }, W('hidrógeno') - .3);
  CM.head(H, tl, 'UNOS <em>1420 MHz</em>', 'la frecuencia natural del hidrógeno', 4.4, 14.7);
  const zf = svgOf('fis', 'linear-gradient(#2a3a2a, #1a2418)'); mk('rect', { x: 300, y: 160, width: 1320, height: 520, rx: 12, fill: '#24382c', stroke: '#6a5032', 'stroke-width': 20 }, zf);
  const bt = mk('text', { x: 960, y: 440, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 120, fill: '#e8efe6' }, zf); bt.textContent = '1420 MHz = «LLAMADA UNIVERSAL»'; CM.civil(zf, 600, 1000, 2.2, '#2a2a34'); CM.civil(zf, 1320, 1000, 2.2, '#3a3a48');
  tl.from(bt, { opacity: 0, duration: .5 }, W('elegiría') - .3); CM.head(H, tl, '<em>1959</em>', 'Giuseppe Cocconi y Philip Morrison', 15.1, 26.6);
  const zp = svgOf('prot', 'linear-gradient(#9cc4e6, #e8efe0)'); mk('rect', { x: 900, y: 300, width: 40, height: 700, fill: '#8a96a4' }, zp); mk('path', { d: 'M780 300 L1060 300 L920 180Z', fill: '#8a96a4' }, zp);
  const no = mk('g', {}, zp); mk('circle', { cx: 1400, cy: 520, r: 200, fill: 'none', stroke: '#E5484D', 'stroke-width': 30 }, no); mk('line', { x1: 1260, y1: 380, x2: 1540, y2: 660, stroke: '#E5484D', 'stroke-width': 30 }, no); const nt = mk('text', { x: 1400, y: 550, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 70, fill: '#1a2a3a' }, no); nt.textContent = '1420';
  tl.from(no, { scale: 0, duration: .4, ease: 'back.out(2)', transformOrigin: '1400px 520px' }, W('protegida') - .3); CM.head(H, tl, 'BANDA <em>PROTEGIDA</em>', 'no se permite emitir en ella', 27.0, 34.5);
  const zn = svgOf('narrow', '#0e1622'); mk('path', { d: 'M160 820 Q480 380 800 820', stroke: '#5bc0ff', 'stroke-width': 8, fill: 'rgb(91 192 255 / .15)' }, zn); mk('path', { d: 'M1120 820 L1440 820 L1446 300 L1452 820 L1760 820', stroke: '#FFD23F', 'stroke-width': 8, fill: 'none' }, zn);
  const l1 = mk('text', { x: 480, y: 920, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#5bc0ff' }, zn); l1.textContent = 'NATURALEZA: ANCHO'; const l2 = mk('text', { x: 1446, y: 920, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#FFD23F' }, zn); l2.textContent = 'EMISORA: ESTRECHO';
  CM.head(H, tl, 'UNA SOLA <em>NOTA</em>', 'la señal era muy estrecha', 34.9, 45.9);
  const zc = svgOf('cand', NIGHT); WOW.stars(zc, 200); big('cand', 'EL MEJOR <em>CANDIDATO</em>', 360, 46.2, 'font-size:140px'); mid('cand', 'a mensaje extraterrestre de la historia', 560, W('mensaje') - .3);
  fadeIn(['fis', 'prot', 'narrow', 'cand']);
''')

page(4, 57.1, 'El silencio: dos receptores, solo en uno; un mes de búsqueda; Robert Gray y el VLA; la estrella de 2020 y Breakthrough Listen (2022); nunca se repitió.',
 [('horns',3.6,22.1),('month',22.0,28.2),('gray',28.1,39.5),('star',39.4,53.6),('never',53.5,57.1)], r'''
  CM.card($('cards'), tl, 4, 'NUNCA MÁS', 'EL SILENCIO', 0, 4);
  const zh = svgOf('horns', 'linear-gradient(#050a1a, #2a3a5a 58%, #2f5a2a 58%)'); WOW.stars(zh, 100, 1920, 600); const e = WOW.bigEar(zh);
  tl.fromTo(zh, { scale: 1 }, { scale: 2.2, duration: 2, ease: 'power2.inOut', transformOrigin: '960px 760px' }, 6.5);
  const g1 = mk('circle', { cx: 880, cy: 760, r: 0, fill: 'rgb(255 210 63 / .6)' }, zh); tl.to(g1, { attr: { r: 90 }, duration: .4, yoyo: true, repeat: 3 }, W('apareció') - .2);
  const x2 = mk('path', { d: 'M1000 720 L1080 800 M1080 720 L1000 800', stroke: '#E5484D', 'stroke-width': 16, opacity: 0 }, zh); tl.to(x2, { opacity: 1, duration: .2 }, W('otra', 2) - .3);
  CM.head(H, tl, 'DOS <em>RECEPTORES</em>', 'mirando el mismo punto con minutos de diferencia', 4.4, 14.9); CM.head(H, tl, 'EN UNO SÍ… <em>EN EL OTRO NO</em>', '¿se apagó en esos minutos?', 15.1, 21.9);
  const zm = svgOf('month', '#10151c'); const pages = Array.from({ length: 8 }, (_, i) => { const g = mk('g', {}, zm); mk('rect', { x: 760, y: 300, width: 400, height: 460, rx: 20, fill: '#f4f1e6', stroke: '#c9c3b0', 'stroke-width': 4 }, g); mk('rect', { x: 760, y: 300, width: 400, height: 100, rx: 20, fill: '#d0312d' }, g); const t = mk('text', { x: 960, y: 640, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 200, fill: '#2a2a3a' }, g); t.textContent = String(8 + i * 4); return g; });
  tl.to(pages.slice(0, 7), { opacity: 0, y: -200, duration: .25, stagger: .45 }, 22.3); CM.head(H, tl, 'MÁS DE <em>UN MES</em>', 'apuntando a la misma zona', 22.3, 28.0); stamp('month', 'NADA', W('nada.') - .2, 800);
  const zg = svgOf('gray', 'linear-gradient(#e8a86a, #3a2a4a)'); mk('rect', { y: 900, width: 1920, height: 180, fill: '#a8916a' }, zg); dish(zg, 300, 960, .7); [0, 1, 2, 3, 4].forEach(i => dish(zg, 820 + i * 230, 920 + (i % 2) * 20, 1.1));
  CM.head(H, tl, '<em>ROBERT GRAY</em>', 'primero con una antena casera…', 28.4, 35.6); CM.head(H, tl, 'EL <em>VLA</em>', 'Nuevo México', 35.7, 39.3); stamp('gray', 'NADA', W('nada.', 2) - .2, 300);
  const zt = svgOf('star', NIGHT); WOW.stars(zt, 300); const sun = mk('circle', { cx: 960, cy: 520, r: 60, fill: '#FFD23F' }, zt); const halo = mk('circle', { cx: 960, cy: 520, r: 140, fill: 'rgb(255 210 63 / .15)' }, zt);
  tl.from([sun, halo], { scale: 0, opacity: 0, duration: .5, transformOrigin: '960px 520px' }, W('estrella') - .3);
  CM.head(H, tl, 'UNA ESTRELLA <em>COMO EL SOL</em>', 'propuesta como origen en 2020', 39.7, 46.3); CM.head(H, tl, '<em>BREAKTHROUGH LISTEN</em>', '2022 · la observó con atención', 46.5, 53.4); stamp('star', 'NADA', W('nada.', 3) - .2, 780);
  const zv = $('never'); zv.style.background = 'radial-gradient(1200px 800px at 50% 45%, #2a1a1a, #0a0606 75%)'; big('never', 'NUNCA SE HA <em>REPETIDO</em>', 400, 53.7, 'font-size:150px');
  fadeIn(['month', 'gray', 'star', 'never']);
''')

page(5, 67.8, '¿Qué pudo ser?: satélites y aviones (poco probable), el cometa (2017, rechazado), nube de hidrógeno + estrella magnética (Arecibo Wow!, 2024, sin demostrar), extraterrestres.',
 [('q',3.6,9.6),('sat',9.5,20.2),('com',20.1,33.2),('cloud',33.1,57.5),('alien',57.4,67.8)], r'''
  CM.card($('cards'), tl, 5, 'HIPÓTESIS', '¿QUÉ PUDO SER?', 0, 4);
  const zq = svgOf('q', NIGHT); WOW.stars(zq, 200); big('q', '<em>?</em>', 300, 4.4, 'font-size:400px');
  const zs = svgOf('sat', NIGHT); WOW.stars(zs, 160); const sat = mk('g', {}, zs); mk('rect', { x: -40, y: -40, width: 80, height: 80, fill: '#c9cdd4' }, sat); mk('rect', { x: -220, y: -20, width: 160, height: 40, fill: '#2f4f9a' }, sat); mk('rect', { x: 60, y: -20, width: 160, height: 40, fill: '#2f4f9a' }, sat);
  const pl = mk('path', { d: 'M0 0 L160 0 L190 15 L160 30 L0 30Z M60 0 L110 -60 L130 0Z M60 30 L110 90 L130 30Z', fill: '#e8eef4' }, zs);
  gm.onFrame($('sat'), (l, i) => { const t = i.time - 9.5; sat.setAttribute('transform', `translate(${200 + t * 120} 360)`); pl.setAttribute('transform', `translate(${1700 - t * 140} 680)`); });
  CM.head(H, tl, '¿UN <em>SATÉLITE</em> O UN AVIÓN?', 'frecuencia protegida y una fuente fija en el cielo', 9.8, 20.0); mid('sat', '<b>poco probable</b>', 760, W('difícil:') - .3, 'font-size:60px');
  const zc = svgOf('com', NIGHT); WOW.stars(zc, 200); const com = mk('g', {}, zc); mk('path', { d: 'M0 0 L-600 -80 L-600 80Z', fill: 'rgb(180 220 255 / .25)' }, com); mk('circle', { r: 40, fill: '#e8f4ff' }, com);
  gm.onFrame($('com'), (l, i) => com.setAttribute('transform', `translate(${400 + (i.time - 20.1) * 90} ${300 + (i.time - 20.1) * 30})`));
  CM.head(H, tl, '¿UN <em>COMETA</em>?', 'propuesta de 2017', 20.4, 33.0); stamp('com', 'RECHAZADO', W('rechazaron') - .2, 600);
  const zl = svgOf('cloud', NIGHT); WOW.stars(zl, 200); const cl = mk('g', {}, zl); for (let i = 0; i < 14; i++) mk('circle', { cx: 1250 + (gm.random('cx' + i) - .5) * 400, cy: 520 + (gm.random('cy' + i) - .5) * 260, r: 80 + gm.random('cr' + i) * 80, fill: '#5bc0ff', opacity: .12 }, cl);
  const mag = mk('g', {}, zl); mk('circle', { cx: 360, cy: 540, r: 34, fill: '#fff' }, mag); for (let i = 0; i < 6; i++) mk('ellipse', { cx: 360, cy: 540, rx: 60 + i * 30, ry: 160 + i * 20, fill: 'none', stroke: '#b06aff', 'stroke-width': 3, opacity: .6 }, mag);
  const beam = mk('path', { d: 'M400 540 L1100 420 L1100 660Z', fill: 'rgb(255 210 63 / .0)' }, zl); const tB = W('encender') - .4;
  gm.onFrame($('cloud'), (l, i) => { const t = i.time, k = t > tB && t < tB + 3 ? Math.sin((t - tB) / 3 * Math.PI) : 0; beam.setAttribute('fill', `rgb(255 210 63 / ${(k * .5).toFixed(2)})`); cl.setAttribute('opacity', 1 + k * 3); });
  CM.head(H, tl, 'ARECIBO <em>WOW!</em> · 2024', 'señales parecidas, más débiles, en nubes frías de hidrógeno', 33.4, 43.8); CM.head(H, tl, 'UNA ESTRELLA <em>MUY MAGNÉTICA</em>', 'pudo encender por un momento una nube', 44.0, 52.9);
  stamp('cloud', 'SIN DEMOSTRAR', W('demostrada') - .4, 760, '#FFD23F');
  const za = svgOf('alien', NIGHT); WOW.stars(za, 260); dish(za, 1500, 1000, 1.6); const ws = waves(za, 400, 300, 4, '#5bd08a'); pulse('alien', ws, 57.6, 1.8, 360);
  CM.head(H, tl, '¿<em>EXTRATERRESTRES</em>?', 'no se pueden descartar del todo', 57.7, 67.6); mid('alien', 'pero <b>una sola señal</b> no basta para demostrar nada', 860, W('sola') - .3);
  fadeIn(['sat', 'com', 'cloud', 'alien']);
''')

page(6, 42.7, 'El legado: Big Ear desmontado (1998, campo de golf), la tira de papel famosa, la búsqueda sigue, pregunta final.',
 [('golf',3.6,13.0),('doc',12.9,20.2),('now',20.1,26.8),('last',26.7,35.3),('end',35.2,42.7)], r'''
  CM.card($('cards'), tl, 6, 'DESPUÉS', 'EL LEGADO', 0, 4);
  const zg = svgOf('golf', 'linear-gradient(#9cc4e6, #e8efe0 58%, #4f8a3a 58%)'); const ear = WOW.bigEar(zg); const fl = mk('g', {}, zg); mk('rect', { x: 956, y: 560, width: 8, height: 260, fill: '#fff' }, fl); mk('path', { d: 'M964 560 L1080 600 L964 640Z', fill: '#E5484D' }, fl); mk('ellipse', { cx: 960, cy: 830, rx: 40, ry: 12, fill: '#2a3a2a' }, fl);
  tl.to(ear.g, { opacity: 0, duration: 1.5 }, W('desmontado') - .2).from(fl, { opacity: 0, y: 40, duration: .6 }, W('golf') - .4); CM.head(H, tl, '<em>1998</em>', 'Big Ear se desmonta para ampliar un campo de golf', 4.4, 12.8);
  $('doc').style.background = '#1a1612'; const p = WOW.printout($('doc'), { left: 1000, top: 40, w: 800, h: 1000 }); p.d.querySelectorAll('.wc').forEach(c => c.style.color = '#d0312d'); tl.fromTo(p.d, { scale: 1 }, { scale: 1.25, duration: 7, ease: 'none', transformOrigin: '42% 45%' }, 12.9);
  CM.head(H, tl, 'UN DOCUMENTO <em>FAMOSO</em>', 'el «Wow!» de Jerry Ehman', 13.2, 20.0);
  const zn = svgOf('now', NIGHT); WOW.stars(zn, 260); [0, 1, 2, 3, 4, 5].forEach(i => dish(zn, 260 + i * 280, 1000 - (i % 2) * 30, 1)); CM.head(H, tl, 'SIGUEN <em>ESCUCHANDO</em>', 'telescopios mucho más potentes', 20.4, 26.6);
  const zl = svgOf('last', 'radial-gradient(circle at 50% 50%, #1d2a5a, #050a1a 70%)'); WOW.stars(zl, 300); const ws = waves(zl, 960, 540, 5, '#FFD23F'); pulse('last', ws, 30.2, 2.2, 600);
  big('last', '¿UN FENÓMENO <em>NATURAL</em>…', 300, W('quizá') - .3, 'font-size:110px'); big('last', '…O UNA <em>LLAMADA</em>?', 480, W('quizá', 2) - .3, 'font-size:130px');
  const end = document.createElement('div'); end.style.cssText = 'position:absolute;inset:0;z-index:6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;background:radial-gradient(1200px 800px at 50% 45%, #1d2a5a, #050a1a 75%)';
  end.innerHTML = '<div style="font:400 120px/1 \'Bebas Neue\';text-align:center">¿TÚ QUÉ CREES <span style="color:#FFD23F">QUE FUE</span>?</div><div style="font:800 40px Inter;letter-spacing:.06em">CUÉNTAMELO EN LOS COMENTARIOS</div><div class="sub" style="margin-top:30px;padding:22px 60px;border-radius:16px;background:#d0312d;font:800 44px Inter;letter-spacing:.08em">SUSCRÍBETE</div><div style="margin-top:20px;font:400 90px Bebas Neue;letter-spacing:.14em">CURIOSI<span style="color:#FFD23F">MUNDO</span></div>';
  $('end').append(end);
  tl.from(end, { opacity: 0, duration: .5 }, W('tú') - .4).from(end.children[0], { scale: 1.2, opacity: 0, duration: .5, ease: 'expo.out' }, W('tú') - .3)
    .from(end.children[1], { y: 20, opacity: 0, duration: .3 }, W('cuéntamelo') - .2).from(end.children[2], { scale: 0, duration: .4, ease: 'back.out(2.5)' }, W('suscríbete') - .2)
    .to(end.children[2], { scale: 1.08, duration: .4, yoyo: true, repeat: 3, ease: 'sine.inOut' }, W('suscríbete') + .3).from(end.children[3], { y: 30, opacity: 0, letterSpacing: '.4em', duration: .7, ease: 'expo.out' }, W('curiosimundo') - .2);
  fadeIn(['doc', 'now', 'last']);
''')
