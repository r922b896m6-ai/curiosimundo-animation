"""Venus: el infierno de al lado · vídeo largo (6 capítulos). uso: python3 youtube/venus/gen_capitulos.py"""
import sys
R = '/home/user/curiosimundo-animation/'; sys.path.insert(0, R + 'tools')
from largo import Project
P = Project(R + 'youtube/venus', 'Venus: el infierno de al lado', ['space.js'], open(R + 'tools/common_largo.js').read() + r'''
  const VSKY = 'radial-gradient(1600px 1000px at 50% 40%, #1a1430, #05030d 75%)';
  const vp = (id, x, y, r) => { const s = $(id).querySelector('svg'); const v = SP.venus(s, x, y, r); gm.onFrame($(id), (l, i) => v.flow(i.time)); return v; };
  const dusk = s => { const lg = mk('linearGradient', { id: 'dk' + Math.random().toString(36).slice(2), x1: 0, y1: 0, x2: 0, y2: 1 }, s); [['0', '#0b1030'], ['.55', '#3a2a5a'], ['.8', '#e07a4a'], ['1', '#f2b46a']].forEach(([o, c]) => mk('stop', { offset: o, 'stop-color': c }, lg));
    mk('rect', { width: 1920, height: 1080, fill: `url(#${lg.id})` }, s); SP.stars(s, 80, 1920, 500, 'dk'); mk('path', { d: 'M0 860 Q480 820 960 850 T1920 840 L1920 1080 L0 1080Z', fill: '#140c18' }, s);
    const v0 = mk('g', { transform: 'translate(1380 520)' }, s), v = mk('g', {}, v0); mk('circle', { r: 46, fill: '#fff6d8', opacity: .25 }, v); mk('circle', { r: 14, fill: '#fffbe8' }, v); return v; };
  const rain = (s, x0, x1, y0, y1, n = 60, seed = 'r') => { const D = Array.from({ length: n }, (_, i) => ({ el: mk('line', { stroke: '#d8e24a', 'stroke-width': 4, 'stroke-linecap': 'round' }, s), x: x0 + gm.random(seed + i) * (x1 - x0), p: gm.random(seed + 'p' + i) }));
    return t => D.forEach(d => { const k = (t * .7 + d.p) % 1, y = y0 + k * (y1 - y0); d.el.setAttribute('x1', d.x); d.el.setAttribute('x2', d.x - 6); d.el.setAttribute('y1', y); d.el.setAttribute('y2', y + 30); d.el.setAttribute('opacity', 1 - k); }); };
''')

P.page(0, 'Arranque en frío: 465 °C, casi del tamaño de la Tierra, plomo derretido, lluvia ácida, un día más largo que un año, dos horas, el gemelo malvado, ¿océanos?',
 [('s0', 0), ('s1', 'donde'), ('s2', 'nave'), ('s3', 'esta'), ('t', ('venus', 1))], r'''
  const z0 = svgOf('s0', VSKY); SP.stars(z0, 200); const e0 = SP.earth(z0, 560, 600, 210); gm.onFrame($('s0'), (l, i) => e0.rot(i.time)); vp('s0', 1360, 600, 200);
  SP.label(z0, 'TIERRA', 560, 880, 64); SP.label(z0, 'VENUS', 1360, 880, 64, '#FFD23F');
  const n0 = CM.text($('s0'), 'big', '<em>465 °C</em>', 90, 'font-size:240px;text-shadow:0 10px 60px #000'); tl.fromTo(n0, { scale: 1.2 }, { scale: 1, duration: .5, ease: 'expo.out' }, 0).to(n0, { opacity: 0, duration: .3 }, W('tamaño') - .4);
  big('s0', 'CASI DEL <em>MISMO TAMAÑO</em>', 120, W('tamaño') - .3, 'font-size:110px');
  const z1 = svgOf('s1'); SP.venusGround(z1); const rf = rain(z1, 0, 1920, -40, 600, 70); gm.onFrame($('s1'), (l, i) => rf(i.time));
  const lead = mk('g', { transform: 'translate(560 700)' }, z1); const bar = mk('rect', { x: -140, y: -90, width: 280, height: 90, rx: 8, fill: '#8f96a3' }, lead); const pool = mk('ellipse', { cx: 0, cy: 6, rx: 40, ry: 10, fill: '#a8b0bc' }, lead);
  tl.to(bar, { attr: { height: 20, y: -20 }, duration: 1.6 }, W('plomo') - .3).to(pool, { attr: { rx: 220, ry: 26 }, duration: 1.6 }, W('plomo') - .3);
  const lp = SP.label(z1, 'PLOMO', 560, 560, 70); tl.from(lp, { opacity: 0, duration: .2 }, W('plomo') - .3);
  big('s1', 'LLUEVE <em>ÁCIDO</em>', 150, W('ácido') - .3, 'font-size:120px', W('día') - .4); big('s1', '1 DÍA <em>&gt;</em> 1 AÑO', 150, W('día') - .2, 'font-size:150px');
  const z2 = svgOf('s2'); SP.venusGround(z2); const vl = SP.venera(z2, 960, 820, 1.3); const ck = SP.clock(z2, 1500, 300, 140, '#E5484D'); ck.t.textContent = '2 H';
  tl.from(vl.g, { y: -900, duration: 1, ease: 'power2.out' }, S.s2).from(ck.g, { opacity: 0, duration: .3 }, W('dos') - .3); shake(z2, S.s2 + 1, 12);
  const z3 = svgOf('s3', VSKY); SP.stars(z3, 200); const v3 = vp('s3', 960, 560, 330); push('s3', 1.25, 1);
  big('s3', 'EL GEMELO <em>MALVADO</em>', 110, W('gemelo') - .3, 'font-size:130px', W('final') - .3); const oc = mk('circle', { cx: 960, cy: 560, r: 330, fill: '#2f7fd0', opacity: 0 }, z3);
  tl.to(oc, { opacity: .6, duration: .8 }, W('océanos') - .5); big('s3', '¿<em>OCÉANOS</em>?', 110, W('océanos') - .3, 'font-size:140px');
  const t = $('t'); const zt = CM.svgIn(t, 'radial-gradient(1200px 800px at 50% 45%, #3a1a08, #050308 75%)'); SP.stars(zt, 200); const vt = SP.venus(zt, 960, 900, 520); gm.onFrame(t, (l, i) => vt.flow(i.time));
  const h = CM.text(t, 'big', '<em>VENUS</em>', 250, 'font-size:240px'); const a = CM.text(t, 'mid', 'el infierno de al lado', 500, 'font-size:56px;color:#FFD23F');
  tl.from(h, { scale: 1.3, opacity: 0, filter: 'blur(16px)', duration: .8, ease: 'expo.out' }, S.t + .1).to(h, { scale: 1.05, duration: D - S.t - 1, ease: 'sine.inOut' }, S.t + .9).from(a, { y: 30, opacity: 0, duration: .4 }, W('infierno') - .3);
''', off=0, mood='tension_up', last_mood='title', hits=['plomo', 'dos', ('venus', 1)])

P.page(1, 'El gemelo: tamaño y masa parecidos, el más cercano y brillante, lucero del alba y de la tarde, cubierto de nubes, la selva imaginada, 1962.',
 [('cmp', 0), ('sky', 'también'), ('cl', 'pero'), ('jg', 'principios'), ('hk', 'hasta')], r'''
  const zc = svgOf('cmp', VSKY); SP.stars(zc, 200); const e = SP.earth(zc, 560, 520, 240); gm.onFrame($('cmp'), (l, i) => e.rot(i.time)); vp('cmp', 1360, 520 + 0, 228);
  SP.label(zc, 'TIERRA · 12.742 KM', 560, 860, 64); SP.label(zc, 'VENUS · 12.104 KM', 1360, 860, 64, '#FFD23F');
  hd('CASI <em>GEMELOS</em>', 'mismo tamaño y una masa parecida', S.cmp + .3, S.sky); push('cmp', 1.1, 1);
  const zs = svgOf('sky'); const v = dusk(zs); tl.fromTo(v, { scale: .2, opacity: 0 }, { scale: 1, opacity: 1, duration: .8 }, S.sky + .3);
  hd('EL MÁS <em>BRILLANTE</em>', 'después de la Luna', S.sky + .3, W('lucero') - .3); hd('<em>LUCERO</em> DEL ALBA', 'y lucero de la tarde', W('lucero') - .2, W('siglos') - .3); hd('¿DOS <em>ESTRELLAS</em>?', 'durante siglos se pensó que sí', W('siglos') - .2, S.cl);
  const zl = svgOf('cl', '#05030d'); SP.stars(zl, 200); mk('circle', { cx: 960, cy: 540, r: 420, fill: 'none', stroke: '#2a2a3a', 'stroke-width': 60 }, zl); vp('cl', 960, 540, 300);
  hd('CUBIERTO DE <em>NUBES</em>', 'no se ve su superficie', S.cl + .3, S.jg);
  const zj = svgOf('jg', 'linear-gradient(#cfe0a0, #7aa060)'); for (let i = 0; i < 14; i++) { const x = gm.random('jx' + i) * 1920, h = 200 + gm.random('jh' + i) * 360, g = mk('g', { transform: `translate(${x} 1080)` }, zj);
    mk('rect', { x: -10, y: -h, width: 20, height: h, fill: '#5a4a2a' }, g); for (let k = 0; k < 6; k++) mk('path', { d: `M0 ${-h} q${(k - 2.5) * 50} -60 ${(k - 2.5) * 110} 20`, stroke: '#2f6a2a', 'stroke-width': 22, fill: 'none', 'stroke-linecap': 'round' }, g); }
  mk('ellipse', { cx: 960, cy: 1000, rx: 700, ry: 90, fill: '#4a7a6a', opacity: .8 }, zj); mk('rect', { width: 1920, height: 1080, fill: '#c9a46a', opacity: .3 }, zj);
  hd('LO QUE <em>IMAGINABAN</em>', 'pantanos y selvas bajo las nubes', S.jg + .3, S.hk); stamp('jg', '¿?', W('selvas') - .3, 400, '#FFD23F');
  const zh = svgOf('hk', VSKY); SP.stars(zh, 200); vp('hk', 1300, 560, 280); const pr = SP.probe(zh); gm.onFrame($('hk'), (l, i) => pr.setAttribute('transform', `translate(${200 + (i.time - S.hk) * 120} ${300 + (i.time - S.hk) * 30}) scale(.8)`));
  big('hk', '<em>1962</em>', 760, W('sesenta') - .3, 'font-size:180px');
''', card=(1, '12.104 KM', 'EL GEMELO'), hits=['hasta'])

P.page(2, 'El infierno: Mariner 2 (1962), 465 °C, plomo, más caliente que Mercurio, CO2 y efecto invernadero, presión ×90, nubes de ácido sulfúrico, lluvia que se evapora.',
 [('mar', 0), ('heat', 'hoy'), ('mer', ('venus', 2)), ('gh', 'por'), ('pr', 'además'), ('acid', 'sus'), ('hk', 'lugar')], r'''
  const zm = svgOf('mar', VSKY); SP.stars(zm, 200); vp('mar', 700, 560, 300); const pr = SP.probe(zm); gm.onFrame($('mar'), (l, i) => pr.setAttribute('transform', `translate(${1700 - (i.time - S.mar) * 70} ${260 + (i.time - S.mar) * 10}) scale(.9)`));
  hd('<em>MARINER 2</em> · 1962', 'la primera visita con éxito a otro planeta', S.mar + .3, W('calor') - .4); hd('UN CALOR <em>TREMENDO</em>', 'lo que midió en Venus', W('calor') - .3, S.heat);
  const zh = svgOf('heat'); SP.venusGround(zh); const th = SP.thermo(zh, 1500, 860, 620); const tA = S.heat + .3, tB = W('cinco') + .3;
  gm.onFrame($('heat'), (l, i) => { const k = gm.clamp((i.time - tA) / (tB - tA)); th.set(k); th.lab.textContent = Math.round(k * 465) + ' °C'; });
  const lead = mk('g', { transform: 'translate(560 780)' }, zh); const bar = mk('rect', { x: -160, y: -100, width: 320, height: 100, rx: 8, fill: '#8f96a3' }, lead); const pool = mk('ellipse', { cx: 0, cy: 6, rx: 40, ry: 10, fill: '#a8b0bc' }, lead);
  tl.to(bar, { attr: { height: 18, y: -18 }, duration: 2 }, W('plomo') - .3).to(pool, { attr: { rx: 260, ry: 26 }, duration: 2 }, W('plomo') - .3); SP.label(zh, 'PLOMO: SE FUNDE A 327 °C', 560, 600, 60);
  hd('<em>465 °C</em>', 'en la superficie', S.heat + .3, S.mer);
  const zr = svgOf('mer', VSKY); SP.stars(zr, 160); const sn = SP.sun(zr, 160, 540, 200); gm.onFrame($('mer'), (l, i) => sn.spin(i.time));
  SP.planet(zr, 760, 540, 40, '#9a948a'); SP.label(zr, 'MERCURIO', 760, 680, 56); SP.label(zr, 'HASTA ~430 °C DE DÍA', 760, 740, 40, '#9fb3c8'); const v2 = SP.venus(zr, 1440, 540, 110); gm.onFrame($('mer'), (l, i) => v2.flow(i.time));
  SP.label(zr, 'VENUS', 1440, 720, 56, '#FFD23F'); SP.label(zr, '465 °C DÍA Y NOCHE', 1440, 780, 40, '#FFD23F'); mk('path', { d: 'M800 820 L1400 820', stroke: '#9fb3c8', 'stroke-width': 4, 'stroke-dasharray': '12 10' }, zr); SP.label(zr, 'CASI EL DOBLE DE LEJOS', 1100, 870, 44, '#9fb3c8');
  hd('MÁS CALIENTE QUE <em>MERCURIO</em>', '¿cómo es posible?', S.mer + .3, S.gh);
  const zg = svgOf('gh'); SP.venusGround(zg); const atm = mk('rect', { width: 1920, height: 520, fill: '#e8b04a', opacity: .45 }, zg); SP.label(zg, 'CO2', 1700, 160, 120, '#fff');
  const rays = Array.from({ length: 6 }, (_, i) => mk('path', { d: `M${300 + i * 220} -20 L${380 + i * 220} 640`, stroke: '#fff6c0', 'stroke-width': 10, 'stroke-dasharray': '30 20' }, zg));
  const heat = Array.from({ length: 6 }, (_, i) => mk('path', { d: `M${400 + i * 220} 640 L${460 + i * 220} 520 L${520 + i * 220} 640`, stroke: '#E5484D', 'stroke-width': 10, fill: 'none' }, zg));
  gm.onFrame($('gh'), (l, i) => { rays.forEach(r => r.setAttribute('stroke-dashoffset', -i.time * 120)); heat.forEach((h, k) => h.setAttribute('transform', `translate(0 ${Math.sin(i.time * 3 + k) * 20})`)); });
  hd('ATMÓSFERA DE <em>CO2</em>', 'atrapa el calor como una manta', S.gh + .3, W('invernadero') - .3); hd('EFECTO <em>INVERNADERO</em>', 'llevado al extremo', W('invernadero') - .2, S.pr);
  const zp = svgOf('pr', 'linear-gradient(#0c4a8a, #020a1a)'); const sub = mk('g', {}, zp); mk('ellipse', { rx: 160, ry: 46, fill: '#f2c43a' }, sub); mk('rect', { x: -30, y: -86, width: 70, height: 50, rx: 10, fill: '#f2c43a' }, sub); mk('circle', { cx: 60, r: 14, fill: '#5bc0ff' }, sub);
  const dep = SP.label(zp, '0 M', 1600, 540, 120, '#fff'); gm.onFrame($('pr'), (l, i) => { const k = gm.clamp((i.time - S.pr - .3) / (W('kilómetro') - S.pr)); sub.setAttribute('transform', `translate(760 ${200 + k * 560})`); dep.textContent = Math.round(k * 900) + ' M'; });
  big('pr', '<em>×90</em> LA PRESIÓN', 120, W('noventa') - .3, 'font-size:140px'); hd('COMO A CASI <em>1 KM</em>', 'bajo el mar', W('kilómetro') - .3, S.acid);
  const za = svgOf('acid'); SP.venusGround(za); const cl = mk('g', {}, za); for (let i = 0; i < 16; i++) mk('ellipse', { cx: i * 130, cy: 90 + (i % 3) * 30, rx: 160, ry: 70, fill: i % 2 ? '#e8d24a' : '#d8c03a', opacity: .9 }, cl);
  const rf = rain(za, 0, 1920, 140, 520, 80, 'a'); gm.onFrame($('acid'), (l, i) => rf(i.time)); hd('NUBES DE <em>ÁCIDO SULFÚRICO</em>', 'no son de agua', S.acid + .3, W('evapora') - .3); hd('LLUEVE… PERO', 'se evapora antes de tocar el suelo', W('evapora') - .3, S.hk);
  const zk = svgOf('hk', 'linear-gradient(#d98a2a, #f2c46a)'); const vk = SP.venera(zk, 0, 0, 1); const chute = mk('path', { d: 'M-200 -560 Q0 -760 200 -560 L20 -320 M-200 -560 L-20 -320', fill: 'none', stroke: '#fff', 'stroke-width': 6 }, vk.g); mk('path', { d: 'M-200 -560 Q0 -760 200 -560Z', fill: '#E5484D' }, vk.g);
  gm.onFrame($('hk'), (l, i) => vk.w.setAttribute('transform', `translate(960 ${300 + (i.time - S.hk) * 90}) scale(.8)`)); big('hk', 'DECIDIERON <em>ATERRIZAR</em>', 120, W('aterrizar') - .4, 'font-size:120px');
''', card=(2, '465 °C', 'EL INFIERNO'), hits=['plomo', 'noventa', 'aterrizar'])

P.page(3, 'Las naves Venera: las primeras aplastadas, Venera 7 (1970), Venera 9 (1975) primera foto, Venera 13 (1982) fotos en color, 32 → 127 minutos, récord.',
 [('cr', 0), ('v7', ('mil', 1)), ('v9', ('mil', 2)), ('v13', ('mil', 3)), ('tm', 'estaba'), ('hk', ('pero', 2))], r'''
  const zc = svgOf('cr', 'linear-gradient(#d98a2a, #8a4f22)'); const cr = SP.venera(zc, 960, 700, 1.2); const tC = W('aplastadas') - .2;
  tl.from(cr.g, { y: -700, duration: 1.5, ease: 'none' }, S.cr + .2).to(cr.g, { scaleY: .35, scaleX: 1.25, duration: .25, transformOrigin: '0px 0px' }, tC); shake(zc, tC, 18);
  hd('UNIÓN SOVIÉTICA: <em>VENERA</em>', 'las primeras, aplastadas por la presión', S.cr + .3, W('rindieron') - .3); hd('NO SE <em>RINDIERON</em>', '', W('rindieron') - .2, S.v7);
  const z7 = svgOf('v7'); SP.venusGround(z7); const l7 = SP.venera(z7, 760, 820, 1); const ws = Array.from({ length: 4 }, () => mk('circle', { cx: 760, cy: 500, r: 10, fill: 'none', stroke: '#FFD23F', 'stroke-width': 6 }, z7));
  gm.onFrame($('v7'), (l, i) => ws.forEach((c, k) => { const q = ((i.time * .5 + k / 4) % 1); c.setAttribute('r', 20 + q * 500); c.setAttribute('opacity', 1 - q); })); hd('<em>1970</em> · VENERA 7', 'primeros datos desde la superficie de otro planeta', S.v7 + .3, S.v9);
  const z9 = svgOf('v9', '#111'); const ph = mk('g', {}, z9); mk('rect', { x: 160, y: 220, width: 1600, height: 560, fill: '#eee' }, ph); const gs = mk('g', { style: 'filter:grayscale(1) contrast(1.2)' }, ph);
  const inner = mk('svg', { x: 180, y: 240, width: 1560, height: 520, viewBox: '0 300 1920 640', preserveAspectRatio: 'xMidYMid slice' }, gs); SP.venusGround(inner, { sky: ['#3a3a3a', '#6a6a6a'] }); hd('<em>1975</em> · VENERA 9', 'la primera foto del suelo de Venus', S.v9 + .3, S.v13);
  tl.from(ph, { scale: .6, opacity: 0, duration: .6, ease: 'expo.out', transformOrigin: '960px 500px' }, S.v9 + .2);
  const z13 = svgOf('v13', '#111'); const p13 = mk('g', {}, z13); mk('rect', { x: 160, y: 220, width: 1600, height: 560, fill: '#eee' }, p13); const in13 = mk('svg', { x: 180, y: 240, width: 1560, height: 520, viewBox: '0 300 1920 640', preserveAspectRatio: 'xMidYMid slice' }, p13); SP.venusGround(in13);
  SP.venera(in13, 300, 1000, .9); tl.from(p13, { scale: .6, opacity: 0, duration: .6, ease: 'expo.out', transformOrigin: '960px 500px' }, S.v13 + .2); hd('<em>1982</em> · VENERA 13', 'fotos en color: rocas y polvo anaranjado', S.v13 + .3, S.tm);
  const zt = svgOf('tm'); SP.venusGround(zt); SP.venera(zt, 600, 860, 1.1); mk('rect', { x: 1000, y: 380, width: 760, height: 50, rx: 25, fill: 'rgb(6 12 28 / .7)' }, zt); const bar = mk('rect', { x: 1000, y: 380, width: 0, height: 50, rx: 25, fill: '#FFD23F' }, zt);
  const m32 = 1000 + 760 * 32 / 127; mk('line', { x1: m32, x2: m32, y1: 350, y2: 460, stroke: '#fff', 'stroke-width': 6 }, zt); SP.label(zt, 'DISEÑO: 32 MIN', m32, 330, 54);
  const ck = SP.label(zt, '0 MIN', 1380, 600, 160, '#FFD23F'); const t0 = W('resistir') - .2, t1 = W('veintisiete') + .4;
  gm.onFrame($('tm'), (l, i) => { const k = gm.clamp((i.time - t0) / (t1 - t0)); bar.setAttribute('width', 760 * k); ck.textContent = Math.round(k * 127) + ' MIN'; });
  stamp('tm', 'RÉCORD', W('récord') - .3, 720, '#FFD23F');
  const zk = svgOf('hk', VSKY); SP.stars(zk, 200); vp('hk', 960, 560, 300); const cl = SP.clock(zk, 960, 600, 180); cl.t.textContent = '?:??';
  tl.from(cl.g, { scale: 0, opacity: 0, duration: .4, ease: 'back.out(2)', transformOrigin: '960px 520px' }, W('reloj') - .4);
''', card=(3, '127 MIN', 'LAS NAVES VENERA'), hits=['aplastadas', 'récord', 'reloj'])

P.page(4, 'El día más largo: gira en 243 días, año de 225, gira al revés (el Sol sale por el oeste), día solar de 117 días, nubes que dan la vuelta en 4 días a 360 km/h.',
 [('rot', 0), ('orb', ('y', 1)), ('rev', 'además'), ('sol', 'ojo'), ('wind', 'mientras'), ('hk', ('un', 3))], r'''
  const zr = svgOf('rot', VSKY); SP.stars(zr, 200); const vr = vp('rot', 960, 560, 300); const mark = mk('circle', { r: 18, fill: '#E5484D', stroke: '#fff', 'stroke-width': 4 }, zr);
  gm.onFrame($('rot'), (l, i) => { const a = (i.time - S.rot) * .25; mark.setAttribute('cx', 960 + Math.sin(a) * 300); mark.setAttribute('cy', 520); mark.setAttribute('opacity', Math.cos(a) > 0 ? 1 : 0); });
  const c1 = SP.label(zr, '243 DÍAS', 960, 980, 140, '#FFD23F'); tl.from(c1, { opacity: 0, scale: 1.4, duration: .4, transformOrigin: '960px 940px' }, W('cuarenta') - .4); hd('UNA VUELTA SOBRE SÍ MISMO', 'muy, muy despacio', S.rot + .3, S.orb);
  const zo = svgOf('orb', VSKY); SP.stars(zo, 200); const so = SP.sun(zo, 960, 540, 110); mk('circle', { cx: 960, cy: 540, r: 360, fill: 'none', stroke: '#e8c27a', 'stroke-width': 3, 'stroke-dasharray': '10 12' }, zo); const vo = SP.venus(zo, 0, 0, 50);
  gm.onFrame($('orb'), (l, i) => { so.spin(i.time); const a = (i.time - S.orb) * .8; vo.w.setAttribute('transform', `translate(${960 + Math.cos(a) * 360} ${540 + Math.sin(a) * 360})`); vo.flow(i.time); });
  hd('UNA VUELTA AL SOL', '225 días', S.orb + .3, W('decir') - .3); big('orb', '<em>243</em> &gt; 225', 80, W('decir') - .3, 'font-size:180px'); mid('orb', 'su giro dura <b>más que su año</b>', 640, W('giro') - .3);
  const zv = svgOf('rev', 'linear-gradient(#d98a2a, #f2c46a)'); SP.venusGround(zv); const sr = SP.sun(zv, 0, 0, 90); const tR = W('oeste') - 1;
  gm.onFrame($('rev'), (l, i) => { const k = gm.clamp((i.time - tR) / 4); sr.w.setAttribute('transform', `translate(${260 + k * 300} ${700 - k * 400})`); sr.spin(i.time); });
  SP.label(zv, 'OESTE', 220, 760, 90, '#fff'); SP.label(zv, 'ESTE', 1700, 760, 90, '#fff'); hd('GIRA <em>AL REVÉS</em>', 'el Sol sale por el oeste y se pone por el este', S.rev + .3, S.sol);
  const zs = svgOf('sol', VSKY); SP.stars(zs, 160); const dial = mk('g', { transform: 'translate(800 520)' }, zs); mk('circle', { r: 280, fill: '#1d2a4a' }, dial); mk('path', { d: 'M0 -280 A280 280 0 0 1 0 280Z', fill: '#f2c46a' }, dial);
  const hand = mk('line', { x1: 0, y1: 0, x2: 0, y2: -250, stroke: '#E5484D', 'stroke-width': 12, 'stroke-linecap': 'round' }, dial); gm.onFrame($('sol'), (l, i) => hand.setAttribute('transform', `rotate(${(i.time - S.sol) * 40})`));
  const d117 = SP.label(zs, '<tspan fill="#FFD23F">117</tspan> DÍAS', 1560, 600, 150); tl.from(d117, { opacity: 0, x: 40, duration: .4 }, W('ciento') - .3); hd('DE AMANECER A <em>AMANECER</em>', 'su día solar', S.sol + .3, S.wind);
  const zw = svgOf('wind', VSKY); SP.stars(zw, 200); const vw = SP.venus(zw, 960, 560, 320); gm.onFrame($('wind'), (l, i) => vw.flow(i.time * 6));
  const arrows = Array.from({ length: 5 }, (_, k) => mk('path', { d: `M-120 0 L120 0 M90 -26 L124 0 L90 26`, stroke: '#fff', 'stroke-width': 10, fill: 'none', opacity: .8 }, zw));
  gm.onFrame($('wind'), (l, i) => arrows.forEach((a, k) => { const q = ((i.time * .6 + k / 5) % 1); a.setAttribute('transform', `translate(${560 + q * 800} ${360 + k * 90})`); a.setAttribute('opacity', Math.sin(q * Math.PI)); }));
  hd('LAS NUBES <em>VUELAN</em>', 'dan la vuelta a Venus en unos 4 días', S.wind + .3, W('vientos') - .3); hd('<em>360 KM/H</em>', 'vientos en las nubes altas', W('vientos') - .2, S.hk);
  const zk = svgOf('hk', VSKY); SP.stars(zk, 200); vp('hk', 960, 620, 300); big('hk', 'LENTO · <em>ARDIENTE</em> · AL REVÉS', 120, S.hk + .3, 'font-size:110px', W('siempre') - .3); big('hk', '¿SIEMPRE FUE <em>ASÍ</em>?', 120, W('siempre') - .2, 'font-size:140px');
''', card=(4, '243 &gt; 225', 'EL DÍA MÁS LARGO'), hits=['decir', ('un', 3)])

P.page(5, '¿Un pasado con océanos?: modelos de la NASA, el efecto invernadero desbocado, estudios que lo dudan, misiones en los años treinta, lucero al atardecer, pregunta final.',
 [('past', 0), ('run', 'idea'), ('doubt', 'otros'), ('mis', 'para'), ('dusk', 'mientras'), ('end', 'tú')], r'''
  const zp = svgOf('past', VSKY); SP.stars(zp, 200); const vp1 = SP.venus(zp, 960, 560, 320); gm.onFrame($('past'), (l, i) => vp1.flow(i.time)); const sea = mk('circle', { cx: 960, cy: 560, r: 322, fill: '#2f7fd0', opacity: 0 }, zp);
  tl.to(sea, { opacity: .7, duration: 1.5 }, W('océanos') - .8); hd('MODELOS DE LA <em>NASA</em>', 'hace miles de millones de años', S.past + .3, W('clima') - .3); hd('¿CLIMA <em>TEMPLADO</em>?', 'quizá océanos poco profundos', W('clima') - .2, S.run);
  const zr = svgOf('run', 'linear-gradient(#5a6a8a, #c9a46a)'); const water = mk('rect', { x: 0, y: 640, width: 1920, height: 440, fill: '#2f7fd0' }, zr); const steam = Array.from({ length: 14 }, (_, i) => mk('circle', { cx: 80 + i * 135, cy: 640, r: 40, fill: '#fff', opacity: .5 }, zr));
  const tint = mk('rect', { width: 1920, height: 1080, fill: '#e8a040', opacity: 0 }, zr); const th = SP.thermo(zr, 1700, 820, 520);
  gm.onFrame($('run'), (l, i) => { const k = gm.clamp((i.time - S.run) / (S.doubt - S.run)); water.setAttribute('y', 640 + k * 440); tint.setAttribute('opacity', k * .55); th.set(.2 + k * .8);
    steam.forEach((c, j) => { const q = ((i.time * .4 + gm.random('stp' + j)) % 1); c.setAttribute('cx', 80 + gm.random('stx' + j) * 1760); c.setAttribute('cy', 640 + k * 440 - q * 500); c.setAttribute('opacity', .5 * (1 - q) * (1 - k * .6)); }); });
  hd('EL AGUA <em>SE EVAPORA</em>', 'y el vapor atrapa más calor', S.run + .3, W('desbocado') - .3); hd('INVERNADERO <em>DESBOCADO</em>', 'del que nunca salió', W('desbocado') - .2, S.doubt);
  const zd = svgOf('doubt', VSKY); SP.stars(zd, 160); const a = SP.venus(zd, 560, 560, 240); const b = SP.venus(zd, 1360, 560, 240); gm.onFrame($('doubt'), (l, i) => { a.flow(i.time); b.flow(i.time); });
  mk('circle', { cx: 560, cy: 560, r: 242, fill: '#2f7fd0', opacity: .55 }, zd); SP.label(zd, '¿CON OCÉANOS?', 560, 900, 70, '#5bc0ff'); SP.label(zd, '¿SIEMPRE SECO?', 1360, 900, 70, '#FFD23F');
  hd('OTROS ESTUDIOS <em>LO DUDAN</em>', 'todavía no se sabe quién tiene razón', S.doubt + .3, S.mis);
  const zm = svgOf('mis', VSKY); SP.stars(zm, 200); vp('mis', 1500, 560, 260); const ps = [0, 1, 2].map(k => SP.probe(zm));
  gm.onFrame($('mis'), (l, i) => ps.forEach((p, k) => p.setAttribute('transform', `translate(${100 + (i.time - S.mis) * (110 + k * 20) - k * 120} ${300 + k * 200}) scale(.55)`)));
  hd('NUEVAS <em>MISIONES</em>', 'NASA y Agencia Espacial Europea · años treinta', S.mis + .3, S.dusk);
  const zk = svgOf('dusk'); const v = dusk(zk); tl.fromTo(v, { scale: .3 }, { scale: 1.2, duration: S.end - S.dusk, ease: 'none' }, S.dusk); big('dusk', 'TAN BONITO <em>DE LEJOS</em>…', 200, W('bonito') - .3, 'font-size:120px', W('infernal') - .3); big('dusk', '…Y TAN <em>INFERNAL</em> DE CERCA', 200, W('infernal') - .3, 'font-size:120px');
  ender('end', '¿A DÓNDE VIAJARÍAS: <span style="color:#FFD23F">VENUS</span> O <span style="color:#E5484D">MARTE</span>?', S.end + .1);
''', card=(5, '¿OCÉANOS?', 'UN PASADO CON OCÉANOS'), mood='tension', last_mood='end', hits=['desbocado'])
