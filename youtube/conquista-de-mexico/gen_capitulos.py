import sys
D='/home/user/curiosimundo-animation/youtube/conquista-de-mexico/'
def page(n, dur, desc, secs, js, maps=True, off=4):
    sec='\n'.join(f'<section class="scene" id="{i}" data-start="{s}" data-duration="{round(e-s+.1,2)}"></section>' for i,s,e in secs)
    fetch = "Promise.all([fetch('voz.json').then(r => r.json()), fetch('lib/mexico1519.json').then(r => r.json())])"
    html=f'''<!doctype html>
<!-- La conquista de México · Capítulo {n} · {desc} -->
<html data-width="1920" data-height="1080" data-fps="30" data-duration="{dur}">
<head><link rel="stylesheet" href="lib/cm.css"><script src="lib/cm.js"></script><script src="lib/cq.js"></script></head>
<body>
<audio src="voz.mp3" data-start="{off}"></audio>
<audio src="musica.mp3" data-volume="0.5" data-duck="0.4" data-fade-out="1"></audio>
<audio src="sfx.mp3" data-volume="0.5"></audio>
{sec}
<div class="vig"></div><div id="heads"></div><div id="cards"></div><div id="caps"></div>
<script>
const OFF = {off};
gm.wait({fetch}.then(([words, geo]) => {{
  const W = CM.W(words, OFF), G = {{ global: true }}, tl = gm.timeline(null, G), H = document.getElementById('heads'), C = CM.MAPCOL, $ = id => document.getElementById(id), mk = CM.mk;
  const svgOf = id => CM.svgIn($(id)), cy = k => geo.cities[k];
  const fadeIn = ids => ids.forEach(id => tl.from($(id), {{ opacity: 0, duration: .3 }}, +$(id).dataset.start));
  const mexMap = (id) => {{ const m = CM.map($(id), geo); m.color(tl, 'MÉXICO', '#7a5a3a', 0, .01).color(tl, 'CENTROAMÉRICA', '#6a5a3a', 0, .01).color(tl, 'CUBA', '#4a5a6a', 0, .01).color(tl, 'LAGO', '#3f86b4', 0, .01); return m; }};
  const Z = (m, at, c, s, d = .01) => m.zoom(tl, c, s, at, d);
{js}
  return CM.captions(words, OFF);
}}));
</script>
</body>
</html>
'''
    open(D+f'cap{n}/video.html','w').write(html)

# ---------------- CAP 0
page(0, 15.5, 'Introducción: batalla en la calzada, "1519 – 1521", título.', [('b',0,8.3),('t',8.0,15.5)], r'''
  CM.battle($('b'), { id: 'b', left: 'ES', right: 'MEX', terrain: 'dusk', t0: 0, t1: 8.3, n: 7, falls: [], mg: false, def: 5, artillery: [.3, 1.8, 3.4, 5.0, 6.6], labels: false, pan: [0, -1280] });
  const y = CM.text($('b'), 'big', '1519 – <em>1521</em>', 300); tl.fromTo(y, { scale: 1.25 }, { scale: 1, duration: .8, ease: 'expo.out' }, 0).to(y, { opacity: 0, y: -60, duration: .25 }, W('cientos') - .5);
  const n = CM.text($('b'), 'big', 'UNOS <em>CIENTOS</em> DE ESPAÑOLES', 260, 'font-size:110px'), n2 = CM.text($('b'), 'mid', '+ <b>decenas de miles</b> de aliados indígenas', 400);
  tl.from(n, { scale: 1.3, opacity: 0, duration: .45, ease: 'expo.out' }, W('cientos') - .3).from(n2, { y: 30, opacity: 0, duration: .35 }, W('decenas') - .2);
  const t = $('t'); t.style.background = 'radial-gradient(1200px 800px at 50% 45%, #6a3a1a, #1a0e08 75%)';
  t.innerHTML = '<div class="mid" style="top:250px;color:#FFD23F">CURIOSIMUNDO PRESENTA</div><div class="big" style="top:330px;font-size:190px">LA CONQUISTA<br><em>DE MÉXICO</em></div><div class="mid" style="top:760px">1519 – 1521 · en 10 minutos</div>';
  const [p, h, s] = t.children;
  tl.from(t, { opacity: 0, duration: .4 }, 8.0).from(p, { y: 20, opacity: 0, duration: .4 }, 8.2).from(h, { scale: 1.3, opacity: 0, filter: 'blur(16px)', duration: .8, ease: 'expo.out' }, 8.4)
    .to(h, { scale: 1.05, duration: 6, ease: 'sine.inOut' }, 9.2).from(s, { y: 30, opacity: 0, duration: .4 }, W('diez') - .3);
''', off=0)

# ---------------- CAP 1
page(1, 93.7, '1325–1519 · El mundo mexica: Tenochtitlan, calzadas, Triple Alianza, 200.000 habitantes, Templo Mayor, tributo, guerreros, Tlaxcala, Moctezuma.',
 [('c1',3.6,17.1),('map',17.0,27.1),('c2',27.0,50.1),('tr',50.0,57.9),('war',57.8,78.5),('map2',78.4,83.7),('mo',83.6,93.7)], r'''
  CM.card($('cards'), tl, 1, '1325 – 1519', 'EL MUNDO MEXICA', 0, 4);
  const z1 = svgOf('c1'), c1 = CQ.city(z1); gm.onFrame($('c1'), (l, i) => c1.tick(i.time));
  tl.fromTo(c1.g, { scale: 1.15 }, { scale: 1, duration: 13.5, ease: 'none', transformOrigin: '50% 60%' }, 3.6);
  CM.head(H, tl, '<em>TENOCHTITLAN</em>', 'fundada hacia 1325 · en un islote del lago de Texcoco', 4.3, 10.8);
  CM.head(H, tl, 'TRES <em>CALZADAS</em>', 'con puentes que se podían retirar', 11.0, 17.0);
  const m = mexMap('map'); Z(m, 0, cy('Tenochtitlan'), 14);
  const at3 = [W('aliaron'), W('texcoco', 2), W('tlacopan')]; ['Tenochtitlan', 'Texcoco', 'Tlacopan'].forEach((k, i) => m.pin(tl, k, k.toUpperCase(), at3[i] - .2, 26.9, { r: 1.4, size: 3.2, dy: 2.4 }));
  Z(m, W('dominaron') - .4, [300, 610], 3.2, 1.2);
  m.text(tl, 'CENTRO DE MÉXICO', 300, 640, W('dominaron') + .4, 26.9, { size: 12, fill: '#FFD23F' });
  CM.head(H, tl, 'LA <em>TRIPLE ALIANZA</em>', '1428 · Tenochtitlan, Texcoco y Tlacopan', 17.3, 26.9);
  const z2 = svgOf('c2'), c2 = CQ.city(z2); gm.onFrame($('c2'), (l, i) => c2.tick(i.time));
  const pop = CM.text($('c2'), 'big', 'UNAS <em>200.000</em> PERSONAS', 220, 'font-size:120px'); tl.from(pop, { scale: 1.3, opacity: 0, duration: .4, ease: 'expo.out' }, W('doscientas') - .3).to(pop, { opacity: 0, duration: .25 }, 33.3);
  const items = ['CALZADAS', 'CANALES', 'CHINAMPAS', 'ACUEDUCTO', 'MERCADOS'].map((t, i) => CM.text($('c2'), 'mid', t, 240 + i * 70, 'font-size:44px'));
  [W('calzadas', 2), W('canales'), W('chinampas'), W('acueducto'), W('mercados')].forEach((at, i) => tl.from(items[i], { x: -60, opacity: 0, duration: .25 }, at - .2)); tl.to(items, { opacity: 0, duration: .25 }, 39.9);
  tl.to(c2.g, { scale: 2, duration: 1.2, ease: 'power2.inOut', transformOrigin: '960px 420px' }, 40.0);
  const hz = CM.text($('c2'), 'mid', '<b>HUITZILOPOCHTLI</b> · guerra', 320, 'left:120px;right:auto;width:700px;text-align:left'), tz = CM.text($('c2'), 'mid', '<b>TLÁLOC</b> · lluvia', 320, 'left:auto;right:120px;width:600px;text-align:right');
  tl.from(hz, { opacity: 0, x: -40, duration: .3 }, W('huitzilopochtli') - .2).from(tz, { opacity: 0, x: 40, duration: .3 }, W('tláloc') - .2);
  CM.head(H, tl, 'UNA <em>GRAN CIUDAD</em>', 'más grande que casi todas las de Europa', 27.3, 39.9); CM.head(H, tl, 'EL <em>TEMPLO MAYOR</em>', 'dos santuarios en lo alto', 40.2, 49.9);
  const z3 = svgOf('tr'); $('tr').style.background = 'linear-gradient(#e8d9b0, #c9b48c)'; mk('rect', { y: 860, width: 1920, height: 220, fill: '#b9a27a' }, z3);
  const porters = [0, 1, 2, 3].map(i => ({ f: CM.figure(z3, 'MEX', { weapon: 'none', shield: false }), x0: -200 - i * 260, y: 900, s: 1.7 }));
  const loads = porters.map(() => mk('rect', { width: 80, height: 60, rx: 10, fill: '#c9a46a', stroke: '#7a5a3a', 'stroke-width': 4 }, z3));
  gm.onFrame($('tr'), (l, i) => { CQ.walk(porters, i.time, 50.0, 150); porters.forEach((p, k) => loads[k].setAttribute('transform', `translate(${p.x0 + (i.time - 50) * 150 - 70} 700)`)); });
  ['maíz', 'cacao', 'algodón', 'plumas…'].forEach((w, i) => { const t = CM.text($('tr'), 'big', w.replace('…', '').toUpperCase(), 330, `font-size:100px;left:${120 + i * 430}px;right:auto;width:400px`); tl.from(t, { scale: 1.6, opacity: 0, duration: .25, ease: 'expo.out' }, W(w) - .15); });
  CM.head(H, tl, 'EL <em>TRIBUTO</em>', 'los pueblos sometidos pagaban… y muchos estaban hartos', 50.2, 57.7);
  const z4 = svgOf('war'); $('war').style.background = 'linear-gradient(#cfd8e3, #e8d9b0)'; mk('rect', { y: 900, width: 1920, height: 180, fill: '#a8916a' }, z4);
  const ws = [0, 1, 2].map(i => CM.figure(z4, 'MEX')); ws.forEach((f, i) => CM.pose(f, { x: 600 + i * 360, y: 960, s: 3.2, dir: 1 }));
  const no = CM.text($('war'), 'big', 'SIN <em>CABALLOS</em> · SIN <em>HIERRO</em> · SIN <em>RUEDAS</em>', 150, 'font-size:90px'); tl.from(no, { opacity: 0, y: 30, duration: .3 }, W('caballos') - .3).to(no, { opacity: 0, duration: .25 }, 62.9);
  const mq = CM.text($('war'), 'big', '<em>MACUAHUITL</em>', 160, 'font-size:120px'), mq2 = CM.text($('war'), 'mid', 'madera con filos de <b>obsidiana</b> · escudos · armaduras de algodón', 300);
  tl.from(mq, { scale: 1.4, opacity: 0, duration: .35, ease: 'expo.out' }, W('macuahuitl') - .2).from(mq2, { opacity: 0, y: 20, duration: .3 }, W('obsidiana') - .4).to([mq, mq2], { opacity: 0, duration: .25 }, 70.8);
  const cp = CM.text($('war'), 'big', 'CAPTURAR, <em>NO MATAR</em>', 160, 'font-size:120px'); tl.from(cp, { scale: 1.4, opacity: 0, duration: .35, ease: 'expo.out' }, W('capturar') - .3);
  const m2 = mexMap('map2'); Z(m2, 0, cy('Tlaxcala'), 9); m2.pin(tl, 'Tenochtitlan', 'TENOCHTITLAN', 78.6, null, { r: 1.2, size: 3, dy: 2 }); m2.pin(tl, 'Tlaxcala', 'TLAXCALA', W('tlaxcala') - .2, null, { r: 1.8, size: 4, fill: '#E5484D', dy: 3 });
  CM.head(H, tl, 'EL GRAN ENEMIGO: <em>TLAXCALA</em>', 'nunca conquistada por los mexicas', 78.7, 83.6);
  const z5 = svgOf('mo'), c5 = CQ.city(z5, { sky: ['#e8a86a', '#6a4a6a'], dusk: true }); const mo = CM.figure(z5, 'TLA'); CM.pose(mo, { x: 700, y: 1060, s: 3.4, dir: 1 });
  const fleet = [0, 1, 2].map(i => { const s = mk('g', {}, z5); CM.caravel(s); return s; }); gm.onFrame($('mo'), (l, i) => { c5.tick(i.time); fleet.forEach((s, k) => s.setAttribute('transform', `translate(${2100 - Math.max(0, i.time - 89.8) * 420 + k * 170} ${560 + k * 18}) scale(.35)`)); });
  CM.head(H, tl, 'MOCTEZUMA <em>XOCOYOTZIN</em>', 'tlatoani desde 1502', 83.9, 88.2); CM.head(H, tl, '17 AÑOS <em>DESPUÉS…</em>', 'llegaron unos extraños por el mar', 88.3, 93.6);
  fadeIn(['c2', 'tr', 'war', 'map2', 'mo', 'map']);
''')

# shared JS snippets
HORSES = r'''
  const horseIn = (id, t0, n = 2, y = 900, dir = 1, sp = 420) => { const s = $(id).querySelector('svg'), hs = Array.from({ length: n }, (_, i) => ({ h: CM.horse(s, i % 2 ? '#3a2a1a' : '#8a5a36'), r: CM.figure(s, 'ES', { weapon: 'none' }) }));
    gm.onFrame($(id), (l, info) => { const t = info.time - t0; hs.forEach((o, i) => { const x = (dir > 0 ? -300 : 2200) + dir * (t * sp - i * 380); o.h.g.setAttribute('transform', `translate(${x} ${y + i * 40}) scale(${dir * 1.3} 1.3)`); CM.horsePose(o.h, info.time); CM.pose(o.r, { x: x + dir * 8, y: y + i * 40 - 118, s: 1.4, dir }); }); }); };
'''
# ---------------- CAP 2
page(2, 98.4, '1519 · La llegada: Cuba, Cozumel, Centla (retirada maya), Malintzin, enviados de Moctezuma, Veracruz, barcos hundidos, Cempoala.',
 [('map',3.6,23.1),('centla',23.0,32.5),('mal',32.4,47.0),('coast',46.9,73.0),('ships',72.9,82.6),('cem',82.5,98.4)], HORSES + r'''
  CM.card($('cards'), tl, 2, '1519', 'LA LLEGADA', 0, 4);
  const m = mexMap('map'); Z(m, 0, [1000, 520], 1.05);
  m.pin(tl, 'Cuba', 'CUBA', W('cuba') - .2, 23.0, { r: 9, size: 30, dy: 26 }); m.line(tl, 'mar', W('zarpó') - .2, { color: '#FFD23F', width: 6, dash: '14 10', arrow: true, dur: 16 });
  const f = CM.text($('map'), 'mid', '<b>11</b> barcos · unos <b>500</b> soldados · <b>16</b> caballos', 860); tl.from(f, { y: 30, opacity: 0, duration: .35 }, W('once') - .3).to(f, { opacity: 0, duration: .25 }, 17.6);
  m.pin(tl, 'Cozumel', 'COZUMEL', W('cozumel') - .2, 23.0, { r: 8, size: 28, dy: 24 });
  CM.head(H, tl, 'HERNÁN <em>CORTÉS</em>', 'zarpa de Cuba · febrero de 1519', 4.4, 13.3); CM.head(H, tl, 'DIEGO <em>VELÁZQUEZ</em>', 'el gobernador de Cuba intentó detenerlo', 13.4, 17.7);
  CM.head(H, tl, 'JERÓNIMO DE <em>AGUILAR</em>', 'náufrago español que hablaba maya', 17.9, 22.9);
  CM.battle($('centla'), { id: 'ce', left: 'ES', right: 'MAYA', terrain: 'fields', t0: 23.0, t1: 32.5, n: 7, falls: [], mg: false, def: 5, artillery: [23.4, 24.6, 25.8, 27.2, 29.0], outcome: { type: 'retreat', at: W('decidieron') - .2 }, pan: [0, -1280] });
  horseIn('centla', W('caballos', 2) - 1, 2, 900);
  CM.head(H, tl, 'BATALLA DE <em>CENTLA</em>', 'Tabasco · marzo de 1519', 23.3, 32.4);
  const z = svgOf('mal'); $('mal').style.background = 'linear-gradient(#e8a86a, #6a4a6a)'; mk('rect', { y: 900, width: 1920, height: 180, fill: '#8a6a4a' }, z);
  const co = CM.figure(z, 'ES', { weapon: 'none' }); CM.pose(co, { x: 420, y: 980, s: 3, dir: 1 }); const ag = CM.figure(z, 'ES', { weapon: 'none' }); CM.pose(ag, { x: 1500, y: 980, s: 2.8, dir: -1 });
  const mlW = mk('g', {}, z), ml = CQ.woman(mlW, 960, 980, 3, { band: '#2f8f5a' });
  const chain = CM.text($('mal'), 'mid', 'NÁHUATL → <b>MALINTZIN</b> → MAYA → <b>AGUILAR</b> → ESPAÑOL', 240, 'font-size:44px'); tl.from(chain, { opacity: 0, y: 20, duration: .4 }, W('voz') - .6);
  tl.from(mlW, { opacity: 0, y: 40, duration: .4 }, W('una') - .2);
  CM.head(H, tl, 'TRAS LA <em>DERROTA</em>', 'los mayas entregan regalos y 20 mujeres esclavizadas', 32.9, 40.5); CM.head(H, tl, '<em>MALINTZIN</em>', 'la Malinche: hablaba náhuatl y maya', 40.7, 46.9);
  const zc = svgOf('coast'), cs = CQ.coast(zc, { n: 5 });
  const env = [0, 1, 2].map(i => ({ f: CM.figure(zc, 'MEX', { weapon: 'none', shield: false }), x0: 1900 + i * 150, y: 960 + (i % 2) * 20, s: 2 }));
  const gifts = env.map(() => mk('rect', { width: 70, height: 50, rx: 8, fill: '#d8b23a', stroke: '#8a6a2a', 'stroke-width': 4 }, zc));
  const spa = [0, 1, 2].map(i => CM.figure(zc, 'ES')); spa.forEach((f, i) => CM.pose(f, { x: 300 + i * 150, y: 980, s: 2.1, dir: 1 }));
  gm.onFrame($('coast'), (l, info) => { const t = info.time, d = Math.min(t - 48.0, 6); env.forEach((o, i) => { CM.pose(o.f, { x: o.x0 - Math.max(0, d) * 160, y: o.y, s: o.s, dir: -1, run: d < 6 && d > 0 ? .4 : 0, ph: t * 6 + i }); gifts[i].setAttribute('transform', `translate(${o.x0 - Math.max(0, d) * 160 - 30} ${o.y - 380})`); }); });
  const sun = mk('g', {}, zc); mk('circle', { cx: 760, cy: 360, r: 150, fill: '#e8b92a', stroke: '#a8801a', 'stroke-width': 10 }, sun); for (let i = 0; i < 16; i++) mk('rect', { x: 752, y: 180, width: 16, height: 40, fill: '#e8b92a', transform: `rotate(${i * 22.5} 760 360)` }, sun);
  const moon = mk('g', {}, zc); mk('circle', { cx: 1160, cy: 360, r: 150, fill: '#d6d9de', stroke: '#9aa0aa', 'stroke-width': 10 }, moon); mk('circle', { cx: 1210, cy: 330, r: 120, fill: '#c3c8d0' }, moon);
  tl.from(sun, { scale: 0, opacity: 0, duration: .4, ease: 'back.out(1.8)', transformOrigin: '760px 360px' }, W('sol') - .5).from(moon, { scale: 0, opacity: 0, duration: .4, ease: 'back.out(1.8)', transformOrigin: '1160px 360px' }, W('luna') - .5);
  const pt = mk('g', {}, zc); mk('rect', { x: 1340, y: 640, width: 260, height: 180, rx: 6, fill: '#efe7d2', stroke: '#7a5a3a', 'stroke-width': 5 }, pt); const pz = mk('g', { transform: 'translate(1470 760) scale(.4)' }, pt); CM.caravel(pz); const hp = mk('g', { transform: 'translate(1400 800) scale(.35)' }, pt); CM.horse(hp);
  tl.from(pt, { opacity: 0, y: 40, duration: .4 }, W('pintores') - .2).to(pt, { opacity: 0, duration: .3 }, 62.8);
  CM.head(H, tl, '<em>VERACRUZ</em>', 'abril de 1519 · llegan enviados de Moctezuma', 47.2, 53.0); CM.head(H, tl, 'EMBAJADORES, <em>PINTORES</em> Y REGALOS', 'Moctezuma quería saber quiénes eran', 53.1, 62.8);
  CM.head(H, tl, 'EL <em>ORO</em>', 'solo despertó más ambición', 62.9, 66.4); CM.head(H, tl, 'UN <em>SOL</em> DE ORO, UNA <em>LUNA</em> DE PLATA', 'regalos de Moctezuma', 66.5, 72.9);
  const zs = svgOf('ships'), c2 = CQ.coast(zs, { n: 4, sky: ['#7d8b99', '#d8cdb4'] });
  gm.onFrame($('ships'), (l, info) => { const k = gm.clamp((info.time - 78.0) / 3); c2.ships.forEach((s, i) => s.setAttribute('transform', `translate(${900 + i * 200} ${560 + (i % 2) * 40 + k * 120}) rotate(${k * (i % 2 ? -12 : 10)}) scale(${.45 + (i % 2) * .1})`)); });
  CM.head(H, tl, 'VILLA RICA DE LA <em>VERA CRUZ</em>', 'Cortés manda hundir sus barcos', 73.2, 82.4);
  const nq = CM.text($('ships'), 'big', 'NO LOS QUEMÓ: <em>LOS HUNDIÓ</em>', 260, 'font-size:110px'); tl.from(nq, { scale: 1.3, opacity: 0, duration: .4, ease: 'expo.out' }, W('quemó') - .4);
  const zq = svgOf('cem'), cc = CQ.city(zq, { temple: true, causeway: false }); gm.onFrame($('cem'), (l, i) => cc.tick(i.time));
  const cac = CM.figure(zq, 'TOT', { weapon: 'none', shield: false }); CM.pose(cac, { x: 1180, y: 1060, s: 3.2, dir: -1 }); cac.b.setAttribute('transform', 'scale(1.35 1)');
  const cort = CM.figure(zq, 'ES', { weapon: 'none' }); CM.pose(cort, { x: 700, y: 1060, s: 3, dir: 1 });
  const tots = [0, 1, 2, 3].map(i => ({ f: CM.figure(zq, 'TOT'), x0: 2000 + i * 140, y: 1040, s: 2 }));
  gm.onFrame($('cem'), (l, info) => tots.forEach((o, i) => CM.pose(o.f, { x: o.x0 - Math.max(0, Math.min(info.time - 91.6, 3)) * 280, y: o.y, s: o.s, dir: -1, run: info.time > 91.6 && info.time < 94.6 ? .5 : 0, ph: info.time * 7 + i })));
  CM.head(H, tl, '<em>CEMPOALA</em>', 'el «cacique gordo» se queja del tributo mexica', 82.8, 91.6); CM.head(H, tl, 'LOS PRIMEROS <em>ALIADOS</em>', 'los totonacas se unen a Cortés', 91.7, 98.3);
  fadeIn(['map', 'centla', 'mal', 'coast', 'ships', 'cem']);
''')

# ---------------- CAP 3
page(3, 79.7, '1519 · Tlaxcala y Cholula: combates y alianza con Tlaxcala, Xicoténcatl, la matanza de Cholula (tarjeta sobria), Paso de Cortés, el valle.',
 [('map',3.6,8.1),('tlx',8.0,22.4),('ali',22.3,37.0),('xic',36.9,44.9),('cho',44.8,57.4),('map2',57.3,73.0),('val',72.9,79.7)], HORSES + r'''
  CM.card($('cards'), tl, 3, '1519', 'TLAXCALA Y CHOLULA', 0, 4);
  const m = mexMap('map'); Z(m, 0, [320, 590], 5); m.line(tl, 'tierra', 4.6, { color: '#FFD23F', width: 2, dash: '5 4', dur: 3 }); m.pin(tl, 'Veracruz', 'VERACRUZ', 3.8, null, { r: 1.6, size: 6, dy: 4 }); m.pin(tl, 'Tlaxcala', 'TLAXCALA', W('tlaxcala') - .3, null, { r: 2, size: 7, fill: '#E5484D', dy: 4.5 });
  CM.head(H, tl, 'HACIA EL <em>INTERIOR</em>', 'agosto de 1519', 4.4, 8.0);
  CM.battle($('tlx'), { id: 'tx', left: 'ES', right: 'TLX', terrain: 'mountains', t0: 8.0, t1: 22.4, n: 7, falls: [], mg: false, def: 6, artillery: [8.4, 9.8, 11.4, 13.0, 15.0, 17.2, 19.4], pan: [0, -1280] });
  horseIn('tlx', 9.0, 2, 900);
  CM.head(H, tl, 'LOS <em>TLAXCALTECAS</em>', 'semanas de combates · septiembre de 1519', 8.3, 12.8); CM.head(H, tl, 'UN SEÑORÍO <em>CERCADO</em>', 'gobernado por un consejo · sin sal ni algodón', 12.9, 22.3);
  const za = svgOf('ali'); $('ali').style.background = 'linear-gradient(#9cc4e6, #efe2bf)'; mk('path', { d: 'M0 700 L400 420 L800 700 L1200 380 L1920 700 L1920 1080 L0 1080Z', fill: '#7a8f5a' }, za); mk('rect', { y: 900, width: 1920, height: 180, fill: '#a8916a' }, za);
  const e = CM.figure(za, 'ES', { weapon: 'none' }), t = CM.figure(za, 'TLX', { weapon: 'none', shield: false }); CM.pose(e, { x: 760, y: 980, s: 3, dir: 1, armRot: -10 }); CM.pose(t, { x: 1160, y: 980, s: 3, dir: -1, armRot: -10 });
  CM.flag(za, 'ESB', 300, 380, 220, 150); CM.flag(za, 'TLX', 1400, 380, 220, 150);
  CM.head(H, tl, 'LA <em>ALIANZA</em>', 'Tlaxcala y Cortés, contra los mexicas', 24.2, 30.7); CM.head(H, tl, 'UNA <em>OPORTUNIDAD</em>', 'para vengarse de su viejo enemigo', 30.8, 36.9);
  const zx = svgOf('xic'); $('xic').style.background = 'linear-gradient(#5a5f66, #b3a898)'; mk('rect', { y: 900, width: 1920, height: 180, fill: '#6a5a44' }, zx); const x = CM.figure(zx, 'TLX'); CM.pose(x, { x: 960, y: 1000, s: 3.6, dir: -1 });
  CM.head(H, tl, 'XICOTÉNCATL <em>EL JOVEN</em>', 'el capitán tlaxcalteca se opuso a la alianza', 37.1, 44.7); tl.fromTo(zx, { scale: 1 }, { scale: 1.08, duration: 7.8, ease: 'none', transformOrigin: '50% 80%' }, 36.9);
  CQ.memorial($('cho'), 'OCTUBRE DE 1519', '<em>CHOLULA</em>', 'Cortés y sus aliados mataron a miles de cholultecas en pocas horas', tl, 45.0, W);
  const doubt = CM.text($('cho'), 'mid', '¿Una emboscada? <b>Muchos historiadores lo dudan</b>', 760, 'font-size:40px;text-transform:none;letter-spacing:0'); tl.from(doubt, { opacity: 0, y: 20, duration: .5 }, W('emboscada') - .3);
  const m2 = mexMap('map2'); Z(m2, 0, [260, 600], 9); m2.line(tl, 'tierra', 57.5, { color: '#FFD23F', width: 1.2, dash: '3 2', dur: 2 });
  m2.pin(tl, 'Cholula', 'CHOLULA', 57.6, null, { r: 1, size: 3.4, dy: 2.4 }); m2.pin(tl, 'Tenochtitlan', 'TENOCHTITLAN', 58.9, null, { r: 1.2, size: 3.6, fill: '#E5484D', dy: 2.4 });
  Z(m2, 65.0, [214, 598], 16, 1.2); m2.text(tl, 'POPOCATÉPETL', cy('Popocatépetl')[0] + 4, cy('Popocatépetl')[1] + 3, W('popocatépetl') - .2, null, { size: 2.2, fill: '#fff' });
  m2.text(tl, 'IZTACCÍHUATL', cy('Iztaccíhuatl')[0] + 4, cy('Iztaccíhuatl')[1] - 1, W('iztaccíhuatl') - .2, null, { size: 2.2, fill: '#fff' }); m2.pin(tl, 'Paso de Cortés', 'PASO DE CORTÉS', W('paso') - .2, null, { r: .6, size: 2.2, fill: '#FFD23F', dy: -2.4 });
  CM.head(H, tl, 'MÁS <em>EMBAJADAS</em>', 'Moctezuma intentó frenarlo', 57.5, 64.9); CM.head(H, tl, 'EL <em>PASO DE CORTÉS</em>', 'entre los volcanes', 65.2, 72.8);
  const zv = svgOf('val'), cv = CQ.city(zv); gm.onFrame($('val'), (l, i) => cv.tick(i.time)); mk('path', { d: 'M0 1080 L0 820 L500 760 L900 900 L1300 980 L1920 860 L1920 1080Z', fill: '#4a3a2a' }, zv);
  const watch = [0, 1, 2].map(i => CM.figure(zv, i ? 'TLX' : 'ES')); watch.forEach((f, i) => CM.pose(f, { x: 260 + i * 170, y: 800 + i * 10, s: 1.8, dir: 1 }));
  tl.fromTo(cv.g, { scale: 1.1 }, { scale: 1, duration: 6.8, ease: 'none', transformOrigin: '50% 50%' }, 72.9); CM.head(H, tl, 'EL <em>VALLE DE MÉXICO</em>', 'la ciudad sobre el lago', 73.2, 79.6);
  fadeIn(['map', 'tlx', 'ali', 'xic', 'cho', 'map2', 'val']);
''')

# ---------------- CAP 4
page(4, 68.8, '1519–1520 · Tenochtitlan: encuentro en Iztapalapa, «cosa de encantamiento», Tlatelolco, Moctezuma rehén, el oro, Narváez (capturado), Tóxcatl (tarjeta sobria), la ciudad se levanta.',
 [('meet',3.6,14.2),('enc',14.1,28.5),('reh',28.4,43.1),('map',43.0,50.2),('nar',50.1,55.5),('tox',55.4,65.6),('rev',65.5,68.8)], r'''
  CM.card($('cards'), tl, 4, '1519 – 1520', 'TENOCHTITLAN', 0, 4);
  const zm = svgOf('meet'), cm = CQ.city(zm); gm.onFrame($('meet'), (l, i) => cm.tick(i.time)); mk('rect', { y: 900, width: 1920, height: 180, fill: '#bfa77c' }, zm);
  const mo = CM.figure(zm, 'TLA'); CM.pose(mo, { x: 1180, y: 1000, s: 3, dir: -1 }); const es = [0, 1, 2].map(i => CM.figure(zm, 'ES')); es.forEach((f, i) => CM.pose(f, { x: 760 - i * 200, y: 1000 + i * 10, s: 3 - i * .2, dir: 1 }));
  const nob = [0, 1].map(() => CM.figure(zm, 'MEX', { weapon: 'none', shield: false })); nob.forEach((f, i) => CM.pose(f, { x: 1420 + i * 200, y: 1000, s: 2.8, dir: -1 })); const mal = CQ.woman(zm, 960, 1000, 2.8, { band: '#2f8f5a' });
  CM.head(H, tl, '8 DE NOVIEMBRE DE <em>1519</em>', 'Moctezuma recibe a Cortés en la calzada de Iztapalapa', 4.4, 10.7); CM.head(H, tl, 'EL PALACIO DE <em>AXAYÁCATL</em>', 'los españoles, alojados por Moctezuma', 10.8, 14.1);
  const ze = svgOf('enc'), ce = CQ.city(ze); gm.onFrame($('enc'), (l, i) => ce.tick(i.time)); tl.fromTo(ce.g, { scale: 1 }, { scale: 1.12, duration: 5.6, ease: 'none', transformOrigin: '50% 45%' }, 14.1);
  const q = CM.text($('enc'), 'big', '«COSA DE <em>ENCANTAMIENTO</em>»', 250, 'font-size:110px'); tl.from(q, { scale: 1.3, opacity: 0, duration: .5, ease: 'expo.out' }, W('encantamiento') - .8).to(q, { opacity: 0, duration: .25 }, 19.7);
  const mk2 = mk('g', {}, ze); mk('rect', { y: 760, width: 1920, height: 320, fill: '#c9b48c' }, mk2); for (let i = 0; i < 8; i++) { mk('rect', { x: 60 + i * 240, y: 820, width: 200, height: 20, fill: '#8a6a4a' }, mk2); mk('path', { d: `M${50 + i * 240} 820 L${160 + i * 240} 760 L${270 + i * 240} 820Z`, fill: ['#c0392b', '#e8d9b0', '#2f8f5a', '#d8b23a'][i % 4] }, mk2); }
  const crowd = Array.from({ length: 14 }, (_, i) => CM.figure(mk2, 'MEX', { weapon: 'none', shield: false })); crowd.forEach((f, i) => CM.pose(f, { x: 40 + i * 140, y: 1040 + (i % 2) * 30, s: 1.4, dir: i % 2 ? 1 : -1 }));
  tl.from(mk2, { opacity: 0, duration: .4 }, 19.8); CM.head(H, tl, 'BERNAL <em>DÍAZ DEL CASTILLO</em>', 'soldado y cronista', 14.4, 19.7); CM.head(H, tl, 'EL MERCADO DE <em>TLATELOLCO</em>', 'decenas de miles de personas', 19.9, 28.3);
  const zr = svgOf('reh'); $('reh').style.background = 'linear-gradient(#5a4a3a, #2a2018)'; mk('rect', { y: 860, width: 1920, height: 220, fill: '#6a5040' }, zr); for (let i = 0; i < 5; i++) mk('rect', { x: 120 + i * 400, y: 200, width: 80, height: 660, fill: '#7a6050' }, zr);
  const m4 = CM.figure(zr, 'TLA'); CM.pose(m4, { x: 960, y: 960, s: 3.2, dir: 1 }); const gs = [0, 1, 2, 3].map(() => CM.figure(zr, 'ES')); gs.forEach((f, i) => CM.pose(f, { x: [520, 700, 1220, 1400][i], y: 970, s: 2.8, dir: i < 2 ? 1 : -1 }));
  const gold = mk('g', {}, zr); for (let i = 0; i < 12; i++) mk('rect', { x: 1500 + (i % 4) * 90 - Math.floor(i / 4) * 45 + 90, y: 880 - Math.floor(i / 4) * 40, width: 80, height: 36, rx: 4, fill: '#e8b92a', stroke: '#a8801a', 'stroke-width': 3 }, gold);
  tl.from(gold.children, { opacity: 0, y: -40, duration: .2, stagger: .08 }, W('fundieron') - .3);
  CM.head(H, tl, 'MOCTEZUMA, <em>REHÉN</em>', 'en su propia ciudad', 28.6, 34.4); CM.head(H, tl, 'VASALLO DEL <em>REY DE ESPAÑA</em>', 'y el oro del palacio, fundido', 34.5, 42.9);
  const m = mexMap('map'); Z(m, 0, [960, 520], 1.05); m.line(tl, 'narvaez', W('envió') - .3, { color: '#E5484D', width: 6, arrow: true, dur: 2 }); m.pin(tl, 'Cempoala', 'CEMPOALA', W('arrestar') - .3, null, { r: 8, size: 26, dy: 24 });
  CM.head(H, tl, 'PÁNFILO DE <em>NARVÁEZ</em>', 'mayo de 1520 · enviado para arrestar a Cortés', 43.3, 50.1);
  CM.battle($('nar'), { id: 'na', left: 'ES', right: 'ES', terrain: 'night', t0: 50.1, t1: 55.5, n: 7, falls: [], mg: false, def: 4, artillery: [50.3, 51.2], outcome: { type: 'capture', at: 52.3 }, labels: false, pan: [-500, -1280] });
  CM.head(H, tl, '<em>CEMPOALA</em>', 'Cortés derrota a Narváez… y se queda con sus hombres', 50.3, 55.4);
  CQ.memorial($('tox'), 'MAYO DE 1520', '<em>TÓXCATL</em>', 'Pedro de Alvarado atacó a los mexicas durante la fiesta, en el Templo Mayor', tl, 55.6, W);
  const zv = svgOf('rev'), cr = CQ.city(zv, { sky: ['#c96a3a', '#4a2a2a'], dusk: true }); const ws = [0, 1, 2, 3, 4].map(() => CM.figure(zv, 'MEX')); ws.forEach((f, i) => CM.pose(f, { x: 300 + i * 330, y: 1060, s: 2.6, dir: 1, armRot: -40 }));
  CM.head(H, tl, 'LA CIUDAD <em>SE LEVANTA</em>', 'junio de 1520', 65.7, 68.7);
  fadeIn(['enc', 'reh', 'map', 'nar', 'tox', 'rev']);
''')

VIRUS = r'''
  const virus = (s, x, y, r = 80) => { const g = mk('g', {}, s), v = mk('g', { transform: `translate(${x} ${y})` }, g); mk('circle', { r, fill: '#c94a4a' }, v); for (let i = 0; i < 12; i++) { const a = i * Math.PI / 6; mk('line', { x1: Math.cos(a) * r, y1: Math.sin(a) * r, x2: Math.cos(a) * r * 1.4, y2: Math.sin(a) * r * 1.4, stroke: '#c94a4a', 'stroke-width': r / 8 }, v); mk('circle', { cx: Math.cos(a) * r * 1.45, cy: Math.sin(a) * r * 1.45, r: r / 6, fill: '#e07a7a' }, v); } return g; };
'''
# ---------------- CAP 5
page(5, 78.3, '1520 · La Noche Triste: muerte de Moctezuma (causa discutida), huida por la calzada de Tacuba, canoas y puentes quitados, Otumba (retirada mexica), refugio en Tlaxcala, Cuitláhuac y la viruela.',
 [('gue',3.6,17.9),('oro',17.8,23.8),('noche',23.7,44.8),('tri',44.7,48.4),('otu',48.3,55.5),('map',55.4,61.9),('rec',61.8,67.6),('cui',67.5,78.3)], HORSES + VIRUS + r'''
  CM.card($('cards'), tl, 5, '1520', 'LA NOCHE TRISTE', 0, 4);
  const zg = svgOf('gue'), cg = CQ.city(zg, { sky: ['#c96a3a', '#4a2a2a'], dusk: true }); gm.onFrame($('gue'), (l, i) => cg.tick(i.time));
  const v1 = CM.text($('gue'), 'mid', 'Según los españoles: <b>las piedras de su pueblo</b>', 300, 'font-size:46px;text-transform:none;letter-spacing:0;left:260px;right:260px;background:rgb(10 6 4 / .7);padding:12px 24px;border-radius:12px'), v2 = CM.text($('gue'), 'mid', 'Según las fuentes indígenas: <b>los españoles</b>', 400, 'font-size:46px;text-transform:none;letter-spacing:0;left:260px;right:260px;background:rgb(10 6 4 / .7);padding:12px 24px;border-radius:12px');
  tl.from(v1, { opacity: 0, y: 20, duration: .3 }, W('dijeron') - .5).from(v2, { opacity: 0, y: 20, duration: .3 }, W('fuentes') - .3);
  CM.head(H, tl, 'UNA CIUDAD <em>EN GUERRA</em>', 'junio de 1520', 4.4, 7.2); CM.head(H, tl, 'MUERE <em>MOCTEZUMA</em>', 'y todavía se discute cómo', 7.3, 17.7);
  const zo = svgOf('oro'); $('oro').style.background = 'linear-gradient(#2a2018, #120c08)'; mk('rect', { y: 860, width: 1920, height: 220, fill: '#3a2a20' }, zo);
  const gold = mk('g', {}, zo); for (let i = 0; i < 16; i++) mk('rect', { x: 700 + (i % 6) * 90, y: 820 - Math.floor(i / 6) * 40, width: 80, height: 36, rx: 4, fill: '#e8b92a', stroke: '#a8801a', 'stroke-width': 3 }, gold);
  const sl = [0, 1, 2].map(() => CM.figure(zo, 'ES')); sl.forEach((f, i) => CM.pose(f, { x: [400, 1500, 1700][i], y: 960, s: 2.8, dir: i ? -1 : 1, armRot: 20 }));
  CM.head(H, tl, 'HUIR <em>CON EL ORO</em>', 'cada soldado tomó lo que quiso', 18.0, 23.6);
  const zn = svgOf('noche'); $('noche').style.background = 'linear-gradient(#050816, #1a2440)'; for (let i = 0; i < 60; i++) mk('circle', { cx: gm.random('nx' + i) * 1920, cy: gm.random('ny' + i) * 400, r: 1 + gm.random('nr' + i) * 2, fill: '#fff', opacity: .6 }, zn);
  mk('rect', { y: 560, width: 1920, height: 520, fill: '#16304a' }, zn); const cw = mk('rect', { y: 700, width: 1920, height: 70, fill: '#5a4a38' }, zn);
  const gaps = [520, 1240].map(x => mk('rect', { x, y: 700, width: 0, height: 70, fill: '#16304a' }, zn));
  const col = Array.from({ length: 9 }, (_, i) => ({ f: CM.figure(zn, i % 3 === 2 ? 'TLX' : 'ES'), x0: -200 - i * 150, y: 720, s: 1.4 }));
  const hz = CM.horse(zn, '#3a2a1a'); const splash = Array.from({ length: 4 }, () => mk('ellipse', { rx: 0, ry: 0, fill: 'none', stroke: '#9fd0ff', 'stroke-width': 4 }, zn));
  const can = Array.from({ length: 12 }, (_, i) => { const g = mk('g', {}, zn); mk('path', { d: 'M-70 0 L70 0 L52 18 L-52 18Z', fill: '#2a1a10' }, g); for (let k = 0; k < 2; k++) { const w = CM.figure(g, 'MEX', { shield: false }); CM.pose(w, { x: -30 + k * 50, y: 0, s: .9, dir: i % 2 ? -1 : 1 }); } return { g, x: 100 + (i % 6) * 320, y: i < 6 ? 640 : 900 + (i % 3) * 40, side: i < 6 ? -1 : 1 }; });
  const tGap = W('puentes') - .4, tCan = W('cientos') - .4, tFall = W('hundieron') - .5;
  gm.onFrame($('noche'), (l, info) => { const t = info.time, d = t - 23.7;
    col.forEach((o, i) => { let x = o.x0 + Math.min(d, 9.6) * 150; const fall = t > tFall && (i === 1 || i === 4) ? gm.clamp((t - tFall - i * .2) / .5) : 0; CM.pose(o.f, { x, y: o.y + fall * 120, s: o.s, dir: 1, run: d < 9.6 ? .4 : 0, ph: t * 6 + i }); o.f.o.style.opacity = 1 - fall; });
    hz.g.setAttribute('transform', `translate(${-60 + Math.min(d, 9.6) * 150} 720) scale(.9)`); CM.horsePose(hz, t, d < 9.6 ? 1 : 0);
    gaps.forEach(g => g.setAttribute('width', 160 * gm.clamp((t - tGap) / .6)));
    can.forEach((c, i) => { const k = gm.clamp((t - tCan) / 2); c.g.setAttribute('transform', `translate(${c.x} ${c.y + c.side * (1 - k) * 260})`); c.g.style.opacity = k; });
    splash.forEach((s, i) => { const k = gm.clamp((t - tFall - i * .3) / 1); s.setAttribute('cx', 560 + i * 200); s.setAttribute('cy', 800); s.setAttribute('rx', k * 90); s.setAttribute('ry', k * 20); s.setAttribute('opacity', 1 - k); }); });
  CM.head(H, tl, '30 DE JUNIO DE <em>1520</em>', 'huida en silencio por la calzada de Tacuba', 23.9, 31.2); CM.head(H, tl, 'LOS <em>DESCUBRIERON</em>', 'puentes quitados y cientos de canoas', 31.3, 41.8);
  const lost = CM.text($('noche'), 'mid', 'Cortés perdió a <b>gran parte de sus hombres</b>', 260); tl.from(lost, { opacity: 0, y: 20, duration: .35 }, W('perdió') - .4);
  const tri = $('tri'); tri.style.background = 'radial-gradient(circle at 50% 50%, #1a2440, #050816 75%)'; const tt = CM.text(tri, 'big', 'LA <em>NOCHE TRISTE</em>', 400, 'font-size:180px'); tl.from(tt, { scale: 1.3, opacity: 0, filter: 'blur(14px)', duration: .7, ease: 'expo.out' }, 44.9);
  CM.battle($('otu'), { id: 'ot', left: 'ES', right: 'MEX', terrain: 'fields', t0: 48.3, t1: 55.5, n: 6, falls: [], mg: false, def: 6, artillery: [48.6, 49.8], outcome: { type: 'retreat', at: W('ganaron') - .2 }, pan: [-300, -1280] });
  horseIn('otu', 49.0, 2, 900); CM.head(H, tl, '<em>OTUMBA</em>', '7 de julio de 1520 · una victoria desesperada', 48.5, 55.4);
  const m = mexMap('map'); Z(m, 0, [222, 570], 10); m.pin(tl, 'Tenochtitlan', 'TENOCHTITLAN', 55.6, null, { r: 1, size: 3, dy: 2 }); m.line(tl, 'noche', 55.8, { color: '#E5484D', width: 1.2, arrow: true, dur: 2.5 });
  m.pin(tl, 'Otumba', 'OTUMBA', 56.6, null, { r: .9, size: 2.8, dy: -2 }); m.pin(tl, 'Tlaxcala', 'TLAXCALA · REFUGIO', W('llegaron') - .2, null, { r: 1.4, size: 3.2, fill: '#FFD23F', dy: 2.6 });
  CM.head(H, tl, 'REFUGIO EN <em>TLAXCALA</em>', 'sus aliados no los entregaron', 55.6, 61.8);
  const zr = svgOf('rec'), cr = CQ.city(zr); gm.onFrame($('rec'), (l, i) => cr.tick(i.time)); const fl = mk('g', {}, zr); mk('rect', { x: 1000, y: 200, width: 8, height: 250, fill: '#3a2a1a' }, fl); CM.flag(fl, 'MEX', 1008, 200, 150, 100);
  CM.head(H, tl, 'LA CIUDAD, <em>RECUPERADA</em>', 'parecía que la invasión había terminado', 62.0, 67.4);
  const zc = svgOf('cui'); $('cui').style.background = 'radial-gradient(circle at 50% 50%, #2a2420, #0a0806 75%)'; const cu = CM.figure(zc, 'TLA'); CM.pose(cu, { x: 760, y: 980, s: 3.4, dir: 1 }); const vv = virus(zc, 1300, 520, 110);
  tl.from(vv, { scale: 0, opacity: 0, duration: .4, ease: 'back.out(2)', transformOrigin: '1300px 520px' }, W('viruela') - .3);
  CM.head(H, tl, '<em>CUITLÁHUAC</em>', 'nuevo tlatoani · murió de viruela en 1520', 67.8, 78.2);
  fadeIn(['oro', 'noche', 'tri', 'otu', 'map', 'rec', 'cui']);
''')

# ---------------- CAP 6
page(6, 74.9, '1521 · El sitio: Cuauhtémoc, la viruela, 13 bergantines, dominio del lago, calzadas bloqueadas y agua cortada, aliados indígenas, casa por casa, Tlatelolco, captura de Cuauhtémoc.',
 [('cua',3.6,13.0),('berg',12.9,28.9),('map',28.8,45.5),('casa',45.4,60.1),('tla',60.0,64.8),('cap',64.7,74.9)], VIRUS + r'''
  CM.card($('cards'), tl, 6, '1521', 'EL SITIO', 0, 4);
  const zc = svgOf('cua'), cc = CQ.city(zc, { sky: ['#8a96a8', '#d6cbb0'] }); gm.onFrame($('cua'), (l, i) => cc.tick(i.time)); const cu = CM.figure(zc, 'MEX'); CM.pose(cu, { x: 760, y: 1060, s: 3.4, dir: 1 });
  const vv = virus(zc, 1400, 380, 90); tl.from(vv, { scale: 0, opacity: 0, duration: .4, ease: 'back.out(2)', transformOrigin: '1400px 380px' }, W('viruela') - .3);
  CM.head(H, tl, '<em>CUAUHTÉMOC</em>', 'el último tlatoani mexica', 4.4, 8.1); CM.head(H, tl, 'LA <em>VIRUELA</em>', 'miles de muertos en todo el valle', 8.2, 12.8);
  const zb = svgOf('berg'); $('berg').style.background = 'linear-gradient(#9cc4e6, #efe2bf)'; mk('rect', { y: 620, width: 1920, height: 460, fill: '#3f86b4' }, zb); mk('rect', { y: 860, width: 900, height: 220, fill: '#a8916a' }, zb);
  const brig = (s) => { const g = mk('g', {}, s); mk('path', { d: 'M-130 -10 L130 -10 L100 30 L-100 30Z', fill: '#5a3e26', stroke: '#3a2a1a', 'stroke-width': 4 }, g); for (let k = 0; k < 6; k++) mk('line', { x1: -80 + k * 32, y1: 20, x2: -96 + k * 32, y2: 54, stroke: '#3a2a1a', 'stroke-width': 4 }, g);
    mk('rect', { x: -4, y: -170, width: 8, height: 160, fill: '#3a2a1a' }, g); mk('path', { d: 'M4 -160 L80 -50 L4 -40Z', fill: '#efe7d2' }, g); mk('rect', { x: 100, y: -24, width: 40, height: 10, fill: '#222' }, g); const fl = mk('g', { transform: 'translate(-2 -200)' }, g); CM.flag(fl, 'ESB', 0, 0, 40, 28); return g; };
  const b1 = brig(zb), b2 = brig(zb), b3 = brig(zb); const car = [0, 1, 2].map(i => ({ f: CM.figure(zb, 'TLX', { weapon: 'none', shield: false }), x0: -100 - i * 180, y: 960, s: 1.8 }));
  const can = Array.from({ length: 8 }, (_, i) => { const g = mk('g', {}, zb); mk('path', { d: 'M-60 0 L60 0 L44 16 L-44 16Z', fill: '#6b4a2a' }, g); const w = CM.figure(g, 'MEX', { shield: false }); CM.pose(w, { x: 0, y: 0, s: .8, dir: -1 }); return g; });
  const flashes = [0, 1, 2].map(() => mk('circle', { r: 0, fill: 'url(#cmFlash)' }, zb)); const tLake = W('bergantines', 2) - .4;
  gm.onFrame($('berg'), (l, info) => { const t = info.time; CQ.walk(car, Math.min(t, 19.5), 12.9, 110); car.forEach(o => o.f.o.style.display = t < 23.0 ? '' : 'none');
    const launch = gm.clamp((t - (W('botó') - .3)) / 1.2), lake = t >= tLake;
    [b1, b2, b3].forEach((b, i) => { const x = lake ? 400 + i * 320 + (t - tLake) * 60 : 500 + i * 300, y = lake ? 760 + i * 30 : 860 - launch * 140 * (i === 0 ? 1 : 0) + (i ? 0 : 0); b.setAttribute('transform', `translate(${x} ${lake ? y : (i === 0 ? 860 - launch * 120 : 2000)}) scale(${lake ? .9 : 1.1})`); });
    can.forEach((c, i) => { const away = lake ? gm.clamp((t - tLake - 1.5) / 3) : 0; c.setAttribute('transform', `translate(${1300 + (i % 4) * 150 + away * 500} ${700 + Math.floor(i / 4) * 140})`); c.style.display = lake ? '' : 'none'; });
    flashes.forEach((f, i) => { const k = ((t - tLake) * 1.2 + i * .33) % 1; f.setAttribute('cx', 580 + i * 320 + (t - tLake) * 60); f.setAttribute('cy', 740 + i * 30); f.setAttribute('r', lake && k < .3 ? 50 : 0); }); });
  CM.head(H, tl, '<em>13 BERGANTINES</em>', 'construidos con ayuda de miles de tlaxcaltecas · Texcoco', 13.2, 22.9); CM.head(H, tl, 'EL LAGO, <em>DOMINADO</em>', 'cañones contra canoas', 23.1, 28.7);
  const m = mexMap('map'); Z(m, 0, [192, 578], 26); m.pin(tl, 'Tenochtitlan', 'TENOCHTITLAN', 29.0, null, { r: .45, size: 1.4, dy: -1.1 });
  ['cTacuba', 'cIztapalapa', 'cTepeyac'].forEach((k, i) => m.line(tl, k, 29.2 + i * .3, { color: '#c9b48c', width: .7, dur: .6 }));
  const water = m.line(tl, 'agua', 29.8, { color: '#5bc0ff', width: .5, dur: .6 }); m.text(tl, 'CHAPULTEPEC', cy('Chapultepec')[0] - 2, cy('Chapultepec')[1] + 1.8, W('chapultepec') - .3, null, { size: 1.1, fill: '#9fe3ff' });
  const xx = m.text(tl, '✕', cy('Chapultepec')[0] + 2.4, cy('Chapultepec')[1] + .4, W('cortaron') - .2, null, { size: 2.2, fill: '#E5484D' }); tl.to(water, { opacity: .2, duration: .3 }, W('cortaron'));
  [['Tlacopan', 'TLACOPAN'], ['Iztapalapa', 'IZTAPALAPA'], ['Tepeyac', 'TEPEYAC']].forEach(([k, l]) => m.pin(tl, k, l, W('bloquearon') - .2, null, { r: .4, size: 1.1, fill: '#E5484D', dy: 1 }));
  const ally = CM.text($('map'), 'mid', '<b>Decenas de miles</b> de guerreros indígenas', 860, 'background:rgb(10 6 4 / .6);left:420px;right:420px;padding:10px 20px;border-radius:12px'); tl.from(ally, { opacity: 0, y: 20, duration: .35 }, W('decenas') - .3);
  CM.head(H, tl, 'EL <em>SITIO</em>', 'mayo de 1521 · agua cortada y calzadas bloqueadas', 29.1, 37.4); CM.head(H, tl, 'LOS <em>ALIADOS</em>', 'la mayoría del ejército era indígena', 37.6, 45.3);
  CM.battle($('casa'), { id: 'cs', left: 'TLX', right: 'MEX', terrain: 'ruins', t0: 45.4, t1: 60.1, n: 8, falls: [], mg: false, def: 6, artillery: [45.8, 47.4, 49.0, 50.8, 52.6, 54.4], pan: [0, -1280] });
  const hw = CM.text($('casa'), 'big', 'HAMBRE · SIN AGUA · <em>EPIDEMIA</em>', 360, 'font-size:90px'); tl.from(hw, { opacity: 0, scale: 1.2, duration: .35 }, W('hambre') - .3);
  CM.head(H, tl, 'CASA POR <em>CASA</em>', 'derribaban las casas para rellenar los canales', 45.6, 52.0); CM.head(H, tl, 'CASI <em>TRES MESES</em>', 'de resistencia mexica', 52.1, 59.9);
  const zt = svgOf('tla'), ct = CQ.city(zt, { sky: ['#8a7a6a', '#c9b49a'] }); tl.fromTo(ct.g, { scale: 1.3 }, { scale: 1.1, duration: 4.8, ease: 'none', transformOrigin: '50% 50%' }, 60.0);
  CM.head(H, tl, '<em>TLATELOLCO</em>', 'el último refugio', 60.2, 64.6);
  const zk = svgOf('cap'); $('cap').style.background = 'linear-gradient(#9aa7b8, #d6cbb0)'; mk('rect', { y: 560, width: 1920, height: 520, fill: '#3f86b4' }, zk);
  const bg = brig(zk); const cn = mk('g', {}, zk); mk('path', { d: 'M-90 0 L90 0 L66 22 L-66 22Z', fill: '#6b4a2a' }, cn); const ca = CM.figure(cn, 'MEX', { weapon: 'none', shield: false }); const ro = CM.figure(cn, 'MEX', { weapon: 'none', shield: false });
  const tCap = W('capturado') - .4;
  gm.onFrame($('cap'), (l, info) => { const t = info.time, k = gm.clamp((t - 65.5) / 3); cn.setAttribute('transform', `translate(${1500 - k * 600} 800) scale(1.4)`); bg.setAttribute('transform', `translate(${200 + k * 500} 780) scale(1.3)`);
    CM.pose(ca, { x: -20, y: 0, s: 1, dir: -1, up: t > tCap }); CM.pose(ro, { x: 40, y: 0, s: 1, dir: -1, up: t > tCap }); });
  CM.head(H, tl, '13 DE AGOSTO DE <em>1521</em>', 'Cuauhtémoc intenta escapar en canoa… y es capturado', 64.9, 71.9);
  const fall = CM.text($('cap'), 'big', 'TENOCHTITLAN <em>HA CAÍDO</em>', 300, 'font-size:130px'); tl.from(fall, { scale: 1.3, opacity: 0, filter: 'blur(12px)', duration: .6, ease: 'expo.out' }, W('caído') - .8);
  fadeIn(['berg', 'map', 'casa', 'tla', 'cap']);
''')

# ---------------- CAP 7
page(7, 75.9, 'Las consecuencias: Ciudad de México y Nueva España, primer virrey (1535), epidemias, Nojpetén (1697), sociedad mestiza, lenguas indígenas, aliados y viruela, pregunta final.',
 [('cdmx',3.6,10.3),('vir',10.2,20.6),('pop',20.5,32.2),('map',32.1,41.3),('mes',41.2,48.3),('len',48.2,57.2),('ide',57.1,67.5),('end',67.4,75.9)], VIRUS + r'''
  CM.card($('cards'), tl, 7, 'DESPUÉS DE 1521', 'LAS CONSECUENCIAS', 0, 4);
  const zc = svgOf('cdmx'), cc = CQ.city(zc, { temple: false }); const ch = mk('g', {}, zc); mk('rect', { x: 760, y: 360, width: 400, height: 300, fill: '#d8c8a2', stroke: '#a8916a', 'stroke-width': 4 }, ch);
  [[800, 240], [1080, 240]].forEach(([x, y]) => { mk('rect', { x, y, width: 50, height: 120, fill: '#d8c8a2' }, ch); mk('path', { d: `M${x - 6} ${y} L${x + 25} ${y - 40} L${x + 56} ${y}Z`, fill: '#a8916a' }, ch); }); mk('path', { d: 'M900 360 Q960 260 1020 360Z', fill: '#c9b48c' }, ch); mk('rect', { x: 930, y: 540, width: 60, height: 120, fill: '#5a3e26' }, ch);
  tl.from(ch, { y: 300, opacity: 0, duration: 1.2, ease: 'power2.out' }, 4.6); CM.head(H, tl, 'CIUDAD DE <em>MÉXICO</em>', 'sobre las ruinas de Tenochtitlan · capital de la Nueva España', 4.4, 10.2);
  const zv = svgOf('vir'); $('vir').style.background = 'linear-gradient(#5a4a3a, #2a2018)'; const co = CM.figure(zv, 'ES', { weapon: 'none' }); CM.pose(co, { x: 500, y: 980, s: 3, dir: 1 });
  const d = CM.doc($('vir'), 'NUEVA ESPAÑA', 'virreinato', ['1535', 'Primer virrey:', 'Antonio de Mendoza'], { x: 980, y: 240, w: 640, h: 480, rot: 2 }); tl.from(d, { y: 160, opacity: 0, rotate: 8, duration: .5, ease: 'expo.out' }, W('virrey') - .8);
  CM.head(H, tl, 'LA <em>CORONA</em> TOMA EL CONTROL', 'Cortés pierde el poder', 10.4, 20.4);
  const zp = svgOf('pop'); $('pop').style.background = '#0e1218'; const people = Array.from({ length: 10 }, (_, i) => { const g = mk('g', {}, zp); const f = CM.figure(g, 'MEX', { weapon: 'none', shield: false }); CM.pose(f, { x: 240 + i * 160, y: 920, s: 2, dir: 1 }); return g; });
  tl.to(people.slice(1), { opacity: .12, duration: .3, stagger: .15 }, W('noventa') - 1.6); const v = virus(zp, 1700, 300, 70); tl.from(v, { scale: 0, duration: .4, ease: 'back.out(2)', transformOrigin: '1700px 300px' }, W('epidemias') - .3);
  const pct = CM.text($('pop'), 'big', 'HASTA UN <em>90 %</em>', 260, 'font-size:140px'); tl.from(pct, { scale: 1.3, opacity: 0, duration: .4, ease: 'expo.out' }, W('noventa') - .3);
  CM.head(H, tl, 'LAS <em>EPIDEMIAS</em>', 'algunas estimaciones: hasta un 90 % menos en un siglo', 20.7, 32.0);
  const m = mexMap('map'); Z(m, 0, [600, 640], 1.3); m.pin(tl, 'Tenochtitlan', '1521', 32.4, null, { r: 6, size: 22, dy: 16 }); m.pin(tl, 'Nojpetén', 'NOJPETÉN · 1697', W('nojpetén') - .3, null, { r: 7, size: 24, fill: '#FFD23F', dy: 18 });
  CM.head(H, tl, 'EL ÚLTIMO <em>REINO MAYA</em>', 'Nojpetén resistió hasta 1697', 32.4, 41.1);
  const zm = svgOf('mes'); $('mes').style.background = 'linear-gradient(#efe7d2, #d9cfb4)'; const ic = ['CASTELLANO', 'CRISTIANISMO', 'CABALLOS', 'TRIGO'].map((t, i) => CM.text($('mes'), 'big', t, 300 + Math.floor(i / 2) * 170, `font-size:90px;color:#3a2a1a;left:${i % 2 ? 980 : 160}px;right:auto;width:780px`));
  ['castellano', 'cristianismo', 'animales', 'cultivos…'].forEach((w, i) => tl.from(ic[i], { opacity: 0, scale: 1.3, duration: .3 }, W(w) - .2));
  CM.head(H, tl, 'UNA SOCIEDAD <em>MESTIZA</em>', 'llegaron nuevas lenguas, creencias, animales y cultivos', 41.4, 48.1);
  const zl = $('len'); zl.style.background = 'radial-gradient(1200px 800px at 50% 45%, #2f8f5a, #0e2a1a 75%)'; const n7 = CM.text(zl, 'big', '<em>+7.000.000</em>', 280, 'font-size:220px'), n7b = CM.text(zl, 'mid', 'de personas en México hablan una <b>lengua indígena</b>', 560);
  tl.from(n7, { scale: 1.4, opacity: 0, duration: .5, ease: 'expo.out' }, W('siete') - .3).from(n7b, { opacity: 0, y: 20, duration: .3 }, W('personas') - .2);
  CM.head(H, tl, 'LAS LENGUAS <em>SIGUEN VIVAS</em>', 'náhuatl, maya y muchas más', 48.4, 57.0);
  const zi = svgOf('ide'); $('ide').style.background = 'linear-gradient(#9cc4e6, #efe2bf)'; mk('rect', { y: 900, width: 1920, height: 180, fill: '#a8916a' }, zi);
  const few = [0, 1].map(() => CM.figure(zi, 'ES')); few.forEach((f, i) => CM.pose(f, { x: 220 + i * 120, y: 980, s: 2, dir: 1 }));
  const many = Array.from({ length: 18 }, (_, i) => CM.figure(zi, i % 3 ? 'TLX' : 'TOT')); many.forEach((f, i) => CM.pose(f, { x: 520 + (i % 9) * 140, y: 900 + Math.floor(i / 9) * 110, s: 1.4 + Math.floor(i / 9) * .4, dir: 1 }));
  tl.from(many.map(f => f.o), { opacity: 0, duration: .25, stagger: .05 }, W('aliados') - .4); const vi = virus(zi, 1700, 330, 70); tl.from(vi, { scale: 0, duration: .4, ease: 'back.out(2)', transformOrigin: '1700px 330px' }, W('viruela') - .3);
  CM.head(H, tl, '¿QUIÉN <em>CONQUISTÓ</em>?', 'unos cientos de españoles… sus aliados indígenas… y la viruela', 57.3, 67.3);
  const end = document.createElement('div'); end.style.cssText = 'position:absolute;inset:0;z-index:6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;background:radial-gradient(1200px 800px at 50% 45%, #6a3a1a, #1a0e08 75%)';
  end.innerHTML = '<div style="font:400 120px/1 \'Bebas Neue\';text-align:center">¿QUÉ FUE LO MÁS <span style="color:#FFD23F">DECISIVO</span>?</div><div style="font:800 40px Inter;letter-spacing:.06em">CUÉNTAMELO EN LOS COMENTARIOS</div><div class="sub" style="margin-top:30px;padding:22px 60px;border-radius:16px;background:#d0312d;font:800 44px Inter;letter-spacing:.08em">SUSCRÍBETE</div><div style="margin-top:20px;font:400 90px Bebas Neue;letter-spacing:.14em">CURIOSI<span style="color:#FFD23F">MUNDO</span></div>';
  $('end').append(end);
  tl.from(end, { opacity: 0, duration: .5 }, W('qué') - .4).from(end.children[0], { scale: 1.2, opacity: 0, duration: .5, ease: 'expo.out' }, W('qué') - .3)
    .from(end.children[1], { y: 20, opacity: 0, duration: .3 }, W('cuéntamelo') - .2).from(end.children[2], { scale: 0, duration: .4, ease: 'back.out(2.5)' }, W('suscríbete') - .2)
    .to(end.children[2], { scale: 1.08, duration: .4, yoyo: true, repeat: 3, ease: 'sine.inOut' }, W('suscríbete') + .3).from(end.children[3], { y: 30, opacity: 0, letterSpacing: '.4em', duration: .7, ease: 'expo.out' }, W('curiosimundo') - .2);
  fadeIn(['vir', 'pop', 'map', 'mes', 'len', 'ide']);
''')
