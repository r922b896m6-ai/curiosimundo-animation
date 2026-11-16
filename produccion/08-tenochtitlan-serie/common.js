/* CURIOSIMUNDO · serie "El soldado en Tenochtitlan" · helpers comunes (vertical 1080×1920) */
window.S = (function () {
  const mk = CM.mk, $ = id => document.getElementById(id), G = { global: true };
  const sv = (id, bg) => { const s = mk('svg', { viewBox: '0 0 1080 1920', width: 1080, height: 1920, style: 'position:absolute;inset:0' }, $(id)); CM.defs(s); if (bg) $(id).style.background = bg; return s; };
  function titles(tl, T, dur) {
    T.forEach(([at, html], i) => { const h = Object.assign(document.createElement('div'), { className: 'ttl', innerHTML: '<div>' + html + '</div>' }); $('titles').append(h); if (!html) return;
      const end = T[i + 1] ? T[i + 1][0] : 99;
      if (at === 0) { h.style.opacity = 1; tl.fromTo(h, { scale: 1.15 }, { scale: 1, duration: .5, ease: 'expo.out' }, 0); }
      else tl.fromTo(h, { opacity: 0, y: 90, scale: 1.2, filter: 'blur(10px)' }, { opacity: 1, y: 0, scale: 1, filter: 'blur(0px)', duration: .3, ease: 'expo.out' }, at);
      if (end < dur) tl.to(h, { opacity: 0, y: -80, duration: .18, ease: 'power2.in' }, end - .18); }); }
  /* the city: lake, causeway, twin-temple pyramid, houses, canoes, volcanoes */
  const city = (s, sc = 1, oy = 0) => { const g = mk('g', { transform: `translate(540 ${oy}) scale(${sc}) translate(-540 0)` }, s);
    mk('path', { d: 'M-200 760 L120 470 L330 760Z M700 760 L930 430 L1200 760Z', fill: '#6f7f99' }, g); mk('path', { d: 'M880 500 L930 430 L985 505 Q930 490 880 500Z', fill: '#f2f4f7' }, g);
    mk('rect', { x: -200, y: 740, width: 1480, height: 1400, fill: '#3f86b4' }, g);
    for (let i = 0; i < 9; i++) mk('rect', { x: -60 + i * 140, y: 760 + (i % 3) * 22, width: 120, height: 34, rx: 6, fill: '#5e8f3e' }, g);
    for (let i = 0; i < 14; i++) { const x = 40 + i * 74, y = 840 + (i % 2) * 18; mk('rect', { x, y, width: 64, height: 40, fill: '#e4d6b8' }, g); mk('rect', { x: x - 3, y: y - 6, width: 70, height: 8, fill: '#c9b48c' }, g); }
    const py = mk('g', {}, g); [[300, 780, 480], [340, 720, 400], [380, 660, 320], [420, 600, 240]].forEach(([x, y, w]) => mk('rect', { x, y, width: w, height: 64, fill: '#d8c8a2', stroke: '#b7a37a', 'stroke-width': 3 }, py));
    mk('path', { d: 'M520 840 L560 600 L600 840Z', fill: '#c9b48c' }, py); mk('rect', { x: 430, y: 548, width: 84, height: 54, fill: '#c0392b' }, py); mk('rect', { x: 566, y: 548, width: 84, height: 54, fill: '#1f6fb0' }, py);
    mk('path', { d: 'M426 548 L472 520 L518 548Z', fill: '#8f2a20' }, py); mk('path', { d: 'M562 548 L608 520 L654 548Z', fill: '#174f80' }, py);
    mk('rect', { x: -200, y: 900, width: 1480, height: 40, fill: '#bfa77c' }, g);
    const canoes = [0, 1, 2].map(i => { const c = mk('g', {}, g); mk('path', { d: 'M-50 0 L50 0 L36 14 L-36 14Z', fill: '#6b4a2a' }, c); mk('rect', { x: -4, y: -36, width: 8, height: 36, fill: '#a8714a' }, c); mk('circle', { cy: -42, r: 9, fill: '#a8714a' }, c); return c; });
    return { g, canoes }; };

  function captions(words) {
  /* vertical captions */
  const ws = words.map(w => ({ text: w.word, start: w.start, end: w.end })), ph = [[]];
  ws.forEach((w, i) => { const cur = ph.at(-1), prev = ws[i - 1];
    if (cur.length && (cur.length === 3 || cur.map(x => x.text).join(' ').length + w.text.length > 16 || w.start - prev.end > .28 || /[.!?,:…]$/.test(prev.text) || /^¿/.test(w.text))) ph.push([]);
    ph.at(-1).push(w); });
  const ct = gm.timeline(null, G), els = ph.map(p => { const el = document.createElement('div'); el.className = 'vc'; el.innerHTML = '<i class="pl"></i>' + p.map(w => `<span class="w">${w.text}</span>`).join(' '); $('vcaps').append(el); return el; });
  return document.fonts.ready.then(() => ph.forEach((p, k) => {
    const el = els[k], sp = el.querySelectorAll('.w'), pl = el.querySelector('.pl'), nx = ph[k + 1], bx = i => ({ x: sp[i].offsetLeft, width: sp[i].offsetWidth });
    ct.fromTo(pl, { ...bx(0), scale: .5, opacity: 0 }, { scale: 1, opacity: 1, duration: .16, ease: 'back.out(2)' }, p[0].start - .04);
    p.forEach((w, i) => { ct.fromTo(sp[i], { opacity: 0, y: 40, scale: .6 }, { opacity: 1, y: 0, scale: 1, duration: .22, ease: 'back.out(2.4)' }, w.start - .06);
      if (i) ct.to(pl, { ...bx(i), duration: .1, ease: 'power3.out' }, w.start - .08);
      ct.to(sp[i], { '--hl': 1, duration: .05 }, w.start - .03).to(sp[i], { '--hl': 0, duration: .05 }, p[i + 1] ? p[i + 1].start - .08 : Math.min(w.end + .3, nx ? nx[0].start - .2 : 99)); });
    ct.to(el, { opacity: 0, duration: .12 }, nx ? nx[0].start - .18 : p.at(-1).end + .7);
  }));

  }
  /* part badge, top-left */
  function badge(txt) { const d = document.createElement('div'); d.style.cssText = "position:absolute;left:40px;top:150px;z-index:7;font:400 44px/1 'Bebas Neue';letter-spacing:.08em;color:#111;background:#FFD23F;padding:8px 16px;border-radius:10px"; d.textContent = txt; document.body.append(d); }
  return { mk, $, G, sv, titles, city, captions, badge };
})();
