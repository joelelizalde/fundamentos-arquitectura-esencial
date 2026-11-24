MODULE = {
    "num": "01",
    "title": "Pensamiento arquitectónico",
    "sub": "Qué decide un arquitecto y con qué criterios",
    "lessons": [
        {
            "id": "fsam1l1",
            "lnum": 1,
            "title": "Qué es la arquitectura de software",
            "minutes": 9,
            "lead": "La arquitectura no es un dibujo de cajas ni el conjunto de tecnologías de moda. Es la estructura que sostiene el sistema, las cualidades que debe cumplir, las decisiones que la comprometen y los principios que orientan al equipo. Entender esas cuatro piezas permite distinguir una decisión estructural de un detalle de implementación.",
            "diagram": ("stack", ["Estructura", "Características", "Decisiones", "Principios"]),
            "caption": "La arquitectura combina la forma del sistema con las cualidades que debe cumplir, las decisiones que la fijan y los principios que guían el trabajo diario.",
            "sections": [
                {
                    "h": "Cuatro piezas que sostienen la definición",
                    "p": [
                        "La estructura es la primera pieza: qué partes existen y cómo se relacionan. Incluye módulos, servicios, capas, bases de datos y la forma en que se comunican. Sin embargo, dos sistemas con el mismo diagrama pueden tener arquitecturas distintas si difieren en sus cualidades o en las decisiones que los gobiernan. La estructura es necesaria, pero no suficiente.",
                        "Las características de arquitectura son la segunda pieza: los requisitos de calidad que el sistema debe sostener, como disponibilidad, latencia, seguridad o facilidad de despliegue. No son adjetivos decorativos; se expresan con escenarios y umbrales. Un sistema que debe responder en menos de cien milisegundos al percentil 99 tiene una restricción distinta de otro que puede tardar dos segundos.",
                        "Las decisiones y los principios completan el cuadro. Una decisión es una elección concreta que cambia el rumbo y cuesta revertir: usar una base relacional, separar el frontend del backend o adoptar eventos. Un principio es una guía más general que deja margen al equipo, como «ningún servicio accede a la base de otro». Decisiones y principios deben quedar escritos para que no dependan de la memoria de una persona.",
                    ],
                },
                {
                    "h": "Lo que se espera de un arquitecto",
                    "p": [
                        "El arquitecto toma decisiones técnicas, pero también analiza continuamente si la arquitectura sigue encajando con el negocio. Debe mantener la vista en las tendencias sin perseguir cada novedad, y comprobar que las decisiones se cumplen sin convertirse en un policía. Su valor no está en tener siempre la respuesta, sino en formular las preguntas correctas y reducir la incertidumbre del equipo.",
                        "También se espera amplitud: conocer varias tecnologías y estilos lo suficiente para comparar alternativas, aunque no sea experto en todas. Esa amplitud se complementa con conocimiento del dominio. Un arquitecto que entiende cómo se gana dinero, qué regula el sector y qué duele a los usuarios elige mejor que quien solo mira el código.",
                        "Por último, el rol es profundamente interpersonal. Hay que explicar decisiones, negociar prioridades, mediar entre equipos y navegar la política de la organización. Un diseño impecable que nadie adopta no cambia nada. La arquitectura se construye con personas, y las habilidades de comunicación forman parte del trabajo técnico, no un añadido opcional.",
                    ],
                },
                {
                    "h": "Las leyes que evitan atajos",
                    "p": [
                        "La primera ley es que todo es un trade-off. No existe una arquitectura que sea mejor en todo: la caché mejora la latencia y complica la coherencia; los microservicios dan autonomía y multiplican los fallos parciales. Una decisión sin coste declarado probablemente oculta un coste que aparecerá más tarde. El arquitecto maduro nombra lo que gana y lo que pierde.",
                        "La segunda ley es que el «por qué» importa más que el «cómo». La tecnología cambia; la razón que llevó a elegirla suele sobrevivir. Documentar el contexto permite revisar una decisión cuando cambian las circunstancias, en lugar de defenderla por inercia. Sin el porqué, el equipo hereda una regla sin saber cuándo dejó de aplicarse.",
                        "La tercera ley es que las diferencias entre opciones rara vez son absolutas. Casi siempre hay una tercera vía, un híbrido o un cambio de alcance que evita el falso dilema. Cuando dos alternativas parecen irreconciliables, conviene separar los requisitos que realmente compiten y buscar una solución que atienda lo esencial de ambos. La arquitectura es el arte de elegir qué problema dejar abierto.",
                    ],
                },
            ],
            "brief": [
                "Arquitectura = estructura + características + decisiones + principios",
                "Las características se prueban con escenarios, no con adjetivos",
                "El arquitecto decide, analiza, comunica y negocia",
                "Toda decisión tiene un coste que debe nombrarse",
            ],
            "keys": [
                "Distingue una decisión estructural de un detalle reversible.",
                "Escribe las decisiones y su contexto para que sobrevivan al equipo.",
                "Mide las características con umbrales y escenarios concretos.",
                "Desarrolla amplitud técnica, no solo profundidad en una herramienta.",
                "Antes de decidir, comprueba si el dilema es realmente binario.",
            ],
            "example": "Una arquitecta de una tienda en línea recibe la petición de «pasar todo a microservicios». Antes de responder, escribe las características que importan: picos de tráfico en rebajas, despliegues frecuentes del catálogo y un equipo pequeño. Descubre que el problema real es el acoplamiento del catálogo con el checkout. Propone separar esos dos módulos y mantener el resto en un monolito modular. El coste de la solución es una fracción del que tendría la migración completa.",
            "caution": "La «arquitectura por accidente» aparece cuando nadie decide y el sistema crece a base de parches. Si no puedes explicar por qué una parte tiene la forma que tiene, probablemente no sea una decisión, sino una cicatriz.",
            "search": "arquitectura definición estructura características decisiones principios rol del arquitecto trade-off leyes expectativas negocio comunicación",
        },
        {
            "id": "fsam1l2",
            "lnum": 2,
            "title": "Pensar en trade-offs",
            "minutes": 9,
            "lead": "Un arquitecto no elige la mejor tecnología en abstracto: elige la menos mala para un contexto. Para hacerlo necesita separar arquitectura de diseño, mantener amplitud técnica, entender los impulsores del negocio y no perder el contacto con el código. Esta lección ofrece un método para comparar opciones sin caer en el «depende» vacío.",
            "diagram": ("loop", ["Entender el negocio", "Explorar opciones", "Comparar trade-offs", "Decidir y codificar"]),
            "caption": "El pensamiento arquitectónico es un ciclo: el contexto alimenta las opciones, las opciones se comparan y la decisión vuelve a la realidad del código.",
            "sections": [
                {
                    "h": "Arquitectura y diseño no compiten",
                    "p": [
                        "La arquitectura define la estructura y las reglas que no deberían cambiar sin una decisión consciente. El diseño resuelve cómo encajan las piezas dentro de esa estructura: patrones de clases, esquemas de datos, interfaces locales. La frontera no siempre es nítida, y eso está bien. Lo importante es saber qué decisiones necesitan consenso y cuáles puede tomar un equipo sin pedir permiso.",
                        "Cuando todo se trata como arquitectura, el equipo se paraliza esperando aprobación para cada detalle. Cuando nada se trata como arquitectura, cada equipo inventa su propia estructura y el sistema se vuelve incoherente. La práctica útil es reservar la conversación arquitectónica para lo que es caro de revertir o afecta a varios equipos, y delegar el resto con principios claros.",
                        "Una prueba sencilla: si la decisión se puede deshacer en una tarde y solo afecta a un módulo, es diseño. Si cambia contratos entre equipos, datos compartidos o cualidades del sistema, es arquitectura. Esa clasificación evita reuniones innecesarias y, a la vez, protege las decisiones que de verdad importan.",
                    ],
                },
                {
                    "h": "Amplitud técnica y análisis de trade-offs",
                    "p": [
                        "La profundidad sirve para resolver; la amplitud sirve para elegir. Un arquitecto debe conocer el mapa: qué familias de bases de datos existen, cómo se comportan los estilos distribuidos, qué implican los distintos modelos de consistencia. No necesita ser el mejor programador de cada herramienta, pero sí entender sus límites para no aceptar una promesa de marketing.",
                        "El análisis de trade-offs consiste en identificar las fuerzas en conflicto y valorarlas con el contexto. No basta con decir «depende»: hay que explicar de qué depende y en qué dirección inclina la balanza. Una tabla con opciones, características, ventajas, riesgos y condiciones de reversión convierte una discusión circular en una decisión trazable.",
                        "También conviene distinguir lo que se sabe de lo que se supone. Las decisiones arquitectónicas suelen tomarse con información incompleta. Registrar las suposiciones permite revisarlas cuando aparezcan datos nuevos. Una buena decisión con una suposición falsa no es un fracaso del método; es una señal de que hay que actualizar el contexto y volver a decidir.",
                    ],
                },
                {
                    "h": "Entender el negocio y no perder la mano",
                    "p": [
                        "Los impulsores del negocio son el marco de cualquier decisión técnica. Si la empresa necesita lanzar una función en seis semanas para no perder una licitación, la arquitectura perfecta para dentro de tres años es irrelevante. Si el coste de una caída es enorme, la disponibilidad pesa más que la elegancia. El arquitecto traduce esas presiones en características medibles.",
                        "Mantenerse cerca del código evita diseñar castillos en el aire. No se trata de competir con el equipo, sino de conocer las fricciones reales: cuánto tarda una prueba, qué duele al desplegar, qué parte del sistema nadie quiere tocar. Ese conocimiento cambia las decisiones y da credibilidad cuando hay que pedir un esfuerzo.",
                        "El equilibrio es deliberado. Demasiado código y el arquitecto se convierte en un cuello de botella; demasiada distancia y sus decisiones se vuelven teóricas. Una práctica útil es asumir tareas pequeñas de alto valor, revisar los cambios críticos y participar en los incidentes. La arquitectura se corrige con el contacto con la realidad.",
                    ],
                },
            ],
            "brief": [
                "Arquitectura es lo caro de revertir; diseño es lo local y barato",
                "La amplitud técnica permite comparar, no solo ejecutar",
                "Un trade-off se explica: de qué depende y hacia dónde inclina",
                "El negocio y el código corrigen las ideas abstractas",
            ],
            "keys": [
                "Clasifica cada decisión por coste de reversión y alcance.",
                "Escribe las suposiciones junto a la decisión.",
                "Compara opciones con características y condiciones, no con gustos.",
                "Traduce presiones de negocio a umbrales medibles.",
                "Reserva tiempo de código para mantener las decisiones aterrizadas.",
            ],
            "example": "Un equipo duda entre una base relacional y un almacén documental para un catálogo. El arquitecto escribe las suposiciones: los productos tienen atributos distintos por categoría y las consultas más frecuentes son por identificador. Con esos datos, el modelo documental gana para el catálogo, pero la base relacional sigue siendo mejor para pedidos y pagos. La decisión final es usar cada motor donde su modelo encaja, no uno para todo.",
            "caution": "«Depende» sin criterios es una forma elegante de no decidir. Si no puedes enumerar qué observación cambiaría tu elección, todavía no has hecho el análisis.",
            "search": "trade-off arquitectura diseño amplitud técnica profundidad negocio impulsores decisiones suposiciones comparar opciones reversibilidad",
        },
        {
            "id": "fsam1l3",
            "lnum": 3,
            "title": "Características de arquitectura",
            "minutes": 9,
            "lead": "Disponibilidad, escalabilidad, seguridad, testabilidad, facilidad de despliegue. Las características de arquitectura son las cualidades que el sistema debe sostener y las que justifican su forma. El problema es que casi todas suenan deseables. Elegir bien exige separar lo operativo de lo estructural, distinguir lo explícito de lo implícito y aceptar que no se puede maximizar todo.",
            "diagram": ("matrix", {"rows": 5, "cols": 8, "mark": 12}),
            "caption": "Cada celda es una característica que compite por atención; solo unas pocas pueden ser prioritarias en una misma decisión.",
            "sections": [
                {
                    "h": "Qué cuenta como característica",
                    "p": [
                        "Una característica de arquitectura es un requisito de calidad que influye en la estructura y puede evaluarse. No es una función del producto ni una preferencia del equipo. «Los usuarios pueden buscar productos» es funcional; «la búsqueda responde en 300 ms con un millón de productos» es una característica. La segunda obliga a decidir sobre índices, caché o precomputación.",
                        "Las características suelen expresarse como adjetivos terminados en -idad, pero el nombre no basta. Hay que definir un escenario: quién la necesita, en qué condiciones, con qué umbral y cómo se mide. «Alta disponibilidad» sin número es una intención. «El checkout sigue aceptando pedidos si falla una zona, con pérdida máxima de 30 segundos de datos» es una restricción que se puede diseñar y probar.",
                        "Algunas características son de negocio y no técnicas: cumplimiento regulatorio, time-to-market, internacionalización o accesibilidad. También cuentan, porque limitan el espacio de soluciones. Un requisito legal de residencia de datos puede descartar un proveedor cloud antes de que empiece la comparación técnica.",
                    ],
                },
                {
                    "h": "Operativas, estructurales y de dominio",
                    "p": [
                        "Las características operativas describen cómo se comporta el sistema en ejecución: disponibilidad, rendimiento, escalabilidad, resiliencia, seguridad, observabilidad. Se miden en producción o en pruebas de carga y suelen competir entre sí. Añadir réplicas mejora la disponibilidad y complica la consistencia; cifrar extremo a extremo mejora la seguridad y limita la depuración.",
                        "Las características estructurales describen cómo se organiza el código: modularidad, mantenibilidad, testabilidad, portabilidad, facilidad de despliegue. Influyen en la velocidad del equipo más que en la experiencia del usuario, y por eso a veces se ignoran hasta que el sistema se vuelve imposible de cambiar. Un monolito sin límites puede cumplir todos los requisitos funcionales y ser, aun así, una mala arquitectura.",
                        "Las características de dominio nacen del negocio concreto. Un sistema de seguros necesita auditabilidad; una plataforma de subastas, latencia baja y equidad; un banco, integridad y trazabilidad. No se eligen de una lista genérica: se extraen de cómo funciona el sector, qué errores son caros y qué espera el cliente.",
                    ],
                },
                {
                    "h": "El mínimo malo y la prioridad",
                    "p": [
                        "No existe una arquitectura que maximice todas las características. Cada decisión favorece unas y sacrifica otras. El objetivo no es la perfección, sino el «mínimo malo»: la combinación que cumple lo indispensable y deja el resto en un nivel aceptable. Nombrar ese sacrificio es parte de la decisión, no una confesión de debilidad.",
                        "Para priorizar conviene clasificar las características en tres grupos: las que no se pueden negociar, las que se pueden mejorar más adelante y las que se pueden compensar con procesos. La seguridad suele estar en el primer grupo; la elegancia del código, en el segundo; cierta latencia, en el tercero si se puede mitigar con una cola o un mensaje al usuario.",
                        "El exceso de características también es un riesgo. Un equipo que intenta cumplir veinte cualidades a la vez no optimiza ninguna y multiplica la complejidad. Es mejor elegir tres o cuatro drivers, escribir sus escenarios y revisar el resto como restricciones de fondo. La arquitectura se vuelve coherente cuando sabe qué está dispuesta a perder.",
                    ],
                },
            ],
            "brief": [
                "Una característica se define con escenario, umbral y medida",
                "Operativas, estructurales y de dominio compiten entre sí",
                "No se maximiza todo: se busca el mínimo malo aceptable",
                "Tres o cuatro drivers bastan para orientar la arquitectura",
            ],
            "keys": [
                "Convierte cada característica en un escenario verificable.",
                "No aceptes una lista de veinte -ilidades sin prioridades.",
                "Incluye características de negocio y regulatorias.",
                "Declara qué se sacrifica al elegir una opción.",
                "Revisa las características cuando cambie el contexto.",
            ],
            "example": "Una plataforma de reservas define tres drivers: disponibilidad del 99,95 %, latencia de búsqueda por debajo de 400 ms y capacidad de desplegar dos veces al día. La consistencia fuerte del inventario queda como restricción, pero se limita al momento de confirmar la reserva. Esa separación permite usar caché para buscar y una transacción estricta para el último paso, en lugar de exigir consistencia fuerte en todo el sistema.",
            "caution": "Una característica sin forma de medirse no se puede gobernar. Si nadie sabe cómo comprobar «escalable», el equipo acabará discutiendo opiniones en lugar de datos.",
            "search": "características arquitectura atributos calidad ilidades operativas estructurales dominio disponibilidad escalabilidad seguridad mantenibilidad priorizar mínimo malo drivers",
        },
    ],
    "quiz": {
        "id": "fsam1q",
        "title": "Cierre del módulo 01",
        "summary": [
            "La arquitectura combina estructura, características, decisiones y principios; ninguna pieza por sí sola la define.",
            "El arquitecto decide con criterios, comunica, negocia y mantiene contacto con el negocio y con el código.",
            "Todo diseño es un trade-off: la decisión madura nombra lo que gana y lo que pierde.",
            "Las características de arquitectura se eligen, se priorizan y se miden con escenarios concretos.",
        ],
        "questions": [
            {
                "q": "¿Cuál de estas afirmaciones describe mejor una decisión de arquitectura y no un detalle de diseño?",
                "options": [
                    "Renombrar una variable privada de una clase",
                    "Separar el catálogo del checkout en módulos con contratos y datos propios",
                    "Cambiar el color de un botón",
                    "Elegir el formato de una fecha en un formulario",
                ],
                "answer": 1,
                "why": "La separación cambia contratos, límites y posiblemente despliegues; es cara de revertir y afecta a varios equipos. Las otras opciones son locales y reversibles.",
            },
            {
                "q": "Un equipo afirma que su sistema es «altamente disponible». ¿Qué falta para convertirlo en una característica útil?",
                "options": [
                    "Un diagrama de clases más detallado",
                    "Un escenario con condiciones, umbral y forma de medir la disponibilidad",
                    "Elegir una tecnología de moda",
                    "Añadir más microservicios",
                ],
                "answer": 1,
                "why": "Sin escenario ni umbral no hay forma de diseñar ni verificar la cualidad. La disponibilidad debe expresarse como objetivo medible y con condiciones de fallo.",
            },
            {
                "q": "¿Qué significa buscar el «mínimo malo» en arquitectura?",
                "options": [
                    "Elegir siempre la opción más barata",
                    "Aceptar que no se maximiza todo y elegir la combinación que cumple lo indispensable con sacrificios conocidos",
                    "Ignorar las características no funcionales",
                    "Copiar la arquitectura de una empresa grande",
                ],
                "answer": 1,
                "why": "Las características compiten. La decisión madura prioriza lo que no se puede negociar y declara qué se sacrifica, en lugar de prometer excelencia en todo.",
            },
            {
                "q": "¿Por qué conviene mantener contacto con el código siendo arquitecto?",
                "options": [
                    "Para escribir todas las líneas y controlar al equipo",
                    "Para conocer las fricciones reales y mantener las decisiones aterrizadas",
                    "Porque el código sustituye a la conversación con el negocio",
                    "Para evitar documentar decisiones",
                ],
                "answer": 1,
                "why": "El contacto con el código revela costes y límites que los diagramas ocultan. No se trata de sustituir al equipo, sino de tomar decisiones informadas por la realidad.",
            },
        ],
        "exercises": [
            "Elige un sistema que conozcas y escribe sus cuatro piezas: estructura, tres características, dos decisiones y un principio.",
            "Toma una decisión reciente y anota qué ganó, qué perdió y qué observación te haría cambiarla.",
            "Convierte tres adjetivos de calidad de tu proyecto en escenarios medibles con umbral y condición de fallo.",
        ],
        "search": "cierre arquitectura definición características decisiones trade-off prioridad escenarios rol del arquitecto",
    },
}
