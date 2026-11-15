# CURIOSIMUNDO · Vídeo 02 · ¿Y si la Tierra dejara de girar?

**Categoría:** experimento mental · **Duración:** 32 s · **Formato:** 9:16 (1080×1920)
**Estado:** ✅ **vídeo terminado**: `out/tierra-sin-girar.mp4` (animación, voz, subtítulos, música y efectos).

Archivos:
- `video.html`: animación givemotion.
- `guion.txt`, `voz.mp3`, `voz.json`, `subtitulos.srt`, `escenas.md`: guion, narración y subtítulos.
- `musica.mp3`, `sfx.mp3`: música y efectos, generados con `tools/musica_tierra.py`.
- `descripcion.txt`: texto para TikTok.

Para volver a renderizar: `npx givemotion render produccion/02-tierra-sin-girar/video.html -o produccion/02-tierra-sin-girar/out/tierra-sin-girar.mp4`

## A. Título
**¿Y si la Tierra dejara de girar? 🌍**

## B. Gancho (0–2 s)
**Fotograma 0:** la Tierra girando con **+1.600 KM/H** gigante en amarillo y "¿Y SI LA TIERRA DEJARA DE GIRAR?" debajo. En el segundo 1,5 frena en seco con una sacudida.
**Voz:** "Si la Tierra dejara de girar ahora mismo… saldrías disparado a más de mil seiscientos kilómetros por hora."

## C. Guion
1. Si la Tierra dejara de girar ahora mismo… saldrías disparado a más de mil seiscientos kilómetros por hora.
2. Tú, los coches, los edificios… todo seguiría moviéndose hacia el este.
3. Los océanos arrasarían las costas.
4. Y con el tiempo, el agua se iría hacia los polos y dejaría un continente gigante alrededor del ecuador.
5. Ah, y un día duraría un año: seis meses de sol… y seis meses de noche.
6. Tranquilo, es prácticamente imposible.
7. Pero dime: ¿qué harías tú con seis meses de noche? Te leo en comentarios.

## D. Narración
`voz.mp3` (`es-MX-JorgeNeural`), de +7 % a +12 % de velocidad, tono más agudo en el gancho y en la pregunta final.

## E. Escenas (cambio cada 2–4 s)
| # | Tiempo | Qué se ve | Texto |
|---|---|---|---|
| 1 | 0,0–2,5 | La Tierra gira con una flecha amarilla en el ecuador y frena en seco | +1.600 KM/H · ¿Y SI…? |
| 2 | 2,5–6,1 | Ciudad en el ecuador: persona, coche y autobús salen volando hacia el este | +1.600 KM/H |
| 3 | 6,1–10,5 | Cortes de 1 s: persona / coche / edificio / brújula | TÚ · LOS COCHES · LOS EDIFICIOS · TODO AL ESTE |
| 4 | 10,5–12,9 | Ola gigante que barre casas | OLAS GIGANTES |
| 5 | 12,9–16,1 | Tierra desde el espacio: los polos se llenan de agua | EL AGUA A LOS POLOS |
| 6 | 16,1–18,8 | Aparece una franja de tierra en el ecuador | UN MEGACONTINENTE |
| 7 | 18,8–20,8 | El calendario pasa los 12 meses en un día | 1 DÍA = 1 AÑO |
| 8 | 20,8–23,7 | Tierra mitad día abrasador, mitad noche helada | 6 MESES DE SOL · 6 MESES DE NOCHE |
| 9 | 23,7–26,4 | La Tierra vuelve a girar y aparece un visto bueno | TRANQUILO · PRÁCTICAMENTE IMPOSIBLE |
| 10 | 26,4–32,0 | Niño en la línea día/noche con un "?" | ¿QUÉ HARÍAS TÚ? · CURIOSIMUNDO |

## F. Prompts (para rehacerlo con una herramienta de vídeo IA en estilo cartoon 3D, si lo prefieres)
**Estilo base:**
> Animación cartoon 3D educativa, vertical 9:16, colores azul, blanco y amarillo dominantes, iluminación suave, movimiento enérgico. Sin texto en la imagen.

1. Una ciudad en el ecuador; el planeta frena en seco y personas, coches y un autobús salen volando hacia un lado con líneas de velocidad. Cámara: plano general que tiembla.
2. Una ola gigante barre un pueblo costero de casas blancas con tejados rojos. Cámara: contrapicado desde el suelo.
3. La Tierra desde el espacio: los océanos fluyen hacia los polos y aparece un anillo de continente verde en el ecuador. Cámara: órbita lenta.
4. La Tierra mitad día abrasador y mitad noche helada. Zoom a un niño de pie justo en la línea entre ambos, con un signo de interrogación flotando. Cámara: zoom desde el espacio al niño.

## G. Subtítulos
Integrados en el vídeo (palabra a palabra, a 92 px, con píldora amarilla). Archivo aparte: `subtitulos.srt`.

## H. Música y efectos
- **Música:** original, con pulso curioso a 112 BPM desde el segundo 0. Se corta en seco al frenar la Tierra y vuelve con fuerza en el vuelo. Después, un ambiente espacial, tic-tac en el calendario y un cierre con acordes mayores.
- **Efectos:** frenazo y golpe grave, ráfagas de aire, ola, tic-tac de meses, "pop" del visto bueno y brillo final.

## I. Descripción · J. Hashtags
Ver `descripcion.txt`.
Hashtags: `#curiosidades` `#curiosidadesdelmundo` `#curiosidadesaleatorias` `#curiosidadesentiktok` `#curiosimundo` `#tierra`

## K. Portada
El fotograma 0: la Tierra con **+1.600 KM/H** en amarillo y "¿Y SI LA TIERRA DEJARA DE GIRAR?".

---
## Control de calidad
| Dato | Estado | Fuente |
|---|---|---|
| Velocidad de rotación en el ecuador ≈ 1.670 km/h ("más de 1.600") | ✔ | [Esri](https://www.esri.com/about/newsroom/arcuser/what-would-happen-if-earth-stopped-spinning) |
| Todo seguiría moviéndose hacia el este, por inercia | ✔ (física básica: la Tierra gira hacia el este) | — |
| A largo plazo, el agua migra a los polos y emerge un megacontinente ecuatorial | ✔ modelo de Witold Fraczek (Esri) | [Esri](https://www.esri.com/about/newsroom/arcuser/what-would-happen-if-earth-stopped-spinning) · [Big Think](https://bigthink.com/strange-maps/475-the-day-the-earth-stood-still/) |
| Sin rotación, un día solar duraría un año (6 meses de luz y 6 de oscuridad) | ✔ | Consecuencia de que la Tierra solo daría la vuelta al Sol |
| "Prácticamente imposible" | ✔ no hay fuerza conocida capaz de pararla de golpe | [UCSB](https://legacy.geog.ucsb.edu/what-would-happen-if-the-earth-stopped-spinning/) |

- **Escenario hipotético:** está indicado en la descripción.
- **Etiqueta de IA:** actívala en TikTok (la voz es sintética).
