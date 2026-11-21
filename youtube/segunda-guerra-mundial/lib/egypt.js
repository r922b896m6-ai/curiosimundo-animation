/* CURIOSIMUNDO · Cleopatra: personajes (Egipto ptolemaico y Roma), escenarios, barcos de guerra (espacio 1920×1080).
   Estilo plano, sin sangre: las batallas se muestran con formaciones, retiradas y rendiciones. */
(function () {
const mk = CM.mk, EG = window.EG = {}; let UID = 0;
const SK = { cleo: '#c98f62', ptol: '#c98f62', caesar: '#e0b08a', antony: '#d9a27a', octav: '#e8bf98', leg: '#d9a77c', egs: '#a8714a', apo: '#c98f62', sen: '#e0b08a', cit: '#c98f62' };
/* person: feet at (0,0), ~200 px tall, facing right. returns {o, b, legL, legR, arm, kind} */
EG.person = function (parent, kind, { hold } = {}) {
  const o = mk('g', {}, parent), b = mk('g', {}, o), sk = SK[kind] || '#c98f62';
  const legs = [-8, 8].map(x => { const l = mk('g', { transform: `translate(${x} -86)` }, b); mk('rect', { x: -6, y: 0, width: 12, height: 80, rx: 5, fill: sk }, l);
    mk('path', { d: 'M-7 78 h18 l4 8 h-22z', fill: kind === 'leg' ? '#6b4a2a' : '#8a6a3a' }, l); return l; });
  const robe = { cleo: '#f4efe2', caesar: '#f2ede0', octav: '#f2ede0', sen: '#f2ede0', antony: '#b3262d', leg: '#b3262d', egs: '#f4efe2', ptol: '#f4efe2', apo: '#d8c8a8', cit: '#e6d8b8' }[kind] || '#e6d8b8';
  if (kind === 'cleo') { mk('path', { d: 'M-20 -152 Q0 -160 22 -152 L34 -6 L-30 -6Z', fill: robe }, b); mk('path', { d: 'M-26 -60 L30 -60', stroke: '#d8b23a', 'stroke-width': 5 }, b); }
  else if (['caesar', 'octav', 'sen'].includes(kind)) { mk('path', { d: 'M-22 -152 Q0 -160 22 -152 L28 -24 L-26 -24Z', fill: robe }, b); mk('path', { d: 'M-20 -150 L24 -60 L26 -30', stroke: kind === 'octav' ? '#d8cfbf' : '#7a2a6a', 'stroke-width': 8, fill: 'none' }, b); }
  else if (kind === 'ptol' || kind === 'egs') { mk('path', { d: 'M-18 -150 Q0 -156 20 -150 L22 -96 L-20 -96Z', fill: sk }, b); mk('path', { d: 'M-22 -100 L24 -100 L30 -56 L-26 -56Z', fill: robe }, b); mk('rect', { x: -22, y: -104, width: 46, height: 8, fill: '#d8b23a' }, b); }
  else { mk('path', { d: 'M-21 -150 Q0 -156 21 -150 L26 -60 L-24 -60Z', fill: robe }, b); }
  if (kind === 'leg') { for (let i = 0; i < 4; i++) mk('rect', { x: -22, y: -146 + i * 14, width: 46, height: 11, rx: 3, fill: '#9aa3ad', stroke: '#5a626c', 'stroke-width': 2 }, b); mk('path', { d: 'M-22 -150 L-40 -60 L-20 -64Z', fill: '#8a1e24' }, b); }
  if (kind === 'antony') { mk('path', { d: 'M-20 -148 L22 -148 L24 -100 L-22 -100Z', fill: '#c9a45a', stroke: '#8a6a2a', 'stroke-width': 3 }, b); mk('path', { d: 'M-22 -150 L-44 -40 L-22 -50Z', fill: '#7a1a20' }, b); }
  if (kind === 'cleo') mk('path', { d: 'M-18 -150 Q2 -128 22 -150 Q2 -136 -18 -150Z', fill: '#2f8f9a', stroke: '#d8b23a', 'stroke-width': 4 }, b);
  // head
  mk('circle', { cx: 2, cy: -168, r: 14, fill: sk }, b); mk('circle', { cx: 10, cy: -170, r: 1.9, fill: '#1a1410' }, b);
  if (kind === 'cleo') { mk('path', { d: 'M-16 -150 Q-20 -186 2 -186 Q20 -186 16 -170 L12 -170 Q8 -180 -4 -176 L-6 -150Z', fill: '#16120e' }, b); mk('path', { d: 'M-14 -180 Q2 -190 18 -180', stroke: '#d8b23a', 'stroke-width': 4, fill: 'none' }, b); mk('path', { d: 'M16 -182 q6 -6 2 -12 q-4 6 -2 12z', fill: '#d8b23a' }, b); }
  if (kind === 'ptol') { mk('path', { d: 'M-16 -150 L-14 -178 Q2 -188 16 -178 L14 -168 L-4 -168 L-6 -150Z', fill: '#2f5fa0' }, b); for (let i = 0; i < 4; i++) mk('path', { d: `M${-15 + i} ${-174 + i * 7} L${-5} ${-174 + i * 7}`, stroke: '#d8b23a', 'stroke-width': 3 }, b); }
  if (kind === 'egs') { mk('path', { d: 'M-16 -150 L-14 -178 Q2 -186 16 -178 L14 -170 L-4 -170 L-6 -150Z', fill: '#e8dcc0' }, b); mk('path', { d: 'M-14 -166 h-2 M-14 -160 h-2', stroke: '#a8462a', 'stroke-width': 3 }, b); }
  if (kind === 'caesar' || kind === 'sen' || kind === 'octav') { mk('path', { d: 'M-12 -176 Q2 -186 16 -176 L14 -172 Q2 -180 -10 -170Z', fill: kind === 'caesar' ? '#9a9088' : '#6a4a2a' }, b); }
  if (kind === 'caesar') for (let i = 0; i < 5; i++) mk('ellipse', { cx: -10 + i * 6, cy: -180 + Math.abs(i - 2) * 2, rx: 5, ry: 2.6, fill: '#4f8a3a', transform: `rotate(${(i - 2) * 25} ${-10 + i * 6} ${-180})` }, b);
  if (kind === 'antony') mk('path', { d: 'M-14 -174 Q2 -190 18 -176 L16 -170 Q2 -178 -12 -166Z', fill: '#2a1a10' }, b);
  if (kind === 'apo' || kind === 'cit') mk('path', { d: 'M-14 -174 Q2 -188 18 -176 L16 -172 Q2 -180 -12 -168Z', fill: '#2a1a10' }, b);
  if (kind === 'leg') { mk('path', { d: 'M-15 -170 Q2 -190 19 -170 L22 -160 L16 -158 L14 -166 L-10 -166 L-14 -150 L-18 -152Z', fill: '#b0905a', stroke: '#7a5a2a', 'stroke-width': 2 }, b); mk('path', { d: 'M-10 -186 Q2 -206 14 -186', stroke: '#c0262d', 'stroke-width': 10, fill: 'none' }, b); }
  const arm = mk('g', { transform: 'translate(4 -144)' }, b);
  mk('path', { d: 'M-4 -6 L32 6 L30 16 L-6 8Z', fill: ['cleo', 'caesar', 'octav', 'sen'].includes(kind) ? robe : sk }, arm); mk('circle', { cx: 34, cy: 12, r: 6, fill: sk }, arm);
  if (kind === 'leg') { mk('path', { d: 'M30 60 L60 -110', stroke: '#6b4a2a', 'stroke-width': 5 }, arm); mk('path', { d: 'M58 -106 L66 -132 L62 -104Z', fill: '#c9c2b0' }, arm);
    const sh = mk('g', { transform: 'translate(26 -110)' }, b); mk('rect', { x: -6, y: -10, width: 30, height: 84, rx: 6, fill: '#b3262d', stroke: '#d8b23a', 'stroke-width': 4 }, sh); mk('circle', { cx: 9, cy: 32, r: 7, fill: '#d8b23a' }, sh); }
  if (kind === 'egs') { mk('path', { d: 'M30 60 L56 -110', stroke: '#6b4a2a', 'stroke-width': 5 }, arm); mk('path', { d: 'M54 -106 L60 -128 L58 -104Z', fill: '#b08a4a' }, arm);
    const sh = mk('g', { transform: 'translate(28 -112)' }, b); mk('path', { d: 'M0 0 Q14 -10 26 0 L26 60 Q14 72 0 60Z', fill: '#e8dcc0', stroke: '#6b4a2a', 'stroke-width': 3 }, sh); mk('path', { d: 'M4 20 h18 M4 34 h18', stroke: '#6b4a2a', 'stroke-width': 3 }, sh); }
  if (hold === 'sack') { const s = mk('g', { transform: 'translate(-6 -200)' }, b); mk('path', { d: 'M-60 10 Q-70 -30 -20 -36 L60 -30 Q80 -10 60 16 L-40 22Z', fill: '#d8c8a8', stroke: '#8a7a5a', 'stroke-width': 4 }, s); mk('path', { d: 'M-30 -34 L-26 20 M30 -32 L28 18', stroke: '#6b4a2a', 'stroke-width': 4 }, s); }
  return { o, b, legL: legs[0], legR: legs[1], arm, kind };
};
EG.pose = function (f, { x = 0, y = 0, s = 1, dir = 1, run = 0, ph = 0, arm = 0, lean = 0 } = {}) {
  const sw = Math.sin(ph) * 28 * run; f.legL.setAttribute('transform', `translate(-8 -86) rotate(${sw})`); f.legR.setAttribute('transform', `translate(8 -86) rotate(${-sw})`);
  f.arm.setAttribute('transform', `translate(4 -144) rotate(${arm})`); f.o.setAttribute('transform', `translate(${x} ${y - Math.abs(Math.sin(ph)) * 6 * run}) scale(${dir * s} ${s}) rotate(${lean})`);
};
EG.place = (f, x, y, s = 1, dir = 1, arm = 0) => EG.pose(f, { x, y, s, dir, arm });
/* backgrounds */
EG.sky = function (s, top = '#7ab8e8', bot = '#f4dca0', id) { const lg = mk('linearGradient', { id: 'egs' + (++UID), x1: 0, y1: 0, x2: 0, y2: 1 }, s); mk('stop', { offset: 0, 'stop-color': top }, lg); mk('stop', { offset: 1, 'stop-color': bot }, lg); return mk('rect', { width: 1920, height: 1080, fill: `url(#${lg.id})` }, s); };
EG.desert = function (s, { sun = true } = {}) { EG.sky(s, '#6fb0e6', '#f6dca8'); if (sun) { mk('circle', { cx: 1600, cy: 200, r: 90, fill: '#fff2b0', opacity: .5 }, s); mk('circle', { cx: 1600, cy: 200, r: 60, fill: '#fff6d0' }, s); }
  mk('path', { d: 'M0 760 Q400 700 900 750 T1920 730 L1920 1080 L0 1080Z', fill: '#e0b46a' }, s); mk('path', { d: 'M0 860 Q600 820 1100 860 T1920 850 L1920 1080 L0 1080Z', fill: '#d2a258' }, s); };
EG.pyramid = function (s, x, y, w, col = '#e8c27a') { const g = mk('g', {}, s); mk('path', { d: `M${x - w / 2} ${y} L${x} ${y - w * .64} L${x + w / 2} ${y}Z`, fill: col }, g); mk('path', { d: `M${x} ${y - w * .64} L${x + w / 2} ${y} L${x + w * .12} ${y}Z`, fill: '#000', opacity: .18 }, g);
  for (let i = 1; i < 8; i++) mk('line', { x1: x - w / 2 * (1 - i / 8), x2: x + w / 2 * (1 - i / 8), y1: y - w * .64 * i / 8, y2: y - w * .64 * i / 8, stroke: '#b08a4a', 'stroke-width': 1.5, opacity: .5 }, g); return g; };
EG.pyramids = function (s, x = 960, y = 780, sc = 1) { const g = mk('g', {}, s); EG.pyramid(g, x - 420 * sc, y, 420 * sc, '#e2bb72'); EG.pyramid(g, x + 60 * sc, y, 620 * sc); EG.pyramid(g, x + 470 * sc, y, 300 * sc, '#dcb36a'); return g; };
EG.palm = function (s, x, y, sc = 1) { const g = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s); mk('path', { d: 'M-6 0 Q-14 -120 4 -240 L14 -238 Q0 -120 8 0Z', fill: '#7a5a32' }, g);
  for (let k = 0; k < 7; k++) mk('path', { d: `M8 -240 q${(k - 3) * 40} -50 ${(k - 3) * 80} 10`, stroke: '#2f7a3a', 'stroke-width': 18, fill: 'none', 'stroke-linecap': 'round' }, g); return g; };
EG.sea = function (s, y = 620, col = '#2a6fb0') { const g = mk('g', {}, s); mk('rect', { y, width: 1920, height: 1080 - y, fill: col }, g); const waves = mk('g', {}, g);
  for (let r = 0; r < 6; r++) for (let i = 0; i < 14; i++) mk('path', { d: `M${i * 160 - 60 + (r % 2) * 80} ${y + 30 + r * 70} q20 -12 40 0 q20 12 40 0`, stroke: '#cfe6ff', 'stroke-width': 4, fill: 'none', opacity: .35 }, waves);
  return { g, anim: t => waves.setAttribute('transform', `translate(${Math.sin(t * .8) * 30} 0)`) }; };
EG.pharos = function (s, x, y, sc = 1) { const g = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s);
  mk('rect', { x: -90, y: -260, width: 180, height: 260, fill: '#efe6d2', stroke: '#b8a888', 'stroke-width': 4 }, g); mk('rect', { x: -60, y: -420, width: 120, height: 160, fill: '#efe6d2', stroke: '#b8a888', 'stroke-width': 4 }, g);
  mk('rect', { x: -36, y: -520, width: 72, height: 100, fill: '#efe6d2', stroke: '#b8a888', 'stroke-width': 4 }, g); for (let i = 0; i < 4; i++) mk('rect', { x: -14, y: -230 + i * 50, width: 28, height: 28, fill: '#3a3020' }, g);
  const fire = mk('g', {}, g); mk('circle', { cy: -545, r: 70, fill: '#ffb030', opacity: .3 }, fire); mk('path', { d: 'M-24 -520 Q-30 -560 0 -600 Q30 -560 24 -520Z', fill: '#ffb030' }, fire); mk('path', { d: 'M-12 -520 Q-14 -550 0 -575 Q14 -550 12 -520Z', fill: '#fff2a0' }, fire);
  return { g, fire }; };
EG.city = function (s, y = 640, n = 9) { const g = mk('g', {}, s); for (let i = 0; i < n; i++) { const x = 60 + i * 200, w = 150 + (i % 3) * 20, h = 110 + (i % 4) * 40, b = mk('g', {}, g);
    mk('rect', { x, y: y - h, width: w, height: h, fill: i % 2 ? '#f2ead8' : '#e8dcc2' }, b); for (let k = 0; k < 3; k++) mk('rect', { x: x + 20 + k * 44, y: y - h + 24, width: 22, height: 34, fill: '#4a4030', opacity: .6 }, b);
    if (i % 3 === 0) mk('path', { d: `M${x - 10} ${y - h} L${x + w / 2} ${y - h - 50} L${x + w + 10} ${y - h}Z`, fill: '#c9a46a' }, b); } return g; };
EG.columns = function (s, { col = '#e8dcc0', n = 6, top = 120, bottom = 900, cap = 'lotus' } = {}) { const g = mk('g', {}, s);
  for (let i = 0; i < n; i++) { const x = 120 + i * (1680 / (n - 1)); mk('rect', { x: x - 40, y: top + 40, width: 80, height: bottom - top - 40, fill: col }, g); mk('rect', { x: x - 40, y: top + 40, width: 12, height: bottom - top - 40, fill: '#000', opacity: .08 }, g);
    if (cap === 'lotus') mk('path', { d: `M${x - 70} ${top} Q${x} ${top + 70} ${x + 70} ${top} L${x + 46} ${top + 44} L${x - 46} ${top + 44}Z`, fill: '#2f8f9a' }, g); else mk('rect', { x: x - 56, y: top + 10, width: 112, height: 30, fill: col, stroke: '#b8a888', 'stroke-width': 3 }, g);
    mk('rect', { x: x - 52, y: bottom, width: 104, height: 24, fill: col }, g); } return g; };
EG.palace = function (s) { EG.sky(s, '#3a2a1a', '#6a4a2a'); mk('rect', { y: 900, width: 1920, height: 180, fill: '#a8865a' }, s); for (let i = 0; i < 12; i++) mk('rect', { x: i * 160, y: 900, width: 158, height: 180, fill: i % 2 ? '#b8966a' : '#9a7a50' }, s);
  EG.columns(s, { n: 6, top: 80, bottom: 900 }); mk('rect', { y: 0, width: 1920, height: 80, fill: '#2f6f8a' }, s); for (let i = 0; i < 24; i++) mk('rect', { x: i * 80 + 10, y: 20, width: 40, height: 40, fill: i % 2 ? '#d8b23a' : '#c0392b' }, s); };
EG.library = function (s) { EG.sky(s, '#3a2a1a', '#2a1e12'); const g = mk('g', {}, s);
  for (let c = 0; c < 9; c++) for (let r = 0; r < 6; r++) { const x = 80 + c * 200, y = 120 + r * 130; mk('rect', { x, y, width: 180, height: 116, fill: '#5a3e22', stroke: '#3a2610', 'stroke-width': 6 }, g);
    for (let k = 0; k < 4; k++) { mk('circle', { cx: x + 30 + k * 40, cy: y + 70, r: 17, fill: '#efe2c0', stroke: '#b89a60', 'stroke-width': 3 }, g); mk('circle', { cx: x + 30 + k * 40, cy: y + 70, r: 5, fill: '#b89a60' }, g); } } return g; };
EG.temple = function (s, x = 960, y = 880, sc = 1, col = '#eae4d6') { const g = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s);
  mk('rect', { x: -420, y: -30, width: 840, height: 30, fill: col, stroke: '#b8b0a0', 'stroke-width': 3 }, g); mk('rect', { x: -400, y: -60, width: 800, height: 30, fill: col, stroke: '#b8b0a0', 'stroke-width': 3 }, g);
  for (let i = 0; i < 8; i++) { mk('rect', { x: -370 + i * 104, y: -420, width: 44, height: 360, fill: col, stroke: '#b8b0a0', 'stroke-width': 3 }, g); mk('rect', { x: -380 + i * 104, y: -436, width: 64, height: 18, fill: col }, g); }
  mk('rect', { x: -410, y: -470, width: 820, height: 36, fill: col, stroke: '#b8b0a0', 'stroke-width': 3 }, g); mk('path', { d: 'M-430 -470 L0 -600 L430 -470Z', fill: col, stroke: '#b8b0a0', 'stroke-width': 3 }, g); return g; };
EG.nile = function (s) { EG.desert(s, { sun: true }); mk('path', { d: 'M0 860 Q500 800 960 840 T1920 820 L1920 1080 L0 1080Z', fill: '#2a7ab0' }, s);
  for (let i = 0; i < 18; i++) mk('path', { d: `M${i * 110} 1000 q10 -60 0 -110`, stroke: '#4f8a3a', 'stroke-width': 8, fill: 'none' }, s); [200, 520, 1500, 1760].forEach((x, i) => EG.palm(s, x, 790, .9 + (i % 2) * .2)); };
/* galley / warship: facing right; size 1..2, sail colour; returns {g, oars, anim} */
EG.galley = function (s, { size = 1, sail = '#efe6d2', hull = '#6a4a2a', rows = 1, flag } = {}) { const w0 = mk('g', {}, s), g = mk('g', {}, w0), L = 260 * size;
  mk('path', { d: `M${-L} -10 Q${-L - 30} -60 ${-L + 10} -70 L${L - 40} -60 Q${L} -40 ${L + 40} -20 L${L} 10 L${-L + 20} 20Z`, fill: hull, stroke: '#2a1a0a', 'stroke-width': 4 }, g);
  mk('path', { d: `M${L} 0 L${L + 60} 6 L${L} 14Z`, fill: '#b08a4a' }, g); for (let r = 0; r < rows; r++) mk('line', { x1: -L + 40, x2: L - 60, y1: -40 + r * 16, y2: -40 + r * 16, stroke: '#d8b23a', 'stroke-width': 3, opacity: .6 }, g);
  const oars = []; for (let r = 0; r < rows; r++) for (let i = 0; i < Math.round(9 * size); i++) { const x = -L + 60 + i * ((2 * L - 120) / (9 * size)); oars.push(mk('line', { x1: x, y1: -30 + r * 12, x2: x - 20, y2: 60 + r * 10, stroke: '#3a2a1a', 'stroke-width': 4 }, g)); }
  mk('rect', { x: -6, y: -70 - 220 * size, width: 12, height: 220 * size, fill: '#5a3e22' }, g); const sl = mk('path', { d: `M${-110 * size} ${-60 - 200 * size} Q0 ${-40 - 220 * size} ${110 * size} ${-60 - 200 * size} L${100 * size} -90 Q0 -70 ${-100 * size} -90Z`, fill: sail, stroke: '#8a7a5a', 'stroke-width': 3 }, g);
  if (flag) mk('path', { d: `M6 ${-70 - 220 * size} l50 12 l-50 12z`, fill: flag }, g);
  return { w: w0, g, oars, sail: sl, anim: t => oars.forEach((o, i) => o.setAttribute('transform', `rotate(${Math.sin(t * 5 + i * .3) * 14} ${o.getAttribute('x1')} ${o.getAttribute('y1')})`)) };
};
EG.rocket = function (s, x, y, sc = 1) { const g = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s); mk('rect', { x: -30, y: -300, width: 60, height: 300, fill: '#f2f2f2', stroke: '#8a8a8a', 'stroke-width': 3 }, g);
  mk('path', { d: 'M-30 -300 L0 -380 L30 -300Z', fill: '#f2f2f2', stroke: '#8a8a8a', 'stroke-width': 3 }, g); [-200, -120].forEach(yy => mk('rect', { x: -30, y: yy, width: 60, height: 14, fill: '#222' }, g)); mk('path', { d: 'M-30 0 L-56 30 L-30 -40Z M30 0 L56 30 L30 -40Z', fill: '#c0392b' }, g); return g; };
EG.label = (s, txt, x, y, size = 64, fill = '#fff', anchor = 'middle') => { const t = mk('text', { x, y, 'text-anchor': anchor, 'font-family': 'Bebas Neue', 'font-size': size, fill, stroke: 'rgb(0 0 0 / .55)', 'stroke-width': size / 10, 'paint-order': 'stroke' }, s); t.innerHTML = txt; return t; };
EG.laurel = function (s, x, y, sc = 1) { const g = mk('g', { transform: `translate(${x} ${y}) scale(${sc})` }, s); [-1, 1].forEach(k => { mk('path', { d: `M0 40 Q${k * 70} 20 ${k * 60} -50`, stroke: '#4f8a3a', 'stroke-width': 6, fill: 'none' }, g);
  for (let i = 0; i < 6; i++) mk('ellipse', { cx: k * (30 + i * 5), cy: 30 - i * 15, rx: 14, ry: 6, fill: '#4f8a3a', transform: `rotate(${k * (-30 - i * 8)} ${k * (30 + i * 5)} ${30 - i * 15})` }, g); }); return g; };
})();
