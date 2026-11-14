# Sistema de producción CURIOSIMUNDO

> Un mundo de cosas por descubrir.

## Estructura

```
produccion/
  README.md          ← este archivo: flujo, guía de estilo y control de calidad
  calendario.md      ← calendario semanal con fichas, datos y fuentes de cada vídeo
  plantilla/         ← plantilla vacía para cada vídeo nuevo
  01-pulpo/          ← un vídeo = una carpeta (NN-tema)
    paquete.md       ← entrega completa A–K + control de calidad
    guion.txt        ← guion fuente (una línea = una escena)
    voz.mp3/voz.json ← narración IA + tiempos por palabra (generados)
    subtitulos.srt   ← subtítulos sincronizados (generados)
    escenas.md       ← tiempos y subtítulos por escena (generados)
    descripcion.txt  ← texto para TikTok + hashtags
tools/
  producir.sh        ← guion.txt → voz.mp3 + voz.json + subtitulos.srt + escenas.md
  tts_seg.py         ← voz IA frase a frase (ritmo y tono por línea)
  subtitulos.py      ← subtítulos en SRT y tabla por escena
reels/               ← vídeos animados con givemotion (HTML → MP4)
```

## Flujo para cada vídeo

1. **Elegir el tema** del calendario y crear la carpeta: `cp -r produccion/plantilla produccion/02-venus`.
2. **Investigar y verificar** cada dato con al menos una fuente fiable (NASA, ESA, revistas científicas, museos, universidades). Apunta las fuentes en la tabla de control de calidad del paquete.
3. **Escribir `guion.txt`:** una línea por escena con el formato `velocidad|tono|pausa|texto`, por ejemplo `+6%|+2Hz|0.3|Y aquí viene lo curioso…`.
4. **Generar la voz y los subtítulos:** `tools/producir.sh produccion/02-venus`. Si el resultado pasa de 60 s, recorta el guion y repite.
5. **Completar `paquete.md`** con los tiempos reales de `escenas.md`: escenas, prompts, música, descripción, hashtags y portada.
6. **Animar:**
   - **Opción A:** en este repositorio con givemotion, como los reels de `reels/`. Pídeselo a Claude: "anima el vídeo 02".
   - **Opción B:** con los prompts de la sección F en tu herramienta de vídeo IA, y montaje en CapCut con `voz.mp3` y `subtitulos.srt`.
7. **Control de calidad** (lista de abajo), exportar en 1080×1920 y publicar con la etiqueta de contenido IA.

## Guía de estilo

- **Paleta:**

  | Uso | Color |
  |---|---|
  | Azul profundo (fondo) | #0B2A5B |
  | Azul medio | #1565C0 |
  | Blanco (texto) | #FFFFFF |
  | Amarillo (acento, palabra clave, píldora de subtítulos) | #FFD23F |
  | Rojo (solo para alertas) | #E5484D |

- **Tipografía:**
  - Titulares: Bebas Neue (o Montserrat Black).
  - Subtítulos: Inter o Montserrat de grosor 800–900.
- **Subtítulos:**
  - Frases de 1 a 3 palabras; la palabra dicha va en una píldora amarilla.
  - Siempre visibles, a unos 1250 px de alto en vertical. Nada importante en los 380 px inferiores ni en los 220 px superiores.
- **Estructura:**
  - Gancho visual y hablado en los primeros 3 s.
  - Una idea por escena, con un cambio visual cada 3–7 s.
  - Final con una pregunta abierta para comentar.
- **Marca:** el logo CURIOSIMUNDO en blanco y amarillo en el cierre, siempre en la misma posición.
- **Voz:** `es-MX-JorgeNeural` frase a frase. Más rápida y aguda en los ganchos y lo divertido; más lenta y grave en lo serio.

## Control de calidad (antes de publicar)

- [ ] Cada cifra tiene una fuente fiable anotada; nada de estadísticas inventadas ni redondeos que cambien el sentido.
- [ ] Las afirmaciones dudosas se matizan ("unos", "la mayoría", "según…") o se quitan.
- [ ] No hay titulares engañosos: el título y el gancho se cumplen en el vídeo.
- [ ] Ortografía y gramática revisadas, incluidas tildes y signos ¿ ¡.
- [ ] La narración coincide con la escena que se ve (comprobar con `escenas.md`).
- [ ] Los subtítulos están sincronizados y no tapan nada importante.
- [ ] Duración entre 40 y 60 s.
- [ ] Música libre de derechos o de la biblioteca comercial de TikTok.
- [ ] Etiqueta **"Contenido generado por IA"** activada en TikTok si la voz o las imágenes son sintéticas, y mención en la descripción.

## Qué se automatiza y qué no

| Tarea | Automatizada |
|---|---|
| Narración con voz IA y tiempos por palabra | ✔ `tools/producir.sh` |
| Subtítulos sincronizados (SRT) y tiempos por escena | ✔ `tools/producir.sh` |
| Animación y render del vídeo | ✔ con givemotion, a petición ("anima el vídeo 02") |
| Música y efectos originales | ✔ sintetizados, a petición (ver `tools/musica_*.py`) |
| Investigación y guion | Claude los prepara; verifica las fuentes enlazadas |
| Publicar en TikTok | ✘ manual. Claude no publica ni pide contraseñas. |
