"""Música + efectos originales para "El animal que piensa con los brazos" (pulpo, 59,6 s), sintetizados, sin samples.
uso: python3 musica_pulpo.py musica.wav sfx.wav latir=17.46 por=19.25 cobre=24.60 quinientos=33.81 toca=43.43 colarse=48.10 poderes=54.76
Música: marimba submarina juguetona a 100 bpm desde el segundo 0 → se vacía cuando el corazón se para → vuelve →
misteriosa y brillante en el cerebro y las neuronas → juguetona otra vez → cierre abierto en la pregunta.
Efectos: tres latidos, chispazo, chorro, pitido plano del monitor, tintineo del cobre, subida del contador, "blip" al
tocar, "squish" al colarse y "pops" de las tarjetas.
"""
import sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR = 44100; DUR = 60.5; N = int(SR * DUR); rng = np.random.default_rng(5)
W = {k: float(v) for k, v in (a.split('=') for a in sys.argv[3:])}
w = lambda k, d: W.get(k, d)
def hz(n): return 440 * 2 ** ((n - 69) / 12)
def lp(x, f): return sosfilt(butter(2, f, 'low', fs=SR, output='sos'), x)
def hp(x, f): return sosfilt(butter(2, f, 'high', fs=SR, output='sos'), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], 'band', fs=SR, output='sos'), x)
def env(n, a, d):
    e = np.ones(n); a = max(1, min(int(a * SR), n)); d = max(1, min(int(d * SR), n)); e[:a] = np.linspace(0, 1, a); e[-d:] *= np.linspace(1, 0, d); return e
class Bus:
    def __init__(s): s.L = np.zeros(N); s.R = np.zeros(N)
    def add(s, x, at, g=1., pan=0.):
        i = int(at * SR); j = min(N, i + len(x))
        if j <= i or i < 0: return
        x = x[:j - i] * g; s.L[i:j] += x * np.sqrt((1 - pan) / 2) * 1.41; s.R[i:j] += x * np.sqrt((1 + pan) / 2) * 1.41
M, X = Bus(), Bus()
def saw(f, n): return 2 * ((np.arange(n) / SR * f + rng.random()) % 1) - 1
def pad(notes, at, dur, cut=1800, g=.05, a=.4, r=.6):
    n = int(dur * SR); s = sum(saw(hz(m + d), n) for m in notes for d in (-.07, 0, .06)) / len(notes)
    s = lp(s, cut) * env(n, a, r); M.add(s, at, g, -.3); M.add(np.roll(s, 300), at, g, .3)
def pluck(m, at, g=.08, pan=0., dec=5):
    n = int(1.2 * SR); t = np.arange(n) / SR; f = hz(m)
    M.add((np.sin(2 * np.pi * f * t) + .4 * np.sin(4 * np.pi * f * t)) * np.exp(-t * dec) * env(n, .003, .2), at, g, pan)
def bass(m, at, dur, g=.12):
    n = int(dur * SR); t = np.arange(n) / SR; M.add(lp(np.tanh(2.2 * np.sin(2 * np.pi * hz(m) * t)), 600) * env(n, .005, .06), at, g)
def kick(at, g=.3, bus=M):
    n = int(.4 * SR); t = np.arange(n) / SR; f = 48 + 90 * np.exp(-t * 32); bus.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9), at, g)
def hat(at, g=.03):
    n = int(.08 * SR); t = np.arange(n) / SR; M.add(hp(rng.standard_normal(n), 7000) * np.exp(-t * 60), at, g, .2)
def clap(at, g=.06):
    n = int(.25 * SR); t = np.arange(n) / SR; M.add(bp(rng.standard_normal(n), 900, 5000) * np.exp(-t * 25), at, g, -.1)

B = 60 / 100
C, Am, F, G, Em = [60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 55, 59]
def marimba(m, at, g=.07, pan=0.):
    n = int(1.0 * SR); t = np.arange(n) / SR; f = hz(m)
    M.add((np.sin(2 * np.pi * f * t) + .25 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 30)) * np.exp(-t * 7) * env(n, .002, .2), at, g, pan)
def groove(t0, t1, prog, drums=True, mar=True, bassg=.09):
    i = 0
    while t0 + i * B / 2 < t1:
        t = t0 + i * B / 2; ch = prog[(i // 8) % len(prog)]
        if i % 8 == 0: pad([n - 12 for n in ch], t, 4 * B + .2, cut=1300, g=.035, a=.2, r=.3)
        if i % 2 == 0: bass(ch[0] - 24, t, B / 2 * .8, bassg)
        if mar and (i % 8) in (0, 2, 3, 5, 6): marimba(ch[(i * 2) % 3] + 12 + (12 if i % 8 == 6 else 0), t, .07, (-.4, .4)[i % 2])
        if drums:
            if i % 4 == 0: kick(t, .16)
            if i % 4 == 2: clap(t, .035)
            hat(t + B / 4, .015)
        i += 1
fl0, fl1 = w('latir', 17.46) - .1, w('por', 19.25) + .2
groove(0, fl0, [C, Am, F, G])
pad([45, 52, 57], fl0, fl1 - fl0 + .3, cut=500, g=.04, a=.05, r=.3)       # empty while the heart stops
groove(fl1, 28.6, [F, G, C, Am])
pad([45, 52, 59, 64], 28.6, 11.4, cut=900, g=.045, a=1.0, r=.8)            # mysterious brain / neurons
for k in range(18): pluck([76, 79, 83, 88][k % 4], 29 + k * .6, .03, (-.5, .5)[k % 2], dec=2.5)
groove(39.9, 53.0, [C, Em, F, G])
pad([48, 55, 60, 64, 67], 53.0, 7.0, cut=1600, g=.045, a=.3, r=2.5)
for k, m in enumerate([72, 76, 79, 84]): marimba(m, 53.2 + k * .4, .07, (-.3, .3)[k % 2])
# ---------- SFX ----------
def heartbeat(at, g=.35):
    for d, gg in ((0, 1), (.18, .7)):
        n = int(.3 * SR); t = np.arange(n) / SR; f = 45 + 40 * np.exp(-t * 30); X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14), at + d, g * gg)
def zap(at, g=.07):
    n = int(.35 * SR); t = np.arange(n) / SR; f = 2400 * np.exp(-t * 6) + 300; X.add(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-t * 10) * .5, at, g, .3)
def whoosh(at, dur=.6, g=.1, pan=.3):
    n = int(dur * SR); t = np.arange(n) / SR; X.add(bp(rng.standard_normal(n), 300, 3000) * np.sin(np.pi * t / dur) ** 2, at, g, pan)
def beep(at, dur, g=.05):
    n = int(dur * SR); t = np.arange(n) / SR; X.add(np.sin(2 * np.pi * 1000 * t) * env(n, .01, .05), at, g, .2)
def ting(at, g=.08):
    n = int(1.5 * SR); t = np.arange(n) / SR
    X.add(sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * k) for a, f, k in ((1, 1760, 3), (.5, 2640, 4), (.3, 4100, 6))), at, g, -.2)
def riser(at, dur=1.3, g=.06):
    n = int(dur * SR); t = np.arange(n) / SR; f = 200 + 1400 * (t / dur) ** 2; X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * (t / dur), at, g)
def blip(at, g=.1):
    n = int(.12 * SR); t = np.arange(n) / SR; f = 600 + 1200 * t / .12; X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 20), at, g)
def squish(at, g=.12):
    n = int(.5 * SR); t = np.arange(n) / SR; f = 500 - 350 * t / .5
    X.add(lp(np.sin(2 * np.pi * np.cumsum(f) / SR) + .5 * rng.standard_normal(n), 1200) * env(n, .02, .2), at, g)
def pop(at, g=.1):
    n = int(.15 * SR); t = np.arange(n) / SR; f = 500 + 900 * np.exp(-t * 40); X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30), at, g)
for k in range(3): heartbeat(.15 + k * .62, .3)
zap(3.5)
whoosh(14.9, .9, .12); whoosh(15.8, .9, .1)
beep(fl0, fl1 - fl0, .04)
for k in range(3): heartbeat(fl1 + .1 + k * .62, .25)
ting(w('cobre', 24.60))
riser(w('quinientos', 33.81) - .3)
blip(w('toca', 43.43)); blip(w('toca', 43.43) + .15)
squish(w('colarse', 48.10) + .2)
for k in range(4): pop(w('poderes', 54.76) - .4 + k * .15, .1)
# ---------- mix ----------
ir_n = int(1.8 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 3); ir = lp(ir, 5000); ir /= np.sqrt((ir ** 2).sum()) * 4
def out(bus, path, wet, peak):
    L = bus.L + fftconvolve(bus.L, ir)[:N] * wet; R = bus.R + fftconvolve(bus.R, np.roll(ir, 250))[:N] * wet
    st = np.stack([L, R], 1); fo = int(1.2 * SR); st[-fo:] *= np.linspace(1, 0, fo)[:, None]
    st = np.tanh(st / np.abs(st).max() * 1.2) / np.tanh(1.2) * peak
    wavfile.write(path, SR, (st * 32767).astype(np.int16))
out(M, sys.argv[1], .6, .85); out(X, sys.argv[2], .3, .9)
print('ok')
