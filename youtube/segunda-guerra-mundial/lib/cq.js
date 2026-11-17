/* CURIOSIMUNDO · La conquista de México · escenas horizontales (1920×1080) sobre cm.js */
(function () {
const mk = CM.mk, CQ = window.CQ = {};
/* Tenochtitlan on the lake: volcanoes, twin-temple Templo Mayor, houses, chinampas, causeway, canoes */
CQ.city = function (svg, { sky = ['#9cc4e6', '#efe2bf'], dusk = false, causeway = true, temple = true, y0 = 0 } = {}) {
  const g = mk('g', {}, svg), id = 'cqs' + Math.round(Math.random() * 1e9);
  const lg = mk('linearGradient', { id, x1: 0, y1: 0, x2: 0, y2: 1 }, mk('defs', {}, g)); mk('stop', { offset: 0, 'stop-color': sky[0] }, lg); mk('stop', { offset: 1, 'stop-color': sky[1] }, lg);
  mk('rect', { width: 1920, height: 1080, fill: `url(#${id})` }, g);
  mk('path', { d: 'M-100 560 L260 250 L600 560Z', fill: dusk ? '#4a3a5a' : '#6f7f99' }, g); mk('path', { d: 'M200 330 L260 250 L325 335 Q262 318 200 330Z', fill: '#f2f4f7' }, g);
  mk('path', { d: 'M1300 560 L1580 300 L1700 330 L1980 560Z', fill: dusk ? '#4a3a5a' : '#6f7f99' }, g); mk('path', { d: 'M1520 355 L1580 300 L1700 330 L1660 360 Q1590 345 1520 355Z', fill: '#f2f4f7' }, g);
  mk('rect', { y: 540 + y0, width: 1920, height: 600, fill: '#3f86b4' }, g);
  for (let i = 0; i < 12; i++) mk('rect', { x: -40 + i * 170, y: 560 + y0 + (i % 3) * 18, width: 140, height: 28, rx: 6, fill: '#5e8f3e' }, g);
  for (let i = 0; i < 24; i++) { const x = 20 + i * 80, y = 620 + y0 + (i % 2) * 14; mk('rect', { x, y, width: 70, height: 42, fill: '#e4d6b8' }, g); mk('rect', { x: x - 3, y: y - 6, width: 76, height: 8, fill: '#c9b48c' }, g); }
  if (temple) { const py = mk('g', {}, g); [[700, 640, 520], [740, 575, 440], [780, 510, 360], [820, 445, 280]].forEach(([x, y, w]) => mk('rect', { x, y: y + y0, width: w, height: 68, fill: '#d8c8a2', stroke: '#b7a37a', 'stroke-width': 3 }, py));
    mk('path', { d: `M920 ${700 + y0} L960 ${440 + y0} L1000 ${700 + y0}Z`, fill: '#c9b48c' }, py); mk('rect', { x: 830, y: 385 + y0, width: 100, height: 60, fill: '#c0392b' }, py); mk('rect', { x: 990, y: 385 + y0, width: 100, height: 60, fill: '#1f6fb0' }, py);
    mk('path', { d: `M826 ${385 + y0} L880 ${352 + y0} L934 ${385 + y0}Z`, fill: '#8f2a20' }, py); mk('path', { d: `M986 ${385 + y0} L1040 ${352 + y0} L1094 ${385 + y0}Z`, fill: '#174f80' }, py); }
  if (causeway) mk('path', { d: `M-20 ${880 + y0} L700 ${720 + y0} L760 ${730 + y0} L60 ${910 + y0}Z`, fill: '#bfa77c' }, g);
  const canoes = [0, 1, 2, 3, 4].map(i => { const c = mk('g', {}, g); mk('path', { d: 'M-60 0 L60 0 L44 16 L-44 16Z', fill: '#6b4a2a' }, c); mk('rect', { x: -5, y: -40, width: 10, height: 40, fill: '#a8714a' }, c); mk('circle', { cy: -48, r: 10, fill: '#a8714a' }, c); return c; });
  const tick = t => canoes.forEach((c, i) => c.setAttribute('transform', `translate(${(160 + i * 420 + t * (20 + i * 6)) % 2040 - 60} ${840 + y0 + (i % 3) * 70})`));
  tick(0); return { g, canoes, tick };
};
/* beach with sea and ships */
CQ.coast = function (svg, { n = 5, sky = ['#8fb8de', '#f0d9a8'] } = {}) {
  const g = mk('g', {}, svg), id = 'cqc' + Math.round(Math.random() * 1e9);
  const lg = mk('linearGradient', { id, x1: 0, y1: 0, x2: 0, y2: 1 }, mk('defs', {}, g)); mk('stop', { offset: 0, 'stop-color': sky[0] }, lg); mk('stop', { offset: 1, 'stop-color': sky[1] }, lg);
  mk('rect', { width: 1920, height: 1080, fill: `url(#${id})` }, g); mk('rect', { y: 520, width: 1920, height: 560, fill: '#2f6aa0' }, g);
  mk('path', { d: 'M-20 1080 L-20 760 Q700 700 1300 820 Q1700 880 1940 860 L1940 1080Z', fill: '#e2cf9e' }, g);
  for (let i = 0; i < 6; i++) mk('circle', { cx: 80 + i * 60, cy: 700 - (i % 2) * 20, r: 60, fill: '#3f7a3a' }, g);
  const ships = Array.from({ length: n }, (_, i) => { const s = mk('g', {}, g); CM.caravel(s); s.setAttribute('transform', `translate(${900 + i * 200} ${560 + (i % 2) * 40}) scale(${.45 + (i % 2) * .1})`); return s; });
  return { g, ships };
};
/* woman in huipil (for Malintzin and civilians) */
CQ.woman = function (parent, x, y, s = 1, { huipil = '#f2ead6', band = '#c0392b', dir = 1 } = {}) {
  const g = mk('g', { transform: `translate(${x} ${y}) scale(${s * dir} ${s})` }, parent);
  mk('path', { d: 'M-24 -150 Q0 -158 24 -150 L34 0 L-34 0Z', fill: huipil }, g); mk('rect', { x: -26, y: -120, width: 52, height: 12, fill: band }, g); mk('rect', { x: -32, y: -40, width: 64, height: 10, fill: band }, g);
  mk('path', { d: 'M-14 -186 Q2 -196 16 -184 L18 -140 L-16 -140Z', fill: '#1a1410' }, g); mk('circle', { cx: 3, cy: -166, r: 13, fill: '#a8714a' }, g); mk('circle', { cx: 10, cy: -168, r: 1.8, fill: '#1a1410' }, g);
  return g;
};
/* march a group across a scene: list of {f, x0, y, s}; call in onFrame */
CQ.walk = (items, t, t0, sp = 90, dir = 1) => items.forEach((o, i) => CM.pose(o.f, { x: o.x0 + dir * (t - t0) * sp, y: o.y, s: o.s, dir, run: .35, ph: t * 6 + i }));
/* memorial card for massacres: dim scene, text only, no violence */
CQ.memorial = function (sec, date, place, line, tl, at, W) {
  sec.style.background = 'radial-gradient(circle at 50% 50%, #2a2420, #0a0806 75%)';
  const d = CM.text(sec, 'mid', date, 300, 'color:#FFD23F'), p = CM.text(sec, 'big', place, 380, 'font-size:150px'), l = CM.text(sec, 'mid', line, 620, 'font-size:40px;text-transform:none;letter-spacing:0');
  tl.from([d, p, l], { opacity: 0, y: 20, duration: .6, stagger: .3 }, at); return [d, p, l];
};
})();
