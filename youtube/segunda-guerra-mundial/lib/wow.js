/* CURIOSIMUNDO · la señal Wow!: Big Ear, tira impresa, curva de intensidad, espectro */
(function () {
const mk = CM.mk, WOW = window.WOW = {};
/* Big Ear in perspective on a green field (1920x1080 space) */
WOW.bigEar = function (svg, { y0 = 560 } = {}) { const g = mk('g', {}, svg);
  mk('path', { d: `M300 ${y0 + 360} L1620 ${y0 + 360} L1380 ${y0 + 60} L540 ${y0 + 60}Z`, fill: '#c9d2dc', stroke: '#8a96a4', 'stroke-width': 4 }, g);
  for (let i = 1; i < 8; i++) mk('line', { x1: 300 + i * 165, y1: y0 + 360, x2: 540 + i * 105, y2: y0 + 60, stroke: '#aab4c0', 'stroke-width': 2 }, g);
  mk('path', { d: `M520 ${y0 + 70} L1400 ${y0 + 70} L1360 ${y0 - 160} L560 ${y0 - 160}Z`, fill: '#9aa6b4', stroke: '#6a7684', 'stroke-width': 5 }, g);
  for (let i = 0; i < 9; i++) mk('line', { x1: 560 + i * 100, y1: y0 - 160, x2: 520 + i * 110, y2: y0 + 70, stroke: '#7d8996', 'stroke-width': 3 }, g);
  mk('path', { d: `M260 ${y0 + 380} Q960 ${y0 + 110} 1660 ${y0 + 380} L1660 ${y0 + 420} Q960 ${y0 + 160} 260 ${y0 + 420}Z`, fill: '#8a96a4' }, g);
  const horns = [880, 1040].map(x => { const h = mk('g', {}, g); mk('path', { d: `M${x - 30} ${y0 + 220} L${x + 30} ${y0 + 220} L${x + 14} ${y0 + 160} L${x - 14} ${y0 + 160}Z`, fill: '#5a6470' }, h); mk('rect', { x: x - 6, y: y0 + 220, width: 12, height: 60, fill: '#3a4450' }, h); return h; });
  return { g, horns };
};
/* the printout: columns of characters; the Wow column with 6EQUJ5 */
WOW.printout = function (sec, { top = 140, left = 560, w = 800, h = 820, rows = 22 } = {}) {
  const d = document.createElement('div'); d.style.cssText = `position:absolute;left:${left}px;top:${top}px;width:${w}px;height:${h}px;background:#f4f1e6;box-shadow:0 20px 60px rgb(0 0 0 / .5);overflow:hidden;font:700 34px/1.12 'Courier New',monospace;color:#2a2a3a;padding:20px 30px;box-sizing:border-box`;
  for (let i = 0; i < 6; i++) { const hole = document.createElement('div'); hole.style.cssText = `position:absolute;left:8px;top:${30 + i * 140}px;width:14px;height:14px;border-radius:50%;background:#c9c3b0`; d.append(hole); const h2 = hole.cloneNode(); h2.style.left = 'auto'; h2.style.right = '8px'; d.append(h2); }
  const wowCol = 3, wowStart = 8, wowSeq = '6EQUJ5'; let html = '';
  for (let r = 0; r < rows; r++) { let line = ''; for (let c = 0; c < 9; c++) { let ch = gm.random('p' + r + '_' + c) < .7 ? '1' : (gm.random('q' + r + c) < .5 ? '2' : ' ');
      if (c === wowCol && r >= wowStart && r < wowStart + 6) ch = `<span class="wc" style="color:#2a2a3a">${wowSeq[r - wowStart]}</span>`; line += ch + '  '; } html += line + '\n'; }
  const pre = document.createElement('pre'); pre.style.cssText = 'margin:0 0 0 20px;font:inherit;white-space:pre'; pre.innerHTML = html; d.append(pre);
  const ring = document.createElement('div'); ring.style.cssText = `position:absolute;left:${30 + 20 + wowCol * 61.2 - 16}px;top:${20 + wowStart * 38.1 - 10}px;width:56px;height:${6 * 38.1 + 20}px;border:5px solid #d0312d;border-radius:40px`; d.append(ring);
  const wow = document.createElement('div'); wow.textContent = 'Wow!'; wow.style.cssText = `position:absolute;left:${30 + wowCol * 61.2 + 70}px;top:${20 + wowStart * 38.1 + 60}px;font:italic 800 76px/1 Georgia,serif;color:#d0312d;transform:rotate(-8deg)`; d.append(wow);
  sec.append(d); return { d, ring, wow };
};
/* intensity curve: 6 E Q U J 5 */
WOW.curve = function (svg, x0 = 460, y0 = 880, sx = 160, sy = 20) { const g = mk('g', {}, svg), vals = [6, 14, 26, 30, 19, 5], labs = '6EQUJ5';
  mk('line', { x1: x0 - 60, y1: y0, x2: x0 + sx * 6, y2: y0, stroke: '#9fb3c8', 'stroke-width': 4 }, g);
  const bars = vals.map((v, i) => { const r = mk('rect', { x: x0 + i * sx, y: y0 - v * sy, width: sx * .7, height: v * sy, rx: 10, fill: i === 3 ? '#FFD23F' : '#5bc0ff' }, g); const t = mk('text', { x: x0 + i * sx + sx * .35, y: y0 + 70, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 70, fill: '#fff' }, g); t.textContent = labs[i]; return r; });
  return { g, bars };
};
/* spectrum with a narrow spike */
WOW.spectrum = function (svg, x0 = 200, y0 = 800, w = 1520) { const g = mk('g', {}, svg); let d = `M${x0} ${y0}`; for (let x = 0; x <= w; x += 8) { const n = (gm.random('n' + x) - .5) * 40; d += ` L${x0 + x} ${y0 - 40 + n}`; }
  const noise = mk('path', { d, stroke: '#5bc0ff', 'stroke-width': 4, fill: 'none' }, g); const spike = mk('path', { d: `M${x0 + w / 2 - 6} ${y0 - 40} L${x0 + w / 2} ${y0 - 520} L${x0 + w / 2 + 6} ${y0 - 40}`, stroke: '#FFD23F', 'stroke-width': 8, fill: 'none' }, g);
  const t = mk('text', { x: x0 + w / 2, y: y0 + 70, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 64, fill: '#FFD23F' }, g); t.textContent = '1420 MHz'; return { g, spike, noise };
};
WOW.stars = (s, n = 120, w = 1920, h = 1080) => { for (let i = 0; i < n; i++) mk('circle', { cx: gm.random('sx' + i) * w, cy: gm.random('sy' + i) * h, r: .8 + gm.random('sr' + i) * 2.5, fill: '#fff', opacity: .25 + gm.random('so' + i) * .7 }, s); };
})();
