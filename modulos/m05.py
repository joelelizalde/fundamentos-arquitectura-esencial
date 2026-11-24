MODULE = {
    "num": "05",
    "title": "Microservicios y elección",
    "sub": "El coste de repartir el sistema",
    "lessons": [
        {
            "id": "fsam5l1",
            "lnum": 1,
            "title": "SOA orquestada",
            "minutes": 8,
            "lead": "La arquitectura orientada a servicios fue la gran apuesta de integración empresarial: servicios reutilizables, contratos amplios y un bus o un orquestador que coordinaba el conjunto. Muchos de sus problemas explican por qué después llegaron los microservicios. Entenderla evita repetir sus errores con otro nombre.",
            "diagram": ("stack", ["Servicios de negocio", "Servicios empresariales", "Servicios de aplicación", "Infraestructura"]),
            "caption": "La taxonomía SOA separa servicios por nivel de negocio; el orquestador central coordina las llamadas y concentra el conocimiento del proceso.",
            "sections": [
                {
                    "h": "Taxonomía y orquestación",
                    "p": [
                        "SOA organiza los servicios en capas: servicios de aplicación que envuelven sistemas existentes, servicios empresariales que agrupan capacidades comunes, servicios de negocio que representan procesos completos y servicios de infraestructura que cubren seguridad, registro o mensajería. Cada nivel ofrece contratos a los superiores y oculta los detalles de los inferiores.",
                        "El orquestador es el componente que conoce el proceso de negocio y decide el orden de las llamadas. Recibe una petición, invoca servicios, transforma datos, compensa errores y devuelve un resultado. Esa centralización da control y visibilidad, pero también crea un punto único de cambio y de fallo. El proceso vive en el motor, no en los servicios.",
                        "El bus de servicios añade enrutamiento, transformación y mediación de protocolos. Su promesa es integrar sistemas heterogéneos sin tocar cada extremo. Su riesgo es convertirse en una capa de lógica oculta donde se resuelven las diferencias con reglas que nadie documenta. Cuando el bus sabe demasiado del negocio, el acoplamiento se concentra en la infraestructura.",
                    ],
                },
                {
                    "h": "Reutilización y acoplamiento",
                    "p": [
                        "SOA persigue reutilización: un servicio de clientes o de direcciones debe servir a muchos procesos. Esa ambición tiene un precio. Cuantos más consumidores dependen de un servicio, más difícil es cambiar su contrato. La reutilización amplia convierte cada servicio en una API pública de facto, con la carga de compatibilidad que eso implica.",
                        "Los contratos suelen ser amplios y basados en documentos, lo que facilita la integración pero difumina la responsabilidad. Un servicio que devuelve todo lo que alguien podría necesitar se vuelve difícil de entender y de evolucionar. La alternativa es diseñar contratos específicos por consumidor, que reduce el acoplamiento y multiplica las variantes.",
                        "La gobernanza central intenta ordenar ese ecosistema con estándares, registros y revisiones. Funciona cuando hay pocos equipos y un lenguaje común; se vuelve cuello de botella cuando la organización crece. La lección para los microservicios es clara: la autonomía sin contrato explícito no escala, y el contrato sin autonomía tampoco.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "SOA orquestada encaja en integraciones empresariales con sistemas heredados, procesos con pasos obligatorios y necesidad de auditoría central. También cuando la organización ya tiene un bus maduro y un equipo que lo opera. En esos contextos, su control y su reutilización pueden ser valiosos.",
                        "Sus puntos fuertes son la integración, la visibilidad del proceso y la reutilización de capacidades. Sus debilidades son el acoplamiento al orquestador, la complejidad del bus y la dificultad de desplegar cambios sin afectar varios servicios. Un cambio en el proceso suele requerir tocar el motor central y coordinar a todos los participantes.",
                        "En las valoraciones típicas queda bien en integración y gobierno, y flojo en agilidad, escalabilidad granular y simplicidad. No es un estilo para nuevos productos, pero sí una realidad que muchas empresas deben mantener. Conocerlo ayuda a decidir qué conservar y qué migrar.",
                    ],
                },
            ],
            "brief": [
                "Taxonomía de servicios por nivel y un orquestador que conoce el proceso",
                "La reutilización amplia convierte cada servicio en API pública",
                "El bus puede esconder lógica y acoplamiento en la infraestructura",
                "Útil en integración heredada; flojo en agilidad y despliegue",
            ],
            "keys": [
                "Separa la coordinación del proceso de la lógica de cada servicio.",
                "Mide el coste de compatibilidad de cada servicio reutilizado.",
                "Evita que el bus acumule reglas de negocio ocultas.",
                "Documenta los contratos y sus consumidores.",
                "No migres a microservicios solo por rechazo a SOA.",
            ],
            "example": "Un banco mantiene un orquestador que coordina alta de cliente, verificación de identidad y apertura de cuenta. El proceso es estable y auditado, y el orquestador aporta trazabilidad. El equipo decide no desmontarlo, pero aísla la lógica de cada paso en servicios con contrato propio y reduce las reglas del bus. La modernización se hace por partes, sin reescribir el proceso completo.",
            "caution": "Un orquestador que contiene todas las reglas del negocio se convierte en un monolito con llamadas de red. Los servicios quedan como meros accesos a datos y pierden su autonomía.",
            "search": "SOA orientada servicios orquestación orquestador bus taxonomía reutilización acoplamiento contratos integración heredado",
        },
        {
            "id": "fsam5l2",
            "lnum": 2,
            "title": "Microservicios",
            "minutes": 9,
            "lead": "Los microservicios llevan la autonomía al extremo: servicios pequeños, desplegables por separado, dueños de su modelo y sus datos. Bien aplicados, permiten que varios equipos avancen sin coordinar cada cambio. Mal aplicados, convierten una aplicación en una red de llamadas frágiles donde nadie puede reconstruir un proceso completo.",
            "diagram": ("flow", ["Bounded context", "API", "Servicio", "Datos propios"]),
            "caption": "Cada contexto acotado expone una API y posee sus datos; la comunicación entre contextos es explícita y no comparte el modelo interno.",
            "sections": [
                {
                    "h": "Contextos acotados y capa de API",
                    "p": [
                        "El bounded context es la unidad conceptual que da sentido a un microservicio. Dentro de una frontera, un término tiene un significado preciso: «cliente» puede ser quien compra en el contexto de ventas y una entidad fiscal en el de facturación. El microservicio posee su modelo y no lo comparte con los demás. Esa independencia es lo que permite cambiarlo sin romper el resto.",
                        "La capa de API media entre los clientes y los servicios. Puede enrutar, autenticar, limitar tráfico y componer respuestas para una pantalla. No debe contener las reglas del negocio, porque entonces se convierte en un orquestador central. Su función es ofrecer una fachada estable mientras los servicios evolucionan por dentro.",
                        "Los frontends también pueden separarse por contexto. Una aplicación de cliente, una consola de operaciones y un panel de administración tienen necesidades distintas y ciclos distintos. Compartir un único frontend para todo obliga a coordinar cambios y mezcla audiencias. Separarlo permite que cada uno consuma las APIs que necesita.",
                    ],
                },
                {
                    "h": "Comunicación y datos distribuidos",
                    "p": [
                        "La comunicación puede ser síncrona, con llamadas HTTP o gRPC, o asíncrona, con eventos. La síncrona es fácil de entender y de depurar, pero acopla la disponibilidad y la latencia: si un servicio tarda, el llamador espera. La asíncrona desacopla y añade complejidad de orden, reintentos e idempotencia. La elección depende de si el llamador necesita una respuesta inmediata o solo anunciar un hecho.",
                        "Los datos son el punto más delicado. Cada servicio debe poseer su almacenamiento y exponer datos a través de su API, no de una base compartida. Eso evita el acoplamiento por esquema, pero elimina las transacciones entre servicios. Aparecen entonces las sagas, las compensaciones y la consistencia eventual. Un proceso que antes era una transacción local se convierte en una secuencia de pasos con estados intermedios.",
                        "La coreografía deja que cada servicio reaccione a eventos sin un coordinador central. Es muy desacoplada y difícil de seguir cuando el flujo crece. La orquestación explícita da visibilidad y control, pero concentra lógica. Muchos sistemas combinan ambas: coreografía para reacciones laterales y orquestación para procesos críticos con pasos obligatorios.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "Los microservicios encajan cuando hay varios equipos que necesitan desplegar sin coordinarse, dominios con ritmos de cambio distintos y una plataforma capaz de operar servicios: observabilidad, CI/CD, gestión de secretos, redes y políticas. Sin esa base, la autonomía se convierte en caos operativo.",
                        "Sus puntos fuertes son la autonomía de equipos, la escalabilidad granular y la posibilidad de elegir tecnología por servicio. Sus debilidades son la complejidad distribuida, el coste de operación y la dificultad de mantener la coherencia del negocio. Un equipo pequeño que adopta microservicios suele acabar con más infraestructura que producto.",
                        "En las valoraciones típicas destaca en escalabilidad y despliegue, y pierde en simplicidad, coste y testabilidad. La pregunta no es si los microservicios son modernos, sino si el sistema necesita varias unidades independientes y si la organización puede sostenerlas. Si la respuesta es no, un monolito modular es una decisión más avanzada, no más conservadora.",
                    ],
                },
            ],
            "brief": [
                "Cada contexto acotado posee su modelo, su API y sus datos",
                "La API media; no debe convertirse en orquestador de negocio",
                "Sin transacciones distribuidas aparecen sagas y consistencia eventual",
                "Exige plataforma y equipos; no es solo separar carpetas",
            ],
            "keys": [
                "Define la frontera por lenguaje y modelo, no por tecnología.",
                "Prohíbe el acceso directo a la base de otro servicio.",
                "Elige síncrono o asíncrono según la necesidad de respuesta.",
                "Diseña compensaciones para los procesos que cruzan servicios.",
                "No adoptes microservicios sin observabilidad y despliegue automatizado.",
            ],
            "example": "Una plataforma de viajes separa búsqueda, reserva y pagos. Búsqueda puede usar caché y aceptar datos con segundos de retraso; reserva necesita confirmar disponibilidad; pagos exige idempotencia y auditoría. Cada servicio posee su base. La reserva coordina con pagos mediante una saga con compensación: si el pago falla, se libera la plaza. La separación se justifica por ritmos y equipos distintos, no por moda.",
            "caution": "Llamar microservicio a un módulo que comparte base de datos y se despliega junto con los demás es un cambio de nombre, no de arquitectura. La autonomía empieza por los datos y el despliegue.",
            "search": "microservicios bounded context API gateway datos propios comunicación síncrona asíncrona coreografía orquestación sagas consistencia eventual autonomía",
        },
        {
            "id": "fsam5l3",
            "lnum": 3,
            "title": "Cómo elegir un estilo",
            "minutes": 8,
            "lead": "No existe el estilo definitivo. La elección depende de las características que importan, del tamaño del equipo, del dominio y del coste de operación. Copiar la arquitectura de una empresa famosa sin su contexto es una forma cara de aprender. Esta lección ofrece criterios para decidir y para cambiar de opinión a tiempo.",
            "diagram": ("matrix", {"rows": 6, "cols": 8, "mark": 33}),
            "caption": "Cada estilo puntúa distinto en cada característica; la decisión consiste en elegir el perfil que mejor encaja con los drivers, no el que gana en una casilla.",
            "sections": [
                {
                    "h": "Modas, mitos y criterios",
                    "p": [
                        "La industria cambia de moda cada pocos años: capas, SOA, microservicios, serverless, eventos. Cada estilo resuelve un problema y crea otro. El mito más común es que lo distribuido siempre escala mejor. Distribuir mejora ciertas formas de escala y empeora la simplicidad, la coherencia y el coste. La decisión debe empezar por el problema, no por la etiqueta.",
                        "Los criterios útiles son concretos: número de equipos que deben desplegar por separado, frecuencia de cambio por dominio, necesidad de escalar partes distintas, requisitos de disponibilidad, tolerancia a la consistencia eventual y madurez operativa. También cuentan el presupuesto, el plazo y la capacidad de contratar. Una arquitectura que el equipo no puede operar no es una opción.",
                        "El tamaño y la edad del sistema importan. Un producto nuevo con un equipo pequeño suele beneficiarse de un monolito modular; una organización grande con dominios maduros puede necesitar servicios. Un sistema heredado puede quedarse donde está y extraer solo las partes problemáticas. La migración total rara vez es la respuesta más económica.",
                    ],
                },
                {
                    "h": "Monolito, distribuido e híbridos",
                    "p": [
                        "El monolito modular ofrece transacciones locales, despliegue simple y una curva de operación baja. Su reto es mantener los límites internos: sin disciplina, los módulos se convierten en un bloque acoplado. Se puede reforzar con pruebas de dependencias, propiedad de paquetes y una estructura por dominio. Es una opción seria, no un fracaso.",
                        "Los estilos distribuidos ofrecen autonomía y escala granular a cambio de red, complejidad y operación. Service-based es un punto medio útil; event-driven brilla cuando hay reacciones múltiples; space-based es para picos extremos; microservicios exige plataforma y organización. La elección no es binaria: se puede empezar monolítico y extraer servicios cuando la fricción sea medible.",
                        "Los híbridos son frecuentes y sensatos. Un núcleo monolítico con servicios satélite para integraciones, un frontend separado, un motor de eventos para analítica. Lo importante es que cada frontera tenga una razón y un dueño. Un híbrido sin criterio es solo un sistema distribuido con partes que nadie entiende.",
                    ],
                },
                {
                    "h": "Decidir, registrar y revisar",
                    "p": [
                        "La decisión debe quedar escrita con sus drivers, opciones, elección y consecuencias. Ese registro permite revisar cuando cambian las circunstancias y evita que la arquitectura se defienda por identidad. También ayuda a explicar a los nuevos por qué el sistema tiene la forma que tiene, sin depender de la memoria de los fundadores.",
                        "Conviene definir señales de revisión: si el despliegue tarda más de X, si un equipo espera más de Y para cambiar su parte, si la base se satura en picos, si el coste de red supera el de cómputo. Esas señales convierten la arquitectura en algo vivo. Sin ellas, el estilo se fosiliza hasta que el coste de cambiarlo es prohibitivo.",
                        "La elección madura acepta el trade-off y lo comunica. No promete escalabilidad infinita ni simplicidad total. Dice qué se optimiza, qué se sacrifica y qué condición haría cambiar la decisión. Esa honestidad es más valiosa que cualquier diagrama y es la base de una arquitectura sostenible.",
                    ],
                },
            ],
            "brief": [
                "Elegir por drivers, equipo y operación, no por moda",
                "El monolito modular es una opción seria, no un fracaso",
                "Los híbridos funcionan si cada frontera tiene razón y dueño",
                "Registrar la decisión y sus señales de revisión la mantiene viva",
            ],
            "keys": [
                "Empieza por las características y el tamaño del equipo.",
                "Compara coste total, no solo elegancia técnica.",
                "Prefiere extraer servicios cuando la fricción sea medible.",
                "Documenta drivers, opciones y consecuencias.",
                "Define señales que justifiquen revisar la elección.",
            ],
            "example": "Una startup de reservas empieza con un monolito modular porque su equipo es de cinco personas y necesita iterar rápido. Dos años después, el catálogo y las reservas tienen equipos y ritmos distintos, y el despliegue conjunto estorba. Extraen el catálogo como servicio y mantienen reservas y pagos en el monolito. La decisión no fue «microservicios sí o no», sino qué parte necesitaba autonomía.",
            "caution": "Una migración a microservicios justificada solo por «escalar» suele terminar en un sistema más caro y más lento. Si el cuello es una consulta o un esquema, distribuir no lo arregla: lo reparte.",
            "search": "elegir estilo arquitectura modas criterios monolito modular distribuido híbrido microservicios service-based coste equipo revisión",
        },
    ],
    "quiz": {
        "id": "fsam5q",
        "title": "Cierre del módulo 05",
        "summary": [
            "SOA orquestada integra mediante un coordinador central y paga con acoplamiento y complejidad.",
            "Los microservicios separan por contexto acotado y exigen datos propios, plataforma y compensaciones.",
            "La elección de estilo depende de drivers, equipos y operación, no de la etiqueta de moda.",
            "Los híbridos son válidos si cada frontera tiene una razón medible y un dueño.",
        ],
        "questions": [
            {
                "q": "¿Qué diferencia central hay entre un orquestador SOA y una coreografía de microservicios?",
                "options": [
                    "El orquestador conoce y dirige el proceso; en la coreografía cada servicio reacciona sin coordinador central",
                    "La coreografía no usa red",
                    "El orquestador solo funciona con eventos",
                    "La coreografía garantiza transacciones ACID entre servicios",
                ],
                "answer": 0,
                "why": "La orquestación centraliza el conocimiento del flujo; la coreografía lo distribuye en las reacciones de cada servicio. Cada opción tiene costes distintos de visibilidad y acoplamiento.",
            },
            {
                "q": "¿Por qué un microservicio no debe leer directamente la base de otro?",
                "options": [
                    "Porque la red es demasiado rápida",
                    "Porque acopla su evolución al esquema interno ajeno y rompe la autonomía",
                    "Porque las bases de datos no permiten dos conexiones",
                    "Porque impide usar eventos",
                ],
                "answer": 1,
                "why": "El acceso directo convierte el esquema en un contrato implícito. El dueño no puede cambiar sus tablas sin romper a otros, y la frontera deja de ser real.",
            },
            {
                "q": "Un equipo de cinco personas quiere microservicios para «escalar». ¿Qué pregunta debería hacerse primero?",
                "options": [
                    "Qué framework está de moda",
                    "Si el cuello real es la arquitectura o una consulta, y si el equipo puede operar la plataforma distribuida",
                    "Cuántos servicios puede dibujar en un diagrama",
                    "Si puede eliminar las pruebas",
                ],
                "answer": 1,
                "why": "Distribuir no arregla un cuello local y multiplica la operación. Primero hay que medir el problema y evaluar la capacidad real del equipo.",
            },
            {
                "q": "¿Qué señal justificaría revisar la elección de un monolito modular?",
                "options": [
                    "Que el equipo quiera probar una tecnología nueva",
                    "Que el despliegue conjunto impida a equipos con ritmos distintos entregar sin coordinar",
                    "Que la aplicación tenga más de diez clases",
                    "Que exista una base de datos relacional",
                ],
                "answer": 1,
                "why": "La fricción medible de coordinación es una razón legítima para extraer una frontera. La novedad tecnológica, por sí sola, no lo es.",
            },
        ],
        "exercises": [
            "Compara SOA orquestada y microservicios para un proceso de alta de cliente con auditoría.",
            "Define los bounded contexts de un producto que conozcas y una regla de datos por contexto.",
            "Escribe tres señales medibles que te harían pasar de monolito modular a servicios.",
        ],
        "search": "cierre SOA microservicios elegir estilo orquestación coreografía contextos datos autonomía monolito híbrido",
    },
}
