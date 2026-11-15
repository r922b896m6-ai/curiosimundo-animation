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
  US:   { name: 'ESTADOS UNIDOS', tunic: '#6b6a3f', pants: '#625f38', legs: '#b8a77c', boots: '#2a1f14', hat: 'brodie', hatC: '#55553a', belt: '#a99a6a', pack: '#6b6a3f', flag: 'US' },
};
const SKIN = '#d9a77c';
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
    case 'slouch': mk('path', { d: 'M-10 -152 Q3 -170 16 -152Z', fill: c }, g); mk('path', { d: 'M-30 -152 Q3 -158 34 -151 Q3 -147 -30 -152Z', fill: c }, g); mk('path', { d: 'M-12 -152 L-16 -168 L-6 -160Z', fill: c }, g); break;
  }
}
/* figure: feet at (0,0), facing right; returns parts so poses can be animated each frame */
CM.figure = function (parent, nation, opts = {}) {
  const u = U[nation], o = mk('g', {}, parent), b = mk('g', {}, o);
  const legL = mk('g', { transform: 'translate(-8 -84)' }, b), legR = mk('g', { transform: 'translate(8 -84)' }, b);
  for (const lg of [legL, legR]) { mk('path', { d: 'M-9 0 L-7 70 L7 70 L9 0Z', fill: u.pants }, lg); mk('rect', { x: -8, y: 40, width: 15, height: 32, fill: u.legs }, lg); mk('path', { d: 'M-9 70 h18 l6 8 h-24z', fill: u.boots }, lg); }
  if (opts.pack !== false) mk('rect', { x: -38, y: -148, width: 17, height: 52, rx: 6, fill: u.pack }, b);
  if (u.roll) mk('path', { d: 'M-22 -150 Q0 -126 22 -96', stroke: u.roll, 'stroke-width': 9, fill: 'none' }, b);
  mk('path', { d: 'M-21 -150 Q0 -156 21 -150 L25 -82 L-25 -82 Z', fill: u.tunic }, b);
  if (nation === 'FR14') mk('path', { d: 'M-25 -84 L-28 -60 L28 -60 L25 -84Z', fill: u.tunic }, b);     // greatcoat skirt
  mk('rect', { x: -24, y: -104, width: 48, height: 7, fill: u.belt }, b);
  if (u.hat === 'brodie' || u.hat === 'cap' || u.hat === 'slouch') mk('path', { d: 'M-18 -148 L19 -104', stroke: u.belt, 'stroke-width': 5 }, b);
  mk('circle', { cx: 3, cy: -162, r: 13, fill: SKIN }, b); mk('circle', { cx: 10, cy: -164, r: 1.8, fill: '#2a1f14' }, b);
  hat(b, u);
  if (opts.mask) { mk('path', { d: 'M-10 -176 Q20 -178 20 -150 Q18 -138 0 -140 Q-14 -150 -10 -176Z', fill: '#59604a' }, b); mk('circle', { cx: 12, cy: -164, r: 6, fill: '#bcd0c6', stroke: '#2f3426', 'stroke-width': 2 }, b);
    mk('path', { d: 'M14 -150 l14 12 l-6 8 l-14 -10z', fill: '#3d4234' }, b); }
  const arm = mk('g', { transform: 'translate(6 -140)' }, b);
  const weapon = opts.weapon || 'rifle';
  if (weapon === 'rifle') { mk('path', { d: 'M-8 26 L56 -6', stroke: '#6b4a2a', 'stroke-width': 7, 'stroke-linecap': 'round' }, arm); mk('path', { d: 'M50 -3 L92 -24', stroke: '#3a3a3a', 'stroke-width': 4, 'stroke-linecap': 'round' }, arm);
    if (opts.bayonet !== false) mk('path', { d: 'M90 -23 L112 -34', stroke: '#c9c2b0', 'stroke-width': 3, 'stroke-linecap': 'round' }, arm); }
  if (weapon === 'shovel') { mk('path', { d: 'M0 0 L60 0', stroke: '#6b5236', 'stroke-width': 7, 'stroke-linecap': 'round' }, arm); mk('path', { d: 'M58 -12 L86 -9 L88 12 L58 14 Z', fill: '#8e8f86' }, arm); }
  if (weapon === 'club') { mk('path', { d: 'M10 0 L58 0', stroke: '#6b5236', 'stroke-width': 8, 'stroke-linecap': 'round' }, arm); mk('rect', { x: 54, y: -11, width: 30, height: 24, rx: 8, fill: '#4a3826' }, arm); }
  if (weapon === 'grenade') { mk('path', { d: 'M0 0 L40 -6', stroke: '#6b5236', 'stroke-width': 6 }, arm); mk('rect', { x: 36, y: -14, width: 14, height: 20, rx: 3, fill: '#4a4a40' }, arm); }
  const sleeve = mk('path', { d: 'M-4 -7 L34 4 L32 14 L-6 8 Z', fill: u.tunic }, arm); mk('circle', { cx: 36, cy: 10, r: 6, fill: SKIN }, arm);
  if (weapon === 'fist') mk('circle', { cx: 40, cy: 10, r: 9, fill: SKIN }, arm);
  const flash = mk('circle', { cx: 116, cy: -36, r: 22, fill: 'url(#cmFlash)', opacity: 0 }, arm);
  return { o, b, legL, legR, arm, flash, nation };
};
/* run cycle / pose helpers (call every frame) */
CM.pose = function (f, { x = 0, y = 0, s = 1, dir = 1, run = 0, ph = 0, lean = 0, armRot = 0, fall = 0 }) {
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
  if (T.trees) for (let i = 0; i < 14; i++) { const x = 120 + i * 220 + gm.random('tr' + i) * 80; mk('rect', { x: x - 8, y: GY - 160, width: 16, height: 160, fill: '#2a2017' }, world); mk('circle', { cx: x, cy: GY - 180, r: 70, fill: '#2f4a24' }, world); }
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
  const M = cfg.melee, MP = M ? (M.weapons || ['rifle', 'club', 'shovel']).map((wp, i) => ({ a: CM.figure(soldiers, A, { weapon: wp, pack: false }), d: CM.figure(soldiers, D, { weapon: i % 2 ? 'rifle' : 'fist', pack: false }),
    x: toX - dirA * (560 - i * 260), y: GY + 30 + (i % 2) * 40, at: M.at + i * (M.step || .9) })) : [];
  const stars = MP.map(() => mk('use', { href: '#cmStar' }, fx));
  // labels with flags
  const tags = mk('g', {}, svg);
  if (cfg.labels !== false) [[A, att === 'left' ? 90 : 1430], [D, att === 'left' ? 1430 : 90]].forEach(([nat, x]) => { const g = mk('g', { class: 'btag' }, tags); mk('rect', { x, y: 250, width: 400, height: 76, rx: 14, fill: 'rgb(10 12 20 / .72)' }, g);
    CM.flag(g, U[nat].flag, x + 16, 263, 75, 50); const t = mk('text', { x: x + 106, y: 302, 'font-family': 'Bebas Neue', 'font-size': 46, fill: '#fff' }, g); t.textContent = U[nat].name; });
  const pan = cfg.pan || [0, att === 'left' ? -(W - 1920) : 0];
  const shake = { v: 0 };
  gm.onFrame(section, (l, info) => { const t = info.time, p = gm.clamp((t - t0) / (t1 - t0));
    const camX = pan[0] + (pan[1] - pan[0]) * (.5 - .5 * Math.cos(Math.PI * p)); let sx = 0, sy = 0;
    (cfg.artillery || []).forEach(at => { const d = t - at; if (d >= 0 && d < .45) { const k = (1 - d / .45) * 14; sx += (gm.noise(t * 40) - .5) * 2 * k; sy += (gm.noise(t * 40 + 5) - .5) * 2 * k; } });
    world.setAttribute('transform', `translate(${camX + sx} ${sy})`);
    DEF.forEach((d, i) => { const fire = gm.random('df' + i + ':' + Math.floor(t * 3)) > .55; CM.pose(d.f, { x: d.x, y: d.y, s: SC * .95, dir: -dirA, armRot: -8 }); d.f.flash.setAttribute('opacity', t > t0 && fire && (t * 30 % 4) < 1.5 ? 1 : 0); });
    ATT.forEach(a => { const run = Math.max(0, Math.min(t, a.fall) - a.start), x = a.x0 + dirA * Math.min(run * a.sp, Math.abs(toX - fromX) - 430);
      const fall = t > a.fall ? Math.min(1, (t - a.fall) / .45) : 0, moving = t > a.start && run * a.sp < Math.abs(toX - fromX) - 430 && !fall;
      CM.pose(a.f, { x, y: a.y, s: SC, dir: dirA, run: moving ? 1 : 0, ph: t * 11 + a.ph, lean: moving ? 10 : 0, fall: fall ** 2, armRot: 0 });
      a.f.o.style.display = (MP.length && t > M.at - .3) ? 'none' : ''; });
    ex.forEach(f => f(t));
    TR.forEach((ln, i) => { const k0 = Math.floor(t * 2.4 + i / 6), pp = (t * 2.4 + i / 6) % 1, sx0 = toX, sy0 = GY - 40, tx = fromX + dirA * (200 + gm.random('tx' + i + k0) * 1300), ty = GY - 120 + gm.random('ty' + i + k0) * 160;
      const x1 = sx0 + (tx - sx0) * pp, y1 = sy0 + (ty - sy0) * pp, kk = 90 / Math.hypot(tx - sx0, ty - sy0);
      ln.setAttribute('x1', x1); ln.setAttribute('y1', y1); ln.setAttribute('x2', x1 - (tx - sx0) * kk); ln.setAttribute('y2', y1 - (ty - sy0) * kk); ln.setAttribute('opacity', t > t0 + .3 && (!M || t < M.at) ? .9 : 0); });
    MP.forEach((m, i) => { const on = t > M.at - .3; m.a.o.style.display = m.d.o.style.display = on ? '' : 'none'; if (!on) return;
      const d = t - m.at, lunge = d > 0 && d < .25 ? d / .25 : d >= .25 && d < .6 ? 1 - (d - .25) / .35 : 0, hit = d > .2 && d < .9 ? 1 : 0, swing = (m.a.arm.dataset.w = 1);
      const reel = gm.clamp((d - .2) / .3) * (d < 1.6 ? 1 : Math.max(0, 1 - (d - 1.6) / .4));
      const cyc = (t - m.at) % 2.2, again = cyc > 1.2 && cyc < 1.6 ? (cyc - 1.2) / .4 : 0;
      CM.pose(m.a, { x: m.x - dirA * 90 + dirA * 70 * (lunge + Math.sin(Math.PI * again)), y: m.y, s: SC * 1.05, dir: dirA, armRot: -40 * Math.sin(Math.PI * Math.min(1, d / .3)) * (i % 2) });
      CM.pose(m.d, { x: m.x + dirA * 100 + dirA * 40 * reel, y: m.y, s: SC * 1.05, dir: -dirA, lean: -12 * reel });
      const st = stars[i], sd = d - .22, on2 = sd > 0 && sd < .3; st.setAttribute('opacity', on2 ? 1 - sd / .3 : 0); st.setAttribute('transform', `translate(${m.x + dirA * 20} ${m.y - 170}) scale(${on2 ? .6 + sd * 2.4 : 0})`); });
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
CM.tanks = function (sec, t0, { n = 3, inf = 'UK', planes = false, sky = 'linear-gradient(#7d8792, #c9c0a4)' } = {}) {
  const s = CM.svgIn(sec, sky); mk('rect', { y: 800, width: 1920, height: 280, fill: '#4a3a28' }, s);
  for (let i = 0; i < 10; i++) mk('ellipse', { cx: 100 + i * 200, cy: 860 + (i % 3) * 60, rx: 80, ry: 18, fill: '#3a2c1e' }, s);
  const P = planes ? [CM.plane(s, 'UK'), CM.plane(s, 'FR')] : [];
  const T = Array.from({ length: n }, (_, i) => ({ g: CM.tank(s), x0: -300 - i * 520, y: 820 + (i % 2) * 70, sc: .8 + (i % 2) * .15 }));
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
      tl.from(ring, { scale: 0, duration: .35, ease: 'back.out(2.5)', transformOrigin: `${x}px ${y}px` }, at);
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
