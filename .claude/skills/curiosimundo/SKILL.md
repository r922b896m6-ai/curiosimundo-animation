---
name: curiosimundo
description: Reglas del canal de TikTok CURIOSIMUNDO para guiones, narración, subtítulos y vídeos givemotion. Úsala siempre que se cree, edite o anime un vídeo, guion, calendario, descripción o hashtags de CURIOSIMUNDO.
---

# CURIOSIMUNDO: reglas del canal

Eslogan: "Un mundo de cosas por descubrir". Narración en español, 9:16.

## Retención (obligatorio, según las métricas de los primeros vídeos)
- **Duración:** depende del tipo de vídeo (decisión del dueño del canal, 15 de noviembre de 2026):
  - **Serie "¿Y si…?"** (hipotéticos): 25–35 s, máximo 40. Los dos primeros, de 50–62 s, perdieron a casi toda la audiencia antes de la mitad.
  - **Resto de vídeos** (curiosidades, historia, animales, misterios…): hasta 1 minuto (unos 50–60 s).
  - Todas las demás reglas de retención valen para los dos tipos.
  - **Vídeos largos de historia para YouTube:** siempre de unos **10 minutos**, en 16:9 (1920×1080), divididos en capítulos.
    Reutiliza `youtube/primera-guerra-mundial/lib/` (uniformes por país, batallas que terminan dentro de la trinchera enemiga
    cuerpo a cuerpo y sin sangre, mapas, tanques, aviones, barcos, subtítulos) y su flujo: `render_all.sh`, `paquete.md`,
    portada de 1280×720, pantalla final de 20 s (salvo que el dueño diga lo contrario) y resumen de 1 minuto para TikTok.
  - **Descripción de YouTube** (decisión del dueño del canal): **máximo 100 caracteres, hashtags incluidos**
    (`descripcion_youtube.txt`). Los capítulos, fuentes y nota de IA van aparte en `comentario_fijado.txt`.
  - **Desenlace de las batallas** (decisión del dueño del canal): en las **batallas de trincheras**, los atacantes entran en la trinchera
    enemiga y luchan cuerpo a cuerpo. En las que **no son de trincheras** (guerra de movimientos, ciudades, desiertos, playas, mar, aire)
    no hace falta el cuerpo a cuerpo; varía el desenlace según la historia: enemigos capturados (manos arriba, apuntados por el otro
    bando), retiradas, rendiciones, avance de tanques, posiciones tomadas, aviones o barcos derribados o hundidos. Siempre sin sangre y
    con tono informativo.
  - **Serie en curso:** "La historia en 10 minutos". Hecho: Primera Guerra Mundial. Siguiente: Segunda Guerra Mundial. Para después,
    ver qué batalla piden más en los comentarios.
- **Fotograma 0:** acción visual fuerte y el dato más impactante, con número, ya en pantalla. Nada de intros, logos ni títulos lentos. La frase gancho se oye dentro de los primeros 2 s.
- **Ritmo:** un cambio de escena o movimiento cada 2–4 s (corte, zoom, texto animado).
- **Subtítulos:** grandes (unos 90 px), palabra a palabra con píldora amarilla, centrados a unos 1250 px de alto, fuera de la interfaz de TikTok (abajo y a la derecha).
- **Cierre:** pregunta directa al público ("¿Qué harías tú…? Te leo en comentarios.").
- **Serie:** "¿Y si…?" solo para escenarios hipotéticos. No fuerces el "¿Y si…?" en una curiosidad, porque cambiaría la duración que le toca.
- **Hashtags:** `#curiosidades #curiosidadesdelmundo #curiosidadesaleatorias #curiosidadesentiktok #curiosimundo` y uno del tema. Sin #fyp ni #viral.

## Estilo
- **Paleta:** azul #0B2A5B → #1565C0, blanco y amarillo #FFD23F; rojo #E5484D solo para alertas.
- **Tipografía:** Bebas Neue en titulares, Inter 850 en subtítulos.
- **Voz:** `es-MX-JorgeNeural`, frase a frase (`guion.txt` con `velocidad|tono|pausa|texto`): rápida y aguda en el gancho, cercana en la pregunta.

## Datos
- Verifica cada cifra con una fuente fiable y anótala en la tabla de control de calidad del paquete.
- Matiza lo aproximado ("unos", "la mayoría"). En los experimentos mentales, aclara que son hipotéticos.
- Recomienda la etiqueta "Contenido generado por IA" de TikTok.
- No digas nunca que algo se ha publicado si no se ha hecho, y no pidas contraseñas.

## Flujo
1. `produccion/NN-tema/` a partir de `produccion/plantilla/`.
2. `guion.txt` → `tools/producir.sh produccion/NN-tema` (voz, `voz.json`, `subtitulos.srt`, `escenas.md`).
3. `video.html` con givemotion (lee la skill de givemotion), con la música y los efectos sintetizados en `tools/musica_*.py`.
4. `npx givemotion check`, `snapshot` y `render`, y completar `paquete.md` (de la A a la K y el control de calidad).

Ejemplo de referencia que ya cumple las reglas: `produccion/02-tierra-sin-girar/`.
Guía completa: `produccion/README.md`. Calendario: `produccion/calendario.md`.
