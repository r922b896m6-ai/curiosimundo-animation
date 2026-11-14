# Segmented TTS: each line "rate|pitch|pause|text" is voiced separately, then joined with pauses; word times offset.
import asyncio, json, ssl, sys, subprocess, os, re
import edge_tts, edge_tts.communicate as c
c._SSL_CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
segfile, voice, out = sys.argv[1], sys.argv[2], sys.argv[3]
segs = [l.rstrip('\n').split('|', 3) for l in open(segfile) if l.strip() and not l.startswith('#')]
tmp = out + '_parts'; os.makedirs(tmp, exist_ok=True)
async def one(i, rate, pitch, text):
    comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, boundary="WordBoundary")
    words = []
    with open(f"{tmp}/{i}.mp3", "wb") as f:
        async for ch in comm.stream():
            if ch["type"] == "audio": f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                s = ch["offset"] / 1e7; words.append({"word": ch["text"], "start": s, "end": s + ch["duration"] / 1e7})
    return words
async def main():
    allw, t, files = [], 0.25, []
    subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t','0.25',f'{tmp}/lead.wav'])
    files.append(f'{tmp}/lead.wav')
    for i, (rate, pitch, pause, text) in enumerate(segs):
        ws = await one(i, rate, pitch, text)
        subprocess.run(['ffmpeg','-v','error','-y','-i',f'{tmp}/{i}.mp3','-ar','24000','-ac','1',f'{tmp}/{i}.wav'])
        dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{tmp}/{i}.wav']))
        # trim trailing silence estimate: use last word end + 0.12
        end = min(dur, ws[-1]['end'] + 0.15) if ws else dur
        subprocess.run(['ffmpeg','-v','error','-y','-i',f'{tmp}/{i}.wav','-t',str(end),f'{tmp}/{i}t.wav'])
        files.append(f'{tmp}/{i}t.wav')
        toks = text.split(); k = 0
        norm = lambda s: re.sub(r'[^\wáéíóúñü]', '', s.lower())
        for w in ws:
            while norm(toks[k]) == '': k += 1
            assert norm(toks[k]) == norm(w['word']), (toks[k], w['word'])
            allw.append({"word": toks[k], "start": round(t + w['start'], 3), "end": round(t + w['end'], 3)}); k += 1
        t += end
        p = float(pause)
        if p > 0:
            subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t',str(p),f'{tmp}/p{i}.wav'])
            files.append(f'{tmp}/p{i}.wav'); t += p
    open(f'{tmp}/list.txt','w').write(''.join(f"file '{os.path.abspath(f)}'\n" for f in files))
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{tmp}/list.txt','-ar','44100','-ac','2','-b:a','192k',out + '.mp3'])
    json.dump(allw, open(out + '.json', 'w'), ensure_ascii=False)
    print('total', round(t, 2))
asyncio.run(main())
