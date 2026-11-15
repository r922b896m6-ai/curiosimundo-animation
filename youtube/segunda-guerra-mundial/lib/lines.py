import json, re, sys
d = sys.argv[1]; w = json.load(open(d + '/voz.json'))
lines = [l.split('|', 3)[3].strip() for l in open(d + '/guion.txt') if l.strip() and not l.startswith('#')]
norm = lambda s: re.sub(r'[^\wáéíóúüñ]', '', s.lower()); i = 0
for k, L in enumerate(lines, 1):
    n = len([t for t in L.split() if norm(t)]); print(f"L{k} {w[i]['start']:.1f}-{w[i+n-1]['end']:.1f} | {L[:70]}"); i += n
