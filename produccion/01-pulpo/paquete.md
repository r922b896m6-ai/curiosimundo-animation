# CURIOSIMUNDO · Vídeo 01 · El pulpo

**Categoría:** animales y naturaleza · **Duración:** 58,6 s · **Formato:** 9:16 (1080×1920)
**Publicación prevista:** día 1 del calendario · **Estado:** guion, narración y subtítulos listos; falta animar y montar.

Archivos de esta carpeta:
- `guion.txt`: guion fuente. Cada línea es una escena, con su velocidad, tono y pausa para la voz IA.
- `voz.mp3`: narración generada con voz IA (`es-MX-JorgeNeural`).
- `voz.json`: tiempos de cada palabra.
- `subtitulos.srt`: subtítulos sincronizados, para importar en CapCut o en el editor de TikTok.
- `escenas.md`: tiempos exactos y subtítulos de cada escena (generado).
- `descripcion.txt`: descripción y hashtags, listos para copiar.

Para regenerar la voz y los subtítulos después de editar el guion: `tools/producir.sh produccion/01-pulpo`

---

## A. Título

**El animal que piensa con los brazos 🐙**

Alternativas para pruebas A/B:
- Tres corazones y sangre azul: así es el pulpo
- Este animal tiene tres corazones (y los usa raro)

## B. Gancho inicial (0–3 s)

> **"Tres corazones. Sangre azul."** (termina en el segundo 2,9)

Primer fotograma: un pulpo enorme ocupa la pantalla con tres corazones latiendo en su interior y el texto **3 CORAZONES**. La frase se completa en el segundo 4,9 con "Y piensa con los brazos".

## C. Guion completo

1. Tres corazones. Sangre azul. Y piensa con los brazos.
2. Es el pulpo, y es más raro de lo que crees.
3. Primero, los corazones: dos bombean sangre a las branquias y el tercero, al resto del cuerpo.
4. Y aquí viene lo curioso: ese tercer corazón deja de latir cuando nada. Por eso los pulpos prefieren arrastrarse.
5. Su sangre es azul porque transporta el oxígeno con cobre en lugar de hierro, gracias a una proteína llamada hemocianina.
6. Pero lo más alucinante es su cerebro… o mejor dicho, sus cerebros.
7. Tiene unos quinientos millones de neuronas, y la mayoría no está en la cabeza, sino repartida por sus ocho brazos.
8. Cada brazo puede reaccionar por su cuenta… y hasta saborear lo que toca con sus ventosas.
9. Cambia de color y de textura en un instante, y puede colarse por cualquier hueco por donde quepa su pico, la única parte dura de su cuerpo.
10. Si pudieras tener uno de sus poderes, ¿cuál elegirías? Te leo en los comentarios.

## D. Narración lista para voz IA

La narración ya está generada en `voz.mp3`. Para generarla con otra herramienta (ElevenLabs, CapCut, etc.), usa este texto y estas indicaciones:

| Escena | Indicación de voz | Texto |
|---|---|---|
| 1 | rápida (+12 %), tono alto, intriga | Tres corazones. Sangre azul. Y piensa con los brazos. |
| 2 | ritmo normal, cómplice | Es el pulpo, y es más raro de lo que crees. |
| 3 | explicativa, clara | Primero, los corazones: dos bombean sangre a las branquias y el tercero, al resto del cuerpo. |
| 4 | sube la energía en "lo curioso" | Y aquí viene lo curioso: ese tercer corazón deja de latir cuando nada. Por eso los pulpos prefieren arrastrarse. |
| 5 | clara, acentuar "cobre" | Su sangre es azul porque transporta el oxígeno con cobre en lugar de hierro, gracias a una proteína llamada hemocianina. |
| 6 | pausa en los puntos suspensivos | Pero lo más alucinante es su cerebro… o mejor dicho, sus cerebros. |
| 7 | firme, acentuar "ocho brazos" | Tiene unos quinientos millones de neuronas, y la mayoría no está en la cabeza, sino repartida por sus ocho brazos. |
| 8 | divertida | Cada brazo puede reaccionar por su cuenta… y hasta saborear lo que toca con sus ventosas. |
| 9 | ágil | Cambia de color y de textura en un instante, y puede colarse por cualquier hueco por donde quepa su pico, la única parte dura de su cuerpo. |
| 10 | cercana, pregunta abierta | Si pudieras tener uno de sus poderes, ¿cuál elegirías? Te leo en los comentarios. |

Pronunciación: "hemocianina" se dice he-mo-cia-NI-na.

## E. Escenas numeradas (tiempos reales de la narración)

| # | Tiempo | Qué se ve | Texto en pantalla |
|---|---|---|---|
| 1 | 0,0–5,2 s | Pulpo gigante de frente; dentro, 3 corazones que laten; su piel se vuelve azul; un brazo se ilumina como un circuito | 3 CORAZONES · SANGRE AZUL |
| 2 | 5,2–8,3 s | Tarjeta de presentación: el pulpo posa sobre una roca | EL PULPO |
| 3 | 8,3–14,3 s | Infografía del cuerpo transparente: 2 corazones en las branquias y 1 central, con flechas de flujo | 2 + 1 CORAZONES |
| 4 | 14,3–21,6 s | El pulpo nada a chorro: el corazón central se para (línea de pulso plana); después se arrastra feliz y el corazón vuelve a latir | ¡SE PARA AL NADAR! |
| 5 | 21,6–28,6 s | Zoom a una gota de sangre: moléculas con átomo de cobre (Cu) azul frente a hierro (Fe) rojo | COBRE, NO HIERRO |
| 6 | 28,6–33,0 s | Cabeza del pulpo con un cerebro que se multiplica en 9 puntos de luz (cabeza + 8 brazos) | SUS CEREBROS |
| 7 | 33,0–39,9 s | Contador de neuronas hasta 500 millones; la mayoría de las luces bajan hacia los brazos | 500 MILLONES DE NEURONAS |
| 8 | 39,9–45,1 s | Primer plano de un brazo que toca un cangrejo y "saborea": iconos de sabor que salen de las ventosas | SABOREA CON LAS VENTOSAS |
| 9 | 45,1–53,0 s | Camuflaje sobre una roca y coral; después se cuela por un tubo estrecho, con el pico marcado como lo único rígido | SOLO EL PICO ES DURO |
| 10 | 53,0–59,6 s | 4 tarjetas de poderes (3 corazones · camuflaje · brazos que piensan · colarse) y logo CURIOSIMUNDO | ¿CUÁL ELEGIRÍAS? |

## F. Prompts de animación por escena

**Estilo base (va delante de cada prompt):**
> Animación 2D vectorial plana estilo motion graphics educativo, formato vertical 9:16, paleta azul profundo #0B2A5B a #1565C0, blanco #FFFFFF y amarillo #FFD23F; el pulpo es amarillo anaranjado #FFB547 con ventosas crema; contornos suaves, sombras planas, partículas de burbujas, iluminación submarina con rayos de luz. Sin texto dentro de la imagen.

Escribe los textos en pantalla en el editor, no en el generador: las herramientas de vídeo con IA suelen deformar las letras.

1. **Gancho (5 s):** Primer plano frontal de un pulpo amigable y expresivo que llena el encuadre sobre fondo azul profundo. Su cuerpo es semitransparente y deja ver tres corazones rojos que laten en secuencia. Una ola de color azul recorre su piel. Uno de sus brazos se ilumina con líneas amarillas como un circuito eléctrico. Cámara: empuje rápido hacia el pulpo (push-in) con un leve temblor de energía. Burbujas que suben.
2. **Presentación (3 s):** El pulpo se posa sobre una roca del fondo marino, con algas suaves meciéndose. Se acomoda y guiña un ojo. Cámara: plano medio, deriva lenta hacia la derecha. Rayos de luz que bajan desde la superficie.
3. **Los corazones (6 s):** Vista lateral de infografía: el cuerpo del pulpo se vuelve transparente como un diagrama. Dos pequeños corazones junto a las branquias y un corazón central más grande. Flechas animadas muestran la sangre que va a las branquias y luego al resto del cuerpo. Cámara: fija, con un zoom suave al corazón central al final.
4. **Se para al nadar (7 s):** El pulpo sale disparado a chorro, como un cohete, dejando una estela de burbujas. Arriba aparece un monitor cardíaco cuya línea se vuelve plana. Luego el pulpo se posa y camina arrastrando sus brazos por la arena, y la línea vuelve a latir. Cámara: seguimiento lateral (tracking) del nado y después plano general a ras del suelo.
5. **Sangre azul (7 s):** Zoom extremo a un vaso sanguíneo: glóbulos azules fluyen. Aparece una molécula estilizada con un átomo central brillante de cobre (azul) junto a otra con átomo de hierro (rojo) que se desvanece. Cámara: zoom continuo hacia dentro (de macro a micro) y luego un giro lento alrededor de la molécula.
6. **Sus cerebros (4 s):** Silueta del pulpo en azul oscuro. En la cabeza se enciende un cerebro de luz amarilla que se divide en nueve puntos brillantes: uno en la cabeza y ocho que viajan a cada brazo. Cámara: plano general centrado, leve empuje.
7. **500 millones de neuronas (7 s):** Miles de puntos de luz (neuronas) llenan la silueta del pulpo. La mayoría fluye desde la cabeza hacia los ocho brazos como un río de luciérnagas, dejando la cabeza con menos luces. Cámara: panorámica vertical de la cabeza a la punta de los brazos.
8. **Saborea con las ventosas (5 s):** Primer plano de un brazo que se acerca a un pequeño cangrejo. Al tocarlo, las ventosas se iluminan y salen pequeñas ondas de "sabor". El brazo reacciona solo, mientras la cabeza del pulpo, al fondo, sigue distraída mirando a otro lado. Cámara: macro, enfoque selectivo en las ventosas.
9. **Camuflaje y escape (8 s):** El pulpo cambia de color y de textura hasta fundirse con una roca con coral. Después se estira y se cuela por un tubo estrecho; su pico se resalta con un contorno amarillo como la única parte rígida. Cámara: plano fijo para el camuflaje y luego seguimiento del pulpo por el tubo, con un ligero zoom al pico.
10. **Cierre (6 s):** Cuatro tarjetas redondeadas aparecen en cuadrícula sobre fondo azul con un icono en cada una: tres corazones, camaleón/camuflaje, brazo con cerebro, pulpo pasando por un tubo. El pulpo señala las tarjetas con sus brazos. Al final, el logotipo CURIOSIMUNDO en blanco y amarillo. Cámara: plano fijo con un leve rebote de las tarjetas.

## G. Subtítulos por escena

Archivo listo para importar: `subtitulos.srt`, con frases de 1 a 3 palabras y tiempos exactos de la voz. El detalle por escena está en `escenas.md`.

Estilo recomendado: Inter o Montserrat Black, de 80 a 90 px, blanco con sombra. La palabra que se está diciendo va sobre una píldora amarilla #FFD23F con texto azul oscuro. Colócalos centrados a unos 1250 px de alto, fuera de la zona inferior de la app (los 380 px de abajo).

## H. Música y efectos de sonido

- **Música:** ambiente submarino suave, curioso y algo juguetón (pizzicato, marimba o sintetizador con burbujas), a unos 90–100 BPM, bajo la voz (−18 a −22 dB respecto a la narración). Usa música libre de derechos o de la biblioteca comercial de TikTok.
- **Efectos:**
  - **Escena 1:** tres latidos sincronizados con los tres corazones y un "whoosh" en el empuje de cámara.
  - **Escena 4:** un chorro de agua al nadar, el pitido plano del monitor y el latido que vuelve.
  - **Escena 5:** un "zoom" con brillo y un tintineo metálico en "cobre".
  - **Escena 6:** nueve "pops" suaves, uno por punto de luz.
  - **Escena 7:** un "riser" (subida) mientras cuenta el número.
  - **Escena 8:** un "blip" al tocar el cangrejo.
  - **Escena 9:** un "squish" elástico al colarse.
  - **Escena 10:** cuatro "pops" para las tarjetas y el golpe del logo.

## I. Descripción para TikTok

Ver `descripcion.txt` (lista para copiar):

> ¿Sabías que el pulpo tiene 3 corazones, sangre azul y que la mayoría de sus neuronas está en sus brazos? 🐙💙 Uno de sus corazones incluso deja de latir cuando nada.
> ¿Qué poder del pulpo elegirías tú? Te leo 👇
> 🎙️ Narración generada con IA.

## J. Hashtags

`#pulpo` `#animales` `#curiosidades` `#ciencia` `#aprendeentiktok`

## K. Portada recomendada

- **Imagen:** el fotograma del pulpo de frente con los tres corazones visibles (escena 1, hacia el segundo 1,5).
- **Texto principal:** **3 CORAZONES** en amarillo #FFD23F, en mayúsculas gruesas, en el tercio superior.
- **Texto secundario:** "y piensa con los brazos" en blanco, debajo.
- **Fondo:** azul profundo con rayos de luz.
- **Marca:** logo pequeño CURIOSIMUNDO abajo a la izquierda, por encima de la zona de la interfaz.

---

## Control de calidad

**Datos verificados:**

| Dato del guion | Estado | Fuente |
|---|---|---|
| 3 corazones: 2 branquiales + 1 sistémico | ✔ verificado | Smithsonian Magazine |
| El corazón sistémico deja de latir al nadar; por eso prefieren arrastrarse | ✔ verificado | Smithsonian Magazine |
| Sangre azul por la hemocianina, que usa cobre en lugar del hierro de la hemoglobina | ✔ verificado | Scientific American, National Geographic |
| Unos 500 millones de neuronas, la mayoría (cerca de dos tercios) en los brazos | ✔ verificado (cifras aproximadas) | Smithsonian Magazine; el guion dice "unos" y "la mayoría" a propósito |
| Saborean con las ventosas (quimiorreceptores; estudio de Harvard en *Cell*, 2020) | ✔ verificado | ScienceAlert, NYSCF |
| Cambian de color y de textura (cromatóforos y papilas) | ✔ conocimiento establecido | — |
| Pueden pasar por cualquier hueco por donde quepa el pico, su única parte dura | ✔ dato ampliamente documentado | — |

**Notas de precisión:**
- El guion no usa la frase "nueve cerebros" como dato literal; dice "o mejor dicho, sus cerebros". Así se evita exagerar: los brazos tienen ganglios nerviosos, no cerebros completos.
- **Coherencia:** la narración y las escenas coinciden con los tiempos de `escenas.md`.
- **Gramática:** revisada.
- **Etiqueta de IA:** al publicar, activa en TikTok la etiqueta **"Contenido generado por IA"** (Más opciones → etiqueta de contenido de IA). La voz es sintética, y también lo serán las escenas si las generas con IA.

Fuentes:
- [Smithsonian Magazine: Ten wild facts about octopuses](https://www.smithsonianmag.com/science-nature/ten-wild-facts-about-octopuses-they-have-three-hearts-big-brains-and-blue-blood-7625828/)
- [Scientific American: blue blood and cold water](https://www.scientificamerican.com/blog/octopus-chronicles/octopuses-survive-sub-zero-temps-thanks-to-specialized-blue-blood/)
- [National Geographic: octopus blood](https://www.nationalgeographic.com/animals/article/150312-blood-antarctica-octopus-animals-science-colors)
- [ScienceAlert: octopuses taste with their arms](https://www.sciencealert.com/octopus-can-taste-things-with-their-eight-arms-here-s-how)
- [NYSCF: How octopuses taste by touch](https://www.nyscf.org/?p=16033)
