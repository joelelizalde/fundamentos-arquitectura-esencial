MODULE = {
    "num": "03",
    "title": "Estilos fundamentales",
    "sub": "Monolitos que resuelven bien un problema",
    "lessons": [
        {
            "id": "fsam3l1",
            "lnum": 1,
            "title": "Arquitectura en capas",
            "minutes": 8,
            "lead": "La arquitectura en capas es el estilo más conocido y el más malinterpretado. Su valor no está en dibujar cuatro cajas, sino en decidir qué dependencias se permiten y qué capas actúan como frontera. Bien usada, aísla cambios y ordena el código; mal usada, produce capas vacías que solo añaden latencia y ceremonia.",
            "diagram": ("stack", ["Presentación", "Negocio", "Persistencia", "Base de datos"]),
            "caption": "Cada capa ofrece un servicio a la superior y consume el de la inferior; las capas cerradas impiden saltarse intermediarios.",
            "sections": [
                {
                    "h": "Topología y capas de aislamiento",
                    "p": [
                        "En su forma clásica, la aplicación se divide en presentación, lógica de negocio, persistencia y base de datos. La presentación atiende la interacción, la lógica aplica reglas, la persistencia traduce objetos a almacenamiento y la base guarda los datos. Las capas pueden ser físicas o lógicas; lo importante es que cada una tenga una responsabilidad y una interfaz.",
                        "En una arquitectura de capas cerradas, una capa solo puede llamar a la inmediatamente inferior. Eso aisla los cambios: sustituir la base de datos no debería tocar la presentación. En una arquitectura de capas abiertas, una capa puede saltarse a otra si aporta valor. La decisión depende de cuánto aislamiento se necesita y de cuánta complejidad se está dispuesto a pagar.",
                        "El aislamiento también tiene un coste. Cada salto añade una traducción y una oportunidad de que la lógica se duplique. Si la capa de negocio solo reenvía llamadas, no está aislando nada. La prueba es simple: ¿qué cambio concreto permite hacer esta capa sin tocar las demás? Si la respuesta no existe, la capa es un peaje.",
                    ],
                },
                {
                    "h": "El efecto sinkhole y las capas que sobran",
                    "p": [
                        "El efecto sinkhole aparece cuando las peticiones atraviesan capas que no hacen nada: la presentación llama al servicio, el servicio llama al repositorio, el repositorio llama a otro repositorio y al final todo es un reenvío. El sistema gana líneas y latencia, pero no separación de responsabilidades. Es el síntoma más común de copiar el patrón sin entender el problema.",
                        "Una solución es permitir capas abiertas para los casos simples, sin forzar el paso por una capa que no aporta. Otra es reducir el número de capas y concentrar la lógica donde se decide. No hay que defender una estructura por su pureza, sino por el cambio que facilita. Si la mayoría de las operaciones son CRUD, quizá no necesites una capa de dominio elaborada.",
                        "También conviene vigilar la dirección de las dependencias. Si la capa de persistencia conoce detalles de la presentación o la de negocio importa clases del framework web, el aislamiento se rompe. Las pruebas de arquitectura, como las que revisan imports entre paquetes, convierten esa regla en una señal automática en lugar de una convención oral.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "La arquitectura en capas encaja bien en aplicaciones con equipos pequeños, requisitos estables y una separación clara entre interfaz, reglas y datos. Es fácil de entender, de probar por partes y de desplegar como una unidad. Para un sistema interno o un producto que empieza, su simplicidad suele ser una ventaja enorme.",
                        "Sus puntos débiles son la escalabilidad granular y la agilidad de despliegue. Todo se despliega junto, así que un cambio pequeño puede requerir una liberación completa. La lógica tiende a concentrarse en la capa de negocio, que puede convertirse en un monolito dentro del monolito si no se ponen límites por dominio.",
                        "Sus valoraciones típicas son buenas en simplicidad, coste y testabilidad, y flojas en escalabilidad y facilidad de despliegue. No es un estilo «anticuado»: es una opción con un perfil concreto. Elegirlo conscientemente es distinto de caer en él por defecto.",
                    ],
                },
            ],
            "brief": [
                "Capas cerradas aíslan; capas abiertas evitan saltos inútiles",
                "Una capa que solo reenvía llamadas no aporta aislamiento",
                "El efecto sinkhole añade latencia y código vacío",
                "Encaja en equipos pequeños y dominios estables",
            ],
            "keys": [
                "Define qué puede importar cada capa y verifícalo.",
                "Elimina capas que no permiten un cambio concreto.",
                "No fuerces saltos por capas que no aportan lógica.",
                "Mantén la lógica de negocio fuera de la presentación.",
                "Acepta el despliegue conjunto como parte del trade-off.",
            ],
            "example": "Una herramienta interna de gestión de incidencias usa capas cerradas: la interfaz habla con servicios de aplicación, estos con el dominio y el dominio con repositorios. Cuando cambian de PostgreSQL a un servicio gestionado, solo se toca la capa de persistencia. La separación se justifica porque ese cambio era probable y ocurrió sin tocar las pantallas.",
            "caution": "Una arquitectura en capas con un único servicio que reenvía todo al repositorio no es una arquitectura: es un formulario con pasos extra. Si no hay reglas en el medio, la capa de negocio sobra.",
            "search": "arquitectura capas layered presentación negocio persistencia capas cerradas abiertas aislamiento sinkhole simplicidad despliegue",
        },
        {
            "id": "fsam3l2",
            "lnum": 2,
            "title": "Arquitectura pipeline",
            "minutes": 8,
            "lead": "Hay sistemas que no responden a una petición: transforman un flujo de datos. Un compilador, una tubería de Unix, un proceso de carga nocturno o una cadena de validación siguen el mismo patrón: una etapa recibe, transforma y entrega a la siguiente. La arquitectura pipeline hace explícito ese flujo y evita que la lógica se mezcle con la orquestación.",
            "diagram": ("flow", ["Entrada", "Filtro A", "Filtro B", "Salida"]),
            "caption": "Los filtros son independientes entre sí; los tubos transportan el resultado de una etapa a la siguiente sin que las etapas se conozcan.",
            "sections": [
                {
                    "h": "Filtros, tubos y unidireccionalidad",
                    "p": [
                        "Un pipeline se compone de filtros y tubos. Cada filtro tiene una entrada, una transformación y una salida; el tubo conecta la salida de uno con la entrada del siguiente. Los filtros no saben quién produce ni quién consume: solo conocen su contrato. Esa ignorancia es lo que permite reordenarlos, sustituirlos o probarlos por separado.",
                        "El flujo es unidireccional. No hay llamadas de vuelta ni estado compartido entre etapas. Si una etapa necesita consultar a otra, el pipeline deja de ser un pipeline y se convierte en una red de dependencias. La unidireccionalidad es la fuente de su simplicidad: cada paso se puede entender mirando solo su entrada y su salida.",
                        "Los filtros pueden ser muy distintos: validar un campo, enriquecer un registro, aplicar una regla, agregar métricas o escribir un archivo. Lo que comparten es el contrato y la independencia. Esa uniformidad facilita la composición, pero también exige disciplina para que las etapas no se acoplen por el formato de los datos.",
                    ],
                },
                {
                    "h": "Ejemplos y variantes",
                    "p": [
                        "La línea de comandos de Unix es el ejemplo canónico: grep, sort y uniq se encadenan sin conocerse. Los compiladores usan el mismo esquema con análisis léxico, sintáctico, semántico, optimización y generación de código. Los procesos ETL aplican filtros de extracción, limpieza, transformación y carga. En todos, el valor está en separar las transformaciones.",
                        "La variante de procesamiento por lotes trabaja sobre un conjunto finito y almacenado; la de streaming trabaja sobre eventos conforme llegan. Ambas mantienen la idea de etapas, pero cambian las garantías: en streaming importan el orden, las ventanas y la tolerancia a eventos tardíos. La arquitectura pipeline no resuelve esos problemas por sí sola; solo ofrece un esqueleto para abordarlos.",
                        "También existen pipelines con ramificaciones, donde una etapa envía a varias. En ese caso conviene distinguir el flujo principal de los efectos secundarios, como auditoría o notificación. Si las ramas compiten por el mismo estado o dependen del orden, la simplicidad del patrón se pierde y hay que evaluar otro estilo.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "El pipeline encaja en transformaciones de datos, procesos por lotes, compiladores, validaciones encadenadas y cualquier tarea donde el resultado de una etapa alimenta a la siguiente. Es fácil de probar porque cada filtro tiene un contrato claro y se puede ejecutar de forma aislada con datos de ejemplo.",
                        "Su punto débil es la interactividad y la coordinación compleja. No es un buen estilo para una interfaz con muchas consultas cruzadas ni para procesos que requieren ida y vuelta entre etapas. Tampoco resuelve por sí mismo la escalabilidad: si una etapa es lenta, el flujo entero se frena, y paralelizar puede romper el orden.",
                        "En las valoraciones típicas destaca en simplicidad, testabilidad y bajo coste, y queda flojo en elasticidad y tolerancia a fallos. Para un proceso batch que puede reintentarse, eso es aceptable. Para una ruta crítica en tiempo real, hay que añadir buffers, checkpoints y una política clara de errores.",
                    ],
                },
            ],
            "brief": [
                "Filtros independientes conectados por tubos unidireccionales",
                "Cada etapa solo conoce su contrato de entrada y salida",
                "Encaja en ETL, compiladores y validaciones encadenadas",
                "Una etapa lenta frena el flujo; el orden puede limitar el paralelismo",
            ],
            "keys": [
                "Define el contrato de datos de cada filtro.",
                "Evita que las etapas se llamen entre sí o compartan estado.",
                "Trata los efectos secundarios como ramas explícitas.",
                "Mide cada etapa para encontrar el cuello.",
                "Añade checkpoints si el proceso debe reanudarse.",
            ],
            "example": "Una aseguradora recibe miles de partes diarios en CSV. El pipeline valida el formato, normaliza fechas y códigos, enriquece con datos de póliza y carga en el almacén. Cada filtro tiene pruebas con ficheros de ejemplo. Cuando cambia el formato de una aseguradora, solo se ajusta el validador; el resto del flujo sigue igual.",
            "caution": "Un pipeline con filtros que consultan una base compartida deja de ser un pipeline. El estado compartido acopla las etapas y elimina la posibilidad de reordenarlas o probarlas por separado.",
            "search": "pipeline pipes filtros tubos unidireccional ETL compilador batch streaming etapas contrato transformación",
        },
        {
            "id": "fsam3l3",
            "lnum": 3,
            "title": "Microkernel",
            "minutes": 8,
            "lead": "Algunos sistemas deben ser estables en el centro y flexibles en los bordes. Un IDE, un navegador o un motor de reglas comparten esa forma: un núcleo pequeño que ofrece el flujo básico y complementos que añaden capacidades sin modificarlo. La arquitectura microkernel convierte la extensibilidad en una decisión de diseño, no en un parche.",
            "diagram": ("flow", ["Petición", "Núcleo", "Registro", "Complemento"]),
            "caption": "El núcleo atiende el flujo común y consulta el registro para delegar en el complemento adecuado; los plugins no modifican el núcleo.",
            "sections": [
                {
                    "h": "Núcleo, registro y contratos",
                    "p": [
                        "El núcleo implementa el flujo mínimo que todos los casos comparten: abrir un documento, procesar una petición, evaluar una regla base. No contiene las variantes. Su tamaño reducido es una ventaja: menos código crítico, menos superficie de fallo y una base estable sobre la que construir.",
                        "El registro es el catálogo que permite al núcleo descubrir qué complementos existen y qué ofrecen. Puede ser un archivo de configuración, una base de datos o un mecanismo de descubrimiento. El núcleo no importa clases concretas de plugins: pide al registro lo que necesita según una clave o un contrato.",
                        "El contrato es la pieza que hace posible la extensión sin acoplamiento. Define qué métodos, datos y eventos expone un plugin, y qué garantías ofrece. Un contrato bien diseñado permite versionar, validar y aislar fallos. Uno mal diseñado obliga a los plugins a conocer detalles internos del núcleo, y la extensibilidad se convierte en una ilusión.",
                    ],
                },
                {
                    "h": "Ejemplos y límites",
                    "p": [
                        "Los IDE son el ejemplo clásico: el editor ofrece el núcleo y las extensiones añaden lenguajes, temas, linters y depuradores. Los navegadores usan complementos para funciones específicas. Las plataformas de seguros o de comercio electrónico usan reglas y conectores para adaptarse a cada mercado sin recompilar el núcleo.",
                        "El patrón no sirve para cualquier variación. Si los plugins necesitan comunicarse entre sí, comparten estado o dependen del orden de ejecución, el núcleo se convierte en un mediador complejo. Si el contrato cambia con frecuencia, cada actualización rompe extensiones y el coste de mantener la compatibilidad crece.",
                        "También hay que decidir dónde vive la lógica común. Si el núcleo empieza a acumular casos especiales para cada plugin, pierde su propósito. Una regla útil es que el núcleo solo conozca el contrato y el flujo general; todo lo específico de un cliente, mercado o formato vive en un complemento.",
                    ],
                },
                {
                    "h": "Cuándo encaja y qué sacrifica",
                    "p": [
                        "Microkernel encaja cuando hay un flujo estable y muchas variantes: productos configurables, plataformas con extensiones, sistemas con reglas por país o cliente. También cuando se quiere que terceros amplíen el sistema sin acceso al código del núcleo. La separación permite evolucionar las variantes a distinto ritmo.",
                        "Sus costes son la complejidad del registro, la gestión de versiones del contrato y la dificultad de probar combinaciones. Un plugin defectuoso puede tumbar el núcleo si no se aísla. La extensibilidad no elimina la necesidad de gobierno: exige reglas claras sobre qué puede hacer un complemento y cómo se despliega.",
                        "En las valoraciones típicas destaca en extensibilidad, personalización y simplicidad del núcleo, y pierde en rendimiento por la indirección y en facilidad de operación cuando hay muchos plugins. Es una buena opción cuando la variación es el corazón del negocio, no cuando es una excepción ocasional.",
                    ],
                },
            ],
            "brief": [
                "Núcleo pequeño y estable; variantes en complementos",
                "El registro descubre plugins; el contrato los aísla",
                "El núcleo no debe acumular casos especiales",
                "Extensible no significa libre: hay que gobernar versiones y fallos",
            ],
            "keys": [
                "Mantén el núcleo libre de lógica específica de cliente.",
                "Diseña un contrato versionado y explícito.",
                "Aísla los fallos de un plugin del flujo principal.",
                "Documenta qué puede y qué no puede hacer una extensión.",
                "Mide el coste de la indirección antes de adoptarlo.",
            ],
            "example": "Una plataforma de comercio permite calcular impuestos distintos por país. El núcleo gestiona el carrito y el checkout; cada país implementa un plugin de impuestos con el mismo contrato. Añadir un mercado nuevo es registrar un complemento y probarlo con casos de ejemplo, sin tocar el flujo de compra ni redeployar el núcleo.",
            "caution": "Un microkernel cuyo núcleo tiene un `if` por cada cliente ha perdido la arquitectura. La variación se ha movido al centro y ahora cada cambio amenaza a todos los mercados.",
            "search": "microkernel núcleo core plugins registro contrato extensibilidad personalización IDE navegador reglas variantes",
        },
    ],
    "quiz": {
        "id": "fsam3q",
        "title": "Cierre del módulo 03",
        "summary": [
            "Las capas aíslan cambios cuando la dependencia es explícita y las capas aportan lógica.",
            "El pipeline separa transformaciones unidireccionales y brilla en procesos de datos.",
            "El microkernel concentra lo común en un núcleo y delega la variación en complementos.",
            "Cada estilo tiene un perfil de características: no hay uno mejor en todo.",
        ],
        "questions": [
            {
                "q": "¿Qué indica el efecto sinkhole en una arquitectura en capas?",
                "options": [
                    "Que hay demasiadas pruebas",
                    "Que las peticiones atraviesan capas que no aportan lógica y solo añaden coste",
                    "Que la base de datos es demasiado rápida",
                    "Que el equipo usa capas abiertas",
                ],
                "answer": 1,
                "why": "El sinkhole es el reenvío vacío entre capas. Si una capa no permite un cambio ni añade una regla, su presencia encarece el sistema sin aislar nada.",
            },
            {
                "q": "¿Qué hace que un pipeline siga siendo un pipeline?",
                "options": [
                    "Que todas las etapas compartan una base de datos",
                    "Que los filtros sean unidireccionales y no se llamen entre sí",
                    "Que haya un orquestador central que decida el orden en tiempo de ejecución",
                    "Que cada etapa conozca el código de las demás",
                ],
                "answer": 1,
                "why": "La independencia y la dirección única son la base del estilo. El estado compartido o las llamadas cruzadas convierten el flujo en una red acoplada.",
            },
            {
                "q": "¿Dónde debe vivir la lógica específica de un cliente en un microkernel?",
                "options": [
                    "En el núcleo, para que todos la vean",
                    "En un complemento conectado mediante el contrato y el registro",
                    "En la base de datos compartida",
                    "En el código de la interfaz",
                ],
                "answer": 1,
                "why": "El núcleo debe permanecer estable y común. La variación por cliente, mercado o formato pertenece a un plugin que cumple el contrato.",
            },
            {
                "q": "Un proceso batch transforma ficheros en etapas y puede reintentarse. ¿Qué estilo encaja mejor?",
                "options": [
                    "Microservicios con eventos",
                    "Pipeline con filtros independientes y checkpoints",
                    "Space-based con rejilla en memoria",
                    "Microkernel con un plugin por fichero",
                ],
                "answer": 1,
                "why": "El pipeline es natural para transformaciones secuenciales sobre datos. Los checkpoints permiten reanudar sin rehacer todo el trabajo.",
            },
        ],
        "exercises": [
            "Dibuja las capas de un sistema que conozcas y marca una capa que podrías eliminar sin perder aislamiento.",
            "Convierte un proceso de validación en un pipeline de tres filtros con contratos explícitos.",
            "Propón un microkernel para un producto configurable y define el contrato mínimo de un plugin.",
        ],
        "search": "cierre capas pipeline microkernel estilos fundamentales sinkhole filtros plugins núcleo contrato",
    },
}
