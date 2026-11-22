"""Corto 14: disculpa por 4 días sin vídeo. uso: python3 produccion/gen_corto_14.py"""
import sys
R = '/home/user/curiosimundo-animation/'; sys.path.insert(0, R + 'tools')
from corto import corto
corto(R + 'produccion/14-disculpa', 'CURIOSIMUNDO · 14 · Disculpa por 4 días sin vídeo', ['space.js', 'egypt.js'],
 [('s0', 0), ('s1', 'perdón'), ('sg', 'verdad'), ('s2', 'preparé'), ('s3', 'planeta'), ('s4', 'historia'), ('s5', 'vuelven')],
 [(0, '<em>4</em> DÍAS'), ('vídeo', 'SIN <em>VÍDEOS</em>'), ('disculpa', 'TE DEBEMOS UNA<br><em>DISCULPA</em>'), ('perdón', '<em>PERDÓN</em>'), ('jugando', 'ME QUEDÉ JUGANDO<br><em>GTA VI</em>'), ('confieso', 'LO <em>CONFIESO</em>'), ('partida', 'ENTRE PARTIDA<br>Y <em>PARTIDA</em>…'), ('parado', 'NO ESTUVE<br><em>PARADO</em>'),
  ('grande', 'ALGO <em>GRANDE</em>'), ('sol', '¿Y SI EL SOL<br>SE <em>APAGARA</em>?'), ('planeta', '<em>VENUS</em>'), ('historia', '<em>CLEOPATRA</em>'), ('vuelven', '¡<em>VOLVEMOS</em>!'), ('gracias', '<em>GRACIAS</em>')],
 r'''
  const NIGHT = 'radial-gradient(1200px 1400px at 50% 40%, #0f1a3a, #03050d 75%)';
  const b0 = scene('s0'); mk('rect', { width: 1920, height: 1080, fill: '#0e2a5a' }, b0);
  const days = [0, 1, 2, 3].map(k => { const x = 300 + k * 440, g = mk('g', {}, b0); mk('rect', { x: x - 170, y: 260, width: 340, height: 420, rx: 30, fill: '#f4efe2' }, g); mk('rect', { x: x - 170, y: 260, width: 340, height: 110, rx: 30, fill: '#E5484D' }, g);
    const t = mk('text', { x, y: 600, 'text-anchor': 'middle', 'font-family': 'Bebas Neue', 'font-size': 220, fill: '#1a2a4a' }, g); t.textContent = k + 1;
    const xx = mk('path', { d: `M${x - 130} 330 L${x + 130} 640 M${x + 130} 330 L${x - 130} 640`, stroke: '#E5484D', 'stroke-width': 30, 'stroke-linecap': 'round' }, g); tl.from(xx, { draw: 0, duration: .25 }, .15 + k * .35); return g; });
  const b1 = scene('s1', NIGHT); SP.stars(b1, 160); const lg = SP.label(b1, 'CURIOSI<tspan fill="#FFD23F">MUNDO</tspan>', 960, 520, 200); const hr = mk('path', { d: 'M960 860 C900 800 820 760 820 700 C820 650 880 630 960 690 C1040 630 1100 650 1100 700 C1100 760 1020 800 960 860Z', fill: '#E5484D' }, b1);
  tl.fromTo(hr, { scale: .8, transformOrigin: '960px 750px' }, { scale: 1.1, duration: .4, yoyo: true, repeat: 7, ease: 'sine.inOut', transformOrigin: '960px 750px' }, S.s1);
  const bg = scene('sg', 'linear-gradient(#1a0a2a, #05030d)'); const lgd = mk('linearGradient', { id: 'gtaSky', x1: 0, y1: 0, x2: 0, y2: 1 }, bg); [['0', '#2a0f4a'], ['.6', '#e0407a'], ['1', '#ffb070']].forEach(([o, c]) => mk('stop', { offset: o, 'stop-color': c }, lgd));
  mk('rect', { x: 360, y: 60, width: 1200, height: 680, rx: 30, fill: '#111', stroke: '#333', 'stroke-width': 10 }, bg); mk('rect', { x: 390, y: 90, width: 1140, height: 620, fill: 'url(#gtaSky)' }, bg);
  mk('circle', { cx: 960, cy: 500, r: 120, fill: '#ffd070', opacity: .9 }, bg); for (let k = 0; k < 9; k++) { const h = 120 + (k * 53) % 200; mk('rect', { x: 400 + k * 125, y: 710 - h, width: 100, height: h, fill: '#1a0a2a' }, bg); }
  EG.palm(bg, 520, 710, .9).querySelectorAll('*').forEach(e => { e.setAttribute('stroke', e.getAttribute('stroke') ? '#1a0a2a' : null); e.setAttribute('fill', e.getAttribute('fill') === 'none' ? 'none' : '#1a0a2a'); }); 
  const gtx = SP.label(bg, 'GTA VI', 960, 300, 200, '#fff'); gtx.setAttribute('stroke', '#e0407a');
  const pad = mk('g', { transform: 'translate(960 900)' }, bg), padi = mk('g', {}, pad); mk('path', { d: 'M-300 -60 Q-300 -120 -200 -120 L200 -120 Q300 -120 300 -60 L340 80 Q350 150 280 150 Q230 150 200 90 L-200 90 Q-230 150 -280 150 Q-350 150 -340 80Z', fill: '#2a2a34', stroke: '#111', 'stroke-width': 6 }, padi);
  [['#5bc0ff', 180, -60], ['#E5484D', 230, -20], ['#5bd08a', 180, 20], ['#FFD23F', 130, -20]].forEach(([c, x, y]) => mk('circle', { cx: x, cy: y, r: 22, fill: c }, padi)); mk('path', { d: 'M-200 -40 h40 v-40 h30 v40 h40 v30 h-40 v40 h-30 v-40 h-40Z', fill: '#111' }, padi);
  tl.to(padi, { y: -12, duration: .12, yoyo: true, repeat: 15, ease: 'sine.inOut' }, S.sg + .3);
  const b2 = scene('s2', NIGHT); SP.stars(b2, 200); const sn = SP.sun(b2, 960, 540, 300); gm.onFrame($('s2'), (l, i) => sn.spin(i.time)); const sh = mk('circle', { cx: 960, cy: 540, r: 0, fill: '#03050d' }, b2); tl.to(sh, { attr: { r: 320 }, duration: 1.4 }, W('apagara') - .3);
  const b3 = scene('s3', 'radial-gradient(1200px 1400px at 50% 40%, #1a1430, #05030d 75%)'); SP.stars(b3, 200); const v = SP.venus(b3, 960, 540, 380); gm.onFrame($('s3'), (l, i) => v.flow(i.time));
  const b4 = scene('s4'); EG.desert(b4); EG.pyramids(b4, 1200, 820, .8); EG.place(EG.person(b4, 'cleo'), 560, 1000, 3.4);
  const b5 = scene('s5', NIGHT); SP.stars(b5, 200); SP.label(b5, 'CURIOSI<tspan fill="#FFD23F">MUNDO</tspan>', 960, 600, 220);
  const sp = Array.from({ length: 36 }, (_, k) => mk('circle', { r: 10, fill: ['#FFD23F', '#E5484D', '#5bc0ff', '#fff'][k % 4] }, b5));
  gm.onFrame($('s5'), (l, i) => { const t = i.time - S.s5; sp.forEach((c, k) => { const a = k / 36 * Math.PI * 2, q = ((t * .6 + (k % 3) * .2) % 1), r = 80 + q * 700; c.setAttribute('cx', 960 + Math.cos(a) * r); c.setAttribute('cy', 540 + Math.sin(a) * r * .6); c.setAttribute('opacity', 1 - q); }); });
''', ('qué', 2), '¿QUÉ TEMA QUIERES<br>QUE <span style="color:#FFD23F">HAGAMOS</span>?',
 [[0, 'grande', 'mourn'], ['grande', 'vuelven', 'tension_up'], ['vuelven', 99, 'end']], hits=['perdón', 'vuelven'])
