# CURIOSIMUNDO · Vídeo 01 · ¿Y si pensaras con los brazos? (el pulpo)

**Categoría:** animales · **Duración:** 28,3 s de narración (unos 29 s de vídeo) · **Formato:** 9:16 (1080×1920)
**Estado:** guion, narración y subtítulos listos (versión de unos 30 s, con las reglas de retención); falta animar.

Archivos:
- `guion.txt`: guion fuente.
- `voz.mp3`: narración IA.
- `voz.json`: tiempos por palabra.
- `subtitulos.srt`: subtítulos sincronizados.
- `escenas.md`: tiempos por escena.
- `descripcion.txt`: texto para TikTok.

Para regenerar la voz y los subtítulos: `tools/producir.sh produccion/01-pulpo`

---

## A. Título
**¿Y si pensaras con los brazos? 🐙**
Alternativas para pruebas A/B:
- Tres corazones y sangre azul
- El animal con el cerebro en los brazos

## B. Gancho (0–2 s)
> **"Tres corazones."** (0,3–1,4 s) · **"Sangre azul."** (2,0–2,9 s)

**Fotograma 0:** el pulpo ya está en pantalla con tres corazones latiendo dentro y el texto **3 CORAZONES**. No hay intro ni logo.

## C. Guion completo
1. Tres corazones. Sangre azul. Y piensa con los brazos.
2. Dos corazones mueven la sangre por las branquias y el tercero, por el resto del cuerpo… y se para cuando nada.
3. Su sangre es azul porque usa cobre, no hierro, para llevar el oxígeno.
4. Y de sus quinientos millones de neuronas, la mayoría está en sus ocho brazos: cada uno reacciona solo… y saborea lo que toca.
5. Si pudieras tener uno de sus poderes, ¿cuál elegirías? Te leo en comentarios.

## D. Narración para voz IA
Ya generada en `voz.mp3` (`es-MX-JorgeNeural`, frase a frase):

| Línea | Velocidad y tono | Intención |
|---|---|---|
| 1 | +12 %, +3 Hz | intriga, rápida |
| 2 | +10 % | explicativa; pausa antes de "y se para cuando nada" |
| 3 | +9 % | clara, acento en "cobre" |
| 4 | +9 %, +2 Hz | asombro en "ocho brazos"; divertida en "saborea" |
| 5 | +7 %, +4 Hz | cercana, pregunta directa |

## E. Escenas (un cambio cada 2–4 s; tiempos reales)
| # | Tiempo | Qué se ve | Texto en pantalla |
|---|---|---|---|
| 1a | 0,0–1,9 s | Pulpo de frente con 3 corazones latiendo dentro | **3 CORAZONES** |
| 1b | 1,9–3,5 s | Ola de color azul por su piel; zoom a una gota azul | **SANGRE AZUL** |
| 1c | 3,5–5,1 s | Un brazo se ilumina como un circuito | **PIENSA CON LOS BRAZOS** |
| 2a | 5,1–8,4 s | Infografía: 2 corazones en las branquias + 1 central, con flechas de flujo | **2 + 1** |
| 2b | 8,4–11,1 s | Nada a chorro → el monitor cardíaco se vuelve plano | **¡SE PARA AL NADAR!** |
| 3 | 11,1–15,5 s | Molécula: Cu (azul) brilla, Fe (rojo) se apaga | **COBRE, NO HIERRO** |
| 4a | 15,5–18,0 s | Contador de neuronas que sube a 500.000.000 | **500 MILLONES** |
| 4b | 18,0–19,8 s | Las luces bajan de la cabeza a los 8 brazos | **EN LOS BRAZOS** |
| 4c | 19,8–23,0 s | Un brazo toca un cangrejo, las ventosas brillan y salen ondas de "sabor" | **SABOREA AL TOCAR** |
| 5 | 23,0–29,0 s | 4 tarjetas de poderes + el pulpo señalándolas; logo CURIOSIMUNDO | **¿CUÁL ELEGIRÍAS?** |

## F. Prompts de animación
**Estilo base:**
> Animación 2D vectorial plana estilo motion graphics educativo, vertical 9:16, paleta azul profundo #0B2A5B a #1565C0, blanco y amarillo #FFD23F; pulpo amarillo anaranjado #FFB547 con ventosas crema; burbujas y rayos de luz submarinos; movimiento enérgico y cortes rápidos. Sin texto dentro de la imagen.

- **1a (2 s):** Primer plano frontal de un pulpo expresivo que ya llena el encuadre en el primer fotograma. Su cuerpo semitransparente deja ver tres corazones rojos que laten en secuencia. Cámara: empuje rápido (push-in) con un pequeño rebote.
- **1b (1,6 s):** Una ola de color azul eléctrico recorre su piel. Corte a una macro de una gota azul que brilla. Cámara: zoom rápido.
- **1c (1,6 s):** Uno de sus brazos se ilumina con líneas amarillas como un circuito que va de la ventosa a la punta. Cámara: barrido (whip) hacia el brazo.
- **2a (3 s):** El cuerpo se vuelve un diagrama: dos corazones pequeños junto a las branquias y uno central grande, con flechas de sangre animadas. Cámara: fija, zoom final al corazón central.
- **2b (2,7 s):** El pulpo sale disparado a chorro con estela de burbujas. Arriba, un monitor cardíaco cuya línea se vuelve plana. Cámara: seguimiento lateral rápido.
- **3 (4,4 s):** Zoom de macro a micro dentro de un vaso sanguíneo. Una molécula estilizada con un átomo de cobre azul que brilla y otra con hierro rojo que se desvanece. Cámara: zoom continuo y giro de 90°.
- **4a (2,5 s):** La silueta del pulpo se llena de miles de puntos de luz (neuronas) mientras un contador grande sube. Cámara: leve empuje.
- **4b (1,8 s):** La mayoría de las luces fluye de la cabeza a los ocho brazos como un río de luciérnagas. Cámara: panorámica vertical rápida hacia abajo.
- **4c (3,2 s):** Macro de un brazo que toca un cangrejo pequeño; las ventosas se iluminan y emiten ondas. La cabeza, al fondo, mira hacia otro lado (el brazo actúa solo). Cámara: enfoque selectivo y pequeño zoom.
- **5 (6 s):** Cuatro tarjetas redondeadas aparecen con rebote en cuadrícula, cada una con un icono: tres corazones, camuflaje, brazo con cerebro, pulpo pasando por un tubo. El pulpo las señala. Al final, logo CURIOSIMUNDO en blanco y amarillo. Cámara: fija.

## G. Subtítulos
Archivo listo: `subtitulos.srt` (35 frases sincronizadas). Detalle por escena: `escenas.md`.
**Estilo:**
- Montserrat o Inter Black de 90 px, blancos con sombra.
- La palabra dicha va en una píldora amarilla #FFD23F con texto azul.
- Posición: centrados a unos 1250 px de alto, fuera de la interfaz de TikTok (abajo y a la derecha).

## H. Música y efectos
- **Música:** submarina curiosa y con ritmo (marimba o pluck y bajo suave, 100–110 BPM), que empieza en el segundo 0 y va bajo la voz.
- **Efectos:**
  - **1a:** tres latidos.
  - **1c:** "zap" eléctrico.
  - **2b:** chorro de agua y pitido plano del monitor.
  - **3:** tintineo metálico en "cobre".
  - **4a:** "riser" del contador.
  - **4c:** "blip" al tocar.
  - **5:** cuatro "pops" para las tarjetas.

## I. Descripción para TikTok
Ver `descripcion.txt`.

## J. Hashtags
`#curiosidades` `#curiosidadesdelmundo` `#curiosidadesaleatorias` `#curiosidadesentiktok` `#curiosimundo` `#pulpo`

## K. Portada
El fotograma 1a con **3 CORAZONES** en amarillo y gran tamaño, y debajo "¿y si pensaras con los brazos?" en blanco, sobre fondo azul.

---
## Control de calidad
| Dato | Estado | Fuente |
|---|---|---|
| 3 corazones (2 branquiales + 1 sistémico) | ✔ | [Smithsonian](https://www.smithsonianmag.com/science-nature/ten-wild-facts-about-octopuses-they-have-three-hearts-big-brains-and-blue-blood-7625828/) |
| El corazón sistémico se detiene al nadar | ✔ | [Smithsonian](https://www.smithsonianmag.com/science-nature/ten-wild-facts-about-octopuses-they-have-three-hearts-big-brains-and-blue-blood-7625828/) |
| Sangre azul: hemocianina, con cobre en lugar de hierro | ✔ | [Scientific American](https://www.scientificamerican.com/blog/octopus-chronicles/octopuses-survive-sub-zero-temps-thanks-to-specialized-blue-blood/) |
| Unos 500 millones de neuronas, la mayoría en los brazos | ✔ (aproximado) | [Smithsonian](https://www.smithsonianmag.com/science-nature/ten-wild-facts-about-octopuses-they-have-three-hearts-big-brains-and-blue-blood-7625828/) |
| Saborean al tocar con las ventosas (*Cell*, 2020) | ✔ | [ScienceAlert](https://www.sciencealert.com/octopus-can-taste-things-with-their-eight-arms-here-s-how) |

- **Precisión del guion:** dice "unos" 500 millones y "la mayoría", sin cifras exactas, y "cada uno reacciona solo" en lugar de "nueve cerebros".
- **Etiqueta de IA:** activa en TikTok "Contenido generado por IA" (la voz es sintética).
