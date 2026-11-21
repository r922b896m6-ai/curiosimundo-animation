/* CURIOSIMUNDO · espacio: Sol, Tierra, Luna, Venus, paisajes, reloj, termómetro, fondo marino, sondas (espacio 1920×1080) */
(function () {
const mk = CM.mk, SP = window.SP = {}; let UID = 0;
SP.defs = function () {
  CM.defs(); if (document.getElementById('spDefs')) return;
  const d = mk('defs', { id: 'spDefs' }, document.getElementById('cmDefsRoot'));
  d.innerHTML = `<radialGradient id="spSun"><stop offset="0" stop-color="#fffbe6"/><stop offset=".55" stop-color="#ffd84a"/><stop offset="1" stop-color="#ff9a1a"/></radialGradient>
  <radialGradient id="spGlow"><stop offset="0" stop-color="#ffcf4a" stop-opacity=".7"/><stop offset=".45" stop-color="#ff9a1a" stop-opacity=".22"/><stop offset="1" stop-color="#ff7a00" stop-opacity="0"/></radialGradient>
  <radialGradient id="spRed"><stop offset="0" stop-color="#ffd0a0"/><stop offset=".6" stop-color="#ff6a3a"/><stop offset="1" stop-color="#b3261e"/></radialGradient>
  <radialGradient id="spRedGlow"><stop offset="0" stop-color="#ff6a3a" stop-opacity=".5"/><stop offset="1" stop-color="#b3261e" stop-opacity="0"/></radialGradient>
  <radialGradient id="spOcean" cx=".4" cy=".35"><stop offset="0" stop-color="#3f9be8"/><stop offset="1" stop-color="#0c3f8a"/></radialGradient>
  <radialGradient id="spShade" cx=".25" cy=".3" r=".9"><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient>
  <radialGradient id="spMoon" cx=".4" cy=".35"><stop offset="0" stop-color="#e8e6e0"/><stop offset="1" stop-color="#8f8c86"/></radialGradient>
  <radialGradient id="spVenus" cx=".4" cy=".35"><stop offset="0" stop-color="#fff0c2"/><stop offset=".6" stop-color="#e8c27a"/><stop offset="1" stop-color="#a8783a"/></radialGradient>
  <radialGradient id="spVent"><stop offset="0" stop-color="#ffb060" stop-opacity=".6"/><stop offset="1" stop-color="#ff7a20" stop-opacity="0"/></radialGradient>
  <linearGradient id="spMercury" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#E5484D"/><stop offset="1" stop-color="#ff8a6a"/></linearGradient>
  <clipPath id="spEarthClip"><circle r="1"/></clipPath>`;
};
SP.stars = (s, n = 160, w = 1920, h = 1080, seed = 's') => { const g = mk('g', {}, s); for (let i = 0; i < n; i++) mk('circle', { cx: gm.random(seed + 'x' + i) * w, cy: gm.random(seed + 'y' + i) * h, r: .8 + gm.random(seed + 'r' + i) * 2.4, fill: '#fff', opacity: .25 + gm.random(seed + 'o' + i) * .7 }, g); return g; };
SP.NIGHT = 'radial-gradient(1600px 1000px at 50% 40%, #0f1a3a, #03050d 75%)';
/* Sun with glow and flickering rays; returns {g, core, glow, rays} */
SP.sun = function (s, x, y, r = 160) { SP.defs(); const w = mk('g', { transform: `translate(${x} ${y})` }, s), g = mk('g', {}, w);
  const glow = mk('circle', { r: r * 2.6, fill: 'url(#spGlow)' }, g); const rays = mk('g', {}, g);
  for (let i = 0; i < 16; i++) mk('path', { d: `M${-r * .09} ${-r * 1.02} L0 ${-r * 1.38} L${r * .09} ${-r * 1.02}Z`, fill: '#ffcf4a', opacity: .55, transform: `rotate(${i * 22.5})` }, rays);
  const core = mk('circle', { r, fill: 'url(#spSun)' }, g);
  for (let i = 0; i < 5; i++) mk('circle', { cx: (gm.random('sp' + i) - .5) * r, cy: (gm.random('sq' + i) - .5) * r, r: r * (.06 + gm.random('sr' + i) * .08), fill: '#ffb020', opacity: .35 }, g);
  return { w, g, core, glow, rays, spin: t => rays.setAttribute('transform', `rotate(${t * 6}) scale(${1 + Math.sin(t * 3) * .04})`) };
};
/* Earth: ocean, continents, clouds, atmosphere, terminator shade */
SP.earth = function (s, x, y, r = 200, { shade = true } = {}) { SP.defs(); const w = mk('g', { transform: `translate(${x} ${y}) scale(${r / 100})` }, s), g = mk('g', {}, w);
  mk('circle', { r: 108, fill: '#5bc0ff', opacity: .18 }, g); mk('circle', { r: 100, fill: 'url(#spOcean)' }, g);
  const cl = mk('clipPath', { id: 'spE' + (++UID) }, g); mk('circle', { r: 100 }, cl);
  const land = mk('g', { 'clip-path': `url(#${cl.id})` }, g), spin = mk('g', {}, land);
  const L = ['M-70 -50 Q-40 -80 -10 -60 Q0 -30 -30 -10 Q-50 10 -60 -10 Q-90 -20 -70 -50Z', 'M-20 10 Q10 0 20 30 Q10 70 -10 80 Q-30 50 -20 10Z', 'M30 -70 Q70 -80 90 -40 Q70 -20 50 -30 Q30 -40 30 -70Z', 'M40 10 Q80 0 90 30 Q70 50 50 40Z', 'M-40 -90 Q0 -100 30 -92 Q0 -84 -40 -90Z'];
  for (const k of [0, 200, -200]) L.forEach(d => mk('path', { d, fill: '#3f9a4a', transform: `translate(${k} 0)` }, spin));
  const clouds = mk('g', { opacity: .7 }, land); [[-50, -20, 30], [20, -50, 24], [40, 50, 28], [-30, 60, 20]].forEach(([cx, cy, rr]) => mk('ellipse', { cx, cy, rx: rr, ry: rr * .3, fill: '#fff' }, clouds));
  const sh = mk('circle', { r: 100, fill: 'url(#spShade)', opacity: shade ? 1 : 0 }, g);
  return { w, g, spin, sh, rot: t => spin.setAttribute('transform', `translate(${((t * 12) % 200) - 0} 0)`) };
};
SP.moon = function (s, x, y, r = 60) { SP.defs(); const g = mk('g', { transform: `translate(${x} ${y})` }, s);
  mk('circle', { r, fill: 'url(#spMoon)' }, g); [[-.3, -.2, .18], [.25, .1, .14], [-.05, .4, .1], [.35, -.35, .08]].forEach(([a, b, c]) => mk('circle', { cx: a * r, cy: b * r, r: c * r, fill: '#7d7a74', opacity: .5 }, g)); return g; };
SP.planet = function (s, x, y, r, fill, ring = false) { const g = mk('g', { transform: `translate(${x} ${y})` }, s); mk('circle', { r, fill }, g);
  if (ring) mk('ellipse', { rx: r * 1.9, ry: r * .45, fill: 'none', stroke: '#d8c48a', 'stroke-width': r * .18, opacity: .8 }, g); mk('circle', { r, fill: 'url(#spShade)' }, g); return g; };
/* Venus seen from space: cloudy bands */
SP.venus = function (s, x, y, r = 220) { SP.defs(); const w = mk('g', { transform: `translate(${x} ${y})` }, s), g = mk('g', {}, w);
  mk('circle', { r: r * 1.12, fill: '#ffe3a0', opacity: .12 }, g); mk('circle', { r, fill: 'url(#spVenus)' }, g);
  const cl = mk('clipPath', { id: 'spV' + (++UID) }, g); mk('circle', { r }, cl); const bands = mk('g', { 'clip-path': `url(#${cl.id})` }, g), mv = mk('g', {}, bands);
  for (let k = -1; k <= 1; k++) for (let i = 0; i < 7; i++) mk('path', { d: `M${-r * 1.2 + k * r * 2.4} ${-r + i * r * .3} q${r * .6} ${-r * .12} ${r * 1.2} 0 t${r * 1.2} 0`, stroke: i % 2 ? '#f6dca0' : '#c99a52', 'stroke-width': r * .1, fill: 'none', opacity: .55 }, mv);
  mk('circle', { r, fill: 'url(#spShade)' }, g);
  return { w, g, mv, flow: t => mv.setAttribute('transform', `translate(${-((t * r * .25) % (r * 2.4))} 0)`) };
};
/* day landscape (sky can fade to night): returns {sky, night, ground} */
SP.landscape = function (s, { sunX = 1500, sunY = 230 } = {}) { SP.defs();
  const sky = mk('rect', { width: 1920, height: 1080, fill: '#7cc0f0' }, s); const sk2 = mk('rect', { width: 1920, height: 760, fill: '#bfe3fa', opacity: .5 }, s);
  const night = mk('g', { opacity: 0 }, s); mk('rect', { width: 1920, height: 1080, fill: '#03050d' }, night); SP.stars(night, 220, 1920, 760, 'ln');
  const sun = SP.sun(s, sunX, sunY, 80);
  const ground = mk('g', {}, s); mk('path', { d: 'M0 760 Q480 700 960 750 T1920 740 L1920 1080 L0 1080Z', fill: '#4f9a3a' }, ground); mk('path', { d: 'M0 840 Q600 800 1200 850 T1920 830 L1920 1080 L0 1080Z', fill: '#3d7f2e' }, ground);
  const tree = (x, y, sc) => { const t = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, ground); mk('rect', { x: -12, y: -120, width: 24, height: 120, fill: '#6b4a2a' }, t); mk('circle', { cy: -160, r: 70, fill: '#2f7a2a' }, t); mk('circle', { cx: -50, cy: -120, r: 50, fill: '#36882f' }, t); mk('circle', { cx: 50, cy: -126, r: 52, fill: '#36882f' }, t); return t; };
  tree(260, 800, 1.2); tree(1650, 790, 1); tree(1820, 820, .8);
  const house = mk('g', { transform: 'translate(760 800)' }, ground); mk('rect', { x: -120, y: -150, width: 240, height: 150, fill: '#f0e2c8' }, house); mk('path', { d: 'M-150 -150 L0 -260 L150 -150Z', fill: '#c0392b' }, house);
  mk('rect', { x: -30, y: -90, width: 60, height: 90, fill: '#6b4a2a' }, house); const win = mk('rect', { x: 60, y: -120, width: 44, height: 44, fill: '#9fd0f0' }, house);
  const dark = mk('rect', { width: 1920, height: 1080, fill: '#02040a', opacity: 0 }, s);
  return { sky, night, sun, ground, dark, win };
};
/* digital clock / countdown text in svg */
SP.clock = function (s, x, y, size = 200, col = '#FFD23F') { const g = mk('g', {}, s);
  mk('rect', { x: x - size * 1.6, y: y - size * .85, width: size * 3.2, height: size * 1.1, rx: 24, fill: 'rgb(6 12 28 / .85)', stroke: col, 'stroke-width': 6 }, g);
  const t = mk('text', { x, y, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': size, fill: col }, g); t.textContent = '8:20';
  return { g, t, set: sec => { sec = Math.max(0, sec); const m = Math.floor(sec / 60), ss = Math.floor(sec % 60); t.textContent = `${m}:${String(ss).padStart(2, '0')}`; } };
};
/* thermometer; set(k 0..1) and label */
SP.thermo = function (s, x, y, h = 600) { SP.defs(); const g = mk('g', {}, s);
  mk('rect', { x: x - 34, y: y - h, width: 68, height: h, rx: 34, fill: '#e8eef4', stroke: '#9fb3c8', 'stroke-width': 6 }, g); mk('circle', { cx: x, cy: y + 30, r: 66, fill: '#e8eef4', stroke: '#9fb3c8', 'stroke-width': 6 }, g);
  const bulb = mk('circle', { cx: x, cy: y + 30, r: 50, fill: '#E5484D' }, g); const col = mk('rect', { x: x - 18, y: y - h * .8, width: 36, height: h * .8 + 20, rx: 18, fill: '#E5484D' }, g);
  for (let i = 0; i <= 10; i++) mk('line', { x1: x + 40, x2: x + 62, y1: y - 40 - i * (h - 80) / 10, y2: y - 40 - i * (h - 80) / 10, stroke: '#9fb3c8', 'stroke-width': 4 }, g);
  const lab = mk('text', { x: x + 90, y: y - h / 2, 'font-family': 'Bebas Neue', 'font-size': 120, fill: '#fff' }, g);
  return { g, lab, set: (k, color) => { const hh = 20 + k * (h - 40); col.setAttribute('y', y - hh); col.setAttribute('height', hh + 20); if (color) { col.setAttribute('fill', color); bulb.setAttribute('fill', color); } } };
};
/* ocean cross-section with ice on top and a hydrothermal vent with life; returns {ice, vent, smoke[], worms[]} */
SP.ocean = function (s) { SP.defs();
  mk('rect', { width: 1920, height: 1080, fill: '#04142e' }, s); mk('rect', { width: 1920, height: 500, fill: '#0b2f5e', opacity: .6 }, s);
  const ice = mk('g', {}, s); mk('path', { d: 'M0 0 L1920 0 L1920 150 Q1700 175 1500 150 T1100 160 T700 148 T300 165 T0 150Z', fill: '#d9f0ff' }, ice); mk('path', { d: 'M0 150 Q300 170 700 150 T1500 155 L1920 150 L1920 170 Q1500 180 1100 172 T300 178 L0 168Z', fill: '#9fd3f5', opacity: .8 }, ice);
  mk('path', { d: 'M0 940 Q300 900 600 930 T1200 920 T1920 940 L1920 1080 L0 1080Z', fill: '#2a2620' }, s);
  const vent = mk('g', { transform: 'translate(1100 940)' }, s); mk('circle', { cy: -260, r: 220, fill: 'url(#spVent)' }, vent);
  mk('path', { d: 'M-90 0 L-50 -200 L-20 -230 L30 -230 L50 -200 L90 0Z', fill: '#3a332a', stroke: '#1e1a14', 'stroke-width': 5 }, vent); mk('path', { d: 'M-50 -120 L50 -120 M-60 -60 L60 -60', stroke: '#4a4234', 'stroke-width': 8 }, vent);
  const smoke = Array.from({ length: 10 }, (_, i) => mk('circle', { cx: 0, cy: -240, r: 30, fill: '#2a2a30', opacity: .6 }, vent));
  const worms = Array.from({ length: 9 }, (_, i) => { const wx = -260 + i * 60 + (i > 4 ? 280 : 0), w = mk('g', { transform: `translate(${wx} 0)` }, vent); const hh = 90 + gm.random('wh' + i) * 70;
    mk('rect', { x: -6, y: -hh, width: 12, height: hh, rx: 6, fill: '#f0eee6' }, w); const tip = mk('ellipse', { cx: 0, cy: -hh - 10, rx: 14, ry: 22, fill: '#e5484d' }, w); return { w, tip, hh }; });
  const crab = mk('g', { transform: 'translate(840 930)' }, s); mk('ellipse', { rx: 40, ry: 24, fill: '#f0e6d6' }, crab); [-1, 1].forEach(k => { mk('path', { d: `M${k * 30} -6 q${k * 30} -30 ${k * 46} -10`, stroke: '#f0e6d6', 'stroke-width': 8, fill: 'none' }, crab); for (let j = 0; j < 3; j++) mk('path', { d: `M${k * 20} 10 l${k * 26} ${16 + j * 4}`, stroke: '#f0e6d6', 'stroke-width': 5 }, crab); });
  const microbes = Array.from({ length: 40 }, (_, i) => mk('circle', { cx: 900 + (gm.random('mx' + i) - .5) * 700, cy: 620 + (gm.random('my' + i) - .5) * 500, r: 3 + gm.random('mr' + i) * 4, fill: '#7cf0c0', opacity: .7 }, s));
  return { ice, vent, smoke, worms, crab, microbes, anim: t => { smoke.forEach((c, i) => { const k = ((t * .3 + i / smoke.length) % 1); c.setAttribute('cy', -240 - k * 600); c.setAttribute('cx', Math.sin(k * 6 + i) * 40 * k); c.setAttribute('r', 30 + k * 90); c.setAttribute('opacity', .6 * (1 - k)); });
    worms.forEach((w, i) => w.tip.setAttribute('transform', `rotate(${Math.sin(t * 2 + i) * 12} 0 ${-w.hh})`)); microbes.forEach((m, i) => m.setAttribute('transform', `translate(${Math.sin(t + i) * 10} ${Math.cos(t * .8 + i) * 10})`)); } };
};
/* Venus surface: orange rocks under yellow-orange sky; optional lander */
SP.venusGround = function (s, { sky = ['#d98a2a', '#f2c46a'] } = {}) {
  const lg = mk('linearGradient', { id: 'spVsky' + (++UID), x1: 0, y1: 0, x2: 0, y2: 1 }, s); mk('stop', { offset: 0, 'stop-color': sky[0] }, lg); mk('stop', { offset: 1, 'stop-color': sky[1] }, lg);
  mk('rect', { width: 1920, height: 1080, fill: `url(#${lg.id})` }, s); mk('path', { d: 'M0 640 Q500 600 900 630 T1920 620 L1920 1080 L0 1080Z', fill: '#a8642a' }, s);
  for (let i = 0; i < 22; i++) { const x = gm.random('vr' + i) * 1920, y = 680 + gm.random('vy' + i) * 380, w = 60 + gm.random('vw' + i) * 160; mk('path', { d: `M${x - w} ${y} L${x - w * .7} ${y - w * .22} L${x + w * .6} ${y - w * .25} L${x + w} ${y}Z`, fill: i % 2 ? '#8a4f22' : '#b87436', stroke: '#6a3a18', 'stroke-width': 3 }, s); }
  const haze = mk('rect', { width: 1920, height: 1080, fill: '#ff9a3a', opacity: .12 }, s); return { haze };
};
SP.venera = function (s, x, y, sc = 1) { const w = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s), g = mk('g', {}, w);
  mk('path', { d: 'M-150 0 L150 0 L120 -40 L-120 -40Z', fill: '#8a8f96', stroke: '#4a4f56', 'stroke-width': 5 }, g); mk('circle', { cy: -120, r: 95, fill: '#c9ced6', stroke: '#6a6f76', 'stroke-width': 5 }, g);
  mk('rect', { x: -110, y: -140, width: 220, height: 26, fill: '#6a6f76' }, g); mk('path', { d: 'M-20 -215 L-20 -290 L20 -290 L20 -215', fill: '#9aa0a8' }, g); mk('ellipse', { cy: -300, rx: 60, ry: 16, fill: '#b0b6be' }, g);
  mk('rect', { x: -40, y: -100, width: 80, height: 30, rx: 6, fill: '#2a2f38' }, g); mk('circle', { cx: 0, cy: -85, r: 10, fill: '#5bc0ff' }, g); return { w, g };
};
SP.probe = function (s) { const g = mk('g', {}, s); mk('path', { d: 'M-40 -40 L40 -40 L50 0 L40 40 L-40 40 L-50 0Z', fill: '#c9cdd4', stroke: '#6a6f76', 'stroke-width': 4 }, g);
  [-1, 1].forEach(k => { mk('rect', { x: k > 0 ? 60 : -260, y: -30, width: 200, height: 60, fill: '#2f4f9a', stroke: '#9fb3c8', 'stroke-width': 3 }, g); for (let i = 1; i < 5; i++) mk('line', { x1: (k > 0 ? 60 : -260) + i * 40, x2: (k > 0 ? 60 : -260) + i * 40, y1: -30, y2: 30, stroke: '#9fb3c8', 'stroke-width': 2 }, g); });
  mk('path', { d: 'M0 -40 L0 -110 M-40 -130 Q0 -90 40 -130', stroke: '#e8eef4', 'stroke-width': 6, fill: 'none' }, g); return g; };
/* label in svg */
SP.label = function (s, txt, x, y, size = 64, fill = '#fff', anchor = 'middle') { const t = mk('text', { x, y, 'text-anchor': anchor, 'font-family': 'Bebas Neue', 'font-size': size, fill, stroke: 'rgb(0 0 0 / .55)', 'stroke-width': size / 10, 'paint-order': 'stroke', 'letter-spacing': '1' }, s); t.innerHTML = txt; return t; };
})();
