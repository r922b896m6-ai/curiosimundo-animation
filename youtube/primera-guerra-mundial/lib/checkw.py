import json, re, sys
d = sys.argv[1]; words = json.load(open(d + '/voz.json')); html = open(d + '/video.html').read()
norm = lambda s: re.sub(r'[^\wáéíóúüñ]', '', s.lower())
cnt = {}
for w in words: cnt[norm(w['word'])] = cnt.get(norm(w['word']), 0) + 1
bad = [(t, n) for t, n in re.findall(r"W\('([^']+)'(?:,\s*(\d+))?\)", html) if cnt.get(norm(t), 0) < int(n or 1)]
print(d, 'OK' if not bad else 'MISSING: ' + str(sorted(set(bad))))
