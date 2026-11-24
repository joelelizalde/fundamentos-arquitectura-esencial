MODULE = {
    "num": "04",
    "title": "Estilos distribuidos",
    "sub": "Cuando la red entra en el diseño",
    "lessons": [
        {
            "id": "fsam4l1",
            "lnum": 1,
            "title": "Service-based",
            "minutes": 9,
            "lead": "La arquitectura service-based ocupa un punto medio entre el monolito y los microservicios: pocos servicios gruesos, cada uno con una responsabilidad de negocio amplia, y a menudo una base de datos compartida. Es un estilo pragmático para organizaciones que necesitan separar despliegues sin asumir toda la complejidad de lo distribuido.",
            "diagram": ("stack", ["Cliente", "API", "Servicios de dominio", "Datos"]),
            "caption": "Un número reducido de servicios de dominio atiende a los clientes a través de una capa de API; los datos pueden ser compartidos o separados por servicio.",
            "sections": [
                {
                    "h": "Topología y variantes",
                    "p": [
                        "El estilo suele tener una interfaz de usuario, una capa de API y entre cuatro y doce servicios de dominio. Cada servicio abarca un área de negocio, como pedidos, inventario o facturación, y expone operaciones relativamente gruesas. No se busca una función por servicio, sino una unidad que un equipo pueda poseer y desplegar.",
                        "La base de datos puede ser única y compartida, o estar particionada por servicio. La primera opción simplifica las transacciones y las consultas entre áreas, pero acopla los equipos al esquema común. La segunda reduce el acoplamiento y obliga a resolver coherencia entre servicios. La elección depende de cuánto cambia cada dominio y de cuánto pesa la integridad inmediata.",
                        "La capa de API puede ser un gateway que enruta, autentica y compone respuestas. No debe convertirse en un lugar donde vive toda la lógica: si el gateway empieza a coordinar procesos de negocio, se transforma en un orquestador central y los servicios pierden autonomía. Su trabajo es mediar, no decidir el negocio.",
                    ],
                },
                {
                    "h": "Diseño y granularidad de servicios",
                    "p": [
                        "Un servicio service-based suele ser más grande que un microservicio. Agrupa varias operaciones relacionadas y comparte transacciones locales dentro de su frontera. Esa amplitud reduce el número de llamadas de red y facilita la consistencia, a cambio de menos independencia entre las funciones que contiene.",
                        "La granularidad correcta se mide por el cambio y por el equipo. Si dos capacidades siempre se modifican juntas y comparten datos, probablemente pertenecen al mismo servicio. Si tienen ritmos distintos, presupuestos distintos o requieren escalar de forma muy diferente, la separación puede compensar. El número de servicios no es una meta; el equilibrio sí.",
                        "Las operaciones deben ser lo bastante gruesas para evitar conversaciones chatty. Una pantalla que necesita veinte llamadas para pintarse está mal repartida. Es mejor una operación que devuelva el agregado necesario, aunque incluya datos de varias tablas del mismo servicio, que una coreografía de llamadas que multiplica la latencia y los fallos.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "Service-based encaja en organizaciones con dominios reconocibles, equipos no demasiado grandes y necesidad de despliegues separados sin una plataforma madura de microservicios. También es útil como paso intermedio: se separan los dominios más problemáticos y se mantiene el resto en una estructura conocida.",
                        "Sus puntos fuertes son la simplicidad relativa, la tolerancia a fallos aceptable y la posibilidad de compartir datos cuando la integridad manda. Sus debilidades son la escalabilidad granular limitada y el riesgo de que la base compartida se convierta en un punto de acoplamiento. Si todos los servicios escriben en las mismas tablas, la separación es solo de despliegue.",
                        "En las valoraciones típicas queda bien en simplicidad, coste y testabilidad, y en un punto medio en escalabilidad y despliegue. Es una opción sensata cuando el problema no exige docenas de servicios ni equipos independientes, pero sí algo más que un único monolito.",
                    ],
                },
            ],
            "brief": [
                "Pocos servicios gruesos con responsabilidades de negocio amplias",
                "Base compartida simplifica transacciones y acopla equipos",
                "Operaciones gruesas evitan conversaciones chatty",
                "Es un punto medio pragmático, no un microservicio incompleto",
            ],
            "keys": [
                "Alinea cada servicio con un área de negocio, no con una tabla.",
                "Decide conscientemente si los datos se comparten o se separan.",
                "Diseña operaciones que devuelvan lo que la pantalla necesita.",
                "Evita que el gateway acumule lógica de negocio.",
                "Vigila el esquema compartido como si fuera una API pública.",
            ],
            "example": "Una cadena de clínicas separa agenda, expediente y facturación en tres servicios sobre una base compartida. La agenda y la facturación se despliegan por separado y escalan distinto en temporada alta. El expediente mantiene transacciones locales con la agenda porque la integridad del paciente manda. El equipo documenta qué tablas puede tocar cada servicio para que la base no se degrade en un espacio común sin reglas.",
            "caution": "Una base compartida sin reglas de propiedad se convierte en un monolito con red. Cada servicio puede cambiar cualquier tabla y ningún equipo puede evolucionar su esquema sin coordinar a los demás.",
            "search": "service-based servicios dominio base compartida particionada granularidad API gateway transacciones latencia despliegue",
        },
        {
            "id": "fsam4l2",
            "lnum": 2,
            "title": "Arquitectura dirigida por eventos",
            "minutes": 9,
            "lead": "En un sistema dirigido por eventos, un componente anuncia que algo ocurrió y otros reaccionan sin que el emisor sepa quiénes son. Esa inversión del control permite desacoplar y añadir reacciones sin tocar al productor, pero también introduce asincronía, errores difíciles de rastrear y decisiones nuevas sobre orden, duplicados y pérdida de mensajes.",
            "diagram": ("flow", ["Productor", "Broker", "Consumidor", "Reacción"]),
            "caption": "El productor publica un evento y sigue; el broker lo retiene y lo entrega a los consumidores, que reaccionan a su propio ritmo.",
            "sections": [
                {
                    "h": "Broker y mediador: dos formas de coordinar",
                    "p": [
                        "En la topología de broker, el productor publica un evento y el intermediario lo entrega a los consumidores interesados. No hay un componente que conozca el proceso completo. Es el modelo más desacoplado y el más difícil de seguir cuando hay muchas etapas. La trazabilidad depende de que cada evento lleve identificadores y contexto suficiente.",
                        "En la topología de mediador, un componente central conoce el flujo y decide qué evento enviar a quién, en qué orden y qué hacer si un paso falla. Gana control y visibilidad, pero concentra lógica y puede convertirse en un orquestador que acopla a todos. La elección depende de si el proceso es emergente o tiene reglas y pasos obligatorios.",
                        "Ambas topologías pueden combinarse. Un mediador puede coordinar los pasos críticos y dejar que otros eventos se propaguen libremente para efectos secundarios. La clave es que el flujo principal tenga dueño y que las reacciones no esenciales no bloqueen ni dupliquen el trabajo del núcleo.",
                    ],
                },
                {
                    "h": "Asincronía, errores y pérdida de datos",
                    "p": [
                        "La asincronía mejora la capacidad de respuesta y la tolerancia a picos: el productor no espera a que todos los consumidores terminen. A cambio, el resultado es eventual y el usuario puede ver un estado intermedio. Hay que decidir qué se muestra mientras el proceso avanza y cómo se informa de un fallo que ocurre después de responder.",
                        "Los errores no desaparecen: se mueven. Un consumidor puede fallar, procesar dos veces o recibir eventos fuera de orden. Las soluciones habituales son reintentos con retroceso, colas de mensajes fallidos, idempotencia y compensaciones. Sin idempotencia, un reintento puede cobrar dos veces o crear dos pedidos; sin orden, una actualización vieja puede pisar a una nueva.",
                        "La pérdida de datos es otro riesgo. Un broker en memoria puede perder eventos si cae; uno persistente puede retenerlos, pero exige políticas de retención y limpieza. También hay que definir qué significa «entregado»: al menos una vez, como máximo una vez o exactamente una vez. Cada garantía tiene un coste y ninguna es gratuita.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "La arquitectura dirigida por eventos encaja en sistemas con reacciones múltiples, integración entre dominios, procesamiento en tiempo real y cargas que varían. También cuando se quiere añadir consumidores sin modificar al productor. Es menos adecuada para flujos simples de petición-respuesta donde la latencia y la claridad mandan.",
                        "Sus puntos fuertes son el desacoplamiento, la elasticidad y la capacidad de broadcast. Sus debilidades son la complejidad operativa, la depuración distribuida y la consistencia eventual. Un equipo sin observabilidad ni disciplina de contratos puede crear un sistema donde nadie sabe por qué un pedido quedó a medias.",
                        "En las valoraciones típicas destaca en escalabilidad y tolerancia a fallos, y pierde en simplicidad y testabilidad. La pregunta decisiva es si el negocio necesita reaccionar a hechos de forma desacoplada o si bastaría con llamadas directas bien diseñadas. Adoptar eventos por moda añade coste sin resolver un problema real.",
                    ],
                },
            ],
            "brief": [
                "Broker desacopla; mediador coordina y concentra lógica",
                "La asincronía traslada los errores al consumidor y al tiempo",
                "Idempotencia, orden y política de pérdida son decisiones obligatorias",
                "Encaja cuando hay reacciones múltiples o cargas variables",
            ],
            "keys": [
                "Define el contrato del evento y su versión.",
                "Elige broker o mediador según el control que necesites.",
                "Haz idempotentes los consumidores y prevé mensajes fallidos.",
                "Decide la garantía de entrega y su coste.",
                "Incluye identificadores de correlación para poder seguir el flujo.",
            ],
            "example": "Una tienda publica un evento de pedido confirmado. El servicio de inventario descuenta stock, el de correo envía la confirmación y el de analítica actualiza métricas. Si el correo falla, el pedido no se cancela: el mensaje va a una cola de reintentos. El inventario es idempotente por identificador de pedido para que un reintento no descuente dos veces.",
            "caution": "Un evento sin contrato estable es una trampa: cualquier consumidor puede depender de un campo interno y romperse cuando el productor cambia. Trata el evento como una API pública y versiónalo.",
            "search": "event-driven eventos broker mediador asincronía idempotencia orden pérdida mensajes reintentos cola fallos request-reply híbrido",
        },
        {
            "id": "fsam4l3",
            "lnum": 3,
            "title": "Space-based",
            "minutes": 8,
            "lead": "Cuando la base de datos se convierte en el cuello de botella y la carga llega en picos impredecibles, añadir servidores no basta. La arquitectura space-based mueve el estado a una rejilla en memoria replicada y procesa en unidades que no dependen de una base central para cada petición. Es un estilo exigente, pensado para elasticidad extrema.",
            "diagram": ("loop", ["Petición", "Unidad de proceso", "Rejilla de datos", "Sincronización"]),
            "caption": "Las unidades de proceso atienden en memoria y comparten el estado por una rejilla replicada; la base de datos queda como respaldo asíncrono.",
            "sections": [
                {
                    "h": "Topología: unidades y middleware virtualizado",
                    "p": [
                        "El estilo se organiza en unidades de procesamiento y un middleware virtualizado. Las unidades son instancias de la aplicación que atienden peticiones y mantienen el estado en memoria. El middleware incluye una rejilla de mensajería para enrutar, una rejilla de datos para replicar el estado, una rejilla de procesamiento para repartir trabajo y un gestor de despliegue que arranca o retira unidades según la carga.",
                        "La rejilla de datos es el corazón. Cada unidad tiene una copia o una partición del estado y las actualizaciones se replican entre nodos. Así una petición se resuelve sin ir a la base de datos. La base sigue existiendo como almacén duradero, pero se actualiza de forma asíncrona y no está en el camino crítico de cada operación.",
                        "El gestor de despliegue ajusta la capacidad según la demanda. Cuando el tráfico sube, añade unidades y replica datos; cuando baja, las retira. Esa elasticidad es la razón de ser del estilo, y también su mayor exigencia: sin un mecanismo fiable de replicación y arranque, el sistema pierde estado o se vuelve inconsistente.",
                    ],
                },
                {
                    "h": "Colisiones, réplicas y caché cercana",
                    "p": [
                        "Si dos unidades actualizan el mismo dato a la vez, aparece una colisión. Las estrategias habituales son la propiedad por partición, los relojes lógicos o vectores de versión, y las reglas de resolución. Sin una política clara, la última escritura gana y se pierde información sin que nadie lo note hasta que un usuario reclama.",
                        "La replicación puede ser completa o por particiones. La completa simplifica la lectura y multiplica el tráfico de sincronización; la particionada escala mejor y complica el enrutamiento. La caché cercana añade otra copia en el cliente o en un nodo próximo para reducir latencia, pero aumenta las lecturas obsoletas y el coste de invalidación.",
                        "El estilo también cambia la forma de pensar la durabilidad. Si la base se actualiza de forma asíncrona, una caída de todas las unidades puede perder los últimos cambios. Hay que decidir cuánto se puede perder, con qué frecuencia se sincroniza y cómo se recupera la rejilla al arrancar. La elasticidad no elimina la necesidad de un plan de recuperación.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "Space-based encaja en picos de tráfico muy altos y variables, subastas, reservas de última hora, juegos en línea o sistemas de precios en tiempo real. También cuando la latencia debe mantenerse baja aunque la carga crezca de golpe. Es menos útil para procesos con transacciones complejas y datos que deben ser exactos en todo momento.",
                        "Sus puntos fuertes son la elasticidad, la latencia y la tolerancia a la caída de la base. Sus debilidades son la complejidad, el coste de memoria y la dificultad de garantizar consistencia. Requiere un equipo con experiencia en sistemas distribuidos y una observabilidad excelente; no es un estilo para empezar.",
                        "En las valoraciones típicas destaca en escalabilidad y rendimiento, y pierde en simplicidad, testabilidad y coste. Antes de adoptarlo conviene comprobar si el cuello es realmente la base de datos o si una caché bien gestionada y un esquema adecuado resolverían el problema con menos riesgo.",
                    ],
                },
            ],
            "brief": [
                "Estado en una rejilla en memoria replicada, no en la base por petición",
                "Middleware virtualizado: mensajería, datos, procesamiento y despliegue",
                "Las colisiones exigen una política explícita de resolución",
                "Brilla en picos extremos y pierde en simplicidad y consistencia",
            ],
            "keys": [
                "Comprueba que la base sea el cuello antes de adoptarlo.",
                "Define propiedad de datos y resolución de colisiones.",
                "Elige replicación completa o particionada según escala.",
                "Fija cuánto dato puedes perder en una caída total.",
                "Invierte en observabilidad y pruebas de recuperación.",
            ],
            "example": "Una plataforma de venta de entradas recibe un millón de usuarios en los primeros minutos de un concierto. Las unidades de proceso mantienen el inventario en una rejilla particionada por evento; la base de datos se actualiza cada pocos segundos como respaldo. Las colisiones se resuelven por asiento y versión. La latencia se mantiene baja aunque la base esté saturada.",
            "caution": "Space-based sin política de durabilidad es una promesa peligrosa: todo va rápido hasta que todas las unidades caen y nadie sabe cuántos pedidos existían. La memoria no sustituye al registro.",
            "search": "space-based rejilla datos memoria unidades procesamiento elasticidad colisiones replicación caché cercana durabilidad picos",
        },
    ],
    "quiz": {
        "id": "fsam4q",
        "title": "Cierre del módulo 04",
        "summary": [
            "Service-based separa dominios con pocos servicios gruesos y un intercambio consciente entre datos compartidos y autonomía.",
            "Event-driven desacopla productores y consumidores a cambio de asincronía, errores trasladados y consistencia eventual.",
            "Space-based mueve el estado a memoria replicada para picos extremos, con un coste alto de complejidad y durabilidad.",
            "Ningún estilo distribuido elimina la red: cambia dónde aparecen sus fallos.",
        ],
        "questions": [
            {
                "q": "¿Cuál es el principal riesgo de una base de datos compartida en service-based?",
                "options": [
                    "Que el sistema sea demasiado rápido",
                    "Que el esquema se convierta en un punto de acoplamiento entre equipos",
                    "Que no se puedan hacer copias de seguridad",
                    "Que desaparezcan las transacciones locales",
                ],
                "answer": 1,
                "why": "Si todos los servicios escriben libremente en las mismas tablas, cualquier cambio de esquema exige coordinar a todos. La separación de despliegue no garantiza autonomía de datos.",
            },
            {
                "q": "En una arquitectura dirigida por eventos, ¿qué resuelve la idempotencia?",
                "options": [
                    "Que los eventos lleguen siempre en orden",
                    "Que repetir el procesamiento de un evento no duplique sus efectos",
                    "Que el broker nunca pierda mensajes",
                    "Que el productor espere la respuesta del consumidor",
                ],
                "answer": 1,
                "why": "Con entrega al menos una vez y reintentos, un consumidor puede recibir el mismo evento varias veces. La idempotencia evita efectos duplicados.",
            },
            {
                "q": "¿Qué componente de space-based mantiene el estado accesible sin ir a la base en cada petición?",
                "options": [
                    "La rejilla de datos replicada",
                    "El orquestador central",
                    "El registro de plugins",
                    "La capa de presentación",
                ],
                "answer": 0,
                "why": "La rejilla de datos replica el estado en memoria entre unidades. La base queda como respaldo asíncrono, fuera del camino crítico.",
            },
            {
                "q": "¿Cuándo es menos recomendable adoptar un estilo distribuido?",
                "options": [
                    "Cuando un equipo pequeño puede operar un monolito modular y no hay necesidad de escalar partes por separado",
                    "Cuando hay picos de tráfico extremos",
                    "Cuando varios equipos necesitan desplegar sin coordinar",
                    "Cuando la latencia debe mantenerse baja con carga variable",
                ],
                "answer": 0,
                "why": "Distribuir añade red, fallos parciales y operación. Si una sola unidad basta para el tamaño y el ritmo del equipo, el coste supera el beneficio.",
            },
        ],
        "exercises": [
            "Compara service-based y microservicios para un dominio con tres equipos y una base compartida.",
            "Diseña el contrato de un evento de pedido confirmado y define qué garantía de entrega usarías.",
            "Explica en una página si un pico de tráfico justificaría space-based o si bastaría con caché y colas.",
        ],
        "search": "cierre service-based event-driven space-based estilos distribuidos base compartida eventos rejilla elasticidad",
    },
}
