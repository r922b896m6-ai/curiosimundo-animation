"""Pantalla final de YouTube (20 s) con huecos marcados para los elementos de YouTube Studio.
uso: python3 tools/endscreen.py <carpeta extras> "<PREGUNTA con <em>…</em>>" "<fondo css>" [libs extra] [js de fondo]"""
import sys, json, subprocess, os
d, q, bg = sys.argv[1], sys.argv[2], sys.argv[3]
libs = sys.argv[4] if len(sys.argv) > 4 else ''
deco = sys.argv[5] if len(sys.argv) > 5 else ''
html = f'''<!doctype html>
<!-- Pantalla final de YouTube (20 s). Zonas libres: vídeo recomendado (izquierda, 16:9) y suscripción (derecha, círculo). -->
<html data-width="1920" data-height="1080" data-fps="30" data-duration="20">
<head><link rel="stylesheet" href="lib/cm.css"><script src="lib/cm.js"></script>{''.join(f'<script src="lib/{l}"></script>' for l in libs.split(',') if l)}</head>
<body>
<audio src="musica.mp3" data-volume="0.6" data-fade-in="0.5" data-fade-out="3"></audio>
<section class="scene" id="e" data-start="0" data-duration="20"></section>
<script>
const e = document.getElementById('e'), tl = gm.timeline('#e'), mk = CM.mk;
const s = CM.svgIn(e, '{bg}');
{deco}
const vbox = mk('rect', {{ x: 230, y: 380, width: 704, height: 396, rx: 22, fill: 'rgb(6 12 28 / .55)', stroke: '#FFD23F', 'stroke-width': 5, 'stroke-dasharray': '18 12' }}, s);
const sub = mk('circle', {{ cx: 1440, cy: 578, r: 170, fill: 'rgb(6 12 28 / .55)', stroke: '#FFD23F', 'stroke-width': 5, 'stroke-dasharray': '18 12' }}, s);
const t1 = CM.text(e, 'big', '{q}', 90, 'font-size:104px');
const t2 = CM.text(e, 'mid', 'cuéntamelo en los <b>comentarios</b>', 230);
const l1 = CM.text(e, 'mid', 'mira este <b>vídeo</b>', 800, 'left:230px;right:auto;width:704px;font-size:38px');
const l2 = CM.text(e, 'mid', '<b>suscríbete</b>', 800, 'left:1240px;right:auto;width:400px;font-size:38px');
const br = CM.text(e, 'big', 'CURIOSI<em>MUNDO</em>', 880, 'font-size:70px;letter-spacing:.14em;top:auto;bottom:40px');
const sl = CM.text(e, 'mid', 'un mundo de cosas por descubrir', 0, 'top:auto;bottom:16px;font-size:22px;color:#cfe3ff');
tl.from(t1, {{ scale: 1.2, opacity: 0, duration: .6, ease: 'expo.out' }}, .2).from(t2, {{ y: 20, opacity: 0, duration: .4 }}, .6)
  .from([vbox, sub], {{ opacity: 0, duration: .5, stagger: .2 }}, .8).from([l1, l2], {{ y: 20, opacity: 0, duration: .4, stagger: .2 }}, 1.1)
  .from(br, {{ y: 30, opacity: 0, letterSpacing: '.4em', duration: .8, ease: 'expo.out' }}, 1.4).from(sl, {{ opacity: 0, duration: .5 }}, 2)
  .to(sub, {{ scale: 1.04, duration: .8, ease: 'sine.inOut', yoyo: true, repeat: 19, transformOrigin: '1440px 578px' }}, 2);
</script>
</body>
</html>
'''
open(d + '/endscreen.html', 'w').write(html)
json.dump({'dur': 20, 'sec': [[0, 20, 'end']]}, open(d + '/audio.json', 'w'))
root = os.path.dirname(os.path.abspath(__file__))
subprocess.run(['python3', root + '/musica_historia.py', d], check=True, capture_output=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', d + '/musica.wav', '-b:a', '192k', d + '/musica.mp3'], check=True); os.remove(d + '/musica.wav'); os.remove(d + '/sfx.wav')
print('ok', d)
