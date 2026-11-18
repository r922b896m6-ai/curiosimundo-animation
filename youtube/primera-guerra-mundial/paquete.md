# CURIOSIMUNDO · YouTube · La Primera Guerra Mundial (historia completa)

**Formato:** 16:9, 1920×1080, 30 fps · **Duración:** 10:02 · **Vídeo final:** `out/primera-guerra-mundial.mp4`
**Estilo:** animación de siluetas con uniformes de época por país, mapas de 1914 a partir de Natural Earth (fronteras aproximadas), sin sangre y con tono informativo.

Archivos:
- `cap0/` … `cap7/`: cada capítulo contiene:
  - `guion.txt`, `voz.mp3`, `voz.json`: guion y narración IA (`es-MX-JorgeNeural`);
  - `video.html`: animación givemotion;
  - `audio.json`, `musica.mp3`, `sfx.mp3`: música y efectos originales, generados con `tools/musica_historia.py`.
- `lib/`: librería compartida:
  - `cm.js`: uniformes, batallas, mapas, tanques, aviones, barcos y subtítulos;
  - `cm.css`: estilos;
  - `europa.json`: mapa proyectado de 1914.
- `subtitulos.srt`: subtítulos de todo el vídeo, para subirlos a YouTube como CC.
- `render_all.sh`: renderiza los 8 capítulos y los une.

## Título
**La Primera Guerra Mundial en 10 minutos: causas, batallas y final (animado)**

Alternativas:
- La Primera Guerra Mundial explicada: de Sarajevo al armisticio
- Así fue la Primera Guerra Mundial (1914–1918) | Historia animada

## Capítulos (para pegar en la descripción de YouTube)
```
0:00 Introducción
0:16 1914 · Las causas y la chispa (Sarajevo)
1:44 1914 · La guerra de movimientos (Marne, Tannenberg, tregua de Navidad)
3:06 1915 · Estancados (gas en Ypres, Galípoli, Lusitania)
4:25 1916 · El año del desgaste (Verdún, Somme, Jutlandia)
6:02 1917 · El año que lo cambió todo (Rusia, Estados Unidos, Caporetto)
7:19 1918 · La última ofensiva y el armisticio
8:58 Las consecuencias
```

## Descripción
En `descripcion_youtube.txt` (completa, con capítulos y fuentes; sin mencionar la IA).

## Miniatura recomendada
- **Imagen:** a la izquierda, un soldado francés de 1914 (abrigo azul y pantalones rojos); a la derecha, uno alemán con casco de pincho.
- **Fondo:** explosión de artillería, en tonos sepia oscuros.
- **Texto:** **"1914–1918"** en amarillo #FFD23F y **"EN 10 MINUTOS"** en blanco, con letra gruesa.
- **Marca:** logo pequeño de CURIOSIMUNDO.
- **Fotograma de base:** cap0, segundo 1,5, o la escena de uniformes de cap2.

## Control de calidad (datos)
| Dato | Fuente / nota |
|---|---|
| Unos 65 millones de soldados movilizados | Cifra habitual (Britannica: unos 65 millones) |
| Sarajevo, 28 de junio de 1914; declaración a Serbia, 28 de julio | Hechos establecidos |
| Rusia moviliza (30 jul); Alemania declara la guerra a Rusia (1 ago) y a Francia (3 ago); invasión de Bélgica y entrada británica (4 ago) | Hechos establecidos |
| Marne, 6–12 sep 1914; avance alemán a menos de 50 km de París; taxis del Marne | Hechos establecidos |
| Tannenberg, finales de agosto de 1914 | 26–30 ago |
| Unos 700 km de trincheras del mar del Norte a Suiza | Cifra habitual (entre unos 640 y 760 km según la fuente) |
| Tregua de Navidad de 1914 | Hecho documentado |
| Gas cloro en Ypres, abril de 1915 | 22 abr 1915 |
| Galípoli: abril de 1915 – enero de 1916; Mustafá Kemal | Hechos establecidos |
| Italia entra con los aliados en mayo de 1915 | Tratado de Londres |
| Lusitania: 1.198 muertos, 128 estadounidenses (7 may 1915) | Hecho establecido |
| Verdún, unos 10 meses, unas 700.000 bajas | [HistoryNet](https://historynet.com/costliest-battles-and-campaigns-of-world-war-i/) · [History Hit](https://www.historyhit.com/biggest-battles-world-war-one/) (las estimaciones varían) |
| Somme: más de 57.000 bajas británicas el primer día; más de 1 millón en total | Primer día: 57.470 · total: entre 1,1 y 1,2 millones |
| Primer tanque, 15 sep 1916 (Flers-Courcelette) | Hecho establecido |
| Jutlandia: los británicos pierden más barcos; la flota alemana casi no vuelve a salir a mar abierto | Hecho establecido |
| Brusílov, 1916 | [Britannica](https://britannica.com/event/Brusilov-Offensive-1916) |
| Barón Rojo (Manfred von Richthofen) | Hecho establecido |
| El zar abdica en marzo de 1917; los bolcheviques toman el poder en noviembre; Brest-Litovsk (mar 1918) | Hechos establecidos |
| Estados Unidos declara la guerra (6 abr 1917); guerra submarina; telegrama Zimmermann | Hechos establecidos |
| Caporetto: más de 260.000 italianos capturados | [Britannica](https://www.britannica.com/event/Battle-of-Caporetto) (entre 265.000 y 275.000) |
| Cambrai, nov 1917, cientos de tanques | Unos 476 tanques |
| Ofensiva de Primavera (21 mar 1918), tropas de asalto | Hecho establecido |
| Bosque de Belleau, junio de 1918, marines | [Army.mil](https://www.army.mil/article/207683) |
| Amiens, 8 ago 1918, "el día negro" (Ludendorff) | Hecho establecido |
| Gripe de 1918 | Hecho establecido |
| Rendiciones: Bulgaria (29 sep), otomanos (30 oct), Austria-Hungría (3 nov) | Hechos establecidos |
| Armisticio en vigor el 11/11/1918 a las 11:00 | Hecho establecido |
| Entre 9 y 10 millones de soldados muertos | Rango habitual |
| Versalles (28 jun 1919), artículo 231, reparaciones; Alsacia y Lorena vuelven a Francia | Hechos establecidos |
| Nacen Polonia, Checoslovaquia, Finlandia y los países bálticos | Hechos establecidos |

**Notas:**
- **Mapas:** las fronteras de 1914 son aproximadas, porque se agrupan países actuales en los imperios de la época (por ejemplo, Polonia dentro del Imperio ruso).
- **Escenas:** las batallas son recreaciones estilizadas, no reconstrucciones exactas de cada combate.
- **Divulgación de IA en YouTube:** la narración es una voz sintética. Al subir, revisa la opción de "contenido alterado o sintético" en YouTube Studio. Las animaciones evidentes no suelen requerirla, pero conviene mencionarlo en la descripción, como ya se hace arriba.
