"""Música + efectos originales para "¿Y si la Tierra dejara de girar?" (32 s), sintetizados, sin samples ni licencias.
uso: python3 musica_tierra.py musica.wav sfx.wav girar=1.43 saldrías=2.63 arrasarían=11.38 continente=16.34 año=20.42 seis=20.95 tranquilo=23.89 qué=27.40
Música: pulso curioso a 112 bpm desde el segundo 0 → se corta en seco al frenar la Tierra → vuelve con fuerza (vuelo)
→ espacio amplio (agua y continente) → tic-tac (1 día = 1 año) → acordes mayores relajados → final abierto.
Efectos: frenazo, ráfagas de aire, golpe grave, ola, tic-tac de meses, "pop" del visto bueno, brillo final.
"""
import sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR = 44100; DUR = 33.0; N = int(SR * DUR); rng = np.random.default_rng(5)
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
B = 60 / 112
C, G, Am, F = [60, 64, 67], [55, 59, 62], [57, 60, 64], [53, 57, 60]
def groove(t0, t1, prog, full=True, arp=True):
    i = 0
    while t0 + i * B / 2 < t1:
        t = t0 + i * B / 2; ch = prog[(i // 8) % len(prog)]
        if i % 8 == 0: pad([n - 12 for n in ch], t, 4 * B + .2, cut=1600, g=.04, a=.15, r=.3)
        if i % 2 == 0: bass(ch[0] - 24, t, B / 2 * .9, .1)
        if arp: pluck(ch[i % 3] + 12 + (12 if i % 4 == 3 else 0), t, .05, (-.4, .4)[i % 2])
        if full:
            if i % 2 == 0: kick(t, .22)
            if i % 4 == 2: clap(t, .05)
            hat(t + B / 4, .02)
        i += 1
stop = w('girar', 1.43) + .1
groove(0, stop, [C, G], full=True)                       # hook: already moving at frame 0
groove(w('saldrías', 2.63) - .05, 10.5, [Am, F, C, G])     # flight
groove(10.5, 12.9, [Am, F], full=True, arp=False)          # wave: driving, no arp
pad([45, 52, 57, 64], 12.9, 6.0, cut=1200, g=.05, a=.8, r=.8)   # space
for k in range(10): pluck([76, 79, 81, 84][k % 4], 13.2 + k * .55, .035, (-.5, .5)[k % 2], dec=2.5)
for k in range(int((w('seis', 20.95) - w('año', 20.42) + 2) / (B / 2))): hat(18.8 + k * B / 2, .05)   # tick-tock of the calendar
groove(20.8, 23.7, [Am, F], full=False)
groove(23.7, 26.4, [C, F, G], full=True)                   # relax, major
pad([48, 55, 60, 64, 67], 26.4, 5.8, cut=2000, g=.05, a=.3, r=2.5)
for k, m in enumerate([72, 76, 79, 84]): pluck(m, 26.5 + k * .45, .05, (-.3, .3)[k % 2], dec=2)
# ---------- SFX ----------
def whoosh(at, dur=.6, g=.12, pan=.4):
    n = int(dur * SR); t = np.arange(n) / SR; s = bp(rng.standard_normal(n), 400, 4000) * np.sin(np.pi * t / dur) ** 2; X.add(s, at, g, pan)
def boom(at, g=.6):
    n = int(2.5 * SR); t = np.arange(n) / SR; f = 30 + 70 * np.exp(-t * 6)
    X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2) + lp(rng.standard_normal(n), 900) * np.exp(-t * 4) * .5, at, g)
def screech(at, dur=.45, g=.08):
    n = int(dur * SR); t = np.arange(n) / SR; f = 1800 - 900 * t / dur
    X.add((np.sin(2 * np.pi * np.cumsum(f) / SR) + .4 * bp(rng.standard_normal(n), 1500, 4000)) * env(n, .01, .15), at, g)
def crash(at, dur=1.8, g=.18):
    n = int(dur * SR); t = np.arange(n) / SR; X.add(lp(rng.standard_normal(n), 2500) * np.exp(-t * 1.5) * env(n, .05, .4), at, g, -.2)
def tick(at, g=.08):
    n = int(.05 * SR); t = np.arange(n) / SR; X.add(np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 120), at, g)
def pop(at, g=.12):
    n = int(.15 * SR); t = np.arange(n) / SR; f = 500 + 900 * np.exp(-t * 40); X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30), at, g)
screech(stop - .3); boom(stop, .7)
for k, p in enumerate((.3, .5, .7)): whoosh(w('saldrías', 2.63) + k * .25, .7, .14, p)
for t in (6.1, 6.8, 7.6, 8.45): whoosh(t - .05, .35, .1, .3)
crash(w('arrasarían', 11.38) - .2); whoosh(10.5, .8, .12, -.3)
whoosh(w('continente', 16.34) - .3, .9, .08, 0)
for k in range(12): tick(w('año', 20.42) - .1 + k * .07, .06)
pop(w('tranquilo', 23.89) + 1.2)
for k in range(5): pop(w('qué', 27.40) + k * .09, .05)
# ---------- mix ----------
ir_n = int(1.8 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 3); ir = lp(ir, 5000); ir /= np.sqrt((ir ** 2).sum()) * 4
def out(bus, path, wet, peak):
    L = bus.L + fftconvolve(bus.L, ir)[:N] * wet; R = bus.R + fftconvolve(bus.R, np.roll(ir, 250))[:N] * wet
    st = np.stack([L, R], 1); fo = int(1.2 * SR); st[-fo:] *= np.linspace(1, 0, fo)[:, None]
    st = np.tanh(st / np.abs(st).max() * 1.2) / np.tanh(1.2) * peak
    wavfile.write(path, SR, (st * 32767).astype(np.int16))
out(M, sys.argv[1], .6, .85); out(X, sys.argv[2], .3, .9)
print('ok')
