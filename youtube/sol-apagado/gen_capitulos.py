"""¿Y si el Sol se apagara? · vídeo largo (6 capítulos). uso: python3 youtube/sol-apagado/gen_capitulos.py"""
import sys, os
R = '/home/user/curiosimundo-animation/'; sys.path.insert(0, R + 'tools')
from largo import Project
P = Project(R + 'youtube/sol-apagado', '¿Y si el Sol se apagara?', ['space.js'], open(R + 'tools/common_largo.js').read() + r'''
  const sunEarth = (s, sx = 330, ex = 1600, y = 560) => { SP.stars(s, 200); const sun = SP.sun(s, sx, y, 170); const e = SP.earth(s, ex, y, 70); return { sun, e }; };
''')

P.page(0, 'Arranque en frío: el Sol apagado hace 5 minutos, 8:20 sin saberlo, oscuridad, preguntas y promesa.',
 [('s0', 0), ('s1', ('qué')), ('s2', 'final'), ('t', ('y', 6))], r'''
  const z0 = svgOf('s0'); const L = SP.landscape(z0); const ck = SP.clock(z0, 960, 480, 230); ck.set(500);
  gm.onFrame($('s0'), (l, i) => { L.sun.spin(i.time); const k = gm.clamp((i.time - 1.0) / (W('oscuridad') - 1.0)); ck.set(500 - k * 500); });
  tl.fromTo(ck.g, { scale: 1.25, transformOrigin: '960px 330px' }, { scale: 1, duration: .5, ease: 'expo.out' }, 0);
  const lab = SP.label(z0, 'EL SOL YA SE APAGÓ', 960, 170, 90, '#FFD23F'); tl.from(lab, { opacity: 0, y: 20, duration: .3 }, W('apagado') - .2);
  tl.to(L.dark, { opacity: .72, duration: .15 }, W('oscuridad') - .1).to(L.night, { opacity: 1, duration: .1 }, W('oscuridad') - .1).to(L.sun.w, { opacity: 0, duration: .1 }, W('oscuridad') - .1).to([ck.g, lab], { opacity: 0, duration: .1 }, W('oscuridad') - .1);
  shake(z0, W('oscuridad') - .1, 20); big('s0', 'OSCURIDAD <em>TOTAL</em>', 420, W('oscuridad') + .1, 'font-size:170px');
  const z1 = svgOf('s1', SP.NIGHT); SP.stars(z1, 220); const e1 = SP.earth(z1, 960, 600, 230); gm.onFrame($('s1'), (l, i) => e1.rot(i.time));
  [['1 HORA', 'hora', 360], ['1 SEMANA', 'semana', 960], ['1 AÑO', 'año', 1560]].forEach(([t, w, x]) => { const g = SP.label(z1, t, x, 230, 110, '#FFD23F'); tl.from(g, { opacity: 0, scale: 1.4, duration: .3, transformOrigin: `${x}px 200px` }, W(w) - .3); });
  const th = SP.thermo(z1, 1650, 900, 420); th.g.setAttribute('opacity', .9); gm.onFrame($('s1'), (l, i) => th.set(1 - gm.clamp((i.time - S.s1) / (S.s2 - S.s1)), '#5bc0ff'));
  push('s1', 1, 1.12);
  const z2 = svgOf('s2', 'radial-gradient(1200px 800px at 50% 70%, #0d3a5e, #020814 75%)'); const oc = SP.ocean(z2); gm.onFrame($('s2'), (l, i) => oc.anim(i.time)); oc.vent.setAttribute('opacity', .25);
  big('s2', '¿QUIÉN <em>SOBREVIVIRÍA</em>?', 360, W('sobreviviría') - .3, 'font-size:150px'); mid('s2', 'no es quien <b>te imaginas</b>', 540, W('imaginas') - .5);
  const t = $('t'); t.style.background = 'radial-gradient(1200px 800px at 50% 45%, #2a1a08, #050308 75%)'; const zt = CM.svgIn(t); SP.stars(zt, 200); const st = SP.sun(zt, 960, 540, 260);
  gm.onFrame(t, (l, i) => st.spin(i.time)); tl.to(st.g, { opacity: .08, duration: 2.5, ease: 'power2.in' }, S.t + .6);
  const h = CM.text(t, 'big', '¿Y SI EL SOL SE <em>APAGARA</em>?', 380, 'font-size:180px'); const a = CM.text(t, 'mid', 'curiosimundo · la serie «¿y si…?»', 600, 'color:#FFD23F');
  tl.from(h, { scale: 1.3, opacity: 0, filter: 'blur(16px)', duration: .8, ease: 'expo.out' }, S.t + .2).to(h, { scale: 1.05, duration: D - S.t - 1, ease: 'sine.inOut' }, S.t + 1).from(a, { y: 30, opacity: 0, duration: .4 }, S.t + .8);
''', off=0, mood='tension_up', last_mood='title', hits=['oscuridad', ('y', 6)])

P.page(1, 'Los ocho minutos: 150 millones de km, luz a 300.000 km/s, el Sol de hace 8 minutos, la luz como un tren, gravedad a la velocidad de la luz (2017), la Tierra sigue girando.',
 [('dist', 0), ('see', 'eso'), ('train', 'si'), ('grav', 'gravedad'), ('orb', 'así'), ('zero', 'pero')], r'''
  const zd = svgOf('dist', SP.NIGHT); const a = sunEarth(zd); gm.onFrame($('dist'), (l, i) => { a.sun.spin(i.time); a.e.rot(i.time); });
  const ln = mk('path', { d: 'M520 760 L1520 760', stroke: '#FFD23F', 'stroke-width': 6, 'stroke-dasharray': '20 14' }, zd); tl.from(ln, { draw: 0, duration: 1 }, OFF + .3);
  const d1 = SP.label(zd, '150 MILLONES DE KM', 1020, 850, 90, '#FFD23F'); tl.from(d1, { opacity: 0, y: 20, duration: .4 }, W('cincuenta') - .2);
  const ph = mk('circle', { cx: 520, cy: 560, r: 22, fill: '#fff6c0' }, zd); const tr = mk('path', { d: 'M520 560 L520 560', stroke: '#ffe680', 'stroke-width': 10, 'stroke-linecap': 'round', opacity: .6 }, zd);
  const t0 = W('luz') - .2, t1 = W('aquí') + .3; gm.onFrame($('dist'), (l, i) => { const k = gm.clamp((i.time - t0) / (t1 - t0)), x = 520 + k * 1000; ph.setAttribute('cx', x); tr.setAttribute('d', `M${Math.max(520, x - 240)} 560 L${x} 560`); ph.setAttribute('opacity', i.time < t0 ? 0 : 1); });
  hd('LA LUZ: <em>300.000 KM/S</em>', 'y aun así tarda en llegar', W('luz') - .2, W('tarda') - .3); hd('<em>8 MIN 20 S</em>', 'del Sol a la Tierra', W('tarda') - .2, S.see);
  const zs = svgOf('see'); const L = SP.landscape(zs, { sunX: 1300, sunY: 260 }); gm.onFrame($('see'), (l, i) => L.sun.spin(i.time));
  const tag = SP.label(zs, 'HACE 8 MINUTOS', 1300, 420, 80, '#FFD23F'); tl.from(tag, { opacity: 0, y: 20, duration: .4 }, W('hace') - .3); hd('NO ES EL SOL <em>DE AHORA</em>', 'es su luz de hace 8 minutos', S.see + .3, S.train); push('see', 1.15, 1, '68%', '25%');
  const zt = svgOf('train', SP.NIGHT); const b = sunEarth(zt); gm.onFrame($('train'), (l, i) => { b.sun.spin(i.time); b.e.rot(i.time); });
  tl.to(b.sun.g, { opacity: 0, duration: .2 }, W('apagara') - .1); const off1 = SP.label(zt, 'APAGADO', 330, 820, 80, '#E5484D'); tl.from(off1, { opacity: 0, duration: .2 }, W('apagara'));
  const pk = mk('rect', { x: 500, y: 530, width: 260, height: 60, rx: 30, fill: '#ffe680', opacity: .85 }, zt); const tb = W('última') - .2;
  gm.onFrame($('train'), (l, i) => pk.setAttribute('x', 500 + gm.clamp((i.time - tb) / (S.grav - tb)) * 760));
  hd('LA ÚLTIMA <em>LUZ</em>', 'sigue viajando hacia nosotros', W('última') - .3, W('tren') - .3); hd('COMO UN <em>TREN</em>', 'que ya salió de la estación', W('tren') - .2, S.grav);
  const zg = svgOf('grav', SP.NIGHT); SP.stars(zg, 200); const ns = [0, 1].map(k => mk('circle', { r: 34, fill: '#cfe6ff' }, zg)); const rings = Array.from({ length: 6 }, () => mk('circle', { cx: 960, cy: 540, r: 10, fill: 'none', stroke: '#b06aff', 'stroke-width': 5 }, zg));
  gm.onFrame($('grav'), (l, i) => { const t = i.time - S.grav, rr = Math.max(30, 200 - t * 14), w = 2 + t * .5; ns.forEach((c, k) => { c.setAttribute('cx', 960 + Math.cos(t * w + k * Math.PI) * rr); c.setAttribute('cy', 540 + Math.sin(t * w + k * Math.PI) * rr * .5); });
    rings.forEach((c, k) => { const q = ((t * .4 + k / rings.length) % 1); c.setAttribute('r', 40 + q * 900); c.setAttribute('opacity', (1 - q) * .8); }); });
  hd('LA GRAVEDAD <em>TAMBIÉN</em>', 'viaja a la velocidad de la luz', S.grav + .3, W('dos') - .3); hd('<em>2017</em>', 'ondas gravitacionales · choque de dos estrellas de neutrones', W('dos') - .2, S.orb);
  const zo = svgOf('orb', SP.NIGHT); SP.stars(zo, 200); mk('circle', { cx: 960, cy: 560, r: 380, fill: 'none', stroke: '#5bc0ff', 'stroke-width': 3, 'stroke-dasharray': '10 12', opacity: .6 }, zo);
  const ghost = mk('circle', { cx: 960, cy: 560, r: 120, fill: 'none', stroke: '#ffcf4a', 'stroke-width': 4, 'stroke-dasharray': '14 10' }, zo); SP.label(zo, '¿?', 960, 590, 90, '#ffcf4a');
  const eo = SP.earth(zo, 0, 0, 50); const ck = SP.clock(zo, 1640, 170, 120);
  gm.onFrame($('orb'), (l, i) => { const t = i.time - S.orb; eo.w.setAttribute('transform', `translate(${960 + Math.cos(t * .5) * 380} ${560 + Math.sin(t * .5) * 380}) scale(.5)`); eo.rot(i.time); ck.set(500 * (1 - gm.clamp(t / (S.zero - S.orb + 1.5)))); });
  hd('UN SOL QUE <em>YA NO EXISTE</em>', 'y nadie lo nota', S.orb + .4, S.zero);
  const zz = svgOf('zero', '#03050d'); const c2 = SP.clock(zz, 960, 600, 300); gm.onFrame($('zero'), (l, i) => c2.set(Math.max(0, 1.6 - (i.time - S.zero))));
  tl.to(c2.t, { attr: { fill: '#E5484D' }, duration: .2 }, W('cero') - .2); shake(zz, W('cero'), 24); big('zero', 'TODO <em>CAMBIA</em>', 170, W('cambia') - .3, 'font-size:140px');
''', card=(1, '8:20', 'LOS OCHO MINUTOS'), hits=['cero'])

P.page(2, 'El apagón: el cielo se apaga, estrellas a mediodía, la Luna desaparece (y Venus, Marte, Júpiter), la Tierra sale en línea recta (30 km/s), la Luna se queda, llega el frío.',
 [('sky', 0), ('stars', 'estrellas'), ('moon', 'luna'), ('line', 'entonces'), ('moon2', ('luna', 2)), ('cold', 'ninguno')], r'''
  const zs = svgOf('sky'); const L = SP.landscape(zs); gm.onFrame($('sky'), (l, i) => L.sun.spin(i.time)); const ck = SP.clock(zs, 960, 400, 200);
  gm.onFrame($('sky'), (l, i) => ck.set(Math.max(0, 2 - (i.time - OFF) * 1.2)));
  const tA = W('apaga') - .1; tl.to(L.dark, { opacity: .72, duration: .15 }, tA).to(L.night, { opacity: 1, duration: .1 }, tA).to(L.sun.w, { opacity: 0, duration: .1 }, tA).to(ck.g, { opacity: 0, duration: .1 }, tA).to(L.win, { attr: { fill: '#ffd88a' }, duration: .3 }, tA + .8);
  shake(zs, tA, 22); hd('MINUTO <em>8:20</em>', 'el cielo se apaga en un instante', OFF + .2, S.stars);
  const zt = svgOf('stars', SP.NIGHT); SP.stars(zt, 500, 1920, 1080, 'st2'); mk('path', { d: 'M0 860 Q480 820 960 850 T1920 840 L1920 1080 L0 1080Z', fill: '#05080e' }, zt);
  const clk = SP.label(zt, '12:00 · MEDIODÍA', 960, 560, 150, '#FFD23F'); tl.from(clk, { opacity: 0, scale: 1.3, duration: .4, transformOrigin: '960px 520px' }, W('mediodía') - .4); push('stars', 1, 1.15);
  hd('ESTRELLAS <em>A MEDIODÍA</em>', 'su luz viene de mucho más lejos', S.stars + .3, S.moon);
  const zm = svgOf('moon', SP.NIGHT); SP.stars(zm, 260); const mo = SP.moon(zm, 960, 470, 200);
  tl.to(mo, { opacity: 0, duration: 1.2 }, W('desaparece') - .3); const lb = SP.label(zm, 'SOLO REFLEJA LA LUZ DEL SOL', 960, 820, 70, '#FFD23F'); tl.from(lb, { opacity: 0, duration: .4 }, W('refleja') - .3).to(lb, { opacity: 0, duration: .3 }, W('rato') - .3);
  [['VENUS', 'venus', 520, '#e8c27a', 70], ['MARTE', 'marte', 960, '#d0603a', 55], ['JÚPITER', 'júpiter', 1400, '#d8b48a', 110]].forEach(([n, w, x, c, r]) => { const p = SP.planet(zm, x, 600, r, c, false); const t = SP.label(zm, n, x, 800, 70);
    tl.from([p, t], { opacity: 0, duration: .3 }, S.moon + .5).to([p, t], { opacity: 0, duration: .8 }, W(w) - .1); });
  hd('LA LUNA <em>SE APAGA</em>', 'no tiene luz propia', S.moon + .3, W('rato') - .3); hd('Y LOS <em>PLANETAS</em>', 'uno detrás de otro', W('rato') - .2, S.line);
  const zl = svgOf('line', SP.NIGHT); SP.stars(zl, 260); mk('circle', { cx: 760, cy: 560, r: 380, fill: 'none', stroke: '#5bc0ff', 'stroke-width': 3, 'stroke-dasharray': '10 12', opacity: .5 }, zl);
  mk('circle', { cx: 760, cy: 560, r: 110, fill: '#1a1408', stroke: '#3a2e18', 'stroke-width': 4 }, zl); const el = SP.earth(zl, 0, 0, 50); const tr = mk('path', { d: '', stroke: '#5bc0ff', 'stroke-width': 4, fill: 'none', opacity: .8, 'stroke-dasharray': '4 10' }, zl);
  const tD = W('disparada') - .2; gm.onFrame($('line'), (l, i) => { const t = i.time; let x, y; const a0 = -Math.PI / 2 - (tD - Math.min(t, tD)) * .6;
    x = 760 + Math.cos(a0) * 380; y = 560 + Math.sin(a0) * 380; if (t > tD) { const d = (t - tD) * 90; x += -Math.sin(a0) * d; y += Math.cos(a0) * d; tr.setAttribute('d', `M${760 + Math.cos(a0) * 380} ${560 + Math.sin(a0) * 380} L${x} ${y}`); } else tr.setAttribute('d', '');
    el.w.setAttribute('transform', `translate(${x} ${y}) scale(.5)`); el.rot(t); });
  hd('LA TIERRA <em>SE SUELTA</em>', 'deja de girar alrededor del Sol', S.line + .3, tD - .1); hd('EN <em>LÍNEA RECTA</em>', '30 km/s · más de 100.000 km/h', tD, S.moon2);
  const zm2 = svgOf('moon2', SP.NIGHT); const sg = mk('g', {}, zm2); SP.stars(sg, 300, 3840, 1080, 'm2'); const e2 = SP.earth(zm2, 960, 560, 150); const m2 = SP.moon(zm2, 0, 0, 40);
  gm.onFrame($('moon2'), (l, i) => { const t = i.time - S.moon2; sg.setAttribute('transform', `translate(${-t * 80} 0)`); e2.rot(i.time); m2.setAttribute('transform', `translate(${960 + Math.cos(t * .9) * 360} ${560 + Math.sin(t * .9) * 140})`); });
  hd('LA LUNA <em>SE QUEDA</em>', 'la sujeta la gravedad de la Tierra', S.moon2 + .3, S.cold);
  const zc = svgOf('cold', SP.NIGHT); SP.stars(zc, 260); const e3 = SP.earth(zc, 960, 560, 260); gm.onFrame($('cold'), (l, i) => e3.rot(i.time));
  const frost = mk('circle', { cx: 960, cy: 560, r: 262, fill: '#dff4ff', opacity: 0 }, zc); tl.to(frost, { opacity: .55, duration: 3 }, W('peligroso') - .5);
  big('cold', 'EL <em>FRÍO</em>', 420, W('frío') - .3, 'font-size:240px'); shake(zc, W('frío'), 16);
''', card=(2, '0:00', 'EL APAGÓN'), hits=['apaga', 'disparada', 'frío'])

P.page(3, 'El frío: en una semana bajo 0 °C, en un año más de −70 °C, sin fotosíntesis, árboles con reservas, mares que se congelan desde arriba.',
 [('th', 0), ('pl', 'fotosíntesis'), ('tr', 'árboles'), ('lake', 'lagos'), ('hook', 'justo')], r'''
  const zt = svgOf('th', SP.NIGHT); SP.stars(zt, 200); const e = SP.earth(zt, 620, 560, 300); gm.onFrame($('th'), (l, i) => e.rot(i.time * .5));
  const fr = mk('circle', { cx: 620, cy: 560, r: 302, fill: '#e6f6ff', opacity: 0 }, zt); const th = SP.thermo(zt, 1400, 900, 640);
  const k1 = W('semana'), k2 = W('año'); gm.onFrame($('th'), (l, i) => { const t = i.time; const temp = t < k1 ? 15 - gm.clamp((t - OFF) / (k1 - OFF)) * 15 : t < k2 ? -gm.clamp((t - k1) / (k2 - k1)) * 8 : -8 - gm.clamp((t - k2) / 2.5) * 64;
    th.set(gm.clamp((temp + 80) / 100), temp > 0 ? '#E5484D' : '#5bc0ff'); th.lab.textContent = `${Math.round(temp)} °C`; fr.setAttribute('opacity', gm.clamp((15 - temp) / 90) * .6); });
  hd('<em>1 SEMANA</em>', 'temperatura media bajo cero', k1 - .3, k2 - .3); hd('<em>1 AÑO</em>', 'más de −70 °C · como el invierno de la Antártida', k2 - .2, S.pl); const ea = SP.label(zt, 'ESTIMACIONES APROXIMADAS', 1400, 1010, 44, '#FFD23F'); tl.from(ea, { opacity: 0, duration: .3 }, W('estimaciones') - .3);
  const zp = svgOf('pl', 'linear-gradient(#0a1020, #1a2236)'); mk('rect', { y: 760, width: 1920, height: 320, fill: '#2a2a20' }, zp); const P = [];
  for (let i = 0; i < 26; i++) { const x = 60 + i * 72, h = 160 + gm.random('ph' + i) * 140, g0 = mk('g', { transform: `translate(${x} 780)` }, zp), g = mk('g', { style: 'transform-origin:0px 0px' }, g0); const st = mk('path', { d: `M0 0 Q${(gm.random('pq' + i) - .5) * 40} ${-h / 2} 0 ${-h}`, stroke: '#3f9a4a', 'stroke-width': 8, fill: 'none' }, g);
    const lf = mk('ellipse', { cx: 18, cy: -h * .6, rx: 26, ry: 10, fill: '#3f9a4a', transform: `rotate(-30 18 ${-h * .6})` }, g); const fl = mk('circle', { cy: -h, r: 18, fill: i % 3 ? '#FFD23F' : '#e5484d' }, g); P.push({ g, st, lf, fl, h }); }
  const tw = W('mayoría') - .5; P.forEach((p, i) => { tl.to([p.st, p.lf], { attr: { stroke: '#7a5a2a', fill: '#7a5a2a' }, duration: 1.5 }, tw + i * .04).to(p.g, { rotate: 18 + gm.random('pr' + i) * 30, duration: 1.5 }, tw + i * .04).to(p.fl, { opacity: 0, duration: 1 }, tw + i * .04); });
  hd('SIN <em>FOTOSÍNTESIS</em>', 'las plantas no pueden fabricar su alimento', S.pl + .3, tw - .3); hd('EN POCAS <em>SEMANAS</em>', 'la mayoría moriría', tw - .2, S.tr);
  const zr = svgOf('tr', 'linear-gradient(#0a1020, #26304a)'); mk('rect', { y: 800, width: 1920, height: 280, fill: '#6f8299' }, zr); const tree = mk('g', { transform: 'translate(760 880) scale(2)' }, zr);
  mk('rect', { x: -14, y: -140, width: 28, height: 140, fill: '#5a3e22' }, tree); [[0, -190, 80], [-60, -150, 56], [60, -156, 58]].forEach(([x, y, r]) => { mk('circle', { cx: x, cy: y, r, fill: '#2c5a2a' }, tree); mk('ellipse', { cx: x, cy: y - r * .7, rx: r * .8, ry: r * .3, fill: '#f4f8fb' }, tree); });
  const cell0 = mk('g', { transform: 'translate(1420 520)' }, zr), cell = mk('g', {}, cell0); mk('circle', { r: 150, fill: 'rgb(255 210 63 / .15)', stroke: '#FFD23F', 'stroke-width': 5 }, cell); SP.label(cell, 'AZÚCAR', 0, 20, 80, '#FFD23F'); tl.from(cell, { scale: 0, duration: .4, ease: 'back.out(2)' }, W('reservas') - .3);
  hd('LOS ÁRBOLES <em>AGUANTAN</em>', 'guardan reservas y el frío los conserva', S.tr + .3, W('animales') - .3); hd('SIN PLANTAS…', 'los animales que comen plantas tampoco durarían', W('animales') - .2, S.lake);
  const zl = svgOf('lake', 'linear-gradient(#0a1020, #1a2236)'); mk('rect', { y: 300, width: 1920, height: 780, fill: '#0c3f8a' }, zl); const ice = mk('rect', { y: 300, width: 1920, height: 0, fill: '#d9f0ff' }, zl);
  tl.to(ice, { attr: { height: 220 }, duration: (S.hook - S.lake), ease: 'power1.out' }, S.lake); const ar = mk('path', { d: 'M1700 340 L1700 520 M1660 480 L1700 530 L1740 480', stroke: '#fff', 'stroke-width': 10, fill: 'none' }, zl);
  hd('SE CONGELAN', 'de arriba hacia abajo', S.lake + .3, S.hook);
  const zh = svgOf('hook', '#04142e'); const oc = SP.ocean(zh); gm.onFrame($('hook'), (l, i) => oc.anim(i.time)); oc.vent.setAttribute('opacity', 0); oc.crab.setAttribute('opacity', 0); oc.microbes.forEach(m => m.setAttribute('opacity', 0));
  big('hook', '<em>?</em>', 400, W('lugar') - .3, 'font-size:300px'); mid('hook', 'debajo del <b>hielo</b>', 760, W('hielo') - .3);
''', card=(3, '−70 °C', 'EL FRÍO'), mood='mourn', hits=['año', 'justo'])

P.page(4, 'Quién sobreviviría: el hielo como manta, el fondo del mar líquido, fuentes hidrotermales, microbios, gusanos, cangrejos; los supervivientes; personas con energía nuclear o geotérmica; la buena noticia.',
 [('ice', 0), ('deep', 'eso'), ('vent', 'allí'), ('life', 'gusanos'), ('ans', 'esa'), ('hum', 'nosotros'), ('good', 'ahora')], r'''
  const zi = svgOf('ice', '#04142e'); const o1 = SP.ocean(zi); gm.onFrame($('ice'), (l, i) => o1.anim(i.time)); o1.vent.setAttribute('opacity', 0); o1.crab.setAttribute('opacity', 0); o1.microbes.forEach(m => m.setAttribute('opacity', 0));
  const bl = mk('path', { d: 'M0 175 Q480 150 960 175 T1920 170', stroke: '#FFD23F', 'stroke-width': 8, fill: 'none' }, zi); tl.from(bl, { draw: 0, duration: 1.2 }, W('manta') - .4);
  SP.label(zi, '−70 °C', 1700, 80, 80, '#9fd3f5'); const w1 = SP.label(zi, 'AGUA LÍQUIDA', 960, 560, 100, '#5bc0ff'); tl.from(w1, { opacity: 0, duration: .4 }, W('aísla') - .3);
  hd('EL HIELO, <em>UNA MANTA</em>', 'aísla el agua de abajo', S.ice + .3, S.deep);
  const zd = svgOf('deep', '#020a1a'); const o2 = SP.ocean(zd); gm.onFrame($('deep'), (l, i) => o2.anim(i.time)); o2.vent.setAttribute('opacity', 0); o2.crab.setAttribute('opacity', 0); push('deep', 1, 1.4, '50%', '90%');
  big('deep', 'CIENTOS DE <em>MILES</em> DE AÑOS', 380, W('cientos') - .3, 'font-size:120px'); hd('EL FONDO DEL MAR', 'seguiría líquido muchísimo tiempo', S.deep + .3, S.vent);
  const zv = svgOf('vent', '#020a1a'); const o3 = SP.ocean(zv); gm.onFrame($('vent'), (l, i) => o3.anim(i.time)); o3.ice.setAttribute('opacity', .3); o3.crab.setAttribute('opacity', 0); o3.worms.forEach(w => w.w.setAttribute('opacity', 0));
  tl.fromTo(zv, { scale: 1.6 }, { scale: 1, duration: 3, ease: 'power2.inOut', transformOrigin: '57% 80%' }, S.vent);
  hd('VIDA <em>SIN SOL</em>', 'en la oscuridad del fondo', S.vent + .3, W('fuentes') - .3); hd('FUENTES <em>HIDROTERMALES</em>', 'chimeneas de agua caliente del interior de la Tierra', W('fuentes') - .2, W('microbios') - .3);
  hd('<em>MICROBIOS</em>', 'se alimentan de sustancias químicas', W('microbios') - .2, S.life);
  const zf = svgOf('life', '#020a1a'); const o4 = SP.ocean(zf); gm.onFrame($('life'), (l, i) => o4.anim(i.time)); o4.ice.setAttribute('opacity', 0);
  tl.fromTo(zf, { scale: 1.9 }, { scale: 1.3, duration: S.ans - S.life, ease: 'none', transformOrigin: '52% 88%' }, S.life);
  [['GUSANOS GIGANTES', 'gusanos', 780], ['CANGREJOS', 'cangrejos', 860], ['ALMEJAS', 'almejas', 940]].forEach(([t, w, y]) => mid('life', `<b>${t}</b>`, y - 600, W(w) - .2, 'font-size:44px', S.ans));
  hd('SIN SOL… <em>NO CAMBIA NADA</em>', 'para ellos', W('ellos') - .3, S.ans);
  const za = svgOf('ans', 'radial-gradient(1200px 800px at 50% 50%, #0d3a5e, #020814 75%)'); for (let i = 0; i < 70; i++) mk('circle', { cx: gm.random('ax' + i) * 1920, cy: gm.random('ay' + i) * 1080, r: 4 + gm.random('ar' + i) * 10, fill: '#7cf0c0', opacity: .5 }, za);
  big('ans', 'LOS <em>SUPERVIVIENTES</em>', 300, S.ans + .5, 'font-size:150px'); mid('ans', 'seres diminutos del <b>fondo del mar</b>', 500, W('diminutos') - .3); mid('ans', 'millones de años <b>sin ver la luz</b>', 580, W('millones') - .3);
  const zh = svgOf('hum', 'linear-gradient(#03050d, #0e1626 70%)'); mk('rect', { y: 800, width: 1920, height: 280, fill: '#6f8299' }, zh); const steam = Array.from({ length: 8 }, (_, i) => mk('circle', { cx: 1300 + (i % 3) * 60, cy: 780, r: 40, fill: '#cfd8e2', opacity: .5 }, zh));
  [[1240, 'M0 0 L0 -120 L60 -120 L60 0Z'], [1380, 'M0 0 L0 -90 L50 -90 L50 0Z']].forEach(([x, d]) => mk('path', { d, fill: '#6a7684', transform: `translate(${x} 800)` }, zh));
  for (let i = 0; i < 5; i++) { const hx = 200 + i * 200, h = mk('g', { transform: `translate(${hx} 800)` }, zh); mk('rect', { x: -60, y: -100, width: 120, height: 100, fill: '#4a4f5a' }, h); mk('path', { d: 'M-75 -100 L0 -160 L75 -100Z', fill: '#e8eef4' }, h); mk('rect', { x: -20, y: -70, width: 40, height: 34, fill: '#ffd88a' }, h); }
  gm.onFrame($('hum'), (l, i) => steam.forEach((c, k) => { const q = ((i.time * .25 + k / 8) % 1); c.setAttribute('cy', 760 - q * 420); c.setAttribute('r', 30 + q * 80); c.setAttribute('opacity', .5 * (1 - q)); }));
  hd('¿Y <em>NOSOTROS</em>?', 'energía nuclear o calor del interior de la Tierra', S.hum + .3, W('islandia') - .3); hd('COMO <em>ISLANDIA</em>', 'calienta casas con calor de la Tierra', W('islandia') - .2, S.good);
  const zg = svgOf('good', 'radial-gradient(1200px 800px at 50% 45%, #2a1a08, #050308 75%)'); SP.stars(zg, 150); const sg = SP.sun(zg, 960, 560, 220); gm.onFrame($('good'), (l, i) => sg.spin(i.time)); tl.from(sg.g, { opacity: 0, scale: .3, duration: 1, ease: 'back.out(1.6)' }, S.good + .2);
  big('good', 'LA BUENA <em>NOTICIA</em>', 120, W('buena') - .3, 'font-size:130px'); stamp('good', 'NO PUEDE PASAR', W('puede') - .3, 820, '#FFD23F');
''', card=(4, 'BAJO EL HIELO', 'QUIÉN SOBREVIVIRÍA'), hits=['respuesta', 'buena'])

P.page(5, 'El futuro real del Sol: 4600 millones de años, 5000 millones más, gigante roja, enana blanca, recapitulación y pregunta final.',
 [('age', 0), ('fuel', 'le'), ('red', 'cuando'), ('wd', 'después'), ('rec', 'así'), ('end', 'qué')], r'''
  const za = svgOf('age', SP.NIGHT); SP.stars(za, 240); const s1 = SP.sun(za, 960, 470, 220); gm.onFrame($('age'), (l, i) => s1.spin(i.time));
  hd('UNA <em>ESTRELLA</em>', 'de unos 4.600 millones de años', S.age + .3, W('bombilla') - .5); stamp('age', 'NO ES UNA BOMBILLA', W('bombilla') - .4, 720, '#FFD23F');
  const zf = svgOf('fuel', SP.NIGHT); SP.stars(zf, 200); mk('rect', { x: 200, y: 520, width: 1520, height: 40, rx: 20, fill: '#1d2a4a' }, zf); const bar = mk('rect', { x: 200, y: 520, width: 1520, height: 40, rx: 20, fill: '#FFD23F' }, zf);
  tl.from(bar, { attr: { width: 0 }, duration: 2, ease: 'power2.out' }, S.fuel + .3); const n = SP.label(zf, 'HOY', 200, 470, 70, '#fff', 'start'); const f = SP.label(zf, '+5.000 MILLONES DE AÑOS', 1720, 640, 80, '#FFD23F', 'end');
  tl.from(f, { opacity: 0, duration: .4 }, W('cinco') - .2); hd('LE QUEDA <em>COMBUSTIBLE</em>', 'para unos 5.000 millones de años', S.fuel + .3, S.red);
  const zr = svgOf('red', SP.NIGHT); SP.stars(zr, 200); [200, 300, 420].forEach((r, k) => mk('circle', { cx: 960, cy: 560, r, fill: 'none', stroke: k === 2 ? '#5bc0ff' : '#9fb3c8', 'stroke-width': 3, 'stroke-dasharray': '8 10', opacity: .7 }, zr));
  const rg = mk('g', {}, zr); mk('circle', { cx: 960, cy: 560, r: 600, fill: 'url(#spRedGlow)' }, rg); const rc = mk('circle', { cx: 960, cy: 560, r: 90, fill: 'url(#spSun)' }, rg), rr = mk('circle', { cx: 960, cy: 560, r: 90, fill: 'url(#spRed)', opacity: 0 }, rg); SP.label(zr, 'ÓRBITA DE LA TIERRA', 1400, 200, 50, '#5bc0ff');
  tl.to([rc, rr], { attr: { r: 420 }, duration: 4, ease: 'power1.inOut' }, W('hinchará') - .3).to(rr, { opacity: 1, duration: 2 }, W('hinchará')); hd('UNA <em>GIGANTE ROJA</em>', 'quizá hasta la órbita de la Tierra', W('gigante') - .3, S.wd);
  const zw = svgOf('wd', SP.NIGHT); SP.stars(zw, 240); const neb = mk('circle', { cx: 960, cy: 560, r: 120, fill: 'none', stroke: '#b06aff', 'stroke-width': 40, opacity: .5 }, zw); const wd = mk('circle', { cx: 960, cy: 560, r: 26, fill: '#eaf4ff' }, zw);
  tl.to(neb, { attr: { r: 460, 'stroke-width': 6 }, opacity: .15, duration: S.rec - S.wd, ease: 'power1.out' }, S.wd); hd('UNA <em>ENANA BLANCA</em>', 'pequeña, densa, enfriándose poco a poco', W('enana') - .3, S.rec);
  const zc = svgOf('rec', SP.NIGHT); const a = sunEarth(zc); gm.onFrame($('rec'), (l, i) => { a.sun.spin(i.time); a.e.rot(i.time); }); const ck = SP.clock(zc, 960, 330, 160);
  big('rec', '<em>8 MINUTOS</em> Y 20 SEGUNDOS', 760, W('exactamente') - .3, 'font-size:110px'); hd('NO SE APAGARÁ', 'de un día para otro', S.rec + .3, W('ahora') - .3);
  ender('end', '¿QUÉ HARÍAS TÚ EN ESOS <span style="color:#FFD23F">8 MINUTOS</span>?', S.end + .1);
''', card=(5, '5.000 M', 'EL FUTURO DEL SOL'), mood='tension', last_mood='end', hits=['exactamente'])
