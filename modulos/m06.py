MODULE = {
    "num": "06",
    "title": "Decisiones y riesgo",
    "sub": "Documentar, evaluar y comunicar",
    "lessons": [
        {
            "id": "fsam6l1",
            "lnum": 1,
            "title": "Decisiones de arquitectura",
            "minutes": 8,
            "lead": "Una arquitectura es, en el fondo, un conjunto de decisiones. Si no se registran, el equipo las redescubre, las contradice o las defiende sin saber por qué existen. Documentar no significa escribir un manual de cien páginas: significa dejar claro qué se decidió, en qué contexto y con qué consecuencias.",
            "diagram": ("flow", ["Contexto", "Decisión", "Consecuencias", "Estado"]),
            "caption": "Un ADR cuenta el contexto que obligó a decidir, la opción tomada, lo que se gana y se pierde, y el estado actual de la decisión.",
            "sections": [
                {
                    "h": "Los anti-patrones que todos reconocen",
                    "p": [
                        "El primero es «cubrirse las espaldas»: se elige la tecnología más segura o la que nadie puede criticar, aunque no resuelva el problema. El segundo es «el día de la marmota»: la misma discusión vuelve cada pocos meses porque nunca se registró la decisión. El tercero es «decisiones por correo»: la arquitectura vive en hilos dispersos que nadie puede reconstruir.",
                        "Estos anti-patrones comparten una causa: la decisión no tiene un lugar estable. Cuando el contexto se pierde, el equipo repite el debate o cambia de rumbo por cansancio. El coste no es solo el tiempo: también la confianza. La gente deja de proponer alternativas porque sabe que la discusión no llevará a ninguna parte.",
                        "La solución no es documentar todo, sino lo significativo. Una decisión menor puede vivir en el código o en un ticket. Una decisión que afecta a varios equipos, cambia un contrato o es cara de revertir merece un registro propio. La pregunta es siempre la misma: ¿qué necesitará saber alguien dentro de un año para entender por qué esto es así?",
                    ],
                },
                {
                    "h": "Qué es arquitectónicamente significativo",
                    "p": [
                        "Una decisión es significativa si cambia la estructura, las características o las dependencias entre equipos. Elegir una base de datos, definir el modelo de despliegue, adoptar un estilo de comunicación o establecer una política de datos son ejemplos. Elegir el nombre de una clase o el formato de un log no lo son, salvo que afecten a un contrato público.",
                        "También es significativa una decisión que cierra opciones. Si elegir una plataforma propietaria impide migrar durante años, el coste de revertir es alto y merece registro. Si una elección se puede cambiar en una tarde, el registro puede ser una línea en el ticket. La profundidad de la documentación debe seguir al coste de equivocarse.",
                        "El arquitecto no decide todo ni documenta todo. Su trabajo es asegurar que las decisiones importantes tienen contexto y dueño, y que las pequeñas pueden tomarlas quienes están más cerca del problema. Esa distribución evita el cuello de botella y mantiene la coherencia donde de verdad importa.",
                    ],
                },
                {
                    "h": "El formato ADR",
                    "p": [
                        "Un Architecture Decision Record se escribe en pocas líneas: título, estado, contexto, decisión y consecuencias. El contexto explica las fuerzas en juego, incluidas las restricciones de negocio. La decisión dice qué se elige. Las consecuencias enumeran lo que se gana, lo que se pierde y lo que queda pendiente. El estado puede ser propuesto, aceptado, reemplazado o descartado.",
                        "Los ADR se guardan junto al código y se versionan con él. Así la decisión viaja con el sistema y aparece en la revisión de cambios. Un índice o una wiki ayuda a navegar, pero el registro debe poder leerse sin herramientas especiales. La brevedad es una virtud: si nadie lo lee, no sirve.",
                        "Los ADR también sirven para cambiar de opinión. Cuando una decisión se reemplaza, el nuevo registro enlaza al anterior y explica qué cambió. Esa historia evita que la arquitectura parezca arbitraria y muestra que el equipo aprende. Una decisión revisada con contexto no es un fracaso; es evidencia de que el sistema está vivo.",
                    ],
                },
            ],
            "brief": [
                "Sin registro, las decisiones se repiten o se contradicen",
                "Documenta lo significativo y caro de revertir, no todo",
                "Un ADR cabe en una página: contexto, decisión, consecuencias, estado",
                "Reemplazar una decisión con un nuevo ADR es sano",
            ],
            "keys": [
                "Pregunta qué necesitará saber alguien dentro de un año.",
                "Registra el contexto y las fuerzas, no solo la opción.",
                "Incluye costes y condiciones de revisión.",
                "Versiona los ADR junto al código.",
                "Enlaza la decisión nueva con la que reemplaza.",
            ],
            "example": "Un equipo decide usar una cola gestionada para desacoplar el envío de correos. El ADR explica que el envío no puede bloquear el checkout, que se acepta un retraso de segundos y que el coste por mensaje es menor que mantener un broker propio. Seis meses después, el volumen crece y el coste se dispara. El nuevo ADR revisa la decisión con datos y propone un broker autogestionado. La historia queda clara.",
            "caution": "Un ADR que solo dice «se decidió usar X» no es un registro, es un anuncio. Sin contexto y consecuencias, el equipo no puede evaluar si la decisión sigue vigente.",
            "search": "decisiones arquitectura ADR anti-patrones cubrirse espaldas día marmota correo significativo contexto consecuencias estado wiki",
        },
        {
            "id": "fsam6l2",
            "lnum": 2,
            "title": "Análisis de riesgo",
            "minutes": 8,
            "lead": "Toda arquitectura apuesta por un futuro que no puede prever. El riesgo no se elimina: se identifica, se prioriza y se vigila. Una matriz de probabilidad e impacto ayuda a ordenar, pero el trabajo real está en las conversaciones que revelan qué podría fallar y qué haría el equipo si ocurriera.",
            "diagram": ("matrix", {"rows": 5, "cols": 5, "mark": 12}),
            "caption": "La matriz cruza probabilidad e impacto; las celdas altas concentran la atención, pero también importan los riesgos de baja probabilidad con impacto catastrófico.",
            "sections": [
                {
                    "h": "Riesgo, incertidumbre y matriz",
                    "p": [
                        "Un riesgo de arquitectura es la posibilidad de que una decisión estructural impida cumplir un objetivo. No es un bug conocido ni una tarea pendiente: es una incertidumbre con consecuencias. Puede venir de una tecnología no probada, de un requisito que cambia, de una dependencia externa o de una capacidad del equipo que no existe.",
                        "La matriz de riesgo cruza probabilidad e impacto. Un riesgo probable y grave exige acción inmediata; uno improbable y leve puede aceptarse. La utilidad de la matriz no está en el número, sino en la conversación: obliga a explicar por qué se cree que algo es probable y qué significaría que ocurriera. Sin esa discusión, se convierte en una hoja de cálculo decorativa.",
                        "Hay riesgos que no caben en la matriz, como los de cola larga: baja probabilidad y daño enorme. Para esos conviene tener planes de contingencia aunque no se prioricen en el día a día. La pregunta es qué haría el equipo si ocurriera y cuánto costaría recuperarse. A veces la respuesta es un seguro, un límite de impacto o una salida de emergencia.",
                    ],
                },
                {
                    "h": "Evaluaciones y risk storming",
                    "p": [
                        "Una evaluación de riesgo puede ser una revisión ligera de la arquitectura con las partes interesadas o un análisis más profundo de escenarios. Lo importante es que participe gente con perspectivas distintas: quien opera, quien desarrolla, quien atiende al cliente y quien toma decisiones de negocio. Cada uno ve riesgos que los demás no ven.",
                        "El risk storming es una técnica colaborativa. Primero se presenta la arquitectura y se identifican las áreas críticas. Después, en silencio y por separado, cada participante marca los riesgos que percibe. Por último se comparan las marcas y se discuten las diferencias. El silencio inicial evita que la persona de mayor jerarquía sesgue el resultado.",
                        "El análisis de historias añade una mirada ágil: para cada historia o funcionalidad, se pregunta qué riesgo introduce en la arquitectura. Una historia que toca pagos, datos personales o integraciones externas puede merecer más atención que una pantalla nueva. Así el riesgo se evalúa en el flujo de trabajo y no solo en una revisión anual.",
                    ],
                },
                {
                    "h": "De la lista al plan",
                    "p": [
                        "Un riesgo sin dueño ni acción es una preocupación. El plan debe decir qué se va a hacer: probar un prototipo, medir una carga, contratar una capacidad, definir una salvaguarda o aceptar el riesgo con seguimiento. También debe decir cuándo se revisará y qué señal indicará que ha cambiado.",
                        "No todos los riesgos se mitigan. Algunos se aceptan porque el coste de reducirlos supera el beneficio; otros se transfieren a un proveedor o a un seguro. Lo importante es que la aceptación sea explícita. Un riesgo aceptado en silencio se convierte en sorpresa cuando ocurre, y la sorpresa suele costar más que el riesgo.",
                        "El análisis de riesgo también alimenta las decisiones de arquitectura. Si un riesgo es alto, quizá convenga elegir una opción más conservadora o añadir una salvaguarda. Si es bajo, se puede apostar por una solución más simple. La arquitectura no busca eliminar la incertidumbre, sino hacer apuestas informadas y mantener la capacidad de corregir.",
                    ],
                },
            ],
            "brief": [
                "Riesgo = incertidumbre con consecuencias, no bug ni tarea",
                "La matriz ordena la conversación, no la sustituye",
                "Risk storming recoge perspectivas antes de discutir",
                "Todo riesgo aceptado debe ser explícito y tener dueño",
            ],
            "keys": [
                "Describe el riesgo como condición y consecuencia.",
                "Involucra a operación, negocio y desarrollo.",
                "Usa silencio inicial para evitar sesgos de jerarquía.",
                "Asigna acción, dueño y fecha de revisión.",
                "Incluye planes para riesgos de baja probabilidad y alto impacto.",
            ],
            "example": "Antes de lanzar una función de pagos, el equipo hace un risk storming. Operaciones señala que el proveedor no tiene un plan de contingencia; negocio, que una caída en campaña sería grave; desarrollo, que la conciliación no está probada. El equipo prioriza dos acciones: un proveedor de respaldo y una prueba de conciliación con datos reales anonimizados. El resto se acepta con seguimiento.",
            "caution": "Una matriz con todos los riesgos en verde suele significar que nadie se atrevió a marcar rojo. Si el ejercicio no produce incomodidad, probablemente no ha explorado los escenarios difíciles.",
            "search": "riesgo arquitectura matriz probabilidad impacto evaluación risk storming historias plan mitigación aceptación contingencia",
        },
        {
            "id": "fsam6l3",
            "lnum": 3,
            "title": "Diagramar y presentar",
            "minutes": 8,
            "lead": "Un diagrama vale lo que ayuda a decidir. Si tiene veinte cajas, flechas sin dirección y colores sin leyenda, no comunica: decora. Presentar arquitectura es elegir la vista adecuada para cada audiencia y contar una historia con ella. El objetivo no es demostrar lo mucho que sabes, sino que el otro entienda qué se decide.",
            "diagram": ("stack", ["Contexto", "Contenedores", "Componentes", "Código"]),
            "caption": "Las vistas van de lo general a lo concreto; cada audiencia necesita un nivel distinto y un propósito explícito.",
            "sections": [
                {
                    "h": "Capas de diagramas y propósito",
                    "p": [
                        "El modelo C4 propone cuatro niveles: contexto, contenedores, componentes y código. El contexto muestra el sistema, sus usuarios y los sistemas externos. Los contenedores muestran aplicaciones, servicios y almacenes. Los componentes muestran las piezas internas de un contenedor. El código muestra clases o módulos, y solo se dibuja cuando aporta algo.",
                        "Cada diagrama debe tener un título, un propósito y una leyenda. Las flechas indican dirección y tipo de dependencia; los colores, una categoría explicada. Si el lector necesita adivinar qué significa una caja, el diagrama ha fallado. La consistencia entre diagramas también importa: los mismos nombres y formas para las mismas cosas.",
                        "No todos los diagramas son estructurales. También hay diagramas de despliegue, de secuencia, de estados y de datos. Elegir el tipo correcto evita forzar una vista para un propósito que no le corresponde. Un diagrama de secuencia explica una interacción; un diagrama de contexto no.",
                    ],
                },
                {
                    "h": "Presentar para una audiencia",
                    "p": [
                        "La presentación empieza por la audiencia y la decisión que se quiere facilitar. Un comité ejecutivo necesita impacto, coste, riesgo y opciones; un equipo técnico necesita contratos, dependencias y detalles de implementación. El mismo sistema se cuenta distinto. Usar el diagrama técnico con negocio o el resumen ejecutivo con el equipo produce desconexión.",
                        "Una narrativa útil sigue un arco: contexto, problema, opciones, trade-offs, recomendación y siguientes pasos. No empieces por la solución sin haber explicado el problema. Reconoce lo que no sabes y lo que la decisión sacrifica. La honestidad genera confianza y evita que las preguntas difíciles aparezcan cuando ya no hay tiempo de responderlas.",
                        "Las herramientas importan menos que la claridad. Una pizarra bien ordenada supera a un diagrama sofisticado y confuso. Si usas una herramienta, versiona los diagramas junto al código y evita que se queden obsoletos. Un diagrama desactualizado es peor que ninguno: da una falsa sensación de conocimiento.",
                    ],
                },
                {
                    "h": "Diagramas que sobreviven",
                    "p": [
                        "Un buen diagrama responde a una pregunta concreta. «¿Qué servicios llaman a qué base?», «¿dónde cruza la frontera de datos?», «¿qué pasa si falla este componente?». Si no puedes formular la pregunta, probablemente no necesites el diagrama. La claridad del propósito guía el nivel de detalle y evita la trampa de dibujarlo todo.",
                        "La evolución también se dibuja. Un diagrama de estado actual y otro de estado objetivo, con las transiciones y los riesgos, comunica mejor una migración que una imagen única. Los equipos necesitan ver el camino, no solo el destino. Y necesitan saber qué se mantiene, qué se reemplaza y en qué orden.",
                        "Por último, un diagrama debe poder mantenerse. Si actualizarlo cuesta una tarde, se abandonará. Prefiere vistas pequeñas, nombres estables y una fuente de verdad cercana al código. La documentación viva no es la que se escribe una vez, sino la que el equipo puede corregir cuando cambia el sistema.",
                    ],
                },
            ],
            "brief": [
                "Cada diagrama responde a una pregunta y tiene una audiencia",
                "Contexto, contenedores, componentes y código son niveles distintos",
                "La narrativa explica problema, opciones y trade-offs antes de la solución",
                "Un diagrama desactualizado es peor que ninguno",
            ],
            "keys": [
                "Define propósito, título y leyenda antes de dibujar.",
                "Adapta el nivel de detalle a la audiencia.",
                "Usa nombres y símbolos consistentes entre vistas.",
                "Cuenta el problema y el trade-off, no solo la solución.",
                "Mantén los diagramas cerca del código y versiónalos.",
            ],
            "example": "Un arquitecto presenta una migración al comité. Empieza con un diagrama de contexto que muestra los sistemas externos y el coste de una caída. Luego usa un diagrama de contenedores para explicar qué se separa y qué se mantiene. Deja los detalles de componentes para una sesión con el equipo. El comité aprueba la fase uno porque entiende el riesgo y el retorno, no porque haya visto más cajas.",
            "caution": "Un diagrama con flechas en ambos sentidos y sin leyenda no muestra una arquitectura: muestra una maraña. La ambigüedad se interpreta de forma distinta en cada reunión y genera decisiones contradictorias.",
            "search": "diagramas arquitectura C4 contexto contenedores componentes código leyenda presentación audiencia narrativa trade-offs documentación viva",
        },
    ],
    "quiz": {
        "id": "fsam6q",
        "title": "Cierre del módulo 06",
        "summary": [
            "Las decisiones significativas necesitan contexto, consecuencias y estado, no solo un anuncio.",
            "El riesgo se gestiona con conversaciones, priorización y planes con dueño.",
            "Los diagramas sirven si responden a una pregunta y se adaptan a la audiencia.",
            "Documentar y presentar son parte de la arquitectura, no tareas posteriores.",
        ],
        "questions": [
            {
                "q": "¿Qué debe incluir un ADR además de la decisión tomada?",
                "options": [
                    "El código completo del módulo",
                    "El contexto, las consecuencias y el estado de la decisión",
                    "La lista de todos los empleados del equipo",
                    "El presupuesto anual de la empresa",
                ],
                "answer": 1,
                "why": "Sin contexto no se puede evaluar la decisión; sin consecuencias no se conocen sus costes; sin estado no se sabe si sigue vigente.",
            },
            {
                "q": "¿Para qué sirve el silencio inicial en un risk storming?",
                "options": [
                    "Para que la reunión termine antes",
                    "Para que cada participante marque riesgos sin sesgarse por la jerarquía o la opinión dominante",
                    "Para evitar que se hable de arquitectura",
                    "Para elegir la tecnología por votación",
                ],
                "answer": 1,
                "why": "Si todos marcan a la vez y en privado, emergen riesgos que no se dirían frente a un líder. Después se comparan y se discuten las diferencias.",
            },
            {
                "q": "¿Qué caracteriza a un diagrama útil?",
                "options": [
                    "Tener el máximo número de cajas posible",
                    "Responder a una pregunta concreta para una audiencia, con propósito y leyenda",
                    "Usar muchos colores sin explicación",
                    "Mostrar el código fuente completo",
                ],
                "answer": 1,
                "why": "El valor del diagrama está en la comunicación. Sin propósito, nivel adecuado y leyenda, el lector interpreta cosas distintas y la decisión se degrada.",
            },
            {
                "q": "Un riesgo de baja probabilidad y alto impacto no aparece en lo alto de la matriz. ¿Qué conviene hacer?",
                "options": [
                    "Ignorarlo porque es improbable",
                    "Definir un plan de contingencia y límites de impacto aunque no se priorice a diario",
                    "Eliminarlo de la lista",
                    "Aumentar la probabilidad para que suba en la matriz",
                ],
                "answer": 1,
                "why": "Los riesgos de cola larga pueden no ser prioritarios, pero su impacto justifica una salvaguarda. La ausencia de plan convierte un evento raro en una crisis.",
            },
        ],
        "exercises": [
            "Escribe un ADR de una página para una decisión reciente de tu proyecto.",
            "Haz un risk storming de tres personas sobre una arquitectura y prioriza dos acciones.",
            "Dibuja un diagrama de contexto y otro de contenedores del mismo sistema para dos audiencias distintas.",
        ],
        "search": "cierre decisiones ADR riesgo matriz risk storming diagramas C4 presentación audiencia narrativa documentación",
    },
}
