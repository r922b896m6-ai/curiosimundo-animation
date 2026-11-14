"""Banda sonora + efectos originales para el reel 'trincheras' (1:52), sintetizados, sin samples ni licencias.
uso: python3 musica_trincheras.py musica.wav sfx.wav avisar=.. nube=.. alarma=.. silbatazo=.. saltaban=.. cuerpo=.. bayonetas=.. palas=.. mazas=.. puños=..
Música: intro (dron + melodía solitaria) | marcha lenta en re menor (vida diaria) | casi nada (artillería) |
 clúster inquietante (gas) | noche tensa → redoble creciente (incursiones, tropas de asalto) | latido que acelera (la orden) |
 batalla a 132 bpm (carga y cuerpo a cuerpo) | duelo (Somme) | cierre en re mayor.
Efectos: lluvia, artillería lejana, proyectil + explosión, siseo del gas, campana de alarma, silbato, explosiones y
ametralladoras en la carga, golpes sordos en el cuerpo a cuerpo.
"""
import sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR = 44100; DUR = 112.5; N = int(SR * DUR); rng = np.random.default_rng(11)
def hz(n): return 440 * 2 ** ((n - 69) / 12)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], 'band', fs=SR, output='sos'), x)
def env(n, a, d):
    e = np.ones(n); a = max(1, min(int(a * SR), n)); d = max(1, min(int(d * SR), n)); e[:a] = np.linspace(0, 1, a); e[-d:] *= np.linspace(1, 0, d); return e
class Bus:
    def __init__(s): s.L = np.zeros(N); s.R = np.zeros(N)
    def add(s, x, at, g=1., pan=0.):
        i = int(at * SR); j = min(N, i + len(x));
        if j <= i: return
        x = x[:j - i] * g; s.L[i:j] += x * np.sqrt((1 - pan) / 2) * 1.41; s.R[i:j] += x * np.sqrt((1 + pan) / 2) * 1.41
M, X = Bus(), Bus()
def saw(f, n): return 2 * ((np.arange(n) / SR * f + rng.random()) % 1) - 1
def strings(notes, at, dur, cut=1200, g=.05, a=1., r=1.2):
    n = int(dur * SR); s = sum(saw(hz(m + d), n) for m in notes for d in (-.08, 0, .07)) / len(notes)
    tt = np.arange(n) / SR; s *= 1 + .08 * np.sin(2 * np.pi * 5 * tt)  # vibrato-ish swell
    s = lp(s, cut) * env(n, a, r); M.add(s, at, g, -.25); M.add(np.roll(s, 400), at, g, .25)
def lead(m, at, dur, g=.07, pan=0.):  # soft horn/bugle-like
    n = int(dur * SR); tt = np.arange(n) / SR; f = hz(m) * (1 + .004 * np.sin(2 * np.pi * 5.5 * tt) * np.clip(tt - .3, 0, 1))
    ph = 2 * np.pi * np.cumsum(f) / SR; s = np.sin(ph) + .5 * np.sin(2 * ph) + .25 * np.sin(3 * ph) + .1 * np.sin(4 * ph)
    M.add(lp(s, 2500) * env(n, .12, .4), at, g, pan)
def snare(at, g=.08, bus=None):
    n = int(.25 * SR); tt = np.arange(n) / SR; s = bp(rng.standard_normal(n), 900, 6000) * np.exp(-tt * 22) + .3 * np.sin(2 * np.pi * 190 * tt) * np.exp(-tt * 30)
    (bus or M).add(s, at, g, .1)
def roll(at, dur, g=.05):
    k = int(dur / .045)
    for i in range(k): snare(at + i * .045, g * (.4 + .6 * i / k))
def timp(m, at, g=.3):
    n = int(2 * SR); tt = np.arange(n) / SR; f = hz(m) * (1 + .15 * np.exp(-tt * 20))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 2.2) + lp(rng.standard_normal(n), 300) * np.exp(-tt * 18) * .4
    M.add(s, at, g)
def low(m, at, dur, g=.1):
    n = int(dur * SR); tt = np.arange(n) / SR; s = np.tanh(2 * np.sin(2 * np.pi * hz(m) * tt)) * env(n, .01, .08); M.add(lp(s, 500), at, g)
def bell(m, at, g=.05, pan=0.):
    n = int(3 * SR); tt = np.arange(n) / SR; f = hz(m)
    s = sum(a * np.sin(2 * np.pi * f * r * tt) * np.exp(-tt * k) for a, r, k in ((1, 1, 1.4), (.4, 2.76, 3), (.2, 5.4, 5)))
    M.add(s * env(n, .005, 1), at, g, pan)
# ---------------- music ----------------
W = {k: float(v) for k, v in (a.split('=') for a in sys.argv[3:])}
Dm, Bb, Gm, A, F, C, D = [50, 57, 62, 65], [46, 53, 58, 62], [43, 55, 58, 62], [45, 57, 61, 64], [41, 53, 57, 60], [48, 55, 60, 64], [50, 57, 62, 66]
# 0-17.85 intro: drone + lonely melody
strings([38, 45, 50], 0, 18.2, cut=500, g=.07, a=2)
for at, m, d in ((1.0, 69, 1.4), (2.6, 74, 1.0), (3.8, 72, .8), (4.8, 69, 2.2), (7.6, 65, 1.0), (8.8, 67, .9), (9.9, 69, 2.4), (13.0, 65, 1.2), (14.4, 62, 3)): lead(m, at, d, .04, -.2)
# 17.85-45.95 slow march
B = 60 / 72; BAR = 4 * B; t0 = 17.85; k = 0; prog = [Dm, Bb, Gm, A]
while t0 + k * BAR < 45.9:
    st = t0 + k * BAR; ch = prog[k % 4]
    strings(ch, st, BAR + .4, cut=900 + 300 * (k % 2), g=.045, a=.6, r=.8); low(ch[0] - 12, st, BAR * .9, .06)
    for j in range(4):
        if st + j * B < 45.9: snare(st + j * B + B / 2, .035); snare(st + j * B + B * .75, .02)
    k += 1
# 45.95-51.1 sparse
strings([38, 50], 45.95, 5.5, cut=400, g=.05, a=1)
# 51.1-65.85 gas: eerie cluster + slow pulses
strings([50, 51, 56, 57], 51.1, 15, cut=700, g=.05, a=2.5, r=1.5)
for i, m in enumerate([77, 78, 77, 76, 77]): bell(m, 52 + i * 2.6, .03, (-.5, .5)[i % 2])
for i in range(8): timp(38, 53 + i * 1.6, .1)
# 65.85-84 night raid + stormtroopers: quiet ticking, then building snare
strings([38, 45, 50], 65.85, 9.6, cut=350, g=.05, a=1.5)
for i in range(int(9 / .42)): snare(66.2 + i * .42, .012)
B3 = 60 / 96; i = 0
while 75.2 + i * B3 < 84:
    tt = 75.2 + i * B3; ch = [Dm, Bb, Gm, A][(i // 4) % 4]
    if i % 4 == 0: strings(ch, tt, 4 * B3 + .3, cut=800 + 120 * (i // 4), g=.045, a=.3, r=.4)
    low(ch[0] - 12, tt, B3 * .8, .055); snare(tt + B3 / 2, .02 + .004 * (i // 4)); i += 1
# 84-87.6 heartbeat accelerating
tt_ = 84.2; gap = .85
while tt_ < 87.5: timp(38, tt_, .22); timp(38, tt_ + .17, .12); tt_ += gap; gap *= .84
strings([50, 53, 56], 84.1, 3.6, cut=900, g=.04, a=2.5, r=.2)
roll(86.5, 1.1, .06)
# 87.6-100.4 battle
B2 = 60 / 132; st = W.get('silbatazo', 87.63); i = 0
while st + i * B2 / 2 < 100.35:
    t_ = st + i * B2 / 2; ch = [Dm, Dm, Bb, A][(i // 16) % 4]
    low(ch[0] - 12 + (0, 0, 12, 0, 7, 0, 12, 5)[i % 8], t_, B2 / 2, .07)
    if i % 4 == 0: timp(38 if (i // 4) % 2 == 0 else 33, t_, .2)
    if i % 2 == 1: snare(t_, .04)
    i += 1
for k in range(6): strings([62, 65, 69] if k % 2 == 0 else [58, 62, 65], st + k * 8 * B2, 8 * B2 + .2, cut=2600, g=.04, a=.2, r=.3)
# 100.4-106.5 mourning
strings([38, 50, 53, 57], 100.45, 6.3, cut=1100, g=.06, a=.8, r=1.8)
for at, m, d in ((101.2, 74, 1.1), (102.4, 72, .6), (103.1, 70, .6), (103.8, 69, 1.4), (105.3, 65, 1.3)): lead(m, at, d, .05)
# 106.5-111.6 close in D major
strings(D, 106.5, 5.6, cut=1800, g=.05, a=.6, r=2.5)
for at, m, d in ((106.9, 66, .8), (107.8, 69, .8), (108.7, 74, 2.6)): lead(m, at, d, .045)
# ---------------- SFX ----------------
n = N; rain = hp(lp(rng.standard_normal(n), 6000), 900) * .05
drops = np.zeros(n); idx = rng.integers(0, n, 9000); drops[idx] = rng.uniform(.1, .5, len(idx)); drops = hp(lp(drops, 5000), 1500)
r_env = np.interp(np.arange(n) / SR, [0, 16.5, 18.5, 65.8, 66.5, 74.8, 75.4, 120], [1, 1, .12, .12, .4, .4, 0, 0])
X.add((rain + drops * .6) * r_env, 0, .25)
def boom(at, g=.6, far=False, pan=0.):
    n_ = int(4 * SR); tt = np.arange(n_) / SR; f = 28 + 55 * np.exp(-tt * 7)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.4) + lp(rng.standard_normal(n_), 1200 if not far else 300) * np.exp(-tt * (2.2 if not far else 1.2)) * .8
    if far: s = lp(s, 250)
    X.add(s, at, g, pan)
def whistle_in(at, dur=.8, g=.12):
    n_ = int(dur * SR); tt = np.arange(n_) / SR; f = 1400 - 700 * tt / dur
    X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.linspace(.2, 1, n_), at, g, .4)
def mg(at, dur, g=.07, pan=.5, rate=9.5):
    for i in range(int(dur * rate)):
        n_ = int(.06 * SR); tt = np.arange(n_) / SR; X.add(bp(rng.standard_normal(n_), 300, 3500) * np.exp(-tt * 70), at + i / rate + rng.uniform(0, .01), g * rng.uniform(.7, 1), pan)
def whistle(at, dur=1.0, g=.13):
    n_ = int(dur * SR); tt = np.arange(n_) / SR; f = 2900 * (1 + .02 * np.sign(np.sin(2 * np.pi * 28 * tt)))
    X.add((np.sin(2 * np.pi * np.cumsum(f) / SR) + .3 * bp(rng.standard_normal(n_), 2500, 3400)) * env(n_, .02, .15), at, g)
def clang(at, g=.12):
    n_ = int(1.6 * SR); tt = np.arange(n_) / SR
    s = sum(a * np.sin(2 * np.pi * f * tt) * np.exp(-tt * k) for a, f, k in ((1, 880, 2.5), (.6, 1430, 3.5), (.4, 2270, 5), (.3, 3110, 7)))
    X.add(s * env(n_, .002, .3), at, g, -.4)
def hiss(at, dur, g=.05):
    n_ = int(dur * SR); s = bp(rng.standard_normal(n_), 2000, 7000) * env(n_, .6, 1.2); X.add(s, at, g, -.3)
def thud(at, g=.35):
    n_ = int(.5 * SR); tt = np.arange(n_) / SR; f = 70 + 90 * np.exp(-tt * 40)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 12) + lp(rng.standard_normal(n_), 2500) * np.exp(-tt * 35) * .6
    X.add(s, at, g, rng.uniform(-.3, .3))
for at in (3.0, 9.5, 22.0, 33.5, 40.5, 69.5): boom(at, .22, True, rng.uniform(-.7, .7))
av = W.get('avisar', 47.39); whistle_in(av - .75); boom(av + .05, .9)
hiss(W.get('nube', 55.72) - .3, 6, .045)
al = W.get('alarma', 59.62)
for i in range(8): clang(al + i * .24, .1)
whistle(W.get('silbatazo', 87.63))
s14 = 89.8
for d in (.3, .9, 1.5, 2.1, 2.7): boom(s14 + d, .4, False, rng.uniform(-.5, .5))
mg(s14 + .2, 2.4, .07, .6); mg(s14 + .4, 2.2, .05, .3, 11)
thud(W.get('saltaban', 93.84) + .3, .3); thud(W.get('saltaban', 93.84) + .45, .25)
for k in ('cuerpo', 'bayonetas', 'palas', 'mazas', 'puños'): thud(W.get(k, 96) + .05, .4)
# ---------------- mix ----------------
ir_n = int(2.6 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 2.4); ir = lp(ir, 4500); ir /= np.sqrt((ir ** 2).sum()) * 4
def out(bus, path, wet, peak):
    L = bus.L + fftconvolve(bus.L, ir)[:N] * wet; R = bus.R + fftconvolve(bus.R, np.roll(ir, 300))[:N] * wet
    st = np.stack([L, R], 1); fo = int(1.5 * SR); st[-fo:] *= np.linspace(1, 0, fo)[:, None]
    st = np.tanh(st / np.abs(st).max() * 1.2) / np.tanh(1.2) * peak
    wavfile.write(path, SR, (st * 32767).astype(np.int16))
out(M, sys.argv[1], .9, .85); out(X, sys.argv[2], .35, .9)
print('ok')
