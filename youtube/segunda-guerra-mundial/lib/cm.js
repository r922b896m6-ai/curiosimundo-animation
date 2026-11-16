/* CURIOSIMUNDO · Primera Guerra Mundial · shared animation library (givemotion, 1920×1080)
   Stylised, bloodless, informative: soldiers in period uniforms per nation, battles with rifle fire, machine guns,
   artillery and hand-to-hand fighting shown as silhouettes with impact flashes (no blood, no gore). */
(function () {
const NS = 'http://www.w3.org/2000/svg';
const mk = (tag, attrs, parent) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); parent && parent.append(e); return e; };
const CM = window.CM = { mk, NS };

/* ---------------- uniforms (period-accurate colours, simplified) ---------------- */
const U = CM.U = {
  FR14: { name: 'FRANCIA', tunic: '#2b3f8f', pants: '#c0392b', legs: '#c0392b', boots: '#1b1410', hat: 'kepi', hatC: '#c0392b', hatB: '#2b3f8f', belt: '#3a2a1a', pack: '#5b4a33', flag: 'FR' },
  FR:   { name: 'FRANCIA', tunic: '#7d93ad', pants: '#7d93ad', legs: '#6e8196', boots: '#1b1410', hat: 'adrian', hatC: '#62738a', belt: '#4a3a24', pack: '#5b4a33', flag: 'FR' },
  DE14: { name: 'ALEMANIA', tunic: '#6e7462', pants: '#5e6455', legs: '#1a1a1a', boots: '#111', hat: 'pickel', hatC: '#7a7d6c', belt: '#1d1d1d', pack: '#6b5a3e', flag: 'DE' },
  DE:   { name: 'ALEMANIA', tunic: '#6e7462', pants: '#5e6455', legs: '#1a1a1a', boots: '#111', hat: 'stahl', hatC: '#555c4c', belt: '#1d1d1d', pack: '#6b5a3e', flag: 'DE' },
  UK14: { name: 'REINO UNIDO', tunic: '#8a7a4e', pants: '#7a6c44', legs: '#62573a', boots: '#2a1f14', hat: 'cap', hatC: '#7a6c44', belt: '#b9ac7a', pack: '#6f6343', flag: 'UK' },
  UK:   { name: 'REINO UNIDO', tunic: '#8a7a4e', pants: '#7a6c44', legs: '#62573a', boots: '#2a1f14', hat: 'brodie', hatC: '#5d5a3a', belt: '#b9ac7a', pack: '#6f6343', flag: 'UK' },
  RU:   { name: 'RUSIA', tunic: '#a59a6c', pants: '#5f5a3e', legs: '#151515', boots: '#151515', hat: 'cap', hatC: '#6c6a48', belt: '#3a2a1a', pack: '#7d7a70', roll: '#8a8a80', flag: 'RU' },
  AH:   { name: 'AUSTRIA-HUNGRÍA', tunic: '#8c97a3', pants: '#8c97a3', legs: '#7d8792', boots: '#1b1410', hat: 'kepiAH', hatC: '#8c97a3', belt: '#3a2a1a', pack: '#6b5a3e', flag: 'AH' },
  OT:   { name: 'IMPERIO OTOMANO', tunic: '#9a8a5c', pants: '#8a7b50', legs: '#7a6b45', boots: '#2a1f14', hat: 'kabalak', hatC: '#b3a575', belt: '#5a4a2a', pack: '#6f6343', flag: 'OT' },
  ANZ:  { name: 'ANZAC', tunic: '#8a7a4e', pants: '#7a6c44', legs: '#62573a', boots: '#2a1f14', hat: 'slouch', hatC: '#7a6a42', belt: '#b9ac7a', pack: '#6f6343', flag: 'AU' },
  IT:   { name: 'ITALIA', tunic: '#7b7f63', pants: '#6f735a', legs: '#5f634c', boots: '#1b1410', hat: 'adrian', hatC: '#5f6450', belt: '#4a3a24', pack: '#6b5a3e', flag: 'IT' },
  PL:   { name: 'POLONIA', tunic: '#7d7a52', pants: '#6f6c48', legs: '#5f5c3e', boots: '#1b1410', hat: 'm33', hatC: '#5d5c40', belt: '#4a3a24', pack: '#6b5a3e', flag: 'PL' },
  FR40: { name: 'FRANCIA', tunic: '#8a7f55', pants: '#7d7350', legs: '#6b6346', boots: '#1b1410', hat: 'adrian', hatC: '#6b6a4a', belt: '#4a3a24', pack: '#6b5a3e', flag: 'FR' },
  SU:   { name: 'UNIÓN SOVIÉTICA', tunic: '#8f8a5c', pants: '#6b6a48', legs: '#151515', boots: '#151515', hat: 'ssh', hatC: '#4f5a3a', belt: '#5a3a1e', pack: '#6b6a48', flag: 'SU' },
  US44: { name: 'ESTADOS UNIDOS', tunic: '#7a7448', pants: '#6f6a45', legs: '#b8a77c', boots: '#2a1f14', hat: 'm1', hatC: '#5a5a3a', belt: '#a99a6a', pack: '#6b6a3f', flag: 'US' },
  JP:   { name: 'JAPÓN', tunic: '#a29a63', pants: '#8f8857', legs: '#8f8857', boots: '#2a1f14', hat: 'jp', hatC: '#6a6a45', belt: '#5a4a2a', pack: '#7a6f48', flag: 'JP' },
  IT40: { name: 'ITALIA', tunic: '#7b7f63', pants: '#6f735a', legs: '#5f634c', boots: '#1b1410', hat: 'm33', hatC: '#5f6450', belt: '#4a3a24', pack: '#6b5a3e', flag: 'IT' },
  DE2:  { name: 'ALEMANIA', tunic: '#6e7462', pants: '#5e6455', legs: '#1a1a1a', boots: '#111', hat: 'stahl', hatC: '#555c4c', belt: '#1d1d1d', pack: '#6b5a3e', flag: 'DE2' },
  DEAK: { name: 'AFRIKA KORPS', tunic: '#c2a96e', pants: '#b39a60', legs: '#8a7a50', boots: '#5a4a2a', hat: 'stahl', hatC: '#b49a62', belt: '#5a4a2a', pack: '#9a8a5a', flag: 'DE2' },
  UKD:  { name: 'REINO UNIDO', tunic: '#c9b07a', pants: '#b89f68', legs: '#9a8656', boots: '#2a1f14', hat: 'brodie', hatC: '#8f8458', belt: '#e0d3a4', pack: '#a8955f', flag: 'UK' },
  MXSF: { name: 'MÉXICO · FUERZAS ESPECIALES', tunic: '#6d7150', pants: '#666a4a', legs: '#666a4a', boots: '#2a2420', hat: 'mich', hatC: '#55593e', belt: '#2f3128', pack: '#55593e', flag: 'MX', vest: '#4a4d38', camo: true },
  MEX:  { name: 'MEXICAS', tunic: '#efe7d2', pants: '#efe7d2', legs: '#a8714a', boots: '#7a5a3a', hat: 'plume', hatC: '#2f8f5a', belt: '#c0392b', pack: '#7a5a3a', flag: 'MEX', skin: '#a8714a', weapon: 'macua', shield: true, noFire: true, noPack: true },
  TLX:  { name: 'TLAXCALA', tunic: '#efe7d2', pants: '#efe7d2', legs: '#a8714a', boots: '#7a5a3a', hat: 'plume', hatC: '#e8e0d0', belt: '#d8b23a', pack: '#7a5a3a', flag: 'TLX', skin: '#a8714a', weapon: 'macua', shield: true, noFire: true, noPack: true },
  ES:   { name: 'ESPAÑA', tunic: '#9aa0aa', pants: '#7a2a2a', legs: '#5a4a3a', boots: '#3a2a1a', hat: 'morion', hatC: '#c3c8d0', belt: '#5a3a1e', pack: '#6b5a3e', flag: 'ESB', noPack: true, bayonet: false },
  US:   { name: 'ESTADOS UNIDOS', tunic: '#6b6a3f', pants: '#625f38', legs: '#b8a77c', boots: '#2a1f14', hat: 'brodie', hatC: '#55553a', belt: '#a99a6a', pack: '#6b6a3f', flag: 'US' },
};
const SKIN0 = '#d9a77c'; let SKIN = SKIN0;
function hat(g, u) {
  const c = u.hatC;
  switch (u.hat) {
    case 'kepi': mk('path', { d: 'M-12 -150 L-10 -168 L16 -170 L18 -150 Z', fill: c }, g); mk('rect', { x: -13, y: -154, width: 32, height: 6, fill: u.hatB }, g); mk('path', { d: 'M12 -150 L28 -147 L14 -146Z', fill: '#111' }, g); break;
    case 'kepiAH': mk('path', { d: 'M-12 -150 L-10 -166 L16 -167 L18 -150 Z', fill: c }, g); mk('path', { d: 'M12 -150 L28 -147 L14 -146Z', fill: '#111' }, g); break;
    case 'adrian': mk('path', { d: 'M-16 -150 Q3 -176 22 -150Z', fill: c }, g); mk('path', { d: 'M-22 -150 Q3 -144 28 -150 Q3 -154 -22 -150Z', fill: c }, g); mk('path', { d: 'M-2 -172 Q3 -180 8 -172 L6 -160 L0 -160Z', fill: c }, g); break;
    case 'pickel': mk('path', { d: 'M-15 -150 Q3 -174 21 -150Z', fill: c }, g); mk('path', { d: 'M1 -170 L3 -184 L5 -170Z', fill: c }, g); mk('path', { d: 'M14 -150 L28 -146 L14 -147Z', fill: '#111' }, g); break;
    case 'stahl': mk('path', { d: 'M-16 -146 Q3 -176 22 -150 L26 -140 L22 -142 L-12 -142 L-16 -138 Z', fill: c }, g); break;
    case 'brodie': mk('path', { d: 'M-10 -152 Q3 -170 16 -152Z', fill: c }, g); mk('path', { d: 'M-24 -151 Q3 -158 30 -151 Q3 -144 -24 -151Z', fill: c }, g); break;
    case 'cap': mk('path', { d: 'M-14 -150 Q-14 -164 3 -166 Q22 -166 20 -152 Z', fill: c }, g); mk('path', { d: 'M10 -151 L28 -148 L12 -147Z', fill: '#2a1f14' }, g); break;
    case 'kabalak': mk('path', { d: 'M-14 -148 Q-16 -170 3 -172 Q22 -170 20 -148 Z', fill: c }, g); mk('path', { d: 'M-14 -160 Q3 -150 20 -160 M-14 -153 Q3 -144 20 -153', stroke: '#8a7c50', 'stroke-width': 3, fill: 'none' }, g); break;
    case 'm1': mk('path', { d: 'M-17 -148 Q3 -182 23 -148 L25 -145 L-19 -145Z', fill: c }, g); mk('path', { d: 'M-12 -160 Q3 -150 18 -160', stroke: 'rgb(0 0 0 / .2)', 'stroke-width': 3, fill: 'none' }, g); break;
    case 'ssh': mk('path', { d: 'M-16 -150 Q3 -180 22 -150Z', fill: c }, g); mk('path', { d: 'M-19 -150 Q3 -144 25 -150 Q3 -154 -19 -150Z', fill: c }, g); break;
    case 'jp': mk('path', { d: 'M-15 -150 Q3 -178 21 -150Z', fill: c }, g); mk('path', { d: 'M-15 -150 L-19 -128 L-8 -132 L-6 -150Z', fill: '#c2b47a' }, g); break;
    case 'morion': mk('path', { d: 'M-26 -150 Q-20 -142 3 -146 Q26 -142 32 -150 Q22 -158 20 -158 Q3 -184 -14 -158 Q-22 -158 -26 -150Z', fill: c, stroke: '#7d838c', 'stroke-width': 2 }, g); mk('path', { d: 'M-8 -160 Q3 -192 14 -160', fill: c, stroke: '#7d838c', 'stroke-width': 2 }, g); break;
    case 'mich': mk('path', { d: 'M-16 -148 Q3 -180 22 -148 L22 -142 L-16 -142Z', fill: c }, g); mk('rect', { x: -2, y: -178, width: 10, height: 8, rx: 2, fill: '#222' }, g); mk('rect', { x: 14, y: -160, width: 12, height: 8, rx: 2, fill: '#2a2a2a' }, g); break;
    case 'plume': mk('path', { d: 'M-12 -156 Q3 -166 18 -156 L18 -150 L-12 -150Z', fill: '#c0392b' }, g); for (let i = 0; i < 5; i++) mk('path', { d: `M${-8 + i * 6} -158 Q${-14 + i * 6} -190 ${-20 + i * 9} -205 Q${-6 + i * 6} -188 ${-4 + i * 6} -158Z`, fill: i % 2 ? '#2f8f5a' : '#1f6fb0' }, g); break;
    case 'm33': mk('path', { d: 'M-16 -148 Q3 -180 22 -148 L23 -144 L-17 -144Z', fill: c }, g); break;
    case 'slouch': mk('path', { d: 'M-10 -152 Q3 -170 16 -152Z', fill: c }, g); mk('path', { d: 'M-30 -152 Q3 -158 34 -151 Q3 -147 -30 -152Z', fill: c }, g); mk('path', { d: 'M-12 -152 L-16 -168 L-6 -160Z', fill: c }, g); break;
  }
}
/* figure: feet at (0,0), facing right; returns parts so poses can be animated each frame */
CM.figure = function (parent, nation, opts = {}) {
  const u = U[nation], o = mk('g', {}, parent), b = mk('g', {}, o); SKIN = u.skin || SKIN0;
  const legL = mk('g', { transform: 'translate(-8 -84)' }, b), legR = mk('g', { transform: 'translate(8 -84)' }, b);
  for (const lg of [legL, legR]) { mk('path', { d: 'M-9 0 L-7 70 L7 70 L9 0Z', fill: u.pants }, lg); mk('rect', { x: -8, y: 40, width: 15, height: 32, fill: u.legs }, lg); mk('path', { d: 'M-9 70 h18 l6 8 h-24z', fill: u.boots }, lg); }
  if (opts.pack !== false && !u.noPack) mk('rect', { x: -38, y: -148, width: 17, height: 52, rx: 6, fill: u.pack }, b);
  if (u.roll) mk('path', { d: 'M-22 -150 Q0 -126 22 -96', stroke: u.roll, 'stroke-width': 9, fill: 'none' }, b);
  mk('path', { d: 'M-21 -150 Q0 -156 21 -150 L25 -82 L-25 -82 Z', fill: u.tunic }, b);
  if (nation === 'FR14') mk('path', { d: 'M-25 -84 L-28 -60 L28 -60 L25 -84Z', fill: u.tunic }, b);     // greatcoat skirt
  if (u.camo) [[-14, -136, 7], [8, -124, 6], [-6, -112, 5], [14, -142, 5]].forEach(([x, y, r]) => mk('ellipse', { cx: x, cy: y, rx: r * 1.6, ry: r, fill: '#4f5338' }, b));
  if (u.vest) { mk('path', { d: 'M-20 -146 L20 -146 L22 -104 L-22 -104Z', fill: u.vest }, b); [-12, 0, 12].forEach(x => mk('rect', { x: x - 4, y: -132, width: 9, height: 14, rx: 2, fill: '#3a3d2c' }, b)); }
  if (nation === 'MEX') mk('path', { d: 'M-24 -100 L24 -100 L20 -84 L-20 -84Z', fill: '#c0392b' }, b);
  mk('rect', { x: -24, y: -104, width: 48, height: 7, fill: u.belt }, b);
  if (u.hat === 'brodie' || u.hat === 'cap' || u.hat === 'slouch') mk('path', { d: 'M-18 -148 L19 -104', stroke: u.belt, 'stroke-width': 5 }, b);
  mk('circle', { cx: 3, cy: -162, r: 13, fill: SKIN }, b); mk('circle', { cx: 10, cy: -164, r: 1.8, fill: '#2a1f14' }, b);
  hat(b, u);
  if (opts.mask) { mk('path', { d: 'M-10 -176 Q20 -178 20 -150 Q18 -138 0 -140 Q-14 -150 -10 -176Z', fill: '#59604a' }, b); mk('circle', { cx: 12, cy: -164, r: 6, fill: '#bcd0c6', stroke: '#2f3426', 'stroke-width': 2 }, b);
    mk('path', { d: 'M14 -150 l14 12 l-6 8 l-14 -10z', fill: '#3d4234' }, b); }
  const arm = mk('g', { transform: 'translate(6 -140)' }, b);
  const weapon = opts.weapon || u.weapon || 'rifle';
  if (weapon === 'rifle') { mk('path', { d: 'M-8 26 L56 -6', stroke: '#6b4a2a', 'stroke-width': 7, 'stroke-linecap': 'round' }, arm); mk('path', { d: 'M50 -3 L92 -24', stroke: '#3a3a3a', 'stroke-width': 4, 'stroke-linecap': 'round' }, arm);
    if (opts.bayonet !== false && u.bayonet !== false) mk('path', { d: 'M90 -23 L112 -34', stroke: '#c9c2b0', 'stroke-width': 3, 'stroke-linecap': 'round' }, arm); }
  if (weapon === 'carbine') { mk('path', { d: 'M-8 24 L40 -2', stroke: '#1d1d1d', 'stroke-width': 8, 'stroke-linecap': 'round' }, arm); mk('path', { d: 'M36 0 L84 -24', stroke: '#2a2a2a', 'stroke-width': 6, 'stroke-linecap': 'round' }, arm); mk('rect', { x: 26, y: -16, width: 22, height: 9, rx: 2, fill: '#111', transform: 'rotate(-28 37 -12)' }, arm); mk('path', { d: 'M30 4 L34 18', stroke: '#1d1d1d', 'stroke-width': 7 }, arm); }
  if (weapon === 'macua') { mk('path', { d: 'M10 0 L70 -28', stroke: '#6b4a2a', 'stroke-width': 10, 'stroke-linecap': 'round' }, arm); for (let i = 0; i < 5; i++) { const x = 30 + i * 9, y = -9 - i * 4.2; mk('path', { d: `M${x} ${y - 6} l4 -7 l4 6z M${x + 2} ${y + 6} l4 6 l3 -7z`, fill: '#1a1a22' }, arm); } }
  if (opts.shield !== undefined ? opts.shield : (!opts.weapon && u.shield)) { const sh = mk('g', { transform: 'translate(22 -120)' }, b); mk('circle', { r: 26, fill: '#efe7d2', stroke: '#c0392b', 'stroke-width': 5 }, sh); mk('path', { d: 'M-14 -10 h28 M-14 0 h28 M-14 10 h28', stroke: '#1f6fb0', 'stroke-width': 4 }, sh); for (let i = 0; i < 5; i++) mk('path', { d: `M${-12 + i * 6} 24 l-2 16`, stroke: '#2f8f5a', 'stroke-width': 4 }, sh); }
  if (weapon === 'shovel') { mk('path', { d: 'M0 0 L60 0', stroke: '#6b5236', 'stroke-width': 7, 'stroke-linecap': 'round' }, arm); mk('path', { d: 'M58 -12 L86 -9 L88 12 L58 14 Z', fill: '#8e8f86' }, arm); }
  if (weapon === 'club') { mk('path', { d: 'M10 0 L58 0', stroke: '#6b5236', 'stroke-width': 8, 'stroke-linecap': 'round' }, arm); mk('rect', { x: 54, y: -11, width: 30, height: 24, rx: 8, fill: '#4a3826' }, arm); }
  if (weapon === 'grenade') { mk('path', { d: 'M0 0 L40 -6', stroke: '#6b5236', 'stroke-width': 6 }, arm); mk('rect', { x: 36, y: -14, width: 14, height: 20, rx: 3, fill: '#4a4a40' }, arm); }
  const sleeve = mk('path', { d: 'M-4 -7 L34 4 L32 14 L-6 8 Z', fill: u.tunic }, arm); mk('circle', { cx: 36, cy: 10, r: 6, fill: SKIN }, arm);
  if (weapon === 'fist') mk('circle', { cx: 40, cy: 10, r: 9, fill: SKIN }, arm);
  const flash = mk('circle', { cx: 116, cy: -36, r: u.noFire ? 0 : 22, fill: 'url(#cmFlash)', opacity: 0 }, arm);
  const up = mk('g', { style: 'display:none' }, b);   // hands up (surrender / captured)
  mk('path', { d: 'M-16 -146 L-24 -206', stroke: u.tunic, 'stroke-width': 13, 'stroke-linecap': 'round' }, up); mk('path', { d: 'M18 -146 L26 -206', stroke: u.tunic, 'stroke-width': 13, 'stroke-linecap': 'round' }, up);
  mk('circle', { cx: -25, cy: -212, r: 7, fill: SKIN }, up); mk('circle', { cx: 27, cy: -212, r: 7, fill: SKIN }, up);
  return { o, b, legL, legR, arm, flash, up, nation };
};
/* run cycle / pose helpers (call every frame) */
CM.pose = function (f, { x = 0, y = 0, s = 1, dir = 1, run = 0, ph = 0, lean = 0, armRot = 0, fall = 0, up = false }) {
  if (f.up) { f.up.style.display = up ? '' : 'none'; f.arm.style.display = up ? 'none' : ''; }
  const sw = Math.sin(ph) * 32 * run;
  f.legL.setAttribute('transform', `translate(-8 -84) rotate(${sw})`); f.legR.setAttribute('transform', `translate(8 -84) rotate(${-sw})`);
  f.arm.setAttribute('transform', `translate(6 -140) rotate(${armRot})`);
  const rot = lean + fall * 82, bob = -Math.abs(Math.sin(ph)) * 8 * run;
  f.o.setAttribute('transform', `translate(${x} ${y + bob}) scale(${dir * s} ${s}) rotate(${rot})`);
};

/* ---------------- flags ---------------- */
CM.flag = function (parent, code, x, y, w = 90, h = 60) {
  const g = mk('g', { transform: `translate(${x} ${y})` }, parent); const R = (a, b, c, d, f) => mk('rect', { x: a, y: b, width: c, height: d, fill: f }, g);
  const v = cs => cs.forEach((c, i) => R(i * w / cs.length, 0, w / cs.length + .5, h, c)), hz = cs => cs.forEach((c, i) => R(0, i * h / cs.length, w, h / cs.length + .5, c));
  ({ FR: () => v(['#2b3f8f', '#fff', '#c0392b']), IT: () => v(['#1f8a4c', '#fff', '#c0392b']), BE: () => v(['#111', '#f6c400', '#d0312d']),
     DE: () => hz(['#111', '#fff', '#c0392b']), RU: () => hz(['#fff', '#2b4fa8', '#c0392b']), AH: () => { hz(['#111', '#f6c400']); },
     SR: () => hz(['#c0392b', '#2b4fa8', '#fff']), BG: () => hz(['#fff', '#1f8a4c', '#c0392b']),
     OT: () => { R(0, 0, w, h, '#c0392b'); mk('circle', { cx: w * .44, cy: h / 2, r: h * .26, fill: '#fff' }, g); mk('circle', { cx: w * .5, cy: h / 2, r: h * .21, fill: '#c0392b' }, g); mk('circle', { cx: w * .66, cy: h / 2, r: h * .08, fill: '#fff' }, g); },
     UK: () => { R(0, 0, w, h, '#1f3a8a'); mk('path', { d: `M0 0 L${w} ${h} M${w} 0 L0 ${h}`, stroke: '#fff', 'stroke-width': h * .2 }, g); mk('path', { d: `M0 0 L${w} ${h} M${w} 0 L0 ${h}`, stroke: '#c0392b', 'stroke-width': h * .07 }, g);
            mk('path', { d: `M${w / 2} 0 V${h} M0 ${h / 2} H${w}`, stroke: '#fff', 'stroke-width': h * .32 }, g); mk('path', { d: `M${w / 2} 0 V${h} M0 ${h / 2} H${w}`, stroke: '#c0392b', 'stroke-width': h * .18 }, g); },
     US: () => { for (let i = 0; i < 7; i++) R(0, i * h / 7, w, h / 14 + .5, '#c0392b'); for (let i = 0; i < 7; i++) R(0, i * h / 7 + h / 14, w, h / 14 + .5, '#fff'); R(0, 0, w * .42, h * .54, '#1f3a8a'); },
     MX: () => { const w3 = w / 3; R(0, 0, w3, h, '#006847'); R(w3, 0, w3, h, '#fff'); R(w3 * 2, 0, w3, h, '#ce1126'); mk('circle', { cx: w / 2, cy: h / 2, r: h * .16, fill: '#8a6a2a' }, g); },
     MEX: () => { R(0, 0, w, h, '#efe7d2'); mk('circle', { cx: w / 2, cy: h / 2, r: h * .34, fill: 'none', stroke: '#1f6fb0', 'stroke-width': 4 }, g); mk('path', { d: `M${w * .3} ${h * .5} h${w * .4} M${w * .5} ${h * .25} v${h * .5}`, stroke: '#c0392b', 'stroke-width': 5 }, g); },
     ESB: () => { R(0, 0, w, h, '#fff'); mk('path', { d: `M${w * .15} ${h * .1} L${w * .85} ${h * .9} M${w * .85} ${h * .1} L${w * .15} ${h * .9}`, stroke: '#c0392b', 'stroke-width': h * .14, 'stroke-dasharray': `${h * .12} ${h * .04}` }, g); },
     TLX: () => { R(0, 0, w, h, '#fff'); mk('path', { d: `M${w * .25} ${h * .75} L${w * .5} ${h * .2} L${w * .75} ${h * .75}Z`, fill: '#d8b23a' }, g); },
     PL: () => hz(['#fff', '#d0312d']), JP: () => { R(0, 0, w, h, '#fff'); mk('circle', { cx: w / 2, cy: h / 2, r: h * .3, fill: '#c0392b' }, g); },
     SU: () => { R(0, 0, w, h, '#c0392b'); mk('path', { d: `M${w * .2} ${h * .18} l4 9 l10 0 l-8 6 l3 10 l-9 -6 l-9 6 l3 -10 l-8 -6 l10 0z`, fill: '#ffd23f', transform: `scale(${h / 60})`, 'transform-origin': `${w * .2}px ${h * .18}px` }, g); },
     DE2: () => { R(0, 0, w, h, '#e9e6dc'); mk('path', { d: `M${w / 2} ${h * .12} V${h * .88} M${w * .3} ${h / 2} H${w * .7}`, stroke: '#111', 'stroke-width': h * .2 }, g); mk('path', { d: `M${w / 2} ${h * .12} V${h * .88} M${w * .3} ${h / 2} H${w * .7}`, stroke: '#111', 'stroke-width': h * .1, 'stroke-linecap': 'square' }, g); },
     AU: () => { R(0, 0, w, h, '#1f3a8a'); mk('circle', { cx: w * .25, cy: h * .75, r: h * .1, fill: '#fff' }, g); [[.7, .25], [.62, .5], [.8, .55], [.72, .8]].forEach(([a, b]) => mk('circle', { cx: w * a, cy: h * b, r: h * .06, fill: '#fff' }, g)); },
  }[code] || (() => R(0, 0, w, h, '#888')))();
  mk('rect', { x: 0, y: 0, width: w, height: h, fill: 'none', stroke: 'rgb(0 0 0 / .4)', 'stroke-width': 2 }, g);
  return g;
};

/* ---------------- shared defs ---------------- */
CM.defs = function () {
  // one shared, always-rendered defs block (gradients inside hidden scenes would not paint elsewhere)
  if (document.getElementById('cmDefsRoot')) return;
  const root = mk('svg', { id: 'cmDefsRoot', width: 0, height: 0, style: 'position:absolute;left:0;top:0' }); document.body.prepend(root);
  const d = mk('defs', {}, root);
  d.innerHTML = `<radialGradient id="cmFlash"><stop offset="0" stop-color="#fff6d0"/><stop offset=".35" stop-color="#ffb347" stop-opacity=".9"/><stop offset="1" stop-color="#ff6a00" stop-opacity="0"/></radialGradient>
  <radialGradient id="cmSmoke"><stop offset="0" stop-color="#5b5550" stop-opacity=".85"/><stop offset="1" stop-color="#5b5550" stop-opacity="0"/></radialGradient>
  <radialGradient id="cmGas"><stop offset="0" stop-color="#d7dc5a" stop-opacity=".8"/><stop offset=".6" stop-color="#b9c24a" stop-opacity=".45"/><stop offset="1" stop-color="#b9c24a" stop-opacity="0"/></radialGradient>
  <g id="cmStar"><path d="M0 -60 L14 -16 L58 -20 L22 6 L40 48 L0 22 L-40 48 L-22 6 L-58 -20 L-14 -16Z" fill="#fff3c4"/><path d="M0 -30 L7 -8 L29 -10 L11 3 L20 24 L0 11 L-20 24 L-11 3 L-29 -10 L-7 -8Z" fill="#FFD23F"/></g>`;
};

/* ---------------- explosion (seekable) ---------------- */
CM.explosion = function (parent, cx, cy, t0, scale = 1, seed = 'e') {
  const g = mk('g', {}, parent), flash = mk('circle', { cx, cy, r: 140 * scale, fill: 'url(#cmFlash)' }, g);
  const smoke = [0, 1, 2].map(() => mk('circle', { cx, cy, r: 90 * scale, fill: 'url(#cmSmoke)' }, g));
  const clods = Array.from({ length: 14 }, (_, i) => ({ el: mk('circle', { r: (6 + gm.random(seed + 'c' + i) * 12) * scale, fill: i % 3 ? '#2a2017' : '#4a3826' }, g),
    vx: (gm.random(seed + 'x' + i) - .5) * 700 * scale, vy: -(380 + gm.random(seed + 'y' + i) * 520) * scale }));
  return t => { const d = t - t0, on = d >= 0 && d < 3; g.style.display = on ? '' : 'none'; if (!on) return;
    flash.setAttribute('opacity', Math.max(0, 1 - d / .35)); flash.setAttribute('r', 140 * scale * (1 + d * 2));
    smoke.forEach((s, i) => { const dd = Math.max(0, d - .05 * i); s.setAttribute('r', 90 * scale * (1 + dd * 1.4 + i * .3)); s.setAttribute('cy', cy - dd * 60 * scale - i * 30 * scale); s.setAttribute('cx', cx + (i - 1) * 50 * scale); s.setAttribute('opacity', Math.max(0, .9 - dd / 3)); });
    clods.forEach(c => { c.el.setAttribute('cx', cx + c.vx * d); c.el.setAttribute('cy', Math.min(cy + c.vy * d + 900 * d * d, cy + 30)); c.el.setAttribute('opacity', d < 1.5 ? 1 : 0); }); };
};

/* ---------------- battle: side view, two armies, rifles, MGs, artillery, melee ---------------- */
const TERRAIN = {
  fields: { ground: '#4d5a32', far: '#6b7a48', sky: ['#9fb6cc', '#d9c9a0'] }, mud: { ground: '#3b2d20', far: '#55452f', sky: ['#5d636d', '#9a9c9a'] },
  beach: { ground: '#c9b07a', far: '#8a7a50', sky: ['#7fb2e0', '#f0d9a8'], sea: true }, mountains: { ground: '#5a5f55', far: '#8a93a0', sky: ['#a9bccf', '#e6eef5'], peaks: true },
  forest: { ground: '#3d4a2a', far: '#2c3a20', sky: ['#7d8f7a', '#c9c9a0'], trees: true }, night: { ground: '#1c1a16', far: '#2a2a30', sky: ['#05080f', '#1a2236'] },
  dusk: { ground: '#3b2d20', far: '#55452f', sky: ['#3e3a3d', '#c97a4a'] },
  ruins: { ground: '#4a4744', far: '#6a6662', sky: ['#5b5f66', '#b3a898'], ruins: true }, desert: { ground: '#d2b77a', far: '#c2a66a', sky: ['#8fbde6', '#f3dfb0'] },
  snow: { ground: '#e3eaf1', far: '#c3ced8', sky: ['#8e9aa8', '#dde4ea'], trees: true }, jungle: { ground: '#3a5a2a', far: '#2c4a20', sky: ['#7fae9a', '#d9e6c0'], trees: true },
};
CM.battle = function (section, cfg) {
  const W = 3200, svg = mk('svg', { viewBox: '0 0 1920 1080', width: 1920, height: 1080, style: 'position:absolute;inset:0' }, section); CM.defs(svg);
  const T = TERRAIN[cfg.terrain || 'mud'], sky = cfg.sky || T.sky;
  const bg = mk('rect', { width: 1920, height: 1080, fill: 'url(#bsky' + cfg.id + ')' }, svg);
  const lg = mk('linearGradient', { id: 'bsky' + cfg.id, x1: 0, y1: 0, x2: 0, y2: 1 }, mk('defs', {}, svg)); mk('stop', { offset: 0, 'stop-color': sky[0] }, lg); mk('stop', { offset: 1, 'stop-color': sky[1] }, lg);
  const world = mk('g', {}, svg);
  const GY = cfg.gy || 790, SC = cfg.scale || 1.5;                    // ground line, figure scale
  if (T.peaks) mk('path', { d: `M0 ${GY} L300 380 L620 560 L980 300 L1400 600 L1800 360 L2300 620 L2700 340 L3200 560 L3200 ${GY}Z`, fill: T.far }, world);
  if (T.sea) mk('rect', { x: 0, y: GY - 40, width: 900, height: 40, fill: '#3d7fbf' }, world);
  mk('path', { d: `M0 ${GY - 30} Q800 ${GY - 70} 1600 ${GY - 30} T${W} ${GY - 40} L${W} 1400 L0 1400Z`, fill: T.far, opacity: .6 }, world);
  mk('path', { d: `M0 ${GY} Q800 ${GY - 20} 1600 ${GY} T${W} ${GY} L${W} 1400 L0 1400Z`, fill: T.ground }, world);
  if (T.ruins) for (let i = 0; i < 12; i++) { const x = 60 + i * 270, h = 260 + gm.random('rh' + i) * 260, w = 180 + gm.random('rw' + i) * 80;
    mk('path', { d: `M${x} ${GY - 10} L${x} ${GY - h} L${x + w * .3} ${GY - h + 40} L${x + w * .55} ${GY - h - 30} L${x + w * .8} ${GY - h + 60} L${x + w} ${GY - h + 20} L${x + w} ${GY - 10}Z`, fill: '#5d5853' }, world);
    for (let r = 0; r < 4; r++) for (let c = 0; c < 3; c++) mk('rect', { x: x + 20 + c * (w / 3.4), y: GY - h + 70 + r * 55, width: 22, height: 30, fill: '#2a2826' }, world); }
  if (T.trees) for (let i = 0; i < 14; i++) { const x = 120 + i * 220 + gm.random('tr' + i) * 80; mk('rect', { x: x - 8, y: GY - 160, width: 16, height: 160, fill: '#2a2017' }, world); mk('circle', { cx: x, cy: GY - 180, r: 70, fill: cfg.terrain === 'snow' ? '#3c5a46' : '#2f4a24' }, world); if (cfg.terrain === 'snow') mk('path', { d: `M${x - 60} ${GY - 190} Q${x} ${GY - 260} ${x + 60} ${GY - 190}`, stroke: '#fff', 'stroke-width': 14, fill: 'none' }, world); }
  if (cfg.hedgehogs) for (let i = 0; i < 8; i++) { const x = 700 + i * 220, y = GY + 20 + (i % 2) * 60; mk('path', { d: `M${x - 30} ${y} L${x + 30} ${y - 50} M${x + 30} ${y} L${x - 30} ${y - 50} M${x} ${y + 5} L${x} ${y - 55}`, stroke: '#2a2a2a', 'stroke-width': 9 }, world); }
  for (let i = 0; i < 9; i++) mk('ellipse', { cx: 600 + i * 260, cy: GY + 40 + (i % 3) * 70, rx: 90, ry: 20, fill: 'rgb(0 0 0 / .25)' }, world);
  const LT = 320, RT = W - 320;                                         // trench x positions
  for (const tx of [LT, RT]) { mk('rect', { x: tx - 90, y: GY - 6, width: 180, height: 60, fill: '#2a2017' }, world);
    for (let k = 0; k < 6; k++) mk('rect', { x: tx - 110 + k * 38, y: GY - 34 - (k % 2) * 8, width: 44, height: 26, rx: 10, fill: '#8a7a58', stroke: '#5e5039', 'stroke-width': 3 }, world); }
  if (cfg.wire !== false) for (const wx of [LT + 420, RT - 420]) { const w = mk('path', { d: `M${wx - 120} ${GY - 10} ` + Array.from({ length: 12 }, (_, k) => `l20 ${k % 2 ? 22 : -22}`).join(' '), stroke: '#1a1410', 'stroke-width': 4, fill: 'none' }, world); }
  const att = cfg.attacker || 'left', A = att === 'left' ? cfg.left : cfg.right, D = att === 'left' ? cfg.right : cfg.left;
  const dirA = att === 'left' ? 1 : -1, fromX = att === 'left' ? LT : RT, toX = att === 'left' ? RT : LT;
  const soldiers = mk('g', {}, world), fx = mk('g', {}, world), tracers = mk('g', { stroke: '#ffe08a', 'stroke-width': 4, 'stroke-linecap': 'round' }, world);
  const t0 = cfg.t0, t1 = cfg.t1;
  // defenders in their trench
  const DEF = Array.from({ length: cfg.def || 4 }, (_, i) => ({ f: CM.figure(soldiers, D), x: toX - dirA * (-80 + i * 60), y: GY + 10, ph: gm.random('d' + i) * 6 }));
  // attackers advancing
  const n = cfg.n || 8, ATT = Array.from({ length: n }, (_, i) => ({ f: CM.figure(soldiers, A), x0: fromX - dirA * (i * 95), y: GY + 30 + (i % 3) * 50, sp: (360 + gm.random('s' + i) * 120),
    fall: cfg.falls && cfg.falls.includes(i) ? t0 + 1.2 + gm.random('f' + i) * (t1 - t0 - 2) : 1e9, ph: gm.random('p' + i) * 6, start: t0 + (cfg.wave || .25) * (i % 4) }));
  const ex = (cfg.artillery || []).map((at, i) => CM.explosion(fx, fromX + dirA * (500 + gm.random('ax' + i) * 1700), GY + 20 + gm.random('ay' + i) * 120, at, 1 + gm.random('as' + i) * .7, cfg.id + 'a' + i));
  const TR = Array.from({ length: cfg.mg ? 6 : 0 }, () => mk('line', {}, tracers));
  // melee pairs near the defenders' trench
  // hand-to-hand: the camera cuts INTO the enemy trench; attackers jump down and fight inside it
  const M = cfg.melee, SCI = 2.0, FY = 905; let MP = [], stars = [], dust = [], inT = null, tIn = 1e9;
  if (M) {
    tIn = M.at - (M.lead || 1.1);
    inT = mk('g', { style: 'display:none' }, svg);
    mk('rect', { width: 1920, height: 1080, fill: 'url(#bsky' + cfg.id + ')' }, inT);
    mk('rect', { y: 330, width: 1920, height: 750, fill: '#2a2017' }, inT); mk('rect', { y: 352, width: 1920, height: 560, fill: '#33271b' }, inT);
    for (let k = 0; k < 9; k++) mk('rect', { x: 40 + k * 230, y: 352, width: 14, height: 560, fill: '#241a12', opacity: .7 }, inT);
    mk('rect', { y: 600, width: 1920, height: 10, fill: '#241a12', opacity: .6 }, inT);
    for (let k = 0; k < 16; k++) mk('rect', { x: -20 + k * 124, y: 300 - (k % 2) * 10, width: 130, height: 50, rx: 18, fill: '#8a7a58', stroke: '#5e5039', 'stroke-width': 4 }, inT);
    mk('rect', { y: FY, width: 1920, height: 26, fill: '#6b5236' }, inT); for (let k = 0; k < 20; k++) mk('rect', { x: k * 100, y: FY, width: 8, height: 26, fill: '#4c3a25' }, inT);
    mk('rect', { y: FY + 26, width: 1920, height: 200, fill: '#2a2017' }, inT);
    const gI = mk('g', {}, inT), xs = [430, 960, 1490];
    MP = (M.weapons || ['rifle', 'club', 'shovel']).map((wp, i) => ({ a: CM.figure(gI, A, { weapon: wp, pack: false }), d: CM.figure(gI, D, { weapon: i % 2 ? 'rifle' : 'fist', pack: false }),
      x: dirA > 0 ? xs[i] : 1920 - xs[i], at: M.at + i * (M.step || .9), jump: tIn + .2 + i * .25 }));
    dust = MP.map(() => mk('ellipse', { rx: 10, ry: 4, fill: '#8a7a5a' }, inT)); stars = MP.map(() => mk('use', { href: '#cmStar' }, inT));
  }
  // labels with flags
  const tags = mk('g', {}, svg);
  if (cfg.labels !== false) [[A, att === 'left' ? 90 : 1430], [D, att === 'left' ? 1430 : 90]].forEach(([nat, x]) => { const g = mk('g', { class: 'btag' }, tags); mk('rect', { x, y: 250, width: 400, height: 76, rx: 14, fill: 'rgb(10 12 20 / .72)' }, g);
    CM.flag(g, U[nat].flag, x + 16, 263, 75, 50); const t = mk('text', { x: x + 106, y: 302, 'font-family': 'Bebas Neue', 'font-size': 46, fill: '#fff' }, g); t.textContent = U[nat].name; });
  // non-trench outcomes: 'capture' (hands up, held at gunpoint), 'retreat' (defenders fall back), 'flag' (position taken)
  const O = cfg.outcome || null, oAt = O ? O.at : 1e9;
  let FP = null;
  if (O && (O.type === 'flag' || O.flag)) { FP = mk('g', {}, world); mk('rect', { x: -4, y: -260, width: 8, height: 260, fill: '#3a2a1a' }, FP); CM.flag(FP, U[A].flag, 4, -260, 120, 78); }
  const pan = cfg.pan || [0, att === 'left' ? -(W - 1920) : 0];
  const shake = { v: 0 };
  gm.onFrame(section, (l, info) => { const t = info.time, p = gm.clamp((t - t0) / (t1 - t0));
    const camX = pan[0] + (pan[1] - pan[0]) * (.5 - .5 * Math.cos(Math.PI * p)); let sx = 0, sy = 0;
    (cfg.artillery || []).forEach(at => { const d = t - at; if (d >= 0 && d < .45) { const k = (1 - d / .45) * 14; sx += (gm.noise(t * 40) - .5) * 2 * k; sy += (gm.noise(t * 40 + 5) - .5) * 2 * k; } });
    world.setAttribute('transform', `translate(${camX + sx} ${sy})`);
    DEF.forEach((d, i) => { const fire = gm.random('df' + i + ':' + Math.floor(t * 3)) > .55, after = t >= oAt;
      if (O && after && O.type === 'retreat') { const r = t - oAt; CM.pose(d.f, { x: d.x + dirA * r * 360, y: d.y, s: SC * .95, dir: dirA, run: 1, ph: t * 11 + i, lean: 10 }); d.f.flash.setAttribute('opacity', 0); return; }
      if (O && after && O.type === 'capture') { CM.pose(d.f, { x: d.x - dirA * 40, y: d.y - 20, s: SC * .95, dir: -dirA, up: true }); d.f.flash.setAttribute('opacity', 0); return; }
      CM.pose(d.f, { x: d.x, y: d.y, s: SC * .95, dir: -dirA, armRot: -8 }); d.f.flash.setAttribute('opacity', t > t0 && t < oAt && fire && (t * 30 % 4) < 1.5 ? 1 : 0); });
    if (FP) { const k = gm.clamp((t - oAt - .3) / .8); FP.setAttribute('transform', `translate(${toX} ${GY - 30}) scale(1 ${k})`); FP.style.display = k > 0 ? '' : 'none'; }
    ATT.forEach(a => { const run = Math.max(0, Math.min(t, a.fall) - a.start), x = a.x0 + dirA * Math.min(run * a.sp, Math.abs(toX - fromX) - 430);
      const fall = t > a.fall ? Math.min(1, (t - a.fall) / .45) : 0, moving = t > a.start && run * a.sp < Math.abs(toX - fromX) - 430 && !fall;
      CM.pose(a.f, { x: O && O.type === 'capture' && t > oAt ? Math.max(Math.min(x, toX - dirA * 420), Math.min(x, toX - dirA * 420)) : x, y: a.y, s: SC, dir: dirA, run: moving ? 1 : 0, ph: t * 11 + a.ph, lean: moving ? 10 : 0, fall: fall ** 2, armRot: O && t > oAt ? -6 : 0 });
      a.f.o.style.display = (M && t > tIn) ? 'none' : ''; });
    ex.forEach(f => f(t));
    TR.forEach((ln, i) => { const k0 = Math.floor(t * 2.4 + i / 6), pp = (t * 2.4 + i / 6) % 1, sx0 = toX, sy0 = GY - 40, tx = fromX + dirA * (200 + gm.random('tx' + i + k0) * 1300), ty = GY - 120 + gm.random('ty' + i + k0) * 160;
      const x1 = sx0 + (tx - sx0) * pp, y1 = sy0 + (ty - sy0) * pp, kk = 90 / Math.hypot(tx - sx0, ty - sy0);
      ln.setAttribute('x1', x1); ln.setAttribute('y1', y1); ln.setAttribute('x2', x1 - (tx - sx0) * kk); ln.setAttribute('y2', y1 - (ty - sy0) * kk); ln.setAttribute('opacity', t > t0 + .3 && (!M || t < M.at) && t < oAt ? .9 : 0); });
    if (inT) inT.style.display = t >= tIn ? '' : 'none';
    MP.forEach((m, i) => { if (t < tIn) return;
      const jp = gm.clamp((t - m.jump) / .38), ay = 250 + (FY - 250) * jp * jp, d = t - m.at;
      const lunge = d > 0 && d < .25 ? d / .25 : d >= .25 && d < .6 ? 1 - (d - .25) / .35 : 0;
      const reel = gm.clamp((d - .2) / .3) * (d < 1.6 ? 1 : Math.max(0, 1 - (d - 1.6) / .4));
      const cyc = d % 2.2, again = d > 0 && cyc > 1.2 && cyc < 1.6 ? (cyc - 1.2) / .4 : 0;
      CM.pose(m.a, { x: m.x - dirA * 150 + dirA * 110 * (lunge + Math.sin(Math.PI * again)), y: ay, s: SCI, dir: dirA, lean: jp < 1 ? 12 : 0, armRot: d > 0 ? -40 * Math.sin(Math.PI * Math.min(1, d / .3)) * (i % 2) : 0 });
      m.a.o.style.opacity = t > m.jump - .05 ? 1 : 0;
      CM.pose(m.d, { x: m.x + dirA * 160 + dirA * 60 * reel, y: FY, s: SCI, dir: -dirA, lean: -12 * reel, armRot: d < 0 ? -8 : 0 });
      const dd = t - m.jump - .38, dOn = dd > 0 && dd < .7; dust[i].setAttribute('cx', m.x - dirA * 150); dust[i].setAttribute('cy', FY);
      dust[i].setAttribute('rx', dOn ? 30 + dd * 220 : 0); dust[i].setAttribute('ry', dOn ? 8 + dd * 30 : 0); dust[i].setAttribute('opacity', dOn ? .7 * (1 - dd / .7) : 0);
      const sd = d - .22, on2 = sd > 0 && sd < .3; stars[i].setAttribute('opacity', on2 ? 1 - sd / .3 : 0); stars[i].setAttribute('transform', `translate(${m.x + dirA * 10} ${FY - 330}) scale(${on2 ? .8 + sd * 3 : 0})`); });
    if (inT && t >= tIn) { let sx2 = 0, sy2 = 0; MP.forEach(m => { const dd = t - m.at - .22; if (dd > 0 && dd < .3) { const k = (1 - dd / .3) * 12; sx2 += (gm.noise(t * 50) - .5) * 2 * k; sy2 += (gm.noise(t * 50 + 3) - .5) * 2 * k; } });
      inT.setAttribute('transform', `translate(${sx2} ${sy2})`); }
  });
  return { svg, world, tags, GY };
};

/* ---------------- tank (British Mark IV style) ---------------- */
CM.tank = function (parent, color = '#6b6a3f') {
  const g = mk('g', {}, parent);
  mk('path', { d: 'M-200 0 Q-230 -40 -170 -110 L170 -110 Q230 -40 200 0 Q0 30 -200 0Z', fill: color, stroke: '#2a2a1a', 'stroke-width': 6 }, g);
  mk('path', { d: 'M-180 -10 Q-200 -40 -150 -95 L150 -95 Q200 -40 180 -10 Q0 15 -180 -10Z', fill: 'none', stroke: '#3a3a26', 'stroke-width': 10, 'stroke-dasharray': '14 10', class: 'track' }, g);
  mk('rect', { x: -60, y: -150, width: 120, height: 44, rx: 6, fill: color, stroke: '#2a2a1a', 'stroke-width': 5 }, g);
  mk('rect', { x: -95, y: -90, width: 60, height: 42, rx: 6, fill: '#5a5934' }, g); mk('path', { d: 'M-65 -70 L-150 -78', stroke: '#2a2a1a', 'stroke-width': 10 }, g);
  return g;
};
/* ---------------- WWII tank (generic turret tank) ---------------- */
CM.tank2 = function (parent, color = '#55583a', mark = 'star', markC = '#fff') {
  const g = mk('g', {}, parent);
  mk('rect', { x: -190, y: -70, width: 380, height: 74, rx: 34, fill: '#2f2f28' }, g);
  mk('path', { d: 'M-180 -36 L-180 -60 L-120 -100 L150 -100 L190 -60 L190 -36Z', fill: color, stroke: '#22231a', 'stroke-width': 4 }, g);
  for (let i = 0; i < 6; i++) mk('circle', { cx: -150 + i * 60, cy: -26, r: 22, fill: '#45453a', stroke: '#22231a', 'stroke-width': 4 }, g);
  mk('rect', { x: -176, y: -70, width: 352, height: 74, rx: 34, fill: 'none', stroke: '#1d1d18', 'stroke-width': 9, 'stroke-dasharray': '12 9', class: 'track' }, g);
  mk('path', { d: 'M-80 -100 L-60 -160 L70 -160 L95 -100Z', fill: color, stroke: '#22231a', 'stroke-width': 4 }, g);
  mk('rect', { x: 80, y: -140, width: 190, height: 16, rx: 5, fill: '#3a3b2c' }, g);
  if (mark === 'star') mk('path', { d: 'M0 -142 l6 14 l15 0 l-12 9 l5 15 l-14 -9 l-14 9 l5 -15 l-12 -9 l15 0z', fill: markC }, g);
  if (mark === 'cross') { mk('path', { d: 'M-20 -64 h40 M0 -84 v40', stroke: '#fff', 'stroke-width': 14 }, g); mk('path', { d: 'M-20 -64 h40 M0 -84 v40', stroke: '#111', 'stroke-width': 7 }, g); }
  return g;
};
/* ---------------- WWII fighter (monoplane) ---------------- */
CM.fighter = function (parent, color = '#6b7a5a', mark = 'roundel') {
  const g = mk('g', {}, parent);
  mk('path', { d: 'M-140 -6 Q-60 -26 70 -20 Q120 -16 130 0 Q120 14 70 16 Q-60 20 -140 6Z', fill: color, stroke: '#222', 'stroke-width': 3 }, g);
  mk('path', { d: 'M-130 -4 L-160 -40 L-140 -40 L-110 -8Z', fill: color, stroke: '#222', 'stroke-width': 3 }, g);
  mk('ellipse', { cx: 0, cy: 6, rx: 70, ry: 12, fill: color, stroke: '#222', 'stroke-width': 3 }, g); mk('path', { d: 'M30 -20 Q50 -40 75 -20Z', fill: '#bcd8ea', stroke: '#222', 'stroke-width': 2 }, g);
  mk('ellipse', { cx: 134, cy: 0, rx: 5, ry: 38, fill: '#ddd', opacity: .6 }, g);
  if (mark === 'roundel') { mk('circle', { cx: -50, cy: 0, r: 13, fill: '#1f3a8a' }, g); mk('circle', { cx: -50, cy: 0, r: 8, fill: '#fff' }, g); mk('circle', { cx: -50, cy: 0, r: 4, fill: '#c0392b' }, g); }
  if (mark === 'cross') { mk('path', { d: 'M-62 0 h24 M-50 -12 v24', stroke: '#fff', 'stroke-width': 9 }, g); mk('path', { d: 'M-62 0 h24 M-50 -12 v24', stroke: '#111', 'stroke-width': 4 }, g); }
  if (mark === 'sun') mk('circle', { cx: -50, cy: 0, r: 13, fill: '#c0392b' }, g);
  if (mark === 'star') { mk('circle', { cx: -50, cy: 0, r: 13, fill: '#1f3a8a' }, g); mk('path', { d: 'M-50 -10 l3 7 l8 0 l-6 5 l2 8 l-7 -5 l-7 5 l2 -8 l-6 -5 l8 0z', fill: '#fff' }, g); }
  return g;
};
CM.carrier = function (parent, color = '#5a6270') { const g = mk('g', {}, parent);
  mk('path', { d: 'M-380 0 L380 0 L340 60 L-350 60Z', fill: color, stroke: '#2a2f38', 'stroke-width': 5 }, g); mk('rect', { x: -400, y: -16, width: 800, height: 18, fill: '#7a6a52' }, g);
  mk('rect', { x: 180, y: -90, width: 60, height: 76, fill: color }, g); mk('rect', { x: 200, y: -130, width: 18, height: 42, fill: '#3a3f48' }, g); return g; };
CM.lcvp = function (parent) { const g = mk('g', {}, parent); mk('path', { d: 'M-120 0 L110 0 L130 -60 L-120 -60Z', fill: '#5a6a5a', stroke: '#2a3a2a', 'stroke-width': 4 }, g); mk('rect', { x: 100, y: -70, width: 30, height: 70, fill: '#4a5a4a' }, g); return g; };
/* dogfight: planes circle; listed ones are shot down (smoke trail, no gore) */
CM.dogfight = function (sec, t0, { a = { color: '#6b7a5a', mark: 'roundel' }, b = { color: '#7a7f86', mark: 'cross' }, n = 2, downs = [], sky = 'linear-gradient(#4f86c4, #cfe0ef)', city = false } = {}) {
  const s = CM.svgIn(sec, sky); const clouds = Array.from({ length: 6 }, () => mk('ellipse', { rx: 220, ry: 60, fill: '#fff', opacity: .7 }, s));
  if (city) for (let i = 0; i < 16; i++) mk('rect', { x: i * 125, y: 980 - 60 - gm.random('cb' + i) * 120, width: 110, height: 200, fill: '#3a4250' }, s);
  const P = []; for (let i = 0; i < n; i++) { P.push({ g: CM.fighter(s, a.color, a.mark), side: 'a', i }); P.push({ g: CM.fighter(s, b.color, b.mark), side: 'b', i }); }
  const smoke = P.map(() => mk('path', { stroke: '#3a3a3a', 'stroke-width': 18, 'stroke-linecap': 'round', fill: 'none', opacity: .55 }, s));
  const tr = mk('path', { stroke: '#ffe08a', 'stroke-width': 4, 'stroke-dasharray': '16 18', fill: 'none' }, s);
  gm.onFrame(sec, (l, info) => { const t = info.time, d = t - t0;
    clouds.forEach((c, i) => { c.setAttribute('cx', ((i * 420 - d * 90) % 2300 + 2300) % 2300 - 200); c.setAttribute('cy', 160 + (i % 3) * 220); });
    P.forEach((p, k) => { const off = (p.side === 'a' ? 0 : -.7) + p.i * 2.2, dn = downs.find(x => x.side === p.side && x.i === p.i), td = dn ? t - dn.at : -1;
      let x = 900 + Math.cos(d * .9 + off) * 560, y = 470 + Math.sin(d * 1.8 + 2 * off) * 180 + p.i * 90;
      let ang = Math.atan2(Math.cos(d * 1.8 + 2 * off) * 324, -Math.sin(d * .9 + off) * 504) * 180 / Math.PI;
      if (td > 0) { const x0 = 900 + Math.cos(dn.at - t0 + .9 * 0 + off) * 560; x = x + td * 120; y = y + td * td * 160; ang = 35 + td * 25; smoke[k].setAttribute('d', `M${x} ${y} Q${x - 80} ${y - 120} ${x - 160} ${y - 260}`); } else smoke[k].setAttribute('d', '');
      p.g.setAttribute('transform', `translate(${x} ${y}) rotate(${ang}) scale(1 ${Math.abs(ang) > 90 && td <= 0 ? -1 : 1})`); p.g.style.display = y > 1150 ? 'none' : ''; p.pos = [x, y]; });
    const A0 = P[0].pos, B0 = P[1].pos; tr.setAttribute('d', (t * 3) % 1 < .5 ? `M${A0[0]} ${A0[1]} L${A0[0] + (B0[0] - A0[0]) * .8} ${A0[1] + (B0[1] - A0[1]) * .8}` : ''); });
  return s;
};

/* civilian silhouette (coat + hat), for crowds / queues */
CM.civil = function (parent, x, y, s = 1, color = '#3a3f48') { const g = mk('g', { transform: `translate(${x} ${y}) scale(${s})` }, parent);
  mk('path', { d: 'M-22 -150 Q0 -158 22 -150 L28 -40 L-28 -40Z', fill: color }, g); mk('path', { d: 'M-16 -40 L-14 0 L-4 0 L-2 -40 M2 -40 L4 0 L14 0 L16 -40', fill: '#222' }, g);
  mk('circle', { cx: 2, cy: -168, r: 14, fill: '#d9a77c' }, g); mk('path', { d: 'M-22 -176 L26 -176 L18 -182 L16 -196 L-12 -196 L-14 -182Z', fill: '#2a2a2a' }, g); return g; };
/* document card (treaty, telegram…) */
CM.doc = function (sec, title, sub, lines, { x = 520, y = 200, w = 880, h = 600, rot = -2 } = {}) { const d = document.createElement('div');
  d.style.cssText = `position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;background:#efe6cf;border-radius:10px;box-shadow:0 30px 80px rgb(0 0 0 / .6);color:#3a2a1a;padding:44px 60px;font:600 34px/1.55 Georgia,serif;transform:rotate(${rot}deg);z-index:3`;
  d.innerHTML = `<div style="font:400 70px/1 'Bebas Neue'">${title}</div><div style="font-size:26px;margin:6px 0 22px">${sub}</div>` + lines.map(l => `<div class="it">${l}</div>`).join(''); sec.append(d); return d; };

/* ---------------- biplane ---------------- */
CM.plane = function (parent, nation, color) {
  const g = mk('g', {}, parent), c = color || ({ DE: '#c0392b', UK: '#a8a27a', FR: '#a8a27a' }[nation] || '#a8a27a');
  mk('rect', { x: -110, y: -46, width: 220, height: 14, rx: 6, fill: c }, g); mk('rect', { x: -110, y: 6, width: 220, height: 14, rx: 6, fill: c }, g);
  mk('path', { d: 'M-90 -14 L80 -18 Q110 -8 80 8 L-90 4Z', fill: c, stroke: '#222', 'stroke-width': 3 }, g); mk('path', { d: 'M-90 -14 L-120 -40 L-110 -4 Z', fill: c }, g);
  mk('path', { d: 'M-60 -32 V6 M60 -32 V6', stroke: '#222', 'stroke-width': 4 }, g); mk('ellipse', { cx: 104, cy: -5, rx: 6, ry: 34, fill: '#ddd', opacity: .6 }, g);
  if (nation === 'DE') mk('path', { d: 'M-40 -46 h20 v-14 h14 v14 h20 v14 h-20 v14 h-14 v-14 h-20z', fill: '#111', transform: 'translate(0 5) scale(.8)' }, g);
  else { mk('circle', { cx: -20, cy: -39, r: 9, fill: '#c0392b' }, g); mk('circle', { cx: -20, cy: -39, r: 5, fill: '#fff' }, g); mk('circle', { cx: -20, cy: -39, r: 2.5, fill: '#1f3a8a' }, g); }
  return g;
};
/* ---------------- warship ---------------- */
CM.ship = function (parent, color = '#5a6270') {
  const g = mk('g', {}, parent);
  mk('path', { d: 'M-300 0 L300 0 L260 50 L-270 50 Z', fill: color, stroke: '#2a2f38', 'stroke-width': 5 }, g);
  mk('rect', { x: -120, y: -60, width: 200, height: 60, fill: color }, g); mk('rect', { x: -40, y: -120, width: 50, height: 60, fill: color }, g);
  mk('rect', { x: 30, y: -150, width: 26, height: 90, fill: '#3a3f48' }, g); mk('rect', { x: -90, y: -140, width: 26, height: 80, fill: '#3a3f48' }, g);
  [[-230, -20], [180, -20]].forEach(([x, y]) => { mk('rect', { x: x - 30, y: y - 20, width: 60, height: 30, rx: 8, fill: '#4a5260' }, g); mk('path', { d: `M${x} ${y - 6} L${x + 90} ${y - 16}`, stroke: '#2a2f38', 'stroke-width': 8 }, g); });
  return g;
};

/* horse (side view, facing right); call CM.horsePose(h, t) to animate the legs */
CM.horse = function (parent, color = '#7a5236') { const g = mk('g', {}, parent), legs = [];
  [-48, -30, 40, 58].forEach(x => { const l = mk('g', { transform: `translate(${x} -70)` }, g); mk('rect', { x: -6, y: 0, width: 12, height: 70, rx: 5, fill: color }, l); mk('rect', { x: -7, y: 62, width: 14, height: 9, fill: '#2a1f14' }, l); legs.push(l); });
  mk('ellipse', { cx: 6, cy: -96, rx: 78, ry: 38, fill: color }, g); mk('path', { d: 'M60 -116 L92 -168 L120 -160 L128 -140 L104 -132 L84 -100Z', fill: color }, g);
  mk('path', { d: 'M66 -124 L92 -170 L84 -128Z', fill: '#3a2618' }, g); mk('path', { d: 'M-70 -110 Q-110 -90 -96 -40 Q-84 -80 -66 -96Z', fill: '#3a2618' }, g); mk('circle', { cx: 108, cy: -152, r: 3, fill: '#111' }, g);
  return { g, legs }; };
CM.horsePose = function (h, t, run = 1) { h.legs.forEach((l, i) => { const x = [-48, -30, 40, 58][i]; l.setAttribute('transform', `translate(${x} -70) rotate(${Math.sin(t * 9 + i * 1.6) * 24 * run})`); }); };
/* 16th-century caravel/nao (facing right) */
CM.caravel = function (parent) { const g = mk('g', {}, parent);
  mk('path', { d: 'M-150 -20 L160 -20 L120 40 L-120 40Z', fill: '#5a3e26', stroke: '#3a2a1a', 'stroke-width': 4 }, g); mk('path', { d: 'M-150 -20 L-150 -60 L-90 -60 L-90 -20Z M110 -20 L110 -50 L160 -50 L160 -20Z', fill: '#6b4a2e' }, g);
  [[-60, 150], [30, 190], [100, 120]].forEach(([x, hh]) => { mk('rect', { x: x - 4, y: -20 - hh, width: 8, height: hh, fill: '#3a2a1a' }, g); mk('path', { d: `M${x - 40} ${-10 - hh} Q${x} ${-hh + 20} ${x + 40} ${-10 - hh} L${x + 40} ${-50} Q${x} ${-30} ${x - 40} -50Z`, fill: '#efe7d2', stroke: '#c9bfa6', 'stroke-width': 2 }, g); });
  const fl = mk('g', { transform: 'translate(34 -230)' }, g); CM.flag(fl, 'ESB', 0, 0, 44, 30); return g; };
CM.svgIn = function (sec, bg) { if (bg) sec.style.background = bg; const s = mk('svg', { viewBox: '0 0 1920 1080', width: 1920, height: 1080, style: 'position:absolute;inset:0' }, sec); CM.defs(s); return s; };
CM.text = function (sec, cls, html, top, extra = '') { const d = document.createElement('div'); d.className = cls; d.innerHTML = html; d.style.cssText += `;top:${top}px;${extra}`; sec.append(d); return d; };
/* ocean liner (Lusitania-style, 4 funnels) and U-boat */
CM.liner = function (parent) { const g = mk('g', {}, parent);
  mk('path', { d: 'M-520 0 L520 0 L470 90 L-480 90Z', fill: '#1b1b1f' }, g); mk('rect', { x: -420, y: -60, width: 800, height: 60, fill: '#efe8dc' }, g); mk('rect', { x: -360, y: -100, width: 640, height: 40, fill: '#efe8dc' }, g);
  for (let i = 0; i < 4; i++) { mk('rect', { x: -300 + i * 150, y: -220, width: 60, height: 120, fill: '#c0392b' }, g); mk('rect', { x: -300 + i * 150, y: -220, width: 60, height: 26, fill: '#111' }, g); }
  for (let i = 0; i < 24; i++) mk('circle', { cx: -400 + i * 34, cy: -30, r: 6, fill: '#6b7a8a' }, g); return g; };
CM.uboat = function (parent) { const g = mk('g', {}, parent); mk('path', { d: 'M-260 0 Q-200 -40 0 -40 Q200 -40 260 0 Q200 30 0 30 Q-200 30 -260 0Z', fill: '#4a5058' }, g);
  mk('rect', { x: -40, y: -90, width: 80, height: 54, rx: 10, fill: '#4a5058' }, g); mk('rect', { x: -6, y: -150, width: 10, height: 64, fill: '#3a3f46' }, g); return g; };
/* drifting gas cloud (seekable) */
CM.gas = function (parent, t0, t1, { x0 = -200, y = 700, sp = 160, n = 18, spread = 260 } = {}) {
  const B = Array.from({ length: n }, (_, i) => ({ el: mk('circle', { r: 160, fill: 'url(#cmGas)' }, parent), ph: gm.random('g' + i + t0), dy: gm.random('gy' + i + t0) }));
  return t => B.forEach((b, i) => { const d = t - t0, on = d > 0 && t < t1 + 1.2; if (!on) { b.el.setAttribute('opacity', 0); return; }
    const x = x0 + d * sp - b.ph * spread; b.el.setAttribute('cx', x); b.el.setAttribute('cy', y - b.dy * 220 + Math.sin(t * .8 + i) * 18); b.el.setAttribute('r', 150 + b.dy * 90);
    b.el.setAttribute('opacity', gm.clamp((x - x0 + 100) / 200) * gm.clamp((t1 + 1.2 - t) / 1.2)); }); };

/* tank advance with infantry (and optional planes) */
CM.tanks = function (sec, t0, { n = 3, inf = 'UK', planes = false, sky = 'linear-gradient(#7d8792, #c9c0a4)', ww2 = null, ground = '#4a3a28' } = {}) {
  const s = CM.svgIn(sec, sky); mk('rect', { y: 800, width: 1920, height: 280, fill: ground }, s);
  for (let i = 0; i < 10; i++) mk('ellipse', { cx: 100 + i * 200, cy: 860 + (i % 3) * 60, rx: 80, ry: 18, fill: '#3a2c1e' }, s);
  const P = planes ? (ww2 ? [CM.fighter(s, ww2.pc || '#6b7a5a', ww2.pm || 'star'), CM.fighter(s, ww2.pc || '#6b7a5a', ww2.pm || 'star')] : [CM.plane(s, 'UK'), CM.plane(s, 'FR')]) : [];
  const T = Array.from({ length: n }, (_, i) => ({ g: ww2 ? CM.tank2(s, ww2.color, ww2.mark, ww2.markC) : CM.tank(s), x0: -300 - i * 520, y: 820 + (i % 2) * 70, sc: .8 + (i % 2) * .15 }));
  const F = Array.from({ length: 6 }, (_, i) => ({ f: CM.figure(s, Array.isArray(inf) ? inf[i % inf.length] : inf), x0: -500 - i * 260, y: 840 + (i % 2) * 60 }));
  gm.onFrame(sec, (l, info) => { const d = info.time - t0;
    T.forEach(tk => { tk.g.setAttribute('transform', `translate(${tk.x0 + d * 170} ${tk.y + Math.sin(d * 3 + tk.x0) * 3}) scale(${tk.sc})`); tk.g.querySelector('.track').setAttribute('stroke-dashoffset', -d * 90); });
    F.forEach((o, i) => CM.pose(o.f, { x: o.x0 + d * 190, y: o.y, s: 1.25, dir: 1, run: .6, ph: d * 7 + i, lean: 6 }));
    P.forEach((p, i) => p.setAttribute('transform', `translate(${-300 + d * (420 + i * 60) - i * 400} ${200 + i * 110 + Math.sin(d * 2 + i) * 20}) scale(.9)`)); });
  return s;
};

/* ---------------- Europe map ---------------- */
CM.MAPCOL = { land: '#3a4458', allies: '#2f6fcf', central: '#c0392b', neutral: '#6f7684', other: '#2a3242', sea: '#0b1f40' };
CM.map = function (section, data, { id = 'm' } = {}) {
  const svg = mk('svg', { viewBox: '0 0 1920 1080', width: 1920, height: 1080, style: 'position:absolute;inset:0' }, section); CM.defs(svg);
  mk('rect', { width: 1920, height: 1080, fill: CM.MAPCOL.sea }, svg);
  const g = mk('g', { style: 'transform-origin:0px 0px' }, svg), paths = {};
  for (const [k, d] of Object.entries(data.groups)) paths[k] = mk('path', { d, fill: k === 'OTROS' ? CM.MAPCOL.other : k === 'NEUTRAL' ? CM.MAPCOL.neutral : CM.MAPCOL.land, stroke: '#0b1f40', 'stroke-width': 1.5, 'stroke-linejoin': 'round' }, g);
  const over = mk('g', {}, g), labels = mk('g', { 'font-family': 'Bebas Neue', 'text-anchor': 'middle' }, g);
  const api = {
    svg, g, paths, over, labels,
    color(tl, keys, col, at, d = .5) { [].concat(keys).forEach(k => tl.to(paths[k], { fill: col, duration: d, ease: 'power2.inOut' }, at)); return api; },
    text(tl, txt, x, y, at, end, { size = 34, fill = '#fff', stroke = 'rgb(0 0 0 / .6)' } = {}) { const t = mk('text', { x, y, 'font-size': size, fill, stroke, 'stroke-width': size / 8, 'paint-order': 'stroke' }, labels); t.textContent = txt;
      tl.from(t, { opacity: 0, y: 14, duration: .35, ease: 'expo.out' }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; },
    pin(tl, city, txt, at, end, o = {}) { const [x, y] = data.cities[city], pg = mk('g', {}, over); const ring = mk('circle', { cx: x, cy: y, r: o.r || 12, fill: o.fill || '#FFD23F', stroke: '#111', 'stroke-width': 3 }, pg);
      tl.from(pg, { opacity: 0, duration: .01 }, at); tl.from(ring, { scale: 0, duration: .35, ease: 'back.out(2.5)', transformOrigin: `${x}px ${y}px` }, at);
      const pulse = mk('circle', { cx: x, cy: y, r: o.r || 12, fill: 'none', stroke: o.fill || '#FFD23F', 'stroke-width': 4 }, pg);
      tl.fromTo(pulse, { attr: { r: 12 }, opacity: 1 }, { attr: { r: 60 }, opacity: 0, duration: 1.2, repeat: 2 }, at);
      if (txt) api.text(tl, txt, x + (o.dx || 0), y - (o.dy || 26), at + .1, end, { size: o.size || 34 }); if (end) tl.to(pg, { opacity: 0, duration: .25 }, end); return pg; },
    line(tl, key, at, { color = '#FFD23F', width = 8, dash, arrow = false, dur = 1.2, end } = {}) { const p = mk('path', { d: data.lines[key], stroke: color, 'stroke-width': width, fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, over);
      if (dash) p.setAttribute('stroke-dasharray', dash); tl.from(p, { draw: 0, duration: dur, ease: 'power2.inOut' }, at);
      if (arrow) { const pts = data.lines[key].replace('M', '').split(' L').map(s => s.split(' ').map(Number)), [a, b] = pts.slice(-2), ang = Math.atan2(b[1] - a[1], b[0] - a[0]) * 180 / Math.PI;
        const h = mk('path', { d: 'M0 0 L-30 -18 L-30 18 Z', fill: color, transform: `translate(${b[0]} ${b[1]}) rotate(${ang})` }, over); tl.from(h, { opacity: 0, duration: .2 }, at + dur - .1); if (end) tl.to(h, { opacity: 0, duration: .25 }, end); }
      if (end) tl.to(p, { opacity: 0, duration: .25 }, end); return p; },
    zoom(tl, city, s, at, d = 1.2) { const [x, y] = typeof city === 'string' ? data.cities[city] : city; tl.to(g, { x: 960 - x * s, y: 540 - y * s, scale: s, duration: d, ease: 'power2.inOut' }, at); return api; },
  };
  return api;
};

/* ---------------- headline (top-left) and chapter card ---------------- */
CM.head = function (parent, tl, title, sub, at, end) {
  const el = document.createElement('div'); el.className = 'head'; el.innerHTML = `<div class="ht">${title}</div>${sub ? `<div class="hs">${sub}</div>` : ''}`; parent.append(el);
  tl.from(el, { x: -80, opacity: 0, duration: .45, ease: 'expo.out' }, at).from(el.querySelector('.ht'), { letterSpacing: '.2em', duration: .6, ease: 'expo.out' }, at);
  if (end) tl.to(el, { x: -60, opacity: 0, duration: .25, ease: 'power2.in' }, end); return el;
};
CM.card = function (parent, tl, num, year, name, at = 0, dur = 4) {
  const el = document.createElement('div'); el.className = 'card'; el.innerHTML = `<div class="cn">CAPÍTULO ${num}</div><div class="cy">${year}</div><div class="cname">${name}</div>`; parent.append(el);
  tl.from(el.querySelector('.cn'), { y: 30, opacity: 0, duration: .5, ease: 'expo.out' }, at + .1).from(el.querySelector('.cy'), { scale: 1.6, opacity: 0, filter: 'blur(14px)', duration: .7, ease: 'expo.out' }, at + .25)
    .from(el.querySelector('.cname'), { y: 30, opacity: 0, duration: .5, ease: 'expo.out' }, at + .6).to(el.querySelector('.cy'), { scale: 1.06, duration: dur - 1, ease: 'sine.inOut' }, at + .9)
    .to(el, { opacity: 0, duration: .35, ease: 'power2.in' }, at + dur - .35);
  return el;
};

/* ---------------- list panel (e.g. declarations of war) ---------------- */
CM.list = function (parent, tl, items, { x = 1180, y = 200, w = 680, end } = {}) {
  const box = document.createElement('div'); box.style.cssText = `position:absolute;left:${x}px;top:${y}px;width:${w}px;z-index:5`; parent.append(box);
  items.forEach(([at, date, text]) => { const r = document.createElement('div'); r.style.cssText = 'display:flex;gap:18px;align-items:center;margin-bottom:14px;padding:12px 18px;border-radius:14px;background:rgb(6 12 28 / .8);border-left:6px solid #FFD23F';
    r.innerHTML = `<div style="font:400 44px/1 'Bebas Neue';color:#FFD23F;min-width:120px">${date}</div><div style="font:700 28px/1.2 Inter">${text}</div>`; box.append(r);
    tl.from(r, { x: 60, opacity: 0, duration: .35, ease: 'expo.out' }, at); });
  if (end) tl.to(box, { opacity: 0, duration: .25 }, end); return box;
};

/* ---------------- captions for 16:9 (bottom band) ---------------- */
CM.captions = function (words, off = 0) {
  const ws = words.map(w => ({ text: w.word, start: w.start + off, end: w.end + off }));
  const phrases = [[]];
  ws.forEach((w, i) => { const cur = phrases.at(-1), prev = ws[i - 1];
    if (cur.length && (cur.length === 6 || cur.map(x => x.text).join(' ').length + w.text.length > 34 || w.start - prev.end > .3 || /[.!?,:;…»]$/.test(prev.text) || /^[¿«]/.test(w.text))) phrases.push([]);
    phrases.at(-1).push(w); });
  const tl = gm.timeline(null, { global: true }), box = document.getElementById('caps');
  const caps = phrases.map(ph => { const el = document.createElement('div'); el.className = 'cap'; el.innerHTML = '<i class="pill"></i>' + ph.map(w => `<span class="w">${w.text}</span>`).join(' '); box.append(el); return el; });
  return document.fonts.ready.then(() => phrases.forEach((ph, p) => {
    const el = caps[p], spans = el.querySelectorAll('.w'), pill = el.querySelector('.pill'), next = phrases[p + 1];
    const bx = i => ({ x: spans[i].offsetLeft, width: spans[i].offsetWidth });
    tl.fromTo(el, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: .15 }, ph[0].start - .08).fromTo(pill, { ...bx(0), opacity: 0 }, { opacity: 1, duration: .12 }, ph[0].start - .04);
    ph.forEach((w, i) => { if (i) tl.to(pill, { ...bx(i), duration: .1, ease: 'power3.out' }, w.start - .06);
      tl.to(spans[i], { '--hl': 1, duration: .05 }, w.start - .03).to(spans[i], { '--hl': 0, duration: .05 }, ph[i + 1] ? ph[i + 1].start - .06 : w.end + .25); });
    tl.to(el, { opacity: 0, duration: .1 }, next ? next[0].start - .2 : ph.at(-1).end + .6);
  }));
};
CM.W = function (words, off = 0) {
  const norm = s => s.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');
  return (txt, n = 1) => { let c = 0; for (const w of words) if (norm(w.word) === norm(txt) && ++c === n) return w.start + off; throw new Error('word not found: ' + txt + ' #' + n); };
};
})();
