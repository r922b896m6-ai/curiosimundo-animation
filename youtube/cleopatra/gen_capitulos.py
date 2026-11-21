"""Cleopatra: la última reina de Egipto · vídeo largo (8 capítulos). uso: python3 youtube/cleopatra/gen_capitulos.py"""
import sys
R = '/home/user/curiosimundo-animation/'; sys.path.insert(0, R + 'tools')
from largo import Project
P = Project(R + 'youtube/cleopatra', 'Cleopatra: la última reina de Egipto', ['space.js', 'egypt.js'], open(R + 'tools/common_largo.js').read() + r'''
  const fig = (s, kind, x, y, sc = 2.4, dir = 1, o = {}) => { const f = EG.person(s, kind, o); EG.place(f, x, y, sc, dir); return f; };
  const walk = (sec, f, x0, x1, t0, t1, y, sc = 2.4, dir = 1, run = 1) => gm.onFrame($(sec), (l, i) => { const k = gm.clamp((i.time - t0) / (t1 - t0)); EG.pose(f, { x: x0 + (x1 - x0) * k, y, s: sc, dir, run: k > 0 && k < 1 ? run : 0, ph: i.time * 8 }); });
  const row = (s, kind, n, x0, dx, y, sc = 1.6, dir = 1) => Array.from({ length: n }, (_, i) => fig(s, kind, x0 + i * dx, y + (i % 2) * 24, sc, dir));
  const march = (sec, F, t0, t1, sp, y0, sc, dir, run = 1) => gm.onFrame($(sec), (l, i) => F.forEach((f, k) => { const d = gm.clamp(i.time - t0, 0, t1 - t0); EG.pose(f, { x: f.x0 + d * sp, y: y0 + (k % 2) * 24, s: sc, dir, run: i.time > t0 && i.time < t1 ? run : 0, ph: i.time * 8 + k }); }));
  const army = (s, kind, n, x0, dx, y0, sc, dir) => Array.from({ length: n }, (_, i) => { const f = EG.person(s, kind); f.x0 = x0 + i * dx; EG.pose(f, { x: f.x0, y: y0 + (i % 2) * 24, s: sc, dir }); return f; });
  const gold = el => el.setAttribute('style', 'filter: sepia(1) saturate(5) hue-rotate(-12deg) brightness(1.05)');
  const PAL = id => { const s = svgOf(id); EG.palace(s); return s; };
  const NIGHTSEA = 'linear-gradient(#0a1430, #1d2a5a)';
''')

P.page(0, 'Arranque en frío: Cleopatra más cerca de nosotros que de las pirámides, la última reina, el saco, César y Antonio, Roma, Accio, la tumba perdida.',
 [('s0', 0), ('s1', 'fue'), ('s2', 'se'), ('s3', 'ganó'), ('s4', 'desafió'), ('s5', 'pero'), ('s6', 'nadie'), ('t', ('cleopatra', 2))], r'''
  const z0 = svgOf('s0'); EG.desert(z0); EG.pyramid(z0, 330, 800, 460); EG.rocket(z0, 1680, 860, 1.4); mk('line', { x1: 120, x2: 1820, y1: 900, y2: 900, stroke: '#3a2a1a', 'stroke-width': 8 }, z0);
  const c0 = fig(z0, 'cleo', 900, 880, 2.6); const n0 = CM.text($('s0'), 'big', '<em>2.500</em> AÑOS', 90, 'font-size:200px;text-shadow:0 10px 50px rgb(0 0 0 / .6)');
  tl.fromTo(n0, { scale: 1.2 }, { scale: 1, duration: .5, ease: 'expo.out' }, 0).to(n0, { opacity: 0, duration: .3 }, W('época') - .5);
  gm.onFrame($('s0'), (l, i) => { const k = gm.clamp((i.time - W('época') + .6) / 1.5); EG.pose(c0, { x: 900 + k * 420, y: 880, s: 2.6, run: k > 0 && k < 1 ? 1 : 0, ph: i.time * 8 }); });
  big('s0', 'MÁS CERCA DE <em>NOSOTROS</em>', 100, W('época') - .3, 'font-size:120px');
  const z1 = PAL('s1'); const c1 = fig(z1, 'cleo', 960, 900, 3.4); big('s1', 'LA ÚLTIMA <em>REINA</em> DE EGIPTO', 110, W('última') - .3, 'font-size:120px'); push('s1', 1.2, 1, '50%', '60%');
  const z2 = PAL('s2'); const g2 = row(z2, 'egs', 3, 1380, 160, 900, 2.2, -1); const ap = EG.person(z2, 'apo', { hold: 'sack' }); walk('s2', ap, 100, 1200, S.s2, S.s3, 900, 2.4, 1, 1);
  big('s2', 'ESCONDIDA EN UN <em>SACO</em>', 110, W('saco') - .3, 'font-size:120px');
  const z3 = PAL('s3'); fig(z3, 'caesar', 560, 900, 2.8, 1); fig(z3, 'cleo', 960, 900, 3, 1); fig(z3, 'antony', 1360, 900, 2.8, -1);
  EG.label(z3, 'JULIO CÉSAR', 560, 330, 60, '#FFD23F'); EG.label(z3, 'MARCO ANTONIO', 1360, 330, 60, '#FFD23F'); big('s3', 'LOS DOS HOMBRES MÁS <em>PODEROSOS</em>', 110, W('ganó') - .2, 'font-size:100px');
  const z4 = svgOf('s4'); EG.sky(z4, '#8a3a2a', '#e8a060'); mk('rect', { y: 900, width: 1920, height: 180, fill: '#6a4a2a' }, z4); const L4 = army(z4, 'leg', 10, -200, 190, 900, 2.2, -1); march('s4', L4, S.s4, S.s5, 90, 900, 2.2, -1, .8);
  const eagle = mk('g', { transform: 'translate(960 300)' }, z4); mk('rect', { x: -6, y: 0, width: 12, height: 260, fill: '#6b4a2a' }, eagle); mk('path', { d: 'M-80 -10 Q-40 -60 0 -20 Q40 -60 80 -10 Q40 -30 0 10 Q-40 -30 -80 -10Z', fill: '#d8b23a' }, eagle);
  big('s4', 'CONTRA <em>ROMA</em>', 110, W('imperio') - .4, 'font-size:140px');
  const z5 = svgOf('s5', NIGHTSEA); const sea = EG.sea(z5, 560, '#1a4a7a'); const G5 = [0, 1, 2].map(k => EG.galley(z5, { size: 1.1, sail: '#7a2a8a', rows: 2 })); const R5 = [0, 1, 2, 3].map(k => EG.galley(z5, { size: .7, sail: '#e8dcc0', hull: '#4a3a2a' }));
  gm.onFrame($('s5'), (l, i) => { const t = i.time - S.s5; sea.anim(i.time); G5.forEach((g, k) => { g.w.setAttribute('transform', `translate(${300 + k * 520 + t * 60} ${720 + (k % 2) * 90})`); g.anim(i.time); }); R5.forEach((g, k) => { g.w.setAttribute('transform', `translate(${200 + k * 480 - t * 40} ${620 + (k % 2) * 220}) scale(-1 1)`); g.anim(i.time + k); }); });
  big('s5', '¿QUÉ PASÓ EN <em>ACCIO</em>?', 110, W('accio') - .4, 'font-size:140px'); shake(z5, W('derrumbó') - .2, 14);
  const z6 = svgOf('s6'); EG.desert(z6, { sun: false }); const col = EG.columns(z6, { n: 5, top: 300, bottom: 860, cap: 'lotus' }); col.setAttribute('opacity', .55); mk('rect', { width: 1920, height: 1080, fill: '#1a1008', opacity: .45 }, z6);
  big('s6', '¿Y SU <em>TUMBA</em>?', 300, W('tumba') - .4, 'font-size:200px');
  const t = $('t'); const zt = CM.svgIn(t, 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); EG.pyramids(zt, 960, 1080, .9).setAttribute('opacity', .35); const ct = fig(zt, 'cleo', 960, 1060, 2.2); ct.o.setAttribute('opacity', .9);
  const h = CM.text(t, 'big', '<em>CLEOPATRA</em>', 160, 'font-size:220px'); const a = CM.text(t, 'mid', 'la última reina de egipto', 390, 'font-size:56px;color:#FFD23F');
  tl.from(h, { scale: 1.3, opacity: 0, filter: 'blur(16px)', duration: .8, ease: 'expo.out' }, S.t + .1).to(h, { scale: 1.05, duration: D - S.t - 1, ease: 'sine.inOut' }, S.t + .9).from(a, { y: 30, opacity: 0, duration: .4 }, W('última', 2) - .3);
''', off=0, mood='tension_up', last_mood='title', hits=['saco', 'derrumbó', ('cleopatra', 2)])

P.page(1, 'Una reina griega: pirámide (2560 a. C.), Cleopatra, Luna (1969); familia griega de Macedonia; Ptolomeo y Alejandro Magno; Alejandría, biblioteca y faro; 69 a. C., idiomas; su voz; lista y ambiciosa.',
 [('tl', 0), ('mac', 'además'), ('alx', 'antepasado'), ('city', 'capital'), ('born', 'séptima'), ('voz', 'plutarco'), ('hk', ('era', 6))], r'''
  const zt = svgOf('tl'); EG.desert(zt, { sun: false }); mk('rect', { x: 100, y: 700, width: 1720, height: 16, rx: 8, fill: '#3a2a1a' }, zt);
  const p = EG.pyramid(zt, 260, 690, 260); const c = fig(zt, 'cleo', 1060, 690, 1.6); const rk = EG.rocket(zt, 1700, 690, .9);
  [p, c.o].forEach(e => e.setAttribute('opacity', 1)); tl.from(p, { opacity: 0, y: 40, duration: .4 }, W('pirámide') - .3).from(c.o, { opacity: 0, duration: .4 }, W('cleopatra') - .3).from(rk, { opacity: 0, duration: .4 }, W('luna') - .3);
  const l1 = EG.label(zt, '2560 a. C.', 260, 790, 64); const l2 = EG.label(zt, '69 a. C.', 1060, 790, 64); const l3 = EG.label(zt, '1969', 1700, 790, 64);
  tl.from(l1, { opacity: 0, duration: .3 }, W('sesenta') - .3).from(l2, { opacity: 0, duration: .3 }, W('cleopatra') - .2).from(l3, { opacity: 0, duration: .3 }, W('luna') - .2);
  const b1 = mk('path', { d: 'M300 600 Q680 420 1020 600', stroke: '#FFD23F', 'stroke-width': 8, fill: 'none' }, zt), b2 = mk('path', { d: 'M1100 600 Q1400 470 1660 600', stroke: '#5bc0ff', 'stroke-width': 8, fill: 'none' }, zt);
  const g1 = EG.label(zt, '≈ 2.500 AÑOS', 660, 470, 80, '#FFD23F'), g2 = EG.label(zt, '≈ 2.000 AÑOS', 1380, 470, 80, '#5bc0ff');
  tl.from(b1, { draw: 0, duration: .8 }, W('quinientos', 2) - .5).from(g1, { opacity: 0, duration: .3 }, W('quinientos', 2) - .2).from(b2, { draw: 0, duration: .8 }, W('dos', 3) - .5).from(g2, { opacity: 0, duration: .3 }, W('dos', 3) - .2);
  hd('UN DATO QUE <em>SORPRENDE</em>', 'de la pirámide a Cleopatra, de Cleopatra a la Luna', S.tl + .3, S.mac);
  const zm = PAL('mac'); fig(zm, 'cleo', 760, 900, 3.2); const tag = EG.label(zm, 'FAMILIA <tspan fill="#FFD23F">GRIEGA</tspan> · MACEDONIA', 1260, 520, 80); tl.from(tag, { opacity: 0, x: 40, duration: .4 }, W('griega') - .3);
  const pt = EG.label(zm, 'LOS PTOLOMEOS', 1260, 620, 90, '#FFD23F'); tl.from(pt, { opacity: 0, duration: .3 }, W('ptolomeos') - .3); hd('NO ERA <em>EGIPCIA</em>', 'de origen', S.mac + .3, S.alx);
  const za = svgOf('alx', 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); const chain = [['ALEJANDRO MAGNO', 'alejandro'], ['PTOLOMEO I', 'ptolomeo'], ['…', ['familia', 2]], ['CLEOPATRA VII', 'trescientos']];
  chain.forEach(([t, w], k) => { const x = 270 + k * 460; const bx = mk('rect', { x: x - 200, y: 440, width: 400, height: 140, rx: 20, fill: 'rgb(6 12 28 / .8)', stroke: '#FFD23F', 'stroke-width': 4 }, za); const lb = EG.label(za, t, x, 530, 58);
    if (k < 3) { const ar = mk('path', { d: `M${x + 205} 510 L${x + 255} 510`, stroke: '#FFD23F', 'stroke-width': 8 }, za); tl.from(ar, { opacity: 0, duration: .2 }, W(...[].concat(w)) - .1); } tl.from([bx, lb], { opacity: 0, y: 20, duration: .35 }, W(...[].concat(w)) - .3); });
  big('alx', 'CASI <em>300</em> AÑOS', 700, W('trescientos') - .3, 'font-size:130px'); hd('UN GENERAL DE <em>ALEJANDRO</em>', 'se quedó con Egipto', S.alx + .3, S.city);
  const zc = svgOf('city'); EG.sky(zc, '#7ab8e8', '#f4e2b8'); const sc = EG.sea(zc, 760, '#2a7ab0'); EG.city(zc, 760, 9); const ph = EG.pharos(zc, 1600, 800, 1.1); gm.onFrame($('city'), (l, i) => { sc.anim(i.time); ph.fire.setAttribute('opacity', .8 + Math.sin(i.time * 9) * .2); });
  push('city', 1, 1.12, '80%', '50%'); hd('<em>ALEJANDRÍA</em>', 'una de las ciudades más ricas del mundo', S.city + .3, W('biblioteca') - .3); hd('SU ENORME <em>BIBLIOTECA</em>', 'y su faro', W('biblioteca') - .2, W('maravillas') - .4);
  hd('EL <em>FARO</em>', 'una de las 7 maravillas del mundo antiguo', W('maravillas') - .3, S.born);
  const zb = PAL('born'); const cb = fig(zb, 'cleo', 640, 900, 3.2); hd('<em>69 a. C.</em>', 'nace Cleopatra VII', S.born + .3, W('idiomas') - .3);
  [['GRIEGO', 'idiomas', 1100, 420], ['EGIPCIO', 'egipcio', 1500, 560], ['Y MÁS…', 'idiomas', 1120, 680]].forEach(([t, w, x, y]) => { const g = mk('g', {}, zb); mk('rect', { x: x - 170, y: y - 70, width: 340, height: 110, rx: 50, fill: '#fff', stroke: '#2a2a3a', 'stroke-width': 4 }, g); EG.label(g, t, x, y + 10, 64, '#1a1a2a'); tl.from(g, { scale: 0, opacity: 0, duration: .35, ease: 'back.out(2)', transformOrigin: `${x}px ${y}px` }, W(w) - .2); });
  hd('LA PRIMERA EN APRENDER <em>EGIPCIO</em>', 'la lengua de su pueblo', W('egipcio') - .4, S.voz);
  const zv = PAL('voz'); fig(zv, 'cleo', 760, 900, 3.2); const ws = Array.from({ length: 4 }, () => mk('path', { d: 'M0 -60 Q40 0 0 60', stroke: '#FFD23F', 'stroke-width': 8, fill: 'none' }, zv));
  gm.onFrame($('voz'), (l, i) => ws.forEach((w, k) => { const q = ((i.time * .6 + k / 4) % 1); w.setAttribute('transform', `translate(${880 + q * 400} 480) scale(${.6 + q})`); w.setAttribute('opacity', 1 - q); }));
  hd('SEGÚN <em>PLUTARCO</em>', 'lo que más impresionaba era su conversación y su voz', S.voz + .3, S.hk);
  const zh = svgOf('hk', 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); fig(zh, 'cleo', 960, 1000, 3.6); ['LISTA', 'CULTA', 'AMBICIOSA'].forEach((t, k) => { const lb = EG.label(zh, t, 360 + k * 600, 280, 110, '#FFD23F'); tl.from(lb, { opacity: 0, scale: 1.4, duration: .3, transformOrigin: `${360 + k * 600}px 250px` }, W(t.toLowerCase()) - .2); });
''', card=(1, '69 a. C.', 'UNA REINA GRIEGA EN EGIPTO'), hits=['sorprende'])

P.page(2, 'Reina a los 18: muere su padre (51 a. C.), reina con su hermano Ptolomeo XIII, los consejeros la apartan, huye, reúne un ejército, frente a frente, llega César.',
 [('two', 0), ('adv', 'pero'), ('army', 'ella'), ('hk', 'justo')], r'''
  const zt = PAL('two'); fig(zt, 'cleo', 720, 900, 3); fig(zt, 'ptol', 1200, 900, 2.2, -1); EG.label(zt, 'CLEOPATRA · ~18 AÑOS', 720, 320, 56, '#FFD23F'); EG.label(zt, 'PTOLOMEO XIII · UN NIÑO', 1200, 480, 56, '#FFD23F');
  hd('<em>51 a. C.</em>', 'muere su padre', S.two + .3, W('reinar') - .3); hd('DOS <em>REYES</em>', 'hermana y hermano, juntos', W('reinar') - .2, S.adv);
  const za = PAL('adv'); const pt = fig(za, 'ptol', 1200, 900, 2.2, -1); const adv = [1340, 1460, 1060].map((x, k) => fig(za, 'cit', x, 900, 2.6, k === 2 ? 1 : -1)); adv.forEach(a => a.b.querySelectorAll('path')[0].setAttribute('fill', '#3a3048'));
  const cl = EG.person(za, 'cleo'); walk('adv', cl, 700, -200, W('huir') - .5, W('huir') + 2.2, 900, 3, -1);
  hd('LOS <em>CONSEJEROS</em>', 'querían el poder para ellos', S.adv + .3, W('huir') - .4); hd('TUVO QUE <em>HUIR</em>', 'de Alejandría', W('huir') - .3, S.army);
  const zr = svgOf('army'); EG.desert(zr); const A = army(zr, 'egs', 6, 80, 110, 900, 1.9, 1), B = army(zr, 'egs', 8, 1080, 110, 900, 1.9, -1); B.forEach(f => f.b.querySelectorAll('path')[0].setAttribute('fill', '#8a6a4a'));
  march('army', A, S.army + .5, S.army + 4, 40, 900, 1.9, 1, .7); march('army', B, S.army + .5, S.army + 4, -40, 900, 1.9, -1, .7); const cA = fig(zr, 'cleo', 130, 780, 1.6);
  hd('UN <em>EJÉRCITO</em>', 'reunido en la frontera', S.army + .3, W('frente') - .4); big('army', 'FRENTE A <em>FRENTE</em>', 120, W('frente') - .3, 'font-size:130px');
  const zk = svgOf('hk'); EG.sky(zk, '#7ab8e8', '#f4e2b8'); const sk = EG.sea(zk, 720, '#2a7ab0'); EG.city(zk, 720, 9); const gl = EG.galley(zk, { size: 1.3, sail: '#b3262d', rows: 2 });
  gm.onFrame($('hk'), (l, i) => { sk.anim(i.time); gl.w.setAttribute('transform', `translate(${-400 + (i.time - S.hk) * 220} 860)`); gl.anim(i.time); }); big('hk', '<em>JULIO CÉSAR</em>', 110, W('julio') - .3, 'font-size:160px');
''', card=(2, '51 a. C.', 'REINA A LOS 18'), hits=['julio'])

P.page(3, 'El saco y Julio César: César en Alejandría (48 a. C.), el palacio lleno de enemigos, el saco de Apolodoro, la alfombra es leyenda, asedio, batalla del Nilo (retirada), Cesarión, el incendio, Roma.',
 [('arr', 0), ('pal', 'cleopatra'), ('sack', 'según'), ('meet', 'famosa'), ('sieg', ('hermano', 2)), ('nile', 'batalla'), ('son', ('cleopatra', 2)), ('lib', ('durante', 2)), ('hk', 'ahora')], r'''
  const za = svgOf('arr'); EG.sky(za, '#7ab8e8', '#f4e2b8'); const sa = EG.sea(za, 740, '#2a7ab0'); EG.city(za, 740, 9); EG.pharos(za, 1650, 780, .9); const gs = [0, 1, 2].map(() => EG.galley(za, { size: .9, sail: '#b3262d', rows: 1 }));
  gm.onFrame($('arr'), (l, i) => { sa.anim(i.time); gs.forEach((g, k) => { g.w.setAttribute('transform', `translate(${200 + k * 420 + Math.min(i.time - S.arr, 6) * 30} ${860 + (k % 2) * 60})`); g.anim(i.time + k); }); });
  hd('<em>48 a. C.</em>', 'César llega a Alejandría persiguiendo a Pompeyo', S.arr + .3, S.pal);
  const zp = PAL('pal'); row(zp, 'egs', 6, 300, 260, 900, 2.2, 1); hd('UN PALACIO <em>VIGILADO</em>', 'lleno de hombres de su hermano', S.pal + .3, S.sack);
  const zs = svgOf('sack', NIGHTSEA); mk('rect', { y: 860, width: 1920, height: 220, fill: '#3a2a20' }, zs); EG.columns(zs, { n: 6, top: 120, bottom: 860 }).setAttribute('opacity', .5); mk('rect', { width: 1920, height: 1080, fill: '#0a1430', opacity: .35 }, zs);
  const gd = [fig(zs, 'egs', 1500, 880, 2.2, -1), fig(zs, 'egs', 1750, 880, 2.2, -1)]; const ap = EG.person(zs, 'apo', { hold: 'sack' }); walk('sack', ap, -100, 1150, S.sack + .5, S.meet, 880, 2.4, 1, 1);
  hd('SEGÚN <em>PLUTARCO</em>', 'escondida en un saco de ropa de cama', S.sack + .3, W('apolodoro') - .3); hd('<em>APOLODORO</em>', 'la llevó al hombro hasta César', W('apolodoro') - .2, S.meet);
  const zm = PAL('meet'); const cs = fig(zm, 'caesar', 1300, 900, 3, -1); const sk = mk('g', { transform: 'translate(700 880)' }, zm); const sb = mk('path', { d: 'M-150 0 Q-170 -70 -60 -80 L150 -70 Q190 -40 150 0Z', fill: '#d8c8a8', stroke: '#8a7a5a', 'stroke-width': 5 }, sk);
  const cm = EG.person(zm, 'cleo'); EG.place(cm, 700, 900, 3); cm.o.setAttribute('opacity', 0); tl.to(cm.o, { opacity: 1, duration: .4 }, W('truco') - .3).to(sb, { opacity: 0, duration: .3 }, W('truco') - .3);
  stamp('meet', '¿ALFOMBRA? LEYENDA', W('alfombra') - .3, 160, '#FFD23F'); hd('CÉSAR, <em>IMPRESIONADO</em>', 'se puso de su lado', W('impresionado') - .3, S.sieg);
  const zg = PAL('sieg'); const RL = row(zg, 'leg', 4, 200, 150, 900, 2.1, 1); const EGY = army(zg, 'egs', 9, 900, 120, 900, 2, -1); march('sieg', EGY, S.sieg + .3, S.sieg + 3, -30, 900, 2, -1, .6);
  hd('<em>ENCERRADO</em> MESES', 'en Alejandría, hasta que llegaron refuerzos', S.sieg + .3, S.nile);
  const zn = svgOf('nile'); EG.nile(zn); const L = army(zn, 'leg', 7, -200, 150, 860, 1.8, 1); const E = army(zn, 'egs', 7, 1000, 130, 860, 1.8, -1);
  const tR = W('retiró') - .4; march('nile', L, S.nile + .3, S.son, 80, 860, 1.8, 1, .8);
  gm.onFrame($('nile'), (l, i) => E.forEach((f, k) => { const t = i.time; const back = t > tR; const d = back ? (t - tR) * 260 : 0; EG.pose(f, { x: f.x0 + d, y: 860 + (k % 2) * 24, s: 1.8, dir: back ? 1 : -1, run: back ? 1 : 0, ph: t * 9 + k }); }));
  const bt = EG.galley(zn, { size: .4, sail: '#2f5fa0' }); const tA = W('ahogado') - .5; gm.onFrame($('nile'), (l, i) => { const t = i.time; const x = 900 + Math.max(0, t - W('huir') + .3) * 120; bt.w.setAttribute('transform', `translate(${x} ${980 + Math.max(0, t - tA) * 40}) rotate(${Math.min(40, Math.max(0, t - tA) * 30)})`); bt.w.setAttribute('opacity', 1 - gm.clamp((t - tA) / 2)); bt.anim(t); });
  hd('LA BATALLA DEL <em>NILO</em>', '47 a. C.', S.nile + .3, tR); hd('SE <em>RETIRAN</em>', 'el ejército del joven Ptolomeo', tR, S.son);
  const zo = PAL('son'); fig(zo, 'cleo', 860, 900, 3.2); const baby = mk('g', { transform: 'translate(960 560)' }, zo); mk('ellipse', { rx: 44, ry: 26, fill: '#f4efe2' }, baby); mk('circle', { cx: 34, cy: -10, r: 18, fill: '#c98f62' }, baby); tl.from(baby, { opacity: 0, duration: .4 }, W('hijo') - .3);
  hd('OTRA VEZ <em>REINA</em>', 'de Egipto', S.son + .3, W('cesarión') - .4); big('son', '<em>CESARIÓN</em>', 120, W('cesarión') - .3, 'font-size:150px');
  const zl = svgOf('lib'); EG.library(zl); const glow = mk('rect', { width: 1920, height: 1080, fill: '#ff7a20', opacity: 0 }, zl); gm.onFrame($('lib'), (l, i) => glow.setAttribute('opacity', i.time < W('incendio') - .3 ? 0 : .18 + Math.sin(i.time * 7) * .05));
  hd('UN <em>INCENDIO</em> EN EL PUERTO', 'se quemaron muchos libros, según autores antiguos', W('incendio') - .4, W('siguió') - .3); hd('LA BIBLIOTECA <em>SIGUIÓ</em>', 'funcionando mucho tiempo después', W('siguió') - .2, S.hk);
  const zh = svgOf('hk'); EG.sky(zh, '#8a4a2a', '#e8b070'); EG.temple(zh, 960, 900, 1.1); const SN = row(zh, 'sen', 5, 520, 220, 1000, 1.8, 1); big('hk', 'PERO EN <em>ROMA</em>…', 110, W('roma') - .4, 'font-size:150px');
''', card=(3, '48 a. C.', 'EL SACO Y JULIO CÉSAR'), hits=['truco', 'retiró', 'roma'], extra_audio=lambda W: {'far': [round(W('batalla') + 1, 2), round(W('batalla') + 3, 2)], 'hits': [round(W('truco'), 2), round(W('retiró'), 2)]})

P.page(4, 'Roma y los idus de marzo: Cleopatra en Roma, la estatua dorada, el miedo a un rey, 15 de marzo del 44 a. C., vuelta a Egipto, el calendario de 365 días, Marco Antonio.',
 [('villa', 0), ('stat', 'incluso'), ('rex', 'además'), ('ides', 'quince'), ('back', ('cleopatra', 2)), ('cal', 'aquella'), ('hk', ('roma', 3))], r'''
  const zv = svgOf('villa'); EG.sky(zv, '#8ac0e8', '#f4e2b8'); mk('path', { d: 'M0 820 Q480 780 960 820 T1920 800 L1920 900 L0 900Z', fill: '#4a8aa0' }, zv); mk('rect', { y: 880, width: 1920, height: 200, fill: '#7a9a5a' }, zv); EG.temple(zv, 1400, 800, .7); EG.city(zv, 800, 4);
  fig(zv, 'cleo', 600, 1000, 2.4); hd('<em>ROMA</em>', 'una villa de César, al otro lado del Tíber', S.villa + .3, S.stat);
  const zs = svgOf('stat'); EG.sky(zs, '#5a3a2a', '#8a6a4a'); EG.temple(zs, 960, 1000, 1.3); const st = fig(zs, 'cleo', 960, 920, 2.6); gold(st.o); const SN = [fig(zs, 'sen', 300, 1000, 2.2), fig(zs, 'sen', 1620, 1000, 2.2, -1)];
  hd('UNA <em>ESTATUA DORADA</em>', 'de Cleopatra, en un templo', S.stat + .3, W('escándalo') - .3); big('stat', '¡<em>ESCÁNDALO</em>!', 120, W('escándalo') - .3, 'font-size:150px');
  const zr = svgOf('rex', 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); EG.label(zr, 'REX', 960, 640, 360, '#f2ede0'); const xx = mk('path', { d: 'M640 300 L1280 720 M1280 300 L640 720', stroke: '#E5484D', 'stroke-width': 40, 'stroke-linecap': 'round' }, zr);
  tl.from(xx, { draw: 0, duration: .5 }, W('prohibida') - .3); hd('¿CÉSAR, <em>REY</em>?', 'en Roma, la palabra estaba prohibida desde hacía siglos', S.rex + .3, S.ides);
  const zi = svgOf('ides'); EG.sky(zi, '#4a3a30', '#2a2018'); EG.columns(zi, { n: 6, top: 100, bottom: 900, col: '#d8d0c0', cap: 'doric' }); mk('rect', { y: 900, width: 1920, height: 180, fill: '#8a7a68' }, zi);
  const cs = fig(zi, 'caesar', 960, 920, 2.6); const ring = Array.from({ length: 8 }, (_, k) => EG.person(zi, 'sen')); const tS = W('rodeó') - .5, tK = W('asesinó') - .2;
  gm.onFrame($('ides'), (l, i) => ring.forEach((f, k) => { const side = k % 2 ? 1 : -1, x0 = 960 + side * (380 + (k >> 1) * 150), q = gm.clamp((i.time - tS) / 2); EG.pose(f, { x: x0 + (960 + side * (110 + (k >> 1) * 60) - x0) * q, y: 920 + (k >> 1) * 10, s: 2.4, dir: -side, run: q > 0 && q < 1 ? 1 : 0, ph: i.time * 8 + k }); }));
  const dark = mk('rect', { width: 1920, height: 1080, fill: '#000', opacity: 0 }, zi); tl.to(dark, { opacity: .9, duration: .6 }, tK); const lr = EG.laurel(zi, 960, 900, 1.4); lr.setAttribute('opacity', 0); tl.to(lr, { opacity: 1, duration: .5 }, tK + .5);
  hd('15 DE MARZO, <em>44 a. C.</em>', 'los idus de marzo', S.ides + .3, W('senado') - .4); hd('UNA REUNIÓN DEL <em>SENADO</em>', 'los senadores rodean a César', W('senado') - .3, S.back);
  const zb = svgOf('back'); EG.sky(zb, '#7ab8e8', '#f4e2b8'); const sb = EG.sea(zb, 640, '#2a6fb0'); const gb = EG.galley(zb, { size: 1.3, sail: '#7a2a8a', rows: 2 }); const cb = fig(gb.g, 'cleo', 120, -70, 1);
  gm.onFrame($('back'), (l, i) => { sb.anim(i.time); gb.w.setAttribute('transform', `translate(${300 + (i.time - S.back) * 90} 820)`); gb.anim(i.time); }); hd('SIN SU <em>ALIADO</em>', 'vuelve a Egipto', S.back + .3, S.cal);
  const zc = svgOf('cal', '#efe6d2'); const cells = []; for (let r = 0; r < 12; r++) for (let c = 0; c < 31; c++) { if (cells.length >= 365) break; cells.push(mk('rect', { x: 260 + c * 45, y: 230 + r * 52, width: 38, height: 44, rx: 6, fill: '#d8cfbf' }, zc)); }
  const tC = W('calendario') - .2; gm.onFrame($('cal'), (l, i) => { const n = Math.floor(gm.clamp((i.time - tC) / 3) * 365); cells.forEach((c, k) => c.setAttribute('fill', k < n ? '#d8b23a' : '#d8cfbf')); });
  const bis = EG.label(zc, '+1 DÍA CADA 4 AÑOS', 960, 960, 90, '#b3262d'); tl.from(bis, { opacity: 0, duration: .3 }, W('bisiesto') - .3); hd('<em>365 DÍAS</em>', 'César y el astrónomo Sosígenes', W('sosígenes') - .4, W('nuestro') - .3); hd('NUESTRO <em>CALENDARIO</em>', 'viene de él', W('nuestro') - .2, S.hk);
  const zh = svgOf('hk'); EG.sky(zh, '#8a3a2a', '#e8a060'); mk('rect', { y: 900, width: 1920, height: 180, fill: '#6a4a2a' }, zh); row(zh, 'leg', 4, 120, 150, 920, 2, 1); row(zh, 'leg', 4, 1340, 150, 920, 2, -1); fig(zh, 'antony', 960, 960, 2.8);
  big('hk', 'MARCO <em>ANTONIO</em>', 110, W('marco') - .3, 'font-size:150px');
''', card=(4, '44 a. C.', 'ROMA Y LOS IDUS DE MARZO'), mood='tension', hits=['escándalo', 'asesinó', 'marco'])

P.page(5, 'Marco Antonio: el reparto de Roma, Tarso (41 a. C.), el barco dorado, los gemelos Sol y Luna, las Donaciones, la propaganda de Octavio, la perla (leyenda), 32 a. C. guerra.',
 [('tri', 0), ('tar', 'cuarenta'), ('barge', 'según'), ('alx', ('antonio', 3)), ('don', 'años'), ('prop', ('roma', 2)), ('pearl', 'escritor'), ('war', 'treinta')], r'''
  const zt = svgOf('tri'); EG.sky(zt, '#5a3a2a', '#8a6a4a'); EG.temple(zt, 960, 1000, 1.2).setAttribute('opacity', .5); const A = fig(zt, 'antony', 560, 960, 2.8), O = fig(zt, 'octav', 960, 960, 2.6), Lp = fig(zt, 'sen', 1360, 960, 2.6, -1);
  EG.label(zt, 'ANTONIO · ORIENTE', 560, 360, 50, '#FFD23F'); EG.label(zt, 'OCTAVIO · HEREDERO', 960, 300, 50, '#FFD23F'); EG.label(zt, 'LÉPIDO', 1360, 360, 50, '#FFD23F');
  hd('<em>TRES</em> HOMBRES', 'se reparten Roma', S.tri + .3, S.tar);
  const zr = svgOf('tar'); EG.sky(zr, '#7ab8e8', '#f4e2b8'); const s2 = EG.sea(zr, 700, '#2a7ab0'); EG.city(zr, 700, 9); fig(zr, 'antony', 1500, 900, 2.6, -1); mk('rect', { x: 1200, y: 880, width: 720, height: 200, fill: '#c9b48a' }, zr);
  gm.onFrame($('tar'), (l, i) => s2.anim(i.time)); hd('<em>TARSO</em> · 41 a. C.', 'Antonio llama a Cleopatra', S.tar + .3, S.barge);
  const zb = svgOf('barge'); EG.sky(zb, '#f0a860', '#f8dca0'); const s3 = EG.sea(zb, 680, '#2a6fa0'); const bg = EG.galley(zb, { size: 1.8, sail: '#7a1a8a', hull: '#d8b23a', rows: 2 }); bg.oars.forEach(o => o.setAttribute('stroke', '#e8eef4'));
  const cv = fig(bg.g, 'cleo', 220, -70, 1.1); gm.onFrame($('barge'), (l, i) => { s3.anim(i.time); bg.w.setAttribute('transform', `translate(${-300 + (i.time - S.barge) * 120} 860)`); bg.anim(i.time * .6); });
  [['POPA <tspan fill="#FFD23F">DORADA</tspan>', 'dorada'], ['VELAS <tspan fill="#c86ad8">PÚRPURA</tspan>', 'púrpura'], ['REMOS DE <tspan fill="#e8eef4">PLATA</tspan>', 'plata']].forEach(([t, w], k) => { const lb = EG.label(zb, t, 1500, 200 + k * 110, 84); tl.from(lb, { opacity: 0, x: 40, duration: .3 }, W(w) - .3); });
  hd('SEGÚN <em>PLUTARCO</em>', 'vestida como la diosa Venus', S.barge + .3, S.alx);
  const za = PAL('alx'); fig(za, 'antony', 700, 900, 3); fig(za, 'cleo', 1100, 900, 3, -1); const sun = SP.sun(za, 600, 300, 70), moon = SP.moon(za, 1320, 300, 60); tl.from([sun.w, moon], { opacity: 0, duration: .5 }, W('gemelos') - .3);
  const n1 = EG.label(za, 'ALEJANDRO HELIOS', 600, 450, 54, '#FFD23F'), n2 = EG.label(za, 'CLEOPATRA SELENE', 1320, 450, 54, '#cfe6ff'); tl.from(n1, { opacity: 0, duration: .3 }, W('helios') - .3).from(n2, { opacity: 0, duration: .3 }, W('selene') - .3);
  hd('<em>DESLUMBRADO</em>', 'un invierno en Alejandría', S.alx + .3, W('gemelos') - .4); hd('DOS <em>GEMELOS</em>', 'el Sol y la Luna', W('gemelos') - .3, S.don);
  const zd = PAL('don'); fig(zd, 'antony', 640, 900, 2.8); fig(zd, 'cleo', 960, 900, 2.8); fig(zd, 'ptol', 1240, 900, 1.6, -1); fig(zd, 'ptol', 1400, 900, 1.3, -1); hd('UNA GRAN <em>CEREMONIA</em>', 'tierras de Oriente para Cleopatra y sus hijos', S.don + .3, S.prop);
  const zp = svgOf('prop'); EG.sky(zp, '#8ac0e8', '#f4e2b8'); EG.temple(zp, 960, 880, .9).setAttribute('opacity', .6); mk('rect', { y: 880, width: 1920, height: 200, fill: '#a89a80' }, zp); fig(zp, 'octav', 520, 900, 3); row(zp, 'cit', 6, 900, 170, 1010, 1.8, -1);
  const bub = mk('g', {}, zp); mk('rect', { x: 620, y: 200, width: 620, height: 170, rx: 40, fill: '#fff', stroke: '#2a2a3a', 'stroke-width': 5 }, bub); mk('path', { d: 'M660 360 L600 440 L720 370Z', fill: '#fff', stroke: '#2a2a3a', 'stroke-width': 5 }, bub); EG.label(bub, '¡ESTÁ <tspan fill="#b3262d">HECHIZADO</tspan>!', 930, 315, 90, '#1a1a2a');
  tl.from(bub, { scale: 0, opacity: 0, duration: .35, ease: 'back.out(2)', transformOrigin: '660px 370px' }, W('hechizado') - .3); hd('LA <em>PROPAGANDA</em> DE OCTAVIO', 'una reina extranjera contra Roma', S.prop + .3, S.pearl);
  const zl = svgOf('pearl', 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); const cup = mk('g', { transform: 'translate(960 760)' }, zl); mk('path', { d: 'M-160 -260 L160 -260 Q150 -60 0 -40 Q-150 -60 -160 -260Z', fill: '#d8b23a', stroke: '#8a6a2a', 'stroke-width': 6 }, cup); mk('rect', { x: -14, y: -40, width: 28, height: 120, fill: '#d8b23a' }, cup); mk('ellipse', { cy: 90, rx: 110, ry: 22, fill: '#d8b23a' }, cup);
  const pr = mk('circle', { cx: 960, cy: 200, r: 44, fill: '#f6f2ff', stroke: '#c8c0e0', 'stroke-width': 4 }, zl); tl.to(pr, { attr: { cy: 560, r: 30 }, duration: .8, ease: 'power2.in' }, W('perla') - .2).to(pr, { opacity: 0, attr: { r: 2 }, duration: 1.2 }, W('vinagre') - .2);
  stamp('pearl', 'EXAGERACIÓN', W('exageración') - .3, 140, '#FFD23F'); hd('SEGÚN <em>PLINIO</em>', 'el banquete más caro: una perla en vinagre', S.pearl + .3, W('exageración') - .4);
  const zw = svgOf('war'); EG.sky(zw, '#8a3a2a', '#e8a060'); mk('rect', { y: 900, width: 1920, height: 180, fill: '#6a4a2a' }, zw); const L = army(zw, 'leg', 11, -400, 190, 920, 2.1, 1); march('war', L, S.war + .2, D, 80, 920, 2.1, 1, .8);
  big('war', '<em>32 a. C.</em> · GUERRA', 110, W('guerra') - .4, 'font-size:150px'); mid('war', 'todo se decidiría <b>en el mar</b>', 280, W('mar') - .4, 'font-size:54px');
''', card=(5, '41 a. C.', 'MARCO ANTONIO'), hits=['guerra'])

P.page(6, 'La batalla de Accio: la flota de Antonio en Accio, los barcos rápidos de Agripa bloquean el golfo, meses atrapados, 2 de septiembre del 31 a. C., Cleopatra rompe la línea y se aleja, Antonio la sigue, la flota se rinde.',
 [('fl', 0), ('agr', 'pero'), ('trap', 'durante'), ('bat', 'dos'), ('esc', 'repente'), ('sur', 'resto'), ('hk', ('accio', 2))], r'''
  const SEA = s => { EG.sky(s, '#6fa8d8', '#e8dcc0'); mk('path', { d: 'M0 520 L420 430 L700 470 L700 560 L0 560Z M1920 520 L1500 440 L1220 480 L1220 560 L1920 560Z', fill: '#8a7a5a' }, s); return EG.sea(s, 540, '#2a6fa0'); };
  const zf = svgOf('fl'); const s1 = SEA(zf); const AF = [0, 1, 2, 3].map(k => EG.galley(zf, { size: 1.15, sail: '#e8dcc0', hull: '#4a3020', rows: 3 }));
  gm.onFrame($('fl'), (l, i) => { s1.anim(i.time); AF.forEach((g, k) => { g.w.setAttribute('transform', `translate(${380 + k * 380} ${700 + (k % 2) * 140 + Math.sin(i.time + k) * 6}) scale(${.8})`); g.anim(i.time * .3 + k); }); });
  EG.label(zf, 'CABO DE ACCIO · GRECIA', 960, 500, 64, '#FFD23F'); hd('LA FLOTA DE <em>ANTONIO Y CLEOPATRA</em>', 'barcos enormes, con varias filas de remos', S.fl + .3, S.agr);
  const za = svgOf('agr'); const s2 = SEA(za); const BF = Array.from({ length: 6 }, () => EG.galley(za, { size: .6, sail: '#b3262d', hull: '#5a4a3a' }));
  gm.onFrame($('agr'), (l, i) => { s2.anim(i.time); const k0 = gm.clamp((i.time - S.agr) / 4); BF.forEach((g, k) => { g.w.setAttribute('transform', `translate(${2200 - k0 * (1500 - k * 200)} ${620 + k * 70}) scale(-1 1)`); g.anim(i.time * 2 + k); }); });
  hd('<em>MARCO AGRIPA</em>', 'el almirante de Octavio', S.agr + .3, W('pequeños') - .4); hd('PEQUEÑOS Y <em>RÁPIDOS</em>', 'bloquean la salida del golfo', W('pequeños') - .3, S.trap);
  const zt = svgOf('trap'); const s3 = SEA(zt); const TF = [0, 1, 2].map(k => EG.galley(zt, { size: 1.1, sail: '#c9bca0', hull: '#4a3020', rows: 3 })); gm.onFrame($('trap'), (l, i) => { s3.anim(i.time); TF.forEach((g, k) => g.w.setAttribute('transform', `translate(${500 + k * 460} ${760 + (k % 2) * 100}) scale(.75)`)); });
  mk('rect', { width: 1920, height: 1080, fill: '#1a2a3a', opacity: .35 }, zt); [['SIN COMIDA', 'comida'], ['ENFERMEDADES', 'enfermedades'], ['DESERCIONES', 'aliados']].forEach(([t, w], k) => { const lb = EG.label(zt, t, 400 + k * 560, 300, 90, k === 2 ? '#E5484D' : '#FFD23F'); tl.from(lb, { opacity: 0, y: 20, duration: .3 }, W(w) - .3); });
  hd('<em>ATRAPADOS</em> MESES', '', S.trap + .3, S.bat);
  const zb = svgOf('bat'); const s4 = SEA(zb); const BIG = [0, 1, 2, 3].map(k => EG.galley(zb, { size: 1.1, sail: '#c9bca0', hull: '#4a3020', rows: 3 })), SM = Array.from({ length: 7 }, () => EG.galley(zb, { size: .55, sail: '#b3262d', hull: '#5a4a3a' })), CL = Array.from({ length: 5 }, () => EG.galley(zb, { size: .8, sail: '#7a1a8a', hull: '#3a2a3a', rows: 2 }));
  const fl = Array.from({ length: 6 }, () => mk('circle', { r: 30, fill: 'url(#cmFlash)', opacity: 0 }, zb)); const tE = W('repente') - .3;
  gm.onFrame($('bat'), (l, i) => { const t = i.time; s4.anim(t); BIG.forEach((g, k) => { g.w.setAttribute('transform', `translate(${380 + k * 380} ${760 + (k % 2) * 90}) scale(.75)`); g.anim(t * .3 + k); });
    SM.forEach((g, k) => { const a = t * .5 + k * .9, cx = 380 + (k % 4) * 380, x = cx + Math.cos(a) * 230, y = 760 + Math.sin(a) * 120; g.w.setAttribute('transform', `translate(${x} ${y}) scale(${Math.sin(a) > 0 ? .9 : -.9} .9)`); g.anim(t * 2 + k); });
    CL.forEach((g, k) => { const e = Math.max(0, t - tE); g.w.setAttribute('transform', `translate(${300 + k * 120 + e * 260} ${600 + k * 20 - Math.min(e, 3) * 10}) scale(.6)`); g.anim(t + k); g.w.setAttribute('opacity', t < S.bat + .2 ? 0 : 1); });
    fl.forEach((f, k) => { const q = ((t * .7 + k / 6) % 1); f.setAttribute('cx', 380 + (k % 4) * 380 + 60); f.setAttribute('cy', 760 + (k % 2) * 90 - 20); f.setAttribute('opacity', t < tE ? Math.max(0, 1 - q * 4) * .8 : 0); }); });
  hd('2 DE SEPTIEMBRE, <em>31 a. C.</em>', 'Antonio intenta romper el bloqueo', S.bat + .3, W('rodeaban') - .4); hd('LOS RÁPIDOS <em>RODEAN</em>', 'a los gigantes, difíciles de mover', W('rodeaban') - .3, S.esc);
  const ze = svgOf('esc'); const s5 = SEA(ze); const B2 = [0, 1, 2, 3].map(k => EG.galley(ze, { size: 1.1, sail: '#c9bca0', hull: '#4a3020', rows: 3 })), S2 = Array.from({ length: 6 }, () => EG.galley(ze, { size: .55, sail: '#b3262d', hull: '#5a4a3a' })), C2 = Array.from({ length: 6 }, () => EG.galley(ze, { size: .8, sail: '#7a1a8a', hull: '#3a2a3a', rows: 2 }));
  const AN = EG.galley(ze, { size: 1.1, sail: '#c9bca0', hull: '#6a2a20', rows: 3, flag: '#b3262d' }); const tF = W('siguió') - .4;
  gm.onFrame($('esc'), (l, i) => { const t = i.time, e = t - S.esc; s5.anim(t); B2.forEach((g, k) => g.w.setAttribute('transform', `translate(${380 + k * 380} ${800 + (k % 2) * 90}) scale(.7)`));
    S2.forEach((g, k) => { g.w.setAttribute('transform', `translate(${300 + k * 280} ${690 + (k % 2) * 40}) scale(-.8 .8)`); g.anim(t * 2 + k); });
    C2.forEach((g, k) => { g.w.setAttribute('transform', `translate(${100 + k * 130 + e * 320} ${620 + (k % 3) * 40}) scale(.6)`); g.anim(t * 2 + k); });
    AN.w.setAttribute('transform', `translate(${-200 + Math.max(0, t - tF) * 330} 640) scale(.65)`); AN.anim(t * 2); });
  hd('LOS <em>60 BARCOS</em> DE CLEOPATRA', 'atraviesan la línea, rumbo a Egipto', S.esc + .3, tF); hd('ANTONIO LA <em>SIGUE</em>', 'con unos pocos barcos', tF, S.sur);
  const zs = svgOf('sur'); const s6 = SEA(zs); const B3 = [0, 1, 2, 3].map(k => EG.galley(zs, { size: 1.1, sail: '#c9bca0', hull: '#4a3020', rows: 3 })); const W3 = B3.map((g, k) => { const f = mk('path', { d: 'M6 -300 l70 16 l-70 16z', fill: '#fff' }, g.g); return f; });
  gm.onFrame($('sur'), (l, i) => { s6.anim(i.time); B3.forEach((g, k) => g.w.setAttribute('transform', `translate(${380 + k * 380} ${760 + (k % 2) * 100}) scale(.75)`)); });
  tl.to(B3.map(g => g.sail), { attr: { opacity: .15 }, duration: 1 }, W('rindió') - .5).from(W3, { opacity: 0, duration: .4, stagger: .2 }, W('rindió') - .2); big('sur', 'LA FLOTA SE <em>RINDE</em>', 110, W('rindió') - .3, 'font-size:140px');
  const zh = svgOf('hk', 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); fig(zh, 'octav', 960, 1000, 3.6); EG.laurel(zh, 960, 380, 1.4).setAttribute('opacity', .5); big('hk', 'EL PRINCIPIO <em>DEL FIN</em>', 110, W('principio') - .3, 'font-size:130px');
''', card=(6, '31 a. C.', 'LA BATALLA DE ACCIO'), mood='sea', hits=['repente', 'rindió'], extra_audio=lambda W: {'far': [round(W('dos') + k * 1.8, 2) for k in range(1, 6)], 'sec': [[0, 4, 'card'], [4, round(W('dos'), 2), 'sea'], [round(W('dos'), 2), round(W('rindió') + 1, 2), 'battle'], [round(W('rindió') + 1, 2), 999, 'mourn']]})

P.page(7, 'El final: Octavio en Alejandría (30 a. C.), las tropas abandonan a Antonio, Cleopatra no será trofeo, muere en agosto, la cobra (tradición), Egipto provincia romana, Selene reina de Mauritania, Augusto y agosto, la tumba perdida (Taposiris Magna), pregunta final.',
 [('arr', 0), ('cle', ('cleopatra', 1)), ('end1', ('murió', 2)), ('cob', 'tradición'), ('prov', 'egipto'), ('sel', 'hija'), ('aug', ('octavio', 3)), ('tomb', ('tumba', 1)), ('end', 'crees')], r'''
  const za = svgOf('arr'); EG.sky(za, '#7ab8e8', '#f4e2b8'); EG.city(za, 860, 9); mk('rect', { y: 860, width: 1920, height: 220, fill: '#c9b48a' }, za); const L = army(za, 'leg', 8, -1400, 170, 940, 2, 1); march('arr', L, S.arr + .2, S.cle, 160, 940, 2, 1, .9);
  const T = army(za, 'egs', 4, 1300, 130, 940, 2, -1); const tA = W('abandonaron') - .3; gm.onFrame($('arr'), (l, i) => T.forEach((f, k) => { const d = Math.max(0, i.time - tA) * 200; EG.pose(f, { x: f.x0 + d, y: 940 + (k % 2) * 24, s: 2, dir: 1, run: i.time > tA ? 1 : 0, ph: i.time * 8 + k }); }));
  hd('<em>30 a. C.</em>', 'Octavio llega a Alejandría', S.arr + .3, tA); hd('ANTONIO, <em>SOLO</em>', 'sus tropas lo abandonan', tA, S.cle);
  const zc = PAL('cle'); fig(zc, 'cleo', 760, 900, 3.2); const oc = fig(zc, 'octav', 1500, 900, 3, -1); oc.o.setAttribute('opacity', .35); hd('<em>39 AÑOS</em>', 'Octavio quería llevarla a Roma como trofeo', S.cle + .3, S.end1); stamp('cle', 'NO SERÁ UN TROFEO', W('trofeo') - .2, 160, '#FFD23F');
  const ze = svgOf('end1', '#0a0604'); const lamp = mk('g', { transform: 'translate(1260 640)' }, ze); mk('path', { d: 'M-80 0 Q0 60 80 0 L60 -20 L-60 -20Z', fill: '#b08a4a' }, lamp); const flame = mk('path', { d: 'M60 -20 Q70 -70 90 -100 Q100 -50 80 -20Z', fill: '#ffb030' }, lamp); mk('circle', { cx: 78, cy: -60, r: 120, fill: '#ffb030', opacity: .12 }, lamp);
  const crown = mk('g', { transform: 'translate(700 640)' }, ze); mk('path', { d: 'M-120 0 L-120 -80 L-60 -40 L0 -110 L60 -40 L120 -80 L120 0Z', fill: '#d8b23a', stroke: '#8a6a2a', 'stroke-width': 5 }, crown); mk('rect', { x: -260, y: 0, width: 1220, height: 30, fill: '#5a3e22' }, ze);
  tl.to(lamp, { opacity: .25, duration: 2.5 }, W('agosto') - .2); hd('AGOSTO DEL <em>30 a. C.</em>', 'muere Cleopatra', S.end1 + .3, S.cob);
  const zo = svgOf('cob', '#0a0604'); const cb = mk('path', { d: 'M960 900 Q900 800 960 700 Q1020 600 960 500 Q900 420 960 360 Q1060 300 1040 400 Q1000 440 960 420', stroke: '#d8b23a', 'stroke-width': 30, fill: 'none', 'stroke-linecap': 'round' }, zo); tl.from(cb, { draw: 0, duration: 1.2 }, S.cob + .3);
  hd('LA <em>TRADICIÓN</em>', 'dice que fue con una cobra', S.cob + .3, W('historiadores') - .3); stamp('cob', 'NO SE SABE', W('historiadores') - .2, 760, '#FFD23F');
  const zp = svgOf('prov'); EG.desert(zp); EG.pyramids(zp, 960, 820, .8); const eag = mk('g', { transform: 'translate(1600 880)' }, zp); mk('rect', { x: -8, y: -420, width: 16, height: 420, fill: '#6b4a2a' }, eag); mk('path', { d: 'M-100 -430 Q-50 -490 0 -440 Q50 -490 100 -430 Q50 -450 0 -400 Q-50 -450 -100 -430Z', fill: '#d8b23a' }, eag); mk('rect', { x: -60, y: -380, width: 120, height: 80, fill: '#b3262d' }, eag); EG.label(eag, 'SPQR', 0, -325, 44, '#d8b23a');
  hd('EGIPTO, <em>PROVINCIA DE ROMA</em>', 'fin de los Ptolomeos y de los faraones', S.prov + .3, S.sel);
  const zl = svgOf('sel', 'radial-gradient(1200px 800px at 50% 45%, #1d2a5a, #050a1a 75%)'); SP.stars(zl, 160); SP.moon(zl, 1500, 300, 90); fig(zl, 'cleo', 900, 1000, 3); hd('<em>CLEOPATRA SELENE</em>', 'reina de Mauritania, en el norte de África', S.sel + .3, S.aug);
  const zu = svgOf('aug', 'radial-gradient(1200px 800px at 50% 45%, #3a2a10, #0a0604 75%)'); fig(zu, 'octav', 640, 1000, 3.4); const ag = mk('g', { transform: 'translate(1340 520)' }, zu); mk('rect', { x: -260, y: -220, width: 520, height: 440, rx: 24, fill: '#efe6d2' }, ag); mk('rect', { x: -260, y: -220, width: 520, height: 110, rx: 24, fill: '#b3262d' }, ag); EG.label(ag, 'AGOSTO', 0, -140, 90); EG.label(ag, 'AUGUSTO', 0, 60, 120, '#1a1a2a');
  tl.from(ag, { opacity: 0, scale: .8, duration: .4 }, W('agosto', 2) - .4); hd('<em>AUGUSTO</em>', 'el primer emperador de Roma', W('augusto') - .3, S.tomb);
  const zt = svgOf('tomb'); EG.desert(zt, { sun: true }); const ruin = EG.columns(zt, { n: 5, top: 380, bottom: 860, cap: 'doric', col: '#d8c8a0' }); ruin.setAttribute('opacity', .9); const dig = fig(zt, 'cit', 1500, 940, 2.2, -1);
  big('tomb', '¿DÓNDE ESTÁ SU <em>TUMBA</em>?', 110, S.tomb + .3, 'font-size:120px', W('taposiris') - .4); hd('<em>TAPOSIRIS MAGNA</em>', 'un templo cerca de Alejandría · sin pruebas todavía', W('taposiris') - .3, S.end);
  ender('end', '¿ENCONTRARÁN ALGÚN DÍA LA <span style="color:#FFD23F">TUMBA DE CLEOPATRA</span>?', S.end + .1);
''', card=(7, '30 a. C.', 'EL FINAL'), mood='mourn', last_mood='end', hits=['agosto'])
