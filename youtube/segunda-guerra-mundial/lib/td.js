/* CURIOSIMUNDO · tardígrados: dibujo del oso de agua (andando) y del tonel (tun) */
(function () {
const mk = CM.mk, TD = window.TD = {};
/* tardigrade facing right, feet at y=0, ~420 units long; returns {g, legs, setWalk(t, k)} */
TD.bear = function (parent, { body = '#efcfae', line = '#b07e5a', glow = false } = {}) {
  const g = mk('g', {}, parent), legs = [];
  const legX = [-150, -55, 40, 130];
  const legG = mk('g', {}, g);
  legX.forEach((x, i) => { const l = mk('g', { transform: `translate(${x} -70)` }, legG);
    mk('path', { d: 'M-24 0 Q-30 46 -14 62 L16 62 Q30 46 24 0Z', fill: body, stroke: line, 'stroke-width': 5 }, l);
    [-12, 0, 12].forEach(c => mk('path', { d: `M${c} 60 q-6 14 -16 16`, fill: 'none', stroke: '#3a2a1a', 'stroke-width': 4, 'stroke-linecap': 'round' }, l)); legs.push(l); });
  const b = mk('g', {}, g);
  mk('path', { d: 'M-210 -110 Q-230 -190 -140 -215 Q0 -250 140 -215 Q215 -190 225 -120 Q235 -60 160 -55 L-150 -55 Q-215 -60 -210 -110Z', fill: body, stroke: line, 'stroke-width': 6 }, b);
  [-120, -40, 40, 120].forEach(x => mk('path', { d: `M${x} -228 Q${x + 18} -140 ${x} -58`, fill: 'none', stroke: line, 'stroke-width': 3, opacity: .55 }, b));
  mk('path', { d: 'M222 -120 q22 -4 30 8 q-8 12 -30 8z', fill: '#d9a98a', stroke: line, 'stroke-width': 4 }, b);
  mk('circle', { cx: 190, cy: -160, r: 7, fill: '#2a1a12' }, b); mk('circle', { cx: 192, cy: -162, r: 2.5, fill: '#fff' }, b);
  for (let i = 0; i < 9; i++) mk('circle', { cx: -170 + i * 40, cy: -150 + (i % 3) * 22, r: 9 + (i % 2) * 4, fill: '#7fae6a', opacity: .35 }, b);
  if (glow) mk('ellipse', { cx: 0, cy: -140, rx: 300, ry: 170, fill: 'rgb(255 255 255 / .08)' }, g, true);
  const setWalk = (t, k = 1) => legs.forEach((l, i) => l.setAttribute('transform', `translate(${legX[i]} -70) rotate(${Math.sin(t * 7 + i * 1.7) * 18 * k})`));
  return { g, legs, b, setWalk };
};
/* tun: dried barrel */
TD.tun = function (parent, { body = '#c9a07a', line = '#8a6040' } = {}) {
  const g = mk('g', {}, parent);
  mk('path', { d: 'M-150 -60 Q-160 -150 -60 -165 Q60 -175 140 -140 Q175 -95 150 -40 Q110 0 0 0 Q-130 2 -150 -60Z', fill: body, stroke: line, 'stroke-width': 6 }, g);
  for (let i = 0; i < 6; i++) mk('path', { d: `M${-110 + i * 45} -160 Q${-100 + i * 45} -80 ${-112 + i * 45} -6`, fill: 'none', stroke: line, 'stroke-width': 3, opacity: .7 }, g);
  mk('path', { d: 'M-120 -110 q30 -10 60 2 M20 -130 q30 6 50 -4 M-60 -50 q40 -8 70 4', fill: 'none', stroke: line, 'stroke-width': 3, opacity: .6 }, g);
  return g;
};
/* microscope disc: circular viewport with blurry edge */
TD.scope = function (svg, cx = 960, cy = 540, r = 420, color = '#d8e6c8') {
  const id = 'tdclip' + Math.round(Math.random() * 1e9), d = mk('defs', {}, svg); const cp = mk('clipPath', { id }, d); mk('circle', { cx, cy, r }, cp);
  mk('rect', { width: 1920, height: 1080, fill: '#0b0f14' }, svg); const inner = mk('g', { 'clip-path': `url(#${id})` }, svg); mk('circle', { cx, cy, r, fill: color }, inner);
  for (let i = 0; i < 14; i++) mk('circle', { cx: cx - r + gm.random('sb' + i) * 2 * r, cy: cy - r + gm.random('sc' + i) * 2 * r, r: 20 + gm.random('sd' + i) * 60, fill: '#9fbf86', opacity: .35 }, inner);
  mk('circle', { cx, cy, r: r + 6, fill: 'none', stroke: '#1a2028', 'stroke-width': 24 }, svg); return inner;
};
/* moss clump */
TD.moss = function (svg, x, y, s = 1, n = 18) { const g = mk('g', { transform: `translate(${x} ${y}) scale(${s})` }, svg);
  for (let i = 0; i < n; i++) { const a = -Math.PI / 2 + (i - n / 2) * .12, l = 70 + gm.random('ml' + i + x) * 60; mk('path', { d: `M${(i - n / 2) * 8} 0 q${Math.cos(a) * l * .3} ${-l * .6} ${Math.cos(a) * l * .5} ${-l}`, stroke: ['#3f7a3a', '#5e9a42', '#2f6a2a'][i % 3], 'stroke-width': 10, 'stroke-linecap': 'round', fill: 'none' }, g); }
  return g; };
})();
