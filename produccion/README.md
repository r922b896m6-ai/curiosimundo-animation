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
4. **Generar la voz y los subtítulos:** `tools/producir.sh produccion/02-venus`. Si pasa del límite (35 s en "¿Y si…?" o 60 s en el resto), recorta el guion y repite.
5. **Completar `paquete.md`** con los tiempos reales de `escenas.md`: escenas, prompts, música, descripción, hashtags y portada.
6. **Animar:**
   - **Opción A:** en este repositorio con givemotion, como los reels de `reels/`. Pídeselo a Claude: "anima el vídeo 02".
   - **Opción B:** con los prompts de la sección F en tu herramienta de vídeo IA, y montaje en CapCut con `voz.mp3` y `subtitulos.srt`.
7. **Control de calidad** (lista de abajo), exportar en 1080×1920 y publicar con la etiqueta de contenido IA.

## Reglas de retención (desde el 15 de noviembre de 2026)

Salen de las métricas de los dos primeros vídeos publicados:

| Vídeo | Duración | Siguen a los 2 s | Siguen a los 5 s | Lo ven completo | Comentarios |
|---|---|---|---|---|---|
| "¿Y si respiráramos bajo el agua?" | 50 s | 55 % | 38 % | 9 % | 0 |
| "¿Y si desapareciera la Luna?" | 62 s | 43 % | 20 % | 2 % | 0 |

Casi todas las vistas vienen de "Para ti", así que el problema es la retención, no la distribución. Por eso, los vídeos de la serie **"¿Y si…?" duran 25–35 s** y **el resto, hasta 1 minuto**. En todos, el gancho llega en los primeros 2 s, hay un cambio visual cada 2–4 s, los subtítulos son grandes y van palabra a palabra, y el cierre es una pregunta directa.

## Vídeos largos de historia (YouTube)
- **Duración:** siempre unos **10 minutos**, en 16:9 y por capítulos.
- **Modelo:** `youtube/primera-guerra-mundial/`, con su librería de animación, la música por secciones (`tools/musica_historia.py`), la portada, la pantalla final y el resumen de 1 minuto para TikTok.
- **Serie:** "La historia en 10 minutos". La siguiente es la Segunda Guerra Mundial.

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
  - Grandes (unos 90 px) y animados palabra a palabra, en frases de 1 a 3 palabras; la palabra dicha va en una píldora amarilla.
  - Siempre visibles, a unos 1250 px de alto en vertical. Nada importante en los 380 px inferiores ni en los 220 px superiores.
- **Estructura:**
  - **Fotograma 0:** acción visual fuerte y el dato más impactante, con número, ya en pantalla. Nada de intros, logos ni títulos lentos.
  - **Gancho hablado:** dentro de los 2 primeros segundos.
  - **Ritmo:** un cambio de escena o movimiento cada 2–4 s (corte, zoom, texto animado).
  - **Final:** pregunta directa al público ("¿Qué harías tú…? Te leo en comentarios.").
- **Formato de serie:** "¿Y si…?" para los escenarios hipotéticos (25–35 s). Las curiosidades llevan su propio título y pueden durar hasta 1 min.
- **Hashtags:** `#curiosidades` `#curiosidadesdelmundo` `#curiosidadesaleatorias` `#curiosidadesentiktok` `#curiosimundo` y uno del tema. Evita #fyp y #viral.
- **Marca:** el logo CURIOSIMUNDO en blanco y amarillo en el cierre, siempre en la misma posición.
- **Voz:** `es-MX-JorgeNeural` frase a frase. Más rápida y aguda en los ganchos y lo divertido; más lenta y grave en lo serio.

## Control de calidad (antes de publicar)

- [ ] Cada cifra tiene una fuente fiable anotada; nada de estadísticas inventadas ni redondeos que cambien el sentido.
- [ ] Las afirmaciones dudosas se matizan ("unos", "la mayoría", "según…") o se quitan.
- [ ] No hay titulares engañosos: el título y el gancho se cumplen en el vídeo.
- [ ] Ortografía y gramática revisadas, incluidas tildes y signos ¿ ¡.
- [ ] La narración coincide con la escena que se ve (comprobar con `escenas.md`).
- [ ] Los subtítulos están sincronizados y no tapan nada importante.
- [ ] Duración: "¿Y si…?" entre 25 y 35 s (máximo 40); el resto, hasta 60 s.
- [ ] Dato con número en pantalla en el fotograma 0 y gancho hablado antes de los 2 s.
- [ ] Cambio visual cada 2–4 s; termina con una pregunta directa.
- [ ] Música libre de derechos o de la biblioteca comercial de TikTok.
- [ ] Etiqueta **"Contenido generado por IA"** activada en la plataforma si la voz o las imágenes son sintéticas. **No** se menciona la IA en la descripción (decisión del dueño del canal).

## Qué se automatiza y qué no

| Tarea | Automatizada |
|---|---|
| Narración con voz IA y tiempos por palabra | ✔ `tools/producir.sh` |
| Subtítulos sincronizados (SRT) y tiempos por escena | ✔ `tools/producir.sh` |
| Animación y render del vídeo | ✔ con givemotion, a petición ("anima el vídeo 02") |
| Música y efectos originales | ✔ sintetizados, a petición (ver `tools/musica_*.py`) |
| Investigación y guion | Claude los prepara; verifica las fuentes enlazadas |
| Publicar en TikTok | ✘ manual. Claude no publica ni pide contraseñas. |
