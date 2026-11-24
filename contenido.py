"""Contenido del curso «Fundamentos de Arquitectura · Edición esencial».

Cada módulo vive en modulos/mNN.py y expone un diccionario MODULE.
Este archivo los reúne y añade los metadatos del curso y el glosario.
"""

from modulos import m01, m02, m03, m04, m05, m06, m07

MODULES = [
    m01.MODULE,
    m02.MODULE,
    m03.MODULE,
    m04.MODULE,
    m05.MODULE,
    m06.MODULE,
    m07.MODULE,
]

COURSE = {
    "title": "Fundamentos de Arquitectura",
    "brand": "FSA",
    "subtitle": "Edición esencial",
    "tagline": "Las decisiones que sostienen el software",
    "description": (
        "Edición esencial en español de «Fundamentals of Software Architecture», "
        "de Mark Richards y Neal Ford: pensamiento arquitectónico, modularidad, "
        "características, estilos, decisiones, riesgo y las habilidades de equipo "
        "que hacen sostenible una arquitectura, con texto y diagramas originales."
    ),
    "book": "Fundamentals of Software Architecture",
    "author": "Mark Richards y Neal Ford",
    "pdf": "Fundamentos-Arquitectura-Esencial.pdf",
    "year": "2026",
    "global": "FSA",
    "theme_key": "fsa_theme",
}

# Glosario: (término, definición breve, id de lección donde se desarrolla)
GLOSARIO = [
    ("Acoplamiento", "Grado de dependencia entre dos partes del sistema; cuanto mayor, más cuesta cambiarlas por separado.", "fsam2l1"),
    ("Acoplamiento aferente", "Número de componentes externos que dependen de uno; mide cuánto lo usa el resto.", "fsam2l1"),
    ("Acoplamiento de datos", "Dependencia que surge cuando dos partes comparten el mismo esquema o formato de datos.", "fsam2l1"),
    ("Acoplamiento eferente", "Número de componentes externos de los que depende uno; mide cuánto arrastra al cambiar.", "fsam2l1"),
    ("ADR", "Registro breve de una decisión de arquitectura: contexto, decisión, consecuencias y estado.", "fsam6l1"),
    ("Arquitectura", "Estructura del sistema unida a las características que debe cumplir, las decisiones tomadas y los principios que la guían.", "fsam1l1"),
    ("Arquitectura cuántica", "Unidad con despliegue y datos propios que se comporta como un todo coherente frente al resto.", "fsam2l3"),
    ("Arquitectura en capas", "Estilo monolítico que organiza el código en capas cerradas o abiertas con responsabilidades definidas.", "fsam3l1"),
    ("Arquitectura orientada a eventos", "Estilo distribuido donde los componentes publican y consumen eventos en lugar de llamarse directamente.", "fsam4l2"),
    ("Arquitectura orientada a servicios", "Estilo con servicios de negocio coordinados por un bus o un orquestador central.", "fsam5l1"),
    ("Arquitectura pipeline", "Estilo monolítico de filtros unidireccionales que transforman datos de una entrada a una salida.", "fsam3l2"),
    ("Arquitectura space-based", "Estilo distribuido que procesa en memoria sobre una rejilla de datos replicada para evitar el cuello de la base.", "fsam4l3"),
    ("Atributo de calidad", "Propiedad medible del sistema, como latencia, disponibilidad o facilidad de despliegue.", "fsam1l3"),
    ("Autonomía de equipo", "Capacidad de un equipo para decidir y desplegar su parte sin coordinar cada cambio con los demás.", "fsam7l1"),
    ("Bounded context", "Frontera lingüística y de modelo dentro de la cual un término tiene un significado preciso.", "fsam5l2"),
    ("Broker", "Componente intermediario que recibe eventos y los entrega a los consumidores sin conocerlos.", "fsam4l2"),
    ("Característica de arquitectura", "Requisito no funcional o de calidad que da forma a la estructura y se puede evaluar.", "fsam1l3"),
    ("Característica implícita", "Característica que no aparece en el enunciado pero se espera por sentido común o dominio.", "fsam1l3"),
    ("Característica operativa", "Característica ligada a la ejecución: disponibilidad, rendimiento, escalabilidad o seguridad.", "fsam1l3"),
    ("Característica estructural", "Característica ligada a la forma del código: modularidad, mantenibilidad, testabilidad o portabilidad.", "fsam1l3"),
    ("Cohesión", "Grado en que las responsabilidades de un módulo pertenecen al mismo propósito.", "fsam2l1"),
    ("Cohesión coincidental", "Unión de partes sin relación real; el nivel más débil de cohesión.", "fsam2l1"),
    ("Cohesión funcional", "Unión de partes que colaboran en una única tarea bien definida; el nivel más fuerte.", "fsam2l1"),
    ("Componente", "Unidad desplegable o lógica con una responsabilidad y un contrato claros dentro de la arquitectura.", "fsam2l3"),
    ("Connascencia", "Forma de acoplamiento que mide cuánto conocimiento comparten dos partes para funcionar.", "fsam2l1"),
    ("Contrato", "Acuerdo explícito de entradas, salidas y comportamiento que un componente ofrece a quien lo usa.", "fsam3l3"),
    ("Criterio de decisión", "Factor concreto, frecuentemente de negocio o de equipo, que inclina la elección entre estilos.", "fsam5l3"),
    ("Deuda técnica", "Coste futuro acumulado por una solución rápida que no se corrige a tiempo.", "fsam1l2"),
    ("Diagrama de componentes", "Vista de las piezas internas de un contenedor y de sus dependencias.", "fsam6l3"),
    ("Diagrama de contenedores", "Vista de las aplicaciones, servicios y almacenes que forman el sistema y cómo se comunican.", "fsam6l3"),
    ("Diagrama de contexto", "Vista de alto nivel del sistema, sus usuarios y los sistemas externos con los que intercambia información.", "fsam6l3"),
    ("Diseño", "Conjunto de decisiones locales que hacen funcionar una parte dentro de la estructura ya elegida.", "fsam1l2"),
    ("Distancia de la secuencia principal", "Medida de cuánto se aparta un componente del equilibrio ideal entre abstracción e inestabilidad.", "fsam2l1"),
    ("Dominio", "Área de negocio con su vocabulario, sus reglas y sus límites propios.", "fsam5l2"),
    ("Efecto sinkhole", "Peticiones que atraviesan capas sin que ninguna aporte lógica, sumando latencia y código vacío.", "fsam3l1"),
    ("Equipo", "Grupo estable con un objetivo, un límite y la autoridad para decidir sobre su parte del sistema.", "fsam7l1"),
    ("Escalabilidad", "Capacidad de mantener el rendimiento cuando crece una carga concreta.", "fsam1l3"),
    ("Estilo de arquitectura", "Patrón de organización estructural con reglas, ventajas y limitaciones conocidas.", "fsam3l1"),
    ("Evento", "Hecho ocurrido en el sistema que se anuncia a quien pueda interesar, sin destinatario único.", "fsam4l2"),
    ("Facilidad de despliegue", "Grado en que un cambio puede llevarse a producción con poco riesgo y poca coordinación.", "fsam1l3"),
    ("Filtro", "Etapa de un pipeline que transforma los datos que recibe y entrega el resultado a la siguiente.", "fsam3l2"),
    ("Fitness function", "Prueba automática o revisión periódica que comprueba si la arquitectura sigue cumpliendo una característica.", "fsam2l2"),
    ("Gobernanza", "Conjunto de reglas y mecanismos que mantienen las decisiones de arquitectura a lo largo del tiempo.", "fsam2l2"),
    ("Idempotencia", "Propiedad por la cual repetir una operación produce el mismo resultado que ejecutarla una vez.", "fsam4l2"),
    ("Inestabilidad", "Relación entre dependencias salientes y totales de un componente; mide cuánto puede cambiar sin arrastrar a otros.", "fsam2l1"),
    ("Interoperabilidad", "Capacidad de dos sistemas para intercambiar información y usarla sin adaptadores especiales.", "fsam1l3"),
    ("Liderazgo técnico", "Influencia ejercida desde el conocimiento y la confianza, sin depender de la autoridad formal.", "fsam7l2"),
    ("Mantenibilidad", "Facilidad para entender, corregir y ampliar el sistema con el paso del tiempo.", "fsam1l3"),
    ("Matriz de riesgo", "Cuadro que cruza probabilidad e impacto para ordenar los riesgos de una arquitectura.", "fsam6l2"),
    ("Mediador", "Componente que conoce el flujo de un proceso y dirige los eventos entre los participantes.", "fsam4l2"),
    ("Microkernel", "Estilo con un núcleo estable y complementos que añaden capacidades mediante contratos.", "fsam3l3"),
    ("Microservicio", "Servicio pequeño, autónomo y desplegable por separado, dueño de su modelo y sus datos.", "fsam5l2"),
    ("Monolito", "Sistema desplegado como una sola unidad, con todo el código y, a menudo, una sola base de datos.", "fsam5l3"),
    ("Monolito modular", "Aplicación con un solo despliegue pero límites internos bien definidos entre módulos.", "fsam5l3"),
    ("Núcleo", "Parte central de un microkernel que ofrece el flujo mínimo y las interfaces para extenderse.", "fsam3l3"),
    ("Orquestación", "Coordinación centralizada de varios servicios para completar un proceso de negocio.", "fsam5l1"),
    ("Orquestador", "Motor que decide el orden de las llamadas y maneja los errores de un proceso compuesto.", "fsam5l1"),
    ("Pipeline", "Secuencia de etapas donde la salida de una es la entrada de la siguiente.", "fsam3l2"),
    ("Plugin", "Complemento que añade comportamiento al núcleo sin modificarlo.", "fsam3l3"),
    ("Presentación", "Forma de contar la arquitectura a una audiencia concreta para que pueda decidir.", "fsam6l3"),
    ("Registro de plugins", "Catálogo que el núcleo consulta para localizar y cargar complementos.", "fsam3l3"),
    ("Riesgo de arquitectura", "Posibilidad de que una decisión estructural impida cumplir un objetivo del negocio.", "fsam6l2"),
    ("Service-based", "Estilo distribuido con pocos servicios gruesos y, a menudo, una base de datos compartida.", "fsam4l1"),
    ("SOA", "Estilo orientado a servicios con contratos amplios, reutilización y coordinación central.", "fsam5l1"),
    ("Trade-off", "Intercambio entre dos cualidades: mejorar una suele empeorar otra.", "fsam1l2"),
    ("Unidad de procesamiento", "Instancia de aplicación que atiende peticiones en memoria dentro de una arquitectura space-based.", "fsam4l3"),
    ("Velocidad de cambio", "Frecuencia con la que una parte del sistema recibe modificaciones y despliegues.", "fsam1l3"),
    ("Wiki de decisiones", "Repositorio navegable donde se acumulan los ADR y su contexto histórico.", "fsam6l1"),
]
