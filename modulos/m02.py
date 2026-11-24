MODULE = {
    "num": "02",
    "title": "Modularidad y componentes",
    "sub": "Dividir sin romper el sistema",
    "lessons": [
        {
            "id": "fsam2l1",
            "lnum": 1,
            "title": "Modularidad: cohesión y acoplamiento",
            "minutes": 9,
            "lead": "Un sistema se vuelve inmanejable cuando sus partes se conocen demasiado. La modularidad no consiste en tener muchos archivos, sino en agrupar lo que cambia junto y separar lo que puede evolucionar por su cuenta. Cohesión y acoplamiento son las dos fuerzas que permiten juzgar si una división ayuda o solo decora el diagrama.",
            "diagram": ("matrix", {"rows": 5, "cols": 8, "mark": 19}),
            "caption": "Cada celda representa una relación entre partes; la modularidad busca concentrar las relaciones fuertes dentro de un módulo y dejar fuera solo las débiles.",
            "sections": [
                {
                    "h": "Qué significa dividir bien",
                    "p": [
                        "Un módulo es una unidad de código con una responsabilidad reconocible. Puede ser un paquete, una carpeta, una clase o un servicio, pero lo importante es que tenga un límite comprensible. La modularidad mide cuánto se puede cambiar una parte sin tocar las demás y cuánto se puede entender sin leer todo el sistema.",
                        "La cohesión mira hacia dentro: cuánto pertenecen juntas las cosas que están en el mismo módulo. El acoplamiento mira hacia fuera: cuánto depende un módulo de otros. La combinación deseable es alta cohesión y bajo acoplamiento, aunque rara vez se logra de forma perfecta. El objetivo es que las dependencias sean pocas, explícitas y en una dirección clara.",
                        "La división no es gratuita. Cada frontera añade una interfaz, una traducción y una oportunidad de malentendido. Un sistema con demasiados módulos diminutos puede acabar con más ceremonia que lógica. La granularidad correcta depende del ritmo de cambio y del tamaño del equipo, no de una regla universal.",
                    ],
                },
                {
                    "h": "Los niveles de cohesión",
                    "p": [
                        "La cohesión funcional es la más fuerte: todas las partes colaboran en una única tarea bien definida. Le sigue la cohesión secuencial, donde la salida de una parte alimenta la siguiente, y la comunicacional, donde las partes operan sobre los mismos datos. Estos niveles suelen indicar un módulo con propósito claro.",
                        "Más abajo aparecen la cohesión temporal, que agrupa cosas que ocurren al mismo tiempo, como la inicialización; la lógica, que junta alternativas del mismo tipo, como distintos formatos de exportación; y la coincidental, que mezcla elementos sin relación. Los tres últimos son señales de alerta: el módulo existe por conveniencia, no por diseño.",
                        "La cohesión no se mide contando líneas. Se pregunta qué cambia junto. Si dos funciones se modifican siempre por la misma razón de negocio, probablemente pertenecen al mismo módulo aunque hoy estén separadas. Si una clase tiene dos grupos de métodos que cambian por motivos distintos, probablemente haya que dividirla.",
                    ],
                },
                {
                    "h": "Acoplamiento, connascencia y métricas",
                    "p": [
                        "El acoplamiento puede ser por herencia, por composición, por datos compartidos o por dependencia de una biblioteca. No todo acoplamiento es malo: sin alguna dependencia no habría sistema. Lo que importa es si la dependencia es estable, si está en la dirección correcta y si obliga a cambiar cosas que no deberían cambiar juntas.",
                        "La connascencia añade matices: mide cuánto conocimiento comparten dos partes para funcionar. Puede ser estática, cuando depende de nombres, tipos o posiciones, o dinámica, cuando depende del orden de ejecución o de valores en tiempo de ejecución. Cuanto más implícito es ese conocimiento, más frágil es el sistema ante un cambio.",
                        "Las métricas de Robert C. Martin ayudan a ver el equilibrio. El acoplamiento aferente cuenta quién depende de un componente; el eferente, de quién depende él. La inestabilidad relaciona ambos, y la distancia a la secuencia principal señala componentes demasiado concretos y muy usados, o demasiado abstractos y sin uso. No son verdades absolutas, pero sí señales para revisar.",
                    ],
                },
            ],
            "brief": [
                "Cohesión alta y acoplamiento bajo, con dependencias explícitas",
                "La cohesión se juzga por qué cambia junto, no por tamaño",
                "La connascencia mide conocimiento compartido, también el implícito",
                "Las métricas señalan desequilibrios; no sustituyen el juicio",
            ],
            "keys": [
                "Agrupa por razón de cambio, no por tipo de archivo.",
                "Haz explícitas las dependencias y evita ciclos.",
                "Vigila el acoplamiento implícito por orden o convención.",
                "Revisa componentes muy usados y concretos a la vez.",
                "Ajusta la granularidad al ritmo de cambio del dominio.",
            ],
            "example": "Un equipo tiene un paquete llamado utilidades con fechas, impuestos, correo y conexión a base de datos. Nadie sabe qué puede cambiar sin romper algo. Al separarlo por razón de cambio, aparecen un módulo de facturación, uno de notificaciones y una biblioteca de fechas. Las dependencias se reducen y las pruebas se vuelven más rápidas porque cada módulo tiene un contexto acotado.",
            "caution": "Un módulo «reutilizable» que todos usan y nadie posee se convierte en un punto de acoplamiento global. La reutilización sin dueño es deuda técnica con otro nombre.",
            "search": "modularidad cohesión acoplamiento connascencia aferente eferente inestabilidad abstracción secuencia principal módulo granularidad dependencias",
        },
        {
            "id": "fsam2l2",
            "lnum": 2,
            "title": "Identificar y medir características",
            "minutes": 9,
            "lead": "Las características de arquitectura no se eligen de un catálogo: se extraen del dominio, de los requisitos y de las conversaciones con quien conoce el negocio. Después hay que reducirlas a unas pocas que realmente orienten el diseño y crear mecanismos que comprueben si siguen cumpliéndose. Identificar sin medir es solo hacer una lista de deseos.",
            "diagram": ("flow", ["Dominio", "Requisitos", "Prioridades", "Fitness functions"]),
            "caption": "Las preocupaciones del dominio y los requisitos alimentan una lista corta de características; las fitness functions cierran el ciclo comprobando que no se han perdido.",
            "sections": [
                {
                    "h": "Del dominio a las características",
                    "p": [
                        "El dominio aporta pistas que no aparecen en una especificación funcional. Un sistema de salud necesita trazabilidad y privacidad; una plataforma de trading, latencia y auditabilidad; una herramienta interna, facilidad de mantenimiento y bajo coste. Escuchar cómo trabaja la organización revela qué cualidades son inevitables y cuáles serían un lujo.",
                        "Los requisitos escritos suelen mezclar funciones y cualidades. La tarea del arquitecto es separarlas y detectar las implícitas: aquellas que nadie pidió porque se dan por supuestas, como la seguridad de las contraseñas o la capacidad de restaurar una copia. Las implícitas son peligrosas porque no se priorizan hasta que fallan.",
                        "Las entrevistas con usuarios, soporte y operaciones completan el cuadro. Preguntar «¿qué duele cuando el sistema va mal?» o «¿qué cambio cuesta más?» produce información más útil que una lista de adjetivos. El objetivo es construir un vocabulario compartido entre negocio y tecnología, no un documento que nadie lee.",
                    ],
                },
                {
                    "h": "Elegir las que importan",
                    "p": [
                        "Una lista inicial puede tener veinte características. Si todas son prioritarias, ninguna lo es. El siguiente paso es agruparlas, eliminar duplicados y quedarse con tres o cuatro que realmente cambien la estructura. Las demás se conservan como restricciones o se posponen con una condición clara para revisarlas.",
                        "El caso de Silicon Sandwiches, usado en el libro, muestra el método: una cadena de sándwiches quiere franquiciar, operar en varios países y permitir que cada tienda ajuste su menú. De ahí salen características como localización, personalización por tienda, disponibilidad y facilidad de despliegue. La arquitectura se diseña para esas fuerzas, no para una lista genérica.",
                        "Priorizar no significa ignorar. Significa saber qué se optimiza primero y qué se acepta como compromiso. Si la disponibilidad manda, quizá se tolere cierta inconsistencia; si la integridad manda, quizá se acepte más latencia. La prioridad se escribe y se comparte para que las decisiones posteriores tengan un árbitro.",
                    ],
                },
                {
                    "h": "Gobernanza y fitness functions",
                    "p": [
                        "Una fitness function es una comprobación que evalúa si la arquitectura sigue cumpliendo una característica. Puede ser una prueba automatizada de latencia, un análisis de dependencias, una revisión de seguridad o una métrica de despliegue. Su valor está en convertir una intención en una señal que el equipo ve antes de que el problema sea grave.",
                        "La gobernanza no es burocracia centralizada. Es el conjunto de mecanismos que mantienen las decisiones vivas: revisiones ligeras, tableros, pruebas en el pipeline y acuerdos sobre excepciones. Si una regla no tiene forma de comprobarse ni un dueño que la revise, acabará siendo decorativa.",
                        "Las fitness functions también ayudan a discutir trade-offs. Cuando una prueba de latencia falla tras añadir una funcionalidad, el equipo ve el coste de forma concreta. Esa visibilidad permite decidir si se optimiza, se acepta el nuevo umbral o se cambia el diseño, en lugar de descubrir el problema meses después en producción.",
                    ],
                },
            ],
            "brief": [
                "Las características se extraen del dominio y de conversaciones reales",
                "Las implícitas son las que más duelen cuando fallan",
                "Tres o cuatro drivers orientan mejor que veinte deseos",
                "Una fitness function convierte una intención en una señal",
            ],
            "keys": [
                "Entrevista a negocio, soporte y operaciones, no solo al product owner.",
                "Separa funciones de cualidades en cada requisito.",
                "Haz explícitas las características que todos suponen.",
                "Reduce la lista y escribe qué se pospone y por qué.",
                "Automatiza al menos una comprobación por característica prioritaria.",
            ],
            "example": "Una aseguradora pide «modernizar el sistema». Las entrevistas revelan que el problema no es la interfaz, sino que un cambio de tarifa tarda tres semanas por miedo a romper cálculos. El equipo identifica testabilidad y trazabilidad como drivers, escribe escenarios y añade una suite de pruebas de contrato. La modernización empieza por reducir el miedo, no por reescribir la pantalla.",
            "caution": "Una lista de características sin dueño ni medición se convierte en un póster. La gobernanza empieza por saber quién revisa la señal y qué se hace cuando se desvía.",
            "search": "identificar características dominio requisitos implícitas priorizar drivers fitness functions gobernanza medición escenarios Silicon Sandwiches",
        },
        {
            "id": "fsam2l3",
            "lnum": 3,
            "title": "Componentes y cuánto abarcan",
            "minutes": 9,
            "lead": "Un componente no es solo una carpeta con clases: es una unidad con responsabilidad, contrato y límites. Decidir cuántos hay y qué abarca cada uno es una de las decisiones más consecuentes de la arquitectura. Una mala granularidad produce módulos que no se entienden, servicios que se llaman en cadena o equipos que dependen unos de otros para todo.",
            "diagram": ("flow", ["Actores", "Responsabilidades", "Contratos", "Equipos"]),
            "caption": "Identificar componentes es pasar de quién usa el sistema y qué necesita, a límites y contratos que luego se asignan a equipos.",
            "sections": [
                {
                    "h": "Qué es un componente y quién decide",
                    "p": [
                        "Un componente agrupa responsabilidades relacionadas detrás de un contrato. Puede ser un módulo dentro de un monolito o un servicio desplegable, pero en ambos casos debe tener un límite reconocible y una forma estable de comunicarse con el resto. El contrato incluye operaciones, datos de entrada y salida y comportamiento esperado ante errores.",
                        "El arquitecto identifica los componentes de alto nivel y define sus responsabilidades y dependencias. El desarrollador diseña el interior: clases, funciones, estructuras de datos y pruebas. Esta división evita dos extremos: un arquitecto que diseña cada clase y un equipo que inventa fronteras incompatibles con el resto del sistema.",
                        "La frontera debe tener un dueño. Si nadie responde por un componente, las decisiones se reparten y el contrato se degrada. La propiedad no significa aislamiento: significa que hay una persona o un equipo que puede decir qué es un cambio compatible y qué requiere coordinación.",
                    ],
                },
                {
                    "h": "Cómo identificar componentes",
                    "p": [
                        "Una técnica útil es partir de los actores y sus acciones. Quién usa el sistema, qué quiere lograr y qué información necesita. Después se agrupan las acciones que comparten datos y reglas. El error clásico es crear un componente por entidad de base de datos: eso produce un «trampa de entidades» donde cada tabla tiene su servicio y los procesos de negocio quedan repartidos en llamadas inconexas.",
                        "Otra técnica es seguir el flujo de trabajo. Un pedido pasa por validación, reserva de inventario, pago, preparación y envío. Agrupar por etapas del flujo produce componentes alineados con el negocio, siempre que cada etapa tenga un propósito claro y no se convierta en una capa vacía. La granularidad debe reflejar el trabajo real, no la estructura del departamento.",
                        "La granularidad correcta es la que permite cambiar una parte sin reescribir las demás y permite a un equipo entenderla sin depender de otro. Si dos componentes siempre cambian juntos, probablemente sean uno. Si uno cambia por motivos muy distintos en momentos distintos, probablemente sean dos. La respuesta está en el historial de cambios, no solo en el organigrama.",
                    ],
                },
                {
                    "h": "Arquitectura cuántica: monolito o distribuido",
                    "p": [
                        "Una arquitectura cuántica es una unidad que se despliega junta y comparte datos, y que se comporta como un todo coherente frente al resto. Un monolito suele ser una sola cuántica; un conjunto de microservicios puede tener varias. La pregunta no es «monolito o distribuido», sino cuántas unidades independientes necesita el sistema para cumplir sus características.",
                        "La connascencia y el acoplamiento de datos ayudan a decidir. Si dos partes comparten transacciones, cambios coordinados y el mismo modelo, separarlas por red añade latencia y complejidad sin beneficio. Si tienen ciclos de cambio distintos, equipos distintos y datos que pueden ser eventualmente consistentes, la separación puede compensar.",
                        "El tamaño del equipo también cuenta. Un monolito modular bien cuidado puede ser la mejor opción para un equipo pequeño; una organización con muchos equipos quizá necesite fronteras desplegables para no coordinar cada cambio. La arquitectura cuántica correcta es la que reduce la coordinación sin multiplicar los fallos que el equipo no puede operar.",
                    ],
                },
            ],
            "brief": [
                "Componente = responsabilidad + contrato + dueño",
                "El arquitecto define límites; el equipo diseña el interior",
                "Evita componentes por tabla y capas vacías",
                "La cuántica arquitectónica guía la decisión monolito/distribuido",
            ],
            "keys": [
                "Documenta el contrato y el comportamiento ante errores.",
                "Asigna un dueño a cada componente.",
                "Agrupa por flujo de negocio, no por entidad de datos.",
                "Une lo que siempre cambia junto y separa lo que evoluciona aparte.",
                "Cuenta las cuánticas antes de repartir el sistema por la red.",
            ],
            "example": "Una empresa de logística tiene servicios por entidad: camiones, conductores, rutas y paquetes. Cada cambio de una entrega exige coordinar cuatro servicios y una transacción distribuida. Al reagrupar por flujo, aparece un componente de planificación de entregas que posee los datos y las reglas de ese proceso. Los otros quedan como catálogos de apoyo. El número de llamadas y de fallos parciales baja de forma inmediata.",
            "caution": "Un componente sin contrato explícito acaba dependiendo de detalles internos de otro. La frontera existe en el diagrama, pero no en el código ni en las pruebas.",
            "search": "componentes granularidad contrato actores responsabilidades cuántica arquitectónica monolito distribuido trampa entidades flujo negocio equipos",
        },
    ],
    "quiz": {
        "id": "fsam2q",
        "title": "Cierre del módulo 02",
        "summary": [
            "La modularidad se juzga por cohesión y acoplamiento, no por cantidad de archivos.",
            "Las características se extraen del dominio, se priorizan y se comprueban con fitness functions.",
            "Un componente tiene responsabilidad, contrato y dueño; su granularidad sigue el cambio real.",
            "La arquitectura cuántica ayuda a decidir qué debe desplegarse y compartir datos como una unidad.",
        ],
        "questions": [
            {
                "q": "¿Cuál es la señal más clara de que dos funciones deberían estar en el mismo módulo?",
                "options": [
                    "Tienen el mismo número de líneas",
                    "Cambian siempre por la misma razón de negocio",
                    "Usan el mismo lenguaje de programación",
                    "Fueron escritas por la misma persona",
                ],
                "answer": 1,
                "why": "La cohesión se mide por razón de cambio, no por tamaño ni autoría. Si dos partes evolucionan juntas por el mismo motivo, la frontera entre ellas añade coste sin beneficio.",
            },
            {
                "q": "¿Qué es una fitness function en arquitectura?",
                "options": [
                    "Una prueba o revisión que comprueba si se sigue cumpliendo una característica",
                    "Una función del negocio que genera ingresos",
                    "Un tipo de diagrama de clases",
                    "Una herramienta para elegir el lenguaje",
                ],
                "answer": 0,
                "why": "Convierte una característica en una señal verificable, como una prueba de latencia o un análisis de dependencias, para detectar desviaciones a tiempo.",
            },
            {
                "q": "Un equipo crea un servicio por cada tabla de la base de datos. ¿Qué riesgo principal asume?",
                "options": [
                    "Que el sistema sea demasiado simple",
                    "La trampa de entidades: procesos de negocio repartidos en llamadas inconexas y acoplados por datos",
                    "Que disminuya el número de despliegues",
                    "Que desaparezcan las transacciones",
                ],
                "answer": 1,
                "why": "Agrupar por tabla confunde el modelo de datos con el de negocio. Los procesos que cruzan entidades acaban en cadenas de llamadas y transacciones distribuidas.",
            },
            {
                "q": "¿Cuándo tiene más sentido mantener un monolito modular en lugar de microservicios?",
                "options": [
                    "Cuando un equipo pequeño puede desplegar y entender el sistema sin coordinar múltiples unidades",
                    "Cuando se quiere impresionar en una entrevista",
                    "Cuando no hay pruebas automatizadas",
                    "Cuando cada módulo necesita una base de datos distinta",
                ],
                "answer": 0,
                "why": "Si una sola cuántica arquitectónica basta para el ritmo de cambio y el tamaño del equipo, distribuir añade red y fallos parciales sin compensación.",
            },
        ],
        "exercises": [
            "Toma un módulo de tu proyecto y clasifica su cohesión; propone una división o fusión justificada por razón de cambio.",
            "Escribe tres características implícitas de tu sistema y un escenario medible para cada una.",
            "Dibuja las cuánticas arquitectónicas de un sistema conocido y explica si el número actual se justifica.",
        ],
        "search": "cierre modularidad cohesión acoplamiento componentes fitness functions cuántica granularidad contratos gobernanza",
    },
}
