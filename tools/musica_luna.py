"""Banda sonora original para el reel 'sin-luna' (sintetizada, sin samples ni licencias).
Secciones alineadas con la narración:
  0-4.3   misterio (pad agudo, brillo)        4.3  la Luna desaparece: swell + golpe grave
  4.3-12.4 oscuridad (pad grave, notas sueltas)
  12.4-33.3 mareas/corales: arpegio a 96 bpm, bajo suave
  33.3-48.4 tensión: progresión menor, bombo creciente, filtro que se abre
  48.4-52.6 eclipse: casi silencio, campanas      52.6-62.6 la Luna vuelve: acordes mayores cálidos, final en Do
uso: python3 musica_luna.py salida.wav
"""
import sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR = 44100; DUR = 63.5; N = int(SR * DUR)
rng = np.random.default_rng(7)
t = np.arange(N) / SR
L = np.zeros(N); R = np.zeros(N)
def hz(n): return 440 * 2 ** ((n - 69) / 12)
def env_ad(n, a, d):  # attack/decay in samples
    e = np.ones(n); a = max(1, min(a, n)); e[:a] = np.linspace(0, 1, a)
    d = max(1, min(d, n)); e[-d:] *= np.linspace(1, 0, d); return e
def add(sig, start, gain=1.0, pan=0.0):
    i = int(start * SR); j = min(N, i + len(sig)); s = sig[:j - i] * gain
    L[i:j] += s * (1 - pan) ** .5 * 1.0; R[i:j] += s * (1 + pan) ** .5 * 1.0
def lp(x, f, order=2): return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)
def hp(x, f): return sosfilt(butter(2, f, 'high', fs=SR, output='sos'), x)
def saw(f, n, ph=0.0):
    x = (np.arange(n) / SR * f + ph) % 1.0; return 2 * x - 1

def pad(notes, start, dur, cutoff=1400, gain=.06, att=1.2, rel=1.4):
    n = int(dur * SR); s = np.zeros(n)
    for m in notes:
        for det in (-0.09, 0, 0.08):
            s += saw(hz(m + det), n, rng.random())
    s = lp(s / len(notes), cutoff, 2)
    s *= env_ad(n, int(att * SR), int(rel * SR))
    add(s, start, gain, -0.2); add(np.roll(s, 300), start, gain, 0.2)

def pluck(m, start, gain=.18, dec=1.6, pan=0.0):
    n = int(2.5 * SR); tt = np.arange(n) / SR; f = hz(m)
    s = (np.sin(2 * np.pi * f * tt) + .35 * np.sin(4 * np.pi * f * tt) + .12 * np.sin(6 * np.pi * f * tt)) * np.exp(-tt * dec * 2)
    s *= env_ad(n, 60, 2000); add(s, start, gain, pan)

def bell(m, start, gain=.12, pan=0.0):
    n = int(4 * SR); tt = np.arange(n) / SR; f = hz(m)
    s = sum(a * np.sin(2 * np.pi * f * r * tt) * np.exp(-tt * k) for a, r, k in ((1, 1, 1.2), (.5, 2.76, 2.4), (.25, 5.4, 4), (.15, 8.9, 6)))
    add(s * env_ad(n, 40, 4000), start, gain, pan)

def sub(m, start, dur, gain=.16):
    n = int(dur * SR); tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * hz(m) * tt) * env_ad(n, int(.05 * SR), int(.3 * SR)); add(s, start, gain)

def kick(start, gain=.35):
    n = int(.5 * SR); tt = np.arange(n) / SR
    f = 45 + 80 * np.exp(-tt * 30); ph = 2 * np.pi * np.cumsum(f) / SR
    add(np.sin(ph) * np.exp(-tt * 7), start, gain)

def swell(start, dur, gain=.12, rev=False):
    n = int(dur * SR); s = hp(lp(rng.standard_normal(n), 3000), 300)
    e = np.linspace(0, 1, n) ** 2.5; e = e[::-1] if rev else e
    add(s * e, start, gain, 0)

def boom(start, gain=.5):
    n = int(3 * SR); tt = np.arange(n) / SR
    f = 30 + 60 * np.exp(-tt * 6); s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6)
    s += lp(rng.standard_normal(n), 400) * np.exp(-tt * 3) * .3; add(s, start, gain)

BPM = 96; B = 60 / BPM; BAR = 4 * B
# chord tables (midi)
Am = [57, 60, 64]; F = [53, 57, 60]; C = [48, 55, 60, 64]; G = [55, 59, 62]; Dm = [50, 57, 62, 65]
Bb = [46, 53, 58, 62]; E = [52, 56, 59, 64]; Em = [52, 55, 59]; Fmaj7 = [53, 57, 60, 64]

# --- 0-4.3 mystery
pad([69, 72, 76], 0, 4.8, cutoff=2500, gain=.045, att=.4, rel=1.2)
for i, m in enumerate([81, 84, 88, 86]): bell(m, .3 + i * 1.0, .05, (-.5, .5)[i % 2])
swell(2.6, 1.7, .10)
boom(4.3, .55)
# --- 4.3-12.4 darkness
pad([45, 52, 57, 60], 4.3, 4.3, cutoff=600, gain=.07, att=1.5)
pad([41, 48, 53, 57], 8.4, 4.4, cutoff=520, gain=.07, att=1.5)
for tt_, m in ((5.6, 76), (7.2, 72), (9.1, 77), (10.7, 69)): bell(m, tt_, .05, rng.uniform(-.6, .6))
swell(11.0, 1.4, .07)
# --- 12.4-33.3 tides/corals: arpeggio
prog = [Am, F, C, G]; t0 = 12.4; k = 0
while t0 + k * BAR < 33.3:
    ch = prog[k % 4]; st = t0 + k * BAR
    pad([n + 12 for n in ch[:3]], st, BAR + .3, cutoff=1600, gain=.04, att=.5, rel=.6)
    sub(ch[0] - 12, st, BAR, .14)
    arp = [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[1] + 24]
    for j in range(8):
        if st + j * B / 2 < 33.2: pluck(arp[j % 4], st + j * B / 2, .085, 2.2, (-.4, .4)[j % 2])
    k += 1
# --- 33.3-48.4 tension
prog = [Dm, Bb, F, E]; t0 = 33.3; k = 0
while t0 + k * BAR < 48.3:
    ch = prog[k % 4]; st = t0 + k * BAR; prog_amt = k / 6
    pad(ch, st, BAR + .3, cutoff=700 + 2200 * prog_amt, gain=.06, att=.3, rel=.5)
    sub(ch[0] - 12, st, BAR, .17)
    for j in range(4):
        if st + j * B < 48.3: kick(st + j * B, .22 + .2 * min(1, prog_amt))
    if k >= 2:
        for j in range(8):
            if st + j * B / 2 < 48.3: pluck(ch[1 + j % (len(ch) - 1)] + 12, st + j * B / 2, .06, 3, (-.5, .5)[j % 2])
    k += 1
swell(46.9, 1.5, .14)
# --- 48.4-52.6 eclipse: near silence
boom(48.4, .35)
pad([45, 52, 57], 48.4, 4.4, cutoff=500, gain=.045, att=.2, rel=2)
for tt_, m in ((49.3, 76), (50.5, 74), (51.5, 69)): bell(m, tt_, .07, rng.uniform(-.5, .5))
swell(51.6, 1.1, .08)
# --- 52.6-63.5 warm return
prog = [Fmaj7, C, G, Am, F, C]; t0 = 52.6
for k, ch in enumerate(prog):
    st = t0 + k * (BAR * .9); dur = BAR * .9 + .4
    if st > 61: break
    pad([n + 12 for n in ch], st, dur, cutoff=2400, gain=.045, att=.6, rel=.8)
    sub(ch[0] - 12, st, BAR * .9, .12)
    for j in range(8): pluck([ch[0] + 24, ch[1] + 24, ch[2] + 24, ch[1] + 36][j % 4], st + j * B * .45, .06, 2.2, (-.4, .4)[j % 2])
pad([48, 55, 60, 64, 67], 61.0, 2.5, cutoff=2600, gain=.05, att=.3, rel=2.2)
bell(84, 61.0, .06)

# --- mix: reverb, glue, fades
ir_n = int(2.8 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 2.2); ir = lp(ir, 5000); ir /= np.abs(ir).sum() ** .5 * 6
wetL = fftconvolve(L, ir)[:N]; wetR = fftconvolve(R, np.roll(ir, 400))[:N]
L2 = L + wetL * .9; R2 = R + wetR * .9
st = np.stack([L2, R2], 1)
fade = np.ones(N); fi = int(.3 * SR); fade[:fi] = np.linspace(0, 1, fi); fo = int(2.2 * SR); fade[-fo:] = np.linspace(1, 0, fo) ** 1.5
st *= fade[:, None]
st /= np.abs(st).max() / 0.89
wavfile.write(sys.argv[1], SR, (st * 32767).astype(np.int16))
print('ok', DUR)
