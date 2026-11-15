"""Música y efectos originales para vídeos de historia de CURIOSIMUNDO (sintetizados, sin samples ni licencias).
Lee <carpeta>/audio.json y escribe <carpeta>/musica.wav y <carpeta>/sfx.wav.

audio.json:
  dur: duración en s
  sec: [[t0, t1, ambiente], ...]   ambientes: card, tension, tension_up, march, battle, mourn, sea, gas, air, xmas, title, end
  booms: [t...] artillería cercana · far: [t...] cañonazos lejanos · mg: [[t0, t1]] ametralladoras · hits: [t...] golpes del cuerpo a cuerpo
  hiss: [[t0, t1]] gas · rain: [[t0, t1]] lluvia · tanks: [[t0, t1]] motores de tanque · planes: [[t0, t1]] aviones · bells: [t...] campanas
uso: python3 tools/musica_historia.py youtube/primera-guerra-mundial/cap4
"""
import sys, json, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
D = sys.argv[1]; A = json.load(open(D + '/audio.json'))
SR = 44100; DUR = A['dur'] + .5; N = int(SR * DUR); rng = np.random.default_rng(abs(hash(D)) % 2**32)
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
def strings(notes, at, dur, cut=1200, g=.05, a=1., r=1.2):
    n = int(dur * SR)
    if n <= 0: return
    s = sum(saw(hz(m + d), n) for m in notes for d in (-.08, 0, .07)) / len(notes); t = np.arange(n) / SR
    s = lp(s * (1 + .06 * np.sin(2 * np.pi * 5 * t)), cut) * env(n, a, r); M.add(s, at, g, -.25); M.add(np.roll(s, 400), at, g, .25)
def lead(m, at, dur, g=.05, pan=0.):
    n = int(dur * SR); t = np.arange(n) / SR; f = hz(m) * (1 + .004 * np.sin(2 * np.pi * 5.5 * t) * np.clip(t - .3, 0, 1)); ph = 2 * np.pi * np.cumsum(f) / SR
    M.add(lp(np.sin(ph) + .5 * np.sin(2 * ph) + .25 * np.sin(3 * ph), 2500) * env(n, .1, .35), at, g, pan)
def snare(at, g=.05, bus=M):
    n = int(.25 * SR); t = np.arange(n) / SR; bus.add(bp(rng.standard_normal(n), 900, 6000) * np.exp(-t * 22) + .3 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30), at, g, .1)
def timp(m, at, g=.25):
    n = int(2 * SR); t = np.arange(n) / SR; f = hz(m) * (1 + .15 * np.exp(-t * 20))
    M.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2) + lp(rng.standard_normal(n), 300) * np.exp(-t * 18) * .4, at, g)
def low(m, at, dur, g=.08):
    n = int(dur * SR); t = np.arange(n) / SR; M.add(lp(np.tanh(2 * np.sin(2 * np.pi * hz(m) * t)) * env(n, .01, .08), 500), at, g)
def bell(m, at, g=.05, pan=0., bus=M):
    n = int(3 * SR); t = np.arange(n) / SR; f = hz(m)
    bus.add(sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * k) for a, r, k in ((1, 1, 1.2), (.5, 2.76, 2.6), (.25, 5.4, 4.5))) * env(n, .003, 1), at, g, pan)
Dm, Bb, Gm, A_, F, C, Dmaj, G = [50, 57, 62, 65], [46, 53, 58, 62], [43, 55, 58, 62], [45, 57, 61, 64], [41, 53, 57, 60], [48, 55, 60, 64], [50, 57, 62, 66], [43, 55, 59, 62]
def mood(t0, t1, kind):
    L = t1 - t0
    if kind == 'card':
        timp(38, t0 + .1, .3); strings([38, 45, 50], t0, L + .3, cut=700, g=.06, a=.8, r=.6)
        n = int(1.2 * SR); X.add(bp(rng.standard_normal(n), 300, 3000) * np.linspace(0, 1, n) ** 2, t0 + max(0, L - 1.4), .05)
    elif kind in ('tension', 'tension_up'):
        strings([38, 45, 50, 51], t0, L + .4, cut=600, g=.055, a=1.2, r=1)
        t = t0 + .3
        while t < t1 - .2: timp(38, t, .13); t += 1.25
        for i in range(int(L / 2.5)): bell(74 + (0, 3, 1, -2)[i % 4], t0 + 1 + i * 2.5, .02, (-.5, .5)[i % 2])
        if kind == 'tension_up':
            k = int(2 / .05)
            for i in range(k): snare(t1 - 2 + i * .05, .045 * i / k)
    elif kind == 'march':
        B = 60 / 76; BAR = 4 * B; k = 0; prog = [Dm, Bb, Gm, A_]
        while t0 + k * BAR < t1:
            st = t0 + k * BAR; ch = prog[k % 4]; strings(ch, st, min(BAR + .4, t1 - st + .4), cut=1000, g=.042, a=.5, r=.6); low(ch[0] - 12, st, min(BAR * .9, t1 - st), .055)
            for j in range(4):
                if st + j * B < t1 - .1: snare(st + j * B + B / 2, .03); snare(st + j * B + B * .75, .018)
            k += 1
    elif kind == 'battle':
        B2 = 60 / 132; i = 0
        while t0 + i * B2 / 2 < t1:
            t = t0 + i * B2 / 2; ch = [Dm, Dm, Bb, A_][(i // 16) % 4]; low(ch[0] - 12 + (0, 0, 12, 0, 7, 0, 12, 5)[i % 8], t, B2 / 2, .065)
            if i % 4 == 0: timp(38 if (i // 4) % 2 == 0 else 33, t, .18)
            if i % 2 == 1: snare(t, .035)
            i += 1
        for k in range(int(L / (8 * B2)) + 1): strings([62, 65, 69] if k % 2 == 0 else [58, 62, 65], t0 + k * 8 * B2, min(8 * B2 + .2, t1 - t0 - k * 8 * B2 + .2), cut=2400, g=.035, a=.2, r=.3)
    elif kind == 'mourn':
        strings([38, 50, 53, 57], t0, L + .5, cut=1000, g=.055, a=1, r=1.5)
        mel = [(74, 1.2), (72, .7), (70, .7), (69, 1.6), (65, 1.6), (67, 1.2), (69, 2.0)]; t = t0 + .6
        for m, d in mel:
            if t + d > t1: break
            lead(m, t, d, .045); t += d + .15
    elif kind == 'sea':
        strings([38, 45, 53, 57], t0, L + .4, cut=800, g=.05, a=1, r=1)
        n = int(L * SR); X.add(lp(rng.standard_normal(n), 500) * (.6 + .4 * np.sin(np.arange(n) / SR * 1.2)) * env(n, 1, 1), t0, .06)
    elif kind == 'gas':
        strings([50, 51, 56, 57], t0, L + .5, cut=700, g=.05, a=2, r=1.2)
        for i in range(int(L / 1.6)): timp(38, t0 + .5 + i * 1.6, .1)
    elif kind == 'air':
        B = 60 / 100; k = 0
        while t0 + k * 4 * B < t1:
            st = t0 + k * 4 * B; ch = [Dmaj, G, A_, Dmaj][k % 4]; strings(ch, st, 4 * B + .3, cut=2200, g=.045, a=.2, r=.4); low(ch[0] - 12, st, 4 * B * .9, .05)
            for j in range(8):
                if st + j * B / 2 < t1: snare(st + j * B / 2, .02 + .015 * (j % 2))
            k += 1
    elif kind == 'xmas':   # "Stille Nacht" (1818, public domain) on a music box
        strings([55, 59, 62], t0, L + .5, cut=1400, g=.04, a=1, r=1.5)
        mel = [(67, .9), (69, .3), (67, .6), (64, 1.6), (67, .9), (69, .3), (67, .6), (64, 1.6), (74, 1.2), (74, .6), (71, 1.6), (72, 1.2), (72, .6), (67, 1.6)]; t = t0 + .5
        for m, d in mel:
            if t > t1 - .5: break
            bell(m + 12, t, .05); t += d * .9
    elif kind == 'title':
        timp(38, t0, .35); strings([50, 57, 62, 65], t0, L + .5, cut=1600, g=.06, a=.3, r=1.5)
        for i, (m, d) in enumerate([(62, .8), (65, .8), (69, 1.2), (67, .8), (65, 2.0)]): lead(m, t0 + .4 + sum(x[1] for x in [(62, .8), (65, .8), (69, 1.2), (67, .8), (65, 2.0)][:i]), d, .05)
    elif kind == 'end':
        strings([50, 57, 62, 66], t0, L + .5, cut=1800, g=.05, a=1, r=3)
        t = t0 + .8
        for m, d in [(66, 1), (69, 1), (74, 2.4), (73, 1), (71, 1), (69, 2.6)]:
            if t + d > t1: break
            lead(m, t, d, .045); t += d + .1
for t0, t1, k in A['sec']: mood(t0, t1, k)
# ---------------- SFX ----------------
def boom(at, g=.5, far=False, pan=0.):
    n = int(3.5 * SR); t = np.arange(n) / SR; f = 28 + 55 * np.exp(-t * 7)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.5) + lp(rng.standard_normal(n), 300 if far else 1200) * np.exp(-t * (1.2 if far else 2.4)) * .8
    X.add(lp(s, 250) if far else s, at, g, pan)
def whine(at, g=.08):
    n = int(.6 * SR); t = np.arange(n) / SR; f = 1500 - 800 * t / .6; X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.linspace(.2, 1, n), at - .6, g, .4)
def mg(t0, t1, g=.05):
    k = int((t1 - t0) * 9)
    for i in range(k):
        if (i // 12) % 2: continue
        n = int(.05 * SR); t = np.arange(n) / SR; X.add(bp(rng.standard_normal(n), 300, 3500) * np.exp(-t * 70), t0 + i / 9 + rng.uniform(0, .01), g * rng.uniform(.6, 1), .5)
def thud(at, g=.3):
    n = int(.4 * SR); t = np.arange(n) / SR; f = 70 + 90 * np.exp(-t * 40)
    X.add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 12) + lp(rng.standard_normal(n), 2500) * np.exp(-t * 35) * .6, at, g, rng.uniform(-.3, .3))
def loopnoise(t0, t1, kind):
    n = int((t1 - t0) * SR); t = np.arange(n) / SR
    if kind == 'rain': s = hp(lp(rng.standard_normal(n), 6000), 900) * .5
    elif kind == 'hiss': s = bp(rng.standard_normal(n), 2000, 7000) * .4
    elif kind == 'tank': s = lp(np.sign(np.sin(2 * np.pi * 28 * t)) * .5 + rng.standard_normal(n) * .3, 300) * (1 + .3 * np.sin(2 * np.pi * 6 * t))
    else: s = lp(np.sign(np.sin(2 * np.pi * (90 + 10 * np.sin(t * .8)) * t)) * .5 + rng.standard_normal(n) * .2, 900) * .5
    X.add(s * env(n, .6, .8), t0, {'rain': .12, 'hiss': .06, 'tank': .1, 'plane': .06}[kind])
for b in A.get('booms', []): whine(b, .05); boom(b, .45, False, rng.uniform(-.5, .5))
for b in A.get('far', []): boom(b, .25, True, rng.uniform(-.7, .7))
for t0, t1 in A.get('mg', []): mg(t0, t1)
for h in A.get('hits', []): thud(h, .35)
for t0, t1 in A.get('hiss', []): loopnoise(t0, t1, 'hiss')
for t0, t1 in A.get('rain', []): loopnoise(t0, t1, 'rain')
for t0, t1 in A.get('tanks', []): loopnoise(t0, t1, 'tank')
for t0, t1 in A.get('planes', []): loopnoise(t0, t1, 'plane')
for b in A.get('bells', []):
    for i in range(6): bell([67, 64, 62, 55][i % 4], b + i * .7, .12, (-.4, .4)[i % 2], bus=X)
# ---------------- mix ----------------
ir_n = int(2.4 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 2.6); ir = lp(ir, 4500); ir /= np.sqrt((ir ** 2).sum()) * 4
def out(bus, path, wet, peak):
    L = bus.L + fftconvolve(bus.L, ir)[:N] * wet; R = bus.R + fftconvolve(bus.R, np.roll(ir, 300))[:N] * wet
    st = np.stack([L, R], 1); st = np.tanh(st * 1.3) * peak   # fixed gain + soft clip: same loudness in every chapter
    fo = int(.4 * SR); st[-fo:] *= np.linspace(1, 0, fo)[:, None]; wavfile.write(path, SR, (st * 32767).astype(np.int16))
out(M, D + '/musica.wav', .8, .8); out(X, D + '/sfx.wav', .3, .85)
print('ok', D)
