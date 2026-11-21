  const svgOf = (id, bg) => CM.svgIn($(id), bg);
  Object.keys(S).slice(1).forEach(id => tl.from($(id), { opacity: 0, duration: .35 }, S[id]));
  const nxt = id => { const k = Object.keys(S), i = k.indexOf(id); return i + 1 < k.length ? S[k[i + 1]] : D; };
  const hd = (title, sub, at, end) => CM.head(H, tl, title, sub, at, end);
  const big = (id, html, top, at, extra = '', end) => { const t = CM.text($(id), 'big', html, top, extra); tl.from(t, { scale: 1.3, opacity: 0, duration: .4, ease: 'expo.out' }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; };
  const mid = (id, html, top, at, extra = '', end) => { const t = CM.text($(id), 'mid', html, top, extra); tl.from(t, { y: 20, opacity: 0, duration: .35 }, at); if (end) tl.to(t, { opacity: 0, duration: .25 }, end); return t; };
  const stamp = (id, txt, at, top = 420, col = '#E5484D') => { const t = CM.text($(id), 'big', `<span style="border:12px solid ${col};border-radius:20px;padding:0 40px;color:${col}">${txt}</span>`, top, 'font-size:150px;transform:rotate(-8deg)'); tl.from(t, { scale: 2, opacity: 0, duration: .3, ease: 'back.out(2)' }, at); return t; };
  const push = (id, from = 1.15, to = 1, ox = '50%', oy = '50%') => { const s = $(id).querySelector('svg'); tl.fromTo(s, { scale: from }, { scale: to, duration: nxt(id) - S[id], ease: 'none', transformOrigin: `${ox} ${oy}` }, S[id]); };
  const ender = (id, q, at, sub = 'CUÉNTAMELO EN LOS COMENTARIOS') => { const end = document.createElement('div'); end.style.cssText = 'position:absolute;inset:0;z-index:6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;background:radial-gradient(1200px 800px at 50% 45%, #1d2a5a, #050a1a 75%)';
    end.innerHTML = `<div style="font:400 120px/1 'Bebas Neue';text-align:center">${q}</div><div style="font:800 40px Inter;letter-spacing:.06em">${sub}</div><div style="margin-top:30px;padding:22px 60px;border-radius:16px;background:#d0312d;font:800 44px Inter;letter-spacing:.08em">SUSCRÍBETE</div><div style="margin-top:20px;font:400 90px Bebas Neue;letter-spacing:.14em">CURIOSI<span style="color:#FFD23F">MUNDO</span></div>`;
    $(id).append(end); const c = end.children;
    tl.from(end, { opacity: 0, duration: .5 }, at).from(c[0], { scale: 1.2, opacity: 0, duration: .5, ease: 'expo.out' }, at + .1).from(c[1], { y: 20, opacity: 0, duration: .3 }, W('cuéntamelo') - .2)
      .from(c[2], { scale: 0, duration: .4, ease: 'back.out(2.5)' }, W('suscríbete') - .2).to(c[2], { scale: 1.08, duration: .4, yoyo: true, repeat: 3, ease: 'sine.inOut' }, W('suscríbete') + .3)
      .from(c[3], { y: 30, opacity: 0, letterSpacing: '.4em', duration: .7, ease: 'expo.out' }, W('curiosimundo') - .2); };
    const shake = (el, at, amp = 14) => tl.to(el, { x: amp, duration: .06 }, at).to(el, { x: -amp, duration: .08 }, at + .06).to(el, { x: amp * .5, duration: .08 }, at + .14).to(el, { x: 0, duration: .08 }, at + .22);
