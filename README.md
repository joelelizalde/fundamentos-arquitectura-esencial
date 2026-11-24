# Fundamentos de Arquitectura — Edición esencial en español

Manual de estudio estático (sin build para el lector y sin dependencias en el navegador) para pensar y decidir la arquitectura de software: características, modularidad, estilos, decisiones, riesgo y equipos.
Alineado temáticamente con *Fundamentals of Software Architecture* (1.ª edición), de Mark Richards y Neal Ford, pero con texto, ejemplos y diagramas originales.

## Qué incluye

- **21 lecciones** en **7 módulos** (3 lecciones y 1 evaluación por módulo), siguiendo el recorrido del libro: pensamiento arquitectónico → modularidad y componentes → estilos fundamentales → estilos distribuidos → microservicios y elección → decisiones y riesgo → equipos y carrera.
- Lectura continua: botón «Completar y seguir», navegación con ← y →, temario lateral siempre disponible.
- **7 evaluaciones** de 4 preguntas con explicaciones y **21 ejercicios** aplicados.
- Progreso guardado en `localStorage`, glosario con buscador y modo claro/oscuro.
- Buscador global con atajo `⌘K` / `Ctrl+K`.
- **21 diagramas originales** en SVG (flujo, capas, bucle, matriz, curva y barras).
- **68 términos** en el glosario.
- Manual en PDF: `Fundamentos-Arquitectura-Esencial.pdf` (54 páginas).
- Tipografías locales (Fraunces + Inter), sin depender de Google Fonts.

## Estructura

```
index.html                      Portada y temario completo
fsam1l1.html … fsam7q.html      21 lecciones y 7 evaluaciones
glosario.html                   Glosario con búsqueda y filtro por letra
progreso.html                   Progreso por módulo
css/curso.css                   Diseño editorial responsive
js/curso.js                     Navegación, progreso, búsqueda y quizzes
assets/fonts/                   Tipografías locales
modulos/m01.py … m07.py         Contenido de cada módulo
contenido.py                    Reúne módulos, metadatos y glosario
build_site.py                   Generador del sitio
build_pdf.py                    Generador del PDF (WeasyPrint)
Fundamentos-Arquitectura-Esencial.pdf
```

## Módulos

1. **Pensamiento arquitectónico** — definición, rol del arquitecto, trade-offs y características.
2. **Modularidad y componentes** — cohesión, acoplamiento, medición, fitness functions y cuánticas.
3. **Estilos fundamentales** — capas, pipeline y microkernel.
4. **Estilos distribuidos** — service-based, dirigida por eventos y space-based.
5. **Microservicios y elección** — SOA orquestada, microservicios y criterios de decisión.
6. **Decisiones y riesgo** — ADR, análisis de riesgo, diagramas y presentación.
7. **Equipos y carrera** — límites, autonomía, negociación, liderazgo y desarrollo profesional.

## Correspondencia con el libro

| Capítulo | Tema | Lección |
|---|---|---|
| 01 | Introducción y definición | `fsam1l1` |
| 02 | Pensamiento arquitectónico | `fsam1l2` |
| 03 | Modularidad | `fsam2l1` |
| 04 | Características de arquitectura | `fsam1l3` |
| 05 | Identificar características | `fsam2l2` |
| 06 | Medir y gobernar características | `fsam2l2` |
| 07 | Alcance de las características | `fsam2l3` |
| 08 | Pensamiento basado en componentes | `fsam2l3` |
| 09 | Fundamentos de estilos | `fsam3l1` |
| 10 | Arquitectura en capas | `fsam3l1` |
| 11 | Arquitectura pipeline | `fsam3l2` |
| 12 | Microkernel | `fsam3l3` |
| 13 | Service-based | `fsam4l1` |
| 14 | Dirigida por eventos | `fsam4l2` |
| 15 | Space-based | `fsam4l3` |
| 16 | SOA orquestada | `fsam5l1` |
| 17 | Microservicios | `fsam5l2` |
| 18 | Elegir estilo | `fsam5l3` |
| 19 | Decisiones de arquitectura | `fsam6l1` |
| 20 | Análisis de riesgo | `fsam6l2` |
| 21 | Diagramar y presentar | `fsam6l3` |
| 22 | Equipos eficaces | `fsam7l1` |
| 23 | Negociación y liderazgo | `fsam7l2` |
| 24 | Carrera del arquitecto | `fsam7l3` |

## Regenerar

```bash
python3 build_site.py          # solo el sitio
python3 build_site.py --pdf    # sitio + manual en PDF
```

El PDF se compone con WeasyPrint (probado con 70.x) a partir del mismo contenido y las mismas fuentes.

## Añadir o editar contenido

Cada módulo vive en `modulos/mNN.py` y expone un diccionario `MODULE`:

- `num`, `title`, `sub`
- `lessons`: lista de lecciones con `id`, `lnum`, `title`, `minutes`, `lead`, `diagram`, `caption`, `sections`, `brief`, `keys`, `example`, `caution`, `search`.
- `quiz`: `id`, `title`, `summary`, `questions`, `exercises`, `search`.

Los diagramas se declaran como tuplas: `("flow", [...])`, `("stack", [...])`, `("loop", [...])`, `("matrix", {...})`, `("curve", {...})`, `("latency", {...})` o `("bars", [...])`.
Al cambiar contenido, vuelve a ejecutar `build_site.py --pdf` para regenerar páginas y PDF.

## Atajos

| Tecla | Acción |
|---|---|
| ← / → | Lección anterior / siguiente |
| `C` | Marcar la página actual como completada |
| `/` o `⌘K` | Abrir el buscador |
| `Esc` | Cerrar buscador o menú |
| `?` | Recordatorio de atajos |

## Datos locales

El progreso y el tema se guardan solo en el navegador:

- `fsa_progress_v1`
- `fsa_theme`

No se envía nada a un servidor.

## Publicar en GitHub Pages

1. Crea un repositorio con el contenido de esta carpeta en la raíz.
2. **Settings → Pages → Deploy from a branch → main → / (root)**.
3. El sitio quedará en `https://<usuario>.github.io/<repositorio>/`.

No subas claves ni tokens al repositorio: el curso es estático y no necesita credenciales.
