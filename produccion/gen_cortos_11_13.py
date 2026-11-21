"""Cortos 11 (¿Y si el Sol se apagara?), 12 (Venus) y 13 (Cleopatra). uso: python3 produccion/gen_cortos_11_13.py"""
import sys
R = '/home/user/curiosimundo-animation/'; sys.path.insert(0, R + 'tools')
from corto import corto
NIGHT = 'radial-gradient(1200px 1400px at 50% 40%, #0f1a3a, #03050d 75%)'

corto(R + 'produccion/11-sol-apagado', 'CURIOSIMUNDO · 11 · ¿Y si el Sol se apagara?', ['space.js'],
 [('s0', 0), ('s1', 'seguirías'), ('s2', 'luna'), ('s3', 'tierra'), ('s4', 'semana')],
 [(0, '<em>8</em> MINUTOS'), ('apagara', 'SI EL SOL<br>SE <em>APAGARA</em>…'), ('enterarías', 'NO TE<br><em>ENTERARÍAS</em>'), ('seguirías', 'CIELO <em>AZUL</em>…'), ('oscuridad', '¡<em>OSCURIDAD</em>!'),
  ('luna', 'LA LUNA<br><em>TAMBIÉN</em>'), ('tierra', 'LA TIERRA<br><em>SALE DISPARADA</em>'), ('cien', '+<em>100.000</em><br>KM/H'), ('semana', '1 SEMANA:<br><em>BAJO CERO</em>'), ('año', '1 AÑO:<br><em>−70 °C</em>')],
 r'''
  const NIGHT = 'radial-gradient(1200px 1400px at 50% 40%, #0f1a3a, #03050d 75%)';
  const b0 = scene('s0'); const L0 = SP.landscape(b0); const ck = SP.clock(b0, 960, 520, 260); gm.onFrame($('s0'), (l, i) => { L0.sun.spin(i.time); ck.set(500 - i.time * 70); });
  const b1 = scene('s1'); const L1 = SP.landscape(b1); gm.onFrame($('s1'), (l, i) => L1.sun.spin(i.time)); const tA = W('oscuridad') - .1;
  tl.to(L1.dark, { opacity: .72, duration: .15 }, tA).to(L1.night, { opacity: 1, duration: .1 }, tA).to(L1.sun.w, { opacity: 0, duration: .1 }, tA); shake($('s1'), tA, 24);
  const b2 = scene('s2', NIGHT); SP.stars(b2, 240); const mo = SP.moon(b2, 960, 540, 260); tl.to(mo, { opacity: 0, duration: 1.4 }, W('desaparecería') - .2);
  const b3 = scene('s3', NIGHT); const sg = mk('g', {}, b3); SP.stars(sg, 300, 3840, 1080, 'f'); const e3 = SP.earth(b3, 960, 540, 200); gm.onFrame($('s3'), (l, i) => { const t = i.time - S.s3; sg.setAttribute('transform', `translate(${-t * 500} 0)`); e3.rot(i.time); });
  const b4 = scene('s4', NIGHT); SP.stars(b4, 200); const e4 = SP.earth(b4, 640, 540, 280); gm.onFrame($('s4'), (l, i) => e4.rot(i.time * .5)); const fr = mk('circle', { cx: 640, cy: 540, r: 282, fill: '#e6f6ff', opacity: 0 }, b4);
  const th = SP.thermo(b4, 1450, 880, 680); const k1 = W('semana'), k2 = W('año');
  gm.onFrame($('s4'), (l, i) => { const t = i.time, temp = t < k1 ? 15 : t < k2 ? 15 - gm.clamp((t - k1) / 1) * 18 : -3 - gm.clamp((t - k2) / 1.5) * 69; th.set(gm.clamp((temp + 80) / 100), temp > 0 ? '#E5484D' : '#5bc0ff'); th.lab.textContent = Math.round(temp) + ' °C'; fr.setAttribute('opacity', gm.clamp((15 - temp) / 90) * .6); });
''', 'pero', '¿QUIÉN <span style="color:#FFD23F">SOBREVIVIRÍA</span>?<br>TE LO CUENTO EN YOUTUBE',
 [[0, 'oscuridad', 'tension_up'], ['oscuridad', 'pero', 'tension'], ['pero', 99, 'end']], hits=['oscuridad', 'disparada', 'año'], final=('qué', '¿QUÉ HARÍAS TÚ<br>EN <span style="color:#FFD23F">8 MINUTOS</span>?'))

corto(R + 'produccion/12-venus', 'CURIOSIMUNDO · 12 · Venus: un día más largo que un año', ['space.js'],
 [('s0', 0), ('s1', ('sí', 2)), ('s2', ('y', 3)), ('s3', 'suelo'), ('s4', 'nave'), ('s5', 'ojo')],
 [(0, '<em>243</em> DÍAS'), ('venus', 'UNA VUELTA<br>A <em>VENUS</em>'), ('año', 'SU AÑO:<br><em>225</em> DÍAS'), (('sí', 2), '<em>243 &gt; 225</em>'), (('y', 3), 'Y ESO ES LO<br><em>MENOS RARO</em>'), ('oeste', 'EL SOL SALE<br>POR EL <em>OESTE</em>'),
  ('suelo', '<em>465 °C</em>'), ('mercurio', 'MÁS QUE<br><em>MERCURIO</em>'), ('ácido', 'NUBES DE<br><em>ÁCIDO</em>'), ('nave', 'VENERA 13<br><em>1982</em>'), ('veintisiete', '<em>127</em> MINUTOS'), ('ojo', 'DE AMANECER<br>A AMANECER'), ('diecisiete', '<em>117</em> DÍAS')],
 r'''
  const VS = 'radial-gradient(1200px 1400px at 50% 40%, #1a1430, #05030d 75%)';
  const b0 = scene('s0', VS); SP.stars(b0, 200); const v0 = SP.venus(b0, 960, 540, 380); const mk0 = mk('circle', { r: 24, fill: '#E5484D', stroke: '#fff', 'stroke-width': 5 }, b0);
  gm.onFrame($('s0'), (l, i) => { v0.flow(i.time); const a = i.time * .3; mk0.setAttribute('cx', 960 + Math.sin(a) * 380); mk0.setAttribute('cy', 500); mk0.setAttribute('opacity', Math.cos(a) > 0 ? 1 : 0); });
  const b1 = scene('s1', VS); SP.stars(b1, 200); const so = SP.sun(b1, 960, 540, 130); mk('circle', { cx: 960, cy: 540, r: 400, fill: 'none', stroke: '#e8c27a', 'stroke-width': 4, 'stroke-dasharray': '12 14' }, b1); const vo = SP.venus(b1, 0, 0, 70);
  gm.onFrame($('s1'), (l, i) => { so.spin(i.time); const a = (i.time - S.s1) * .9; vo.w.setAttribute('transform', `translate(${960 + Math.cos(a) * 400} ${540 + Math.sin(a) * 400})`); });
  const b2 = scene('s2'); SP.venusGround(b2); const sr = SP.sun(b2, 0, 0, 110); gm.onFrame($('s2'), (l, i) => { const k = gm.clamp((i.time - S.s2 - .5) / 3); sr.w.setAttribute('transform', `translate(${280 + k * 320} ${720 - k * 420})`); sr.spin(i.time); }); SP.label(b2, 'OESTE', 240, 800, 110); SP.label(b2, 'ESTE', 1680, 800, 110);
  const b3 = scene('s3'); SP.venusGround(b3); const th = SP.thermo(b3, 1500, 900, 700); gm.onFrame($('s3'), (l, i) => { const k = gm.clamp((i.time - S.s3) / 2); th.set(k); th.lab.textContent = Math.round(k * 465) + ' °C'; });
  const rd = []; for (let i = 0; i < 50; i++) rd.push(mk('line', { stroke: '#d8e24a', 'stroke-width': 5 }, b3)); gm.onFrame($('s3'), (l, i) => rd.forEach((d, k) => { const q = (i.time * .7 + gm.random('q' + k)) % 1, x = gm.random('x' + k) * 1200; d.setAttribute('x1', x); d.setAttribute('x2', x - 6); d.setAttribute('y1', q * 500); d.setAttribute('y2', q * 500 + 34); d.setAttribute('opacity', i.time > W('ácido') - .3 ? 1 - q : 0); }));
  const b4 = scene('s4'); SP.venusGround(b4); SP.venera(b4, 600, 900, 1.4); mk('rect', { x: 1000, y: 300, width: 800, height: 60, rx: 30, fill: 'rgb(6 12 28 / .7)' }, b4); const bar = mk('rect', { x: 1000, y: 300, width: 0, height: 60, rx: 30, fill: '#FFD23F' }, b4);
  const tm = SP.label(b4, '0 MIN', 1400, 560, 200, '#fff'); gm.onFrame($('s4'), (l, i) => { const k = gm.clamp((i.time - S.s4 - .3) / (W('veintisiete') - S.s4)); bar.setAttribute('width', 800 * k); tm.textContent = Math.round(k * 127) + ' MIN'; });
  const b5 = scene('s5', VS); SP.stars(b5, 160); const dial = mk('g', { transform: 'translate(960 540)' }, b5); mk('circle', { r: 400, fill: '#1d2a4a' }, dial); mk('path', { d: 'M0 -400 A400 400 0 0 1 0 400Z', fill: '#f2c46a' }, dial);
  const hand = mk('line', { x1: 0, y1: 0, x2: 0, y2: -360, stroke: '#E5484D', 'stroke-width': 16, 'stroke-linecap': 'round' }, dial); gm.onFrame($('s5'), (l, i) => hand.setAttribute('transform', `rotate(${(i.time - S.s5) * 60})`));
''', 'historia', 'LA HISTORIA COMPLETA<br>EN <span style="color:#FFD23F">YOUTUBE</span>',
 [[0, ('y', 3), 'tension_up'], [('y', 3), 'historia', 'tension'], ['historia', 99, 'end']], hits=[('y', 3), 'veintisiete'], final=('gustaría', '¿VIVIRÍAS UN DÍA<br>DE <span style="color:#FFD23F">117 DÍAS</span>?'))

corto(R + 'produccion/13-cleopatra', 'CURIOSIMUNDO · 13 · Cleopatra está más cerca de ti que de las pirámides', ['space.js', 'egypt.js'],
 [('s0', 0), ('s1', ('pirámide', 2)), ('s2', 'aquí'), ('s3', 'sea'), ('s4', 'para'), ('s5', 'ni')],
 [(0, '<em>2.500</em> AÑOS'), ('cleopatra', 'CLEOPATRA<br>Y LA <em>PIRÁMIDE</em>'), (('pirámide', 2), '<em>2560</em> a. C.'), (('cleopatra', 2), '<em>69</em> a. C.'), ('aquí', 'Y AQUÍ VIENE<br><em>LO BUENO</em>'), ('luna', 'LA LUNA:<br><em>1969</em>'),
  (('dos', 3), '<em>≈ 2.000</em> AÑOS'), ('sea', 'MÁS CERCA<br>DEL <em>COHETE</em>'), ('para', 'PARA ELLA, YA<br>ERAN <em>ANTIGUAS</em>'), ('heródoto', '<em>HERÓDOTO</em><br>FUE A VERLAS'), ('ni', 'NI SIQUIERA<br>ERA <em>EGIPCIA</em>'), ('griega', 'FAMILIA<br><em>GRIEGA</em>')],
 r'''
  const b0 = scene('s0'); EG.desert(b0); EG.pyramid(b0, 380, 860, 560); const c0 = EG.person(b0, 'cleo'); EG.place(c0, 1380, 920, 3.2); mk('rect', { x: 0, y: 930, width: 1920, height: 14, fill: '#3a2a1a' }, b0);
  const ar = mk('path', { d: 'M520 420 Q900 160 1300 420', stroke: '#FFD23F', 'stroke-width': 12, fill: 'none' }, b0); tl.from(ar, { draw: 0, duration: 1 }, .3);
  const b1 = scene('s1'); EG.desert(b1); mk('rect', { x: 60, y: 800, width: 1800, height: 16, rx: 8, fill: '#3a2a1a' }, b1); EG.pyramid(b1, 260, 790, 300); const c1 = EG.person(b1, 'cleo'); EG.place(c1, 1000, 790, 2);
  const l1 = EG.label(b1, '2560 a. C.', 260, 900, 80); const l2 = EG.label(b1, '69 a. C.', 1000, 900, 80); tl.from(l2, { opacity: 0, duration: .3 }, W('cleopatra', 2) - .2);
  const b2 = scene('s2'); EG.desert(b2); mk('rect', { x: 60, y: 800, width: 1800, height: 16, rx: 8, fill: '#3a2a1a' }, b2); EG.pyramid(b2, 260, 790, 300); const c2 = EG.person(b2, 'cleo'); EG.place(c2, 1000, 790, 2); const rk = EG.rocket(b2, 1680, 790, 1.2);
  EG.label(b2, '2560 a. C.', 260, 900, 70); EG.label(b2, '69 a. C.', 1000, 900, 70); const l3 = EG.label(b2, '1969', 1680, 900, 80, '#fff'); tl.from([rk, l3], { opacity: 0, duration: .4 }, W('luna') - .3);
  const a1 = mk('path', { d: 'M300 600 Q650 380 980 600', stroke: '#FFD23F', 'stroke-width': 10, fill: 'none' }, b2), a2 = mk('path', { d: 'M1040 600 Q1360 420 1640 600', stroke: '#5bc0ff', 'stroke-width': 10, fill: 'none' }, b2);
  tl.from(a1, { draw: 0, duration: .6 }, S.s2 + .3).from(a2, { draw: 0, duration: .6 }, W('dos', 3) - .3);
  const b3 = scene('s3'); EG.desert(b3); mk('rect', { x: 60, y: 800, width: 1800, height: 16, rx: 8, fill: '#3a2a1a' }, b3); EG.pyramid(b3, 260, 790, 300); EG.rocket(b3, 1680, 790, 1.2); const c3 = EG.person(b3, 'cleo');
  gm.onFrame($('s3'), (l, i) => { const k = gm.clamp((i.time - S.s3 - .2) / 2); EG.pose(c3, { x: 1000 + k * 520, y: 790, s: 2, run: k > 0 && k < 1 ? 1 : 0, ph: i.time * 8 }); });
  const b4 = scene('s4'); EG.desert(b4); EG.pyramids(b4, 960, 820, .9); const hd = EG.person(b4, 'cit'); gm.onFrame($('s4'), (l, i) => { const k = gm.clamp((i.time - W('heródoto')) / 3); EG.pose(hd, { x: 1700 - k * 400, y: 960, s: 2.6, dir: -1, run: k > 0 && k < 1 ? 1 : 0, ph: i.time * 8 }); });
  const b5 = scene('s5'); EG.palace(b5); EG.place(EG.person(b5, 'cleo'), 760, 1000, 3.6); const gl = EG.label(b5, 'MACEDONIA · <tspan fill="#FFD23F">GRIEGA</tspan>', 1380, 560, 110); tl.from(gl, { opacity: 0, x: 40, duration: .4 }, W('griega') - .3);
  const eg = EG.label(b5, 'APRENDIÓ <tspan fill="#FFD23F">EGIPCIO</tspan>', 1380, 720, 100); tl.from(eg, { opacity: 0, x: 40, duration: .4 }, W('egipcio') - .3);
''', 'historia', 'SU HISTORIA COMPLETA<br>EN <span style="color:#FFD23F">YOUTUBE</span>',
 [[0, 'aquí', 'tension_up'], ['aquí', 'historia', 'tension'], ['historia', 99, 'end']], hits=['aquí', 'sea'], final=('qué', '¿QUÉ DATO DE HISTORIA<br>TE <span style="color:#FFD23F">ROMPE LA CABEZA</span>?'))
