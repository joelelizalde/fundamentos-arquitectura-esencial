MODULE = {
    "num": "07",
    "title": "Equipos y carrera",
    "sub": "La arquitectura también se negocia",
    "lessons": [
        {
            "id": "fsam7l1",
            "lnum": 1,
            "title": "Equipos eficaces",
            "minutes": 8,
            "lead": "Una arquitectura no funciona por el diagrama, sino por las personas que la construyen. El arquitecto influye en los límites del equipo, en su grado de autonomía y en la claridad de las reglas. Demasiado control ahoga; demasiada ausencia descoordina. El trabajo está en encontrar el punto que hace al equipo capaz y responsable.",
            "diagram": ("curve", {"x": "autonomía del equipo", "y": "capacidad de entrega", "a": "equipo con confianza", "b": "equipo sin dirección"}),
            "caption": "La capacidad crece con la autonomía hasta un punto; sin dirección ni límites, la coordinación se rompe y la entrega cae.",
            "sections": [
                {
                    "h": "Límites, autonomía y control",
                    "p": [
                        "Un equipo eficaz tiene un límite claro: sabe qué posee, qué decide y con quién coordina. Sin límite, todo el mundo opina sobre todo y nadie responde. Con un límite demasiado rígido, el equipo no puede resolver sus propios problemas y depende del arquitecto para cada cambio. La frontera debe incluir personas, código, datos y decisiones.",
                        "El grado de control del arquitecto varía con la madurez y el riesgo. Un equipo nuevo o un dominio crítico puede necesitar más revisión y acompañamiento. Un equipo experimentado con una frontera estable necesita menos. El error es aplicar el mismo nivel a todos: demasiada interferencia en lo maduro y demasiada libertad en lo delicado.",
                        "La autonomía no significa aislamiento. Un equipo autónomo conoce los contratos de los demás y participa en las decisiones que cruzan fronteras. La coordinación se hace por acuerdos explícitos, no por reuniones permanentes. Cuanto mejor es el contrato, menos hace falta negociar cada día.",
                    ],
                },
                {
                    "h": "Personalidades y señales de alerta",
                    "p": [
                        "El arquitecto «controlador» quiere revisar cada decisión y se convierte en cuello de botella. El «de sillón» diseña desde la distancia, sin contacto con el código ni con las fricciones reales. El «efectivo» combina criterio, presencia y delegación: ayuda a decidir, pero no decide por todos. Ningún estilo es puro; el contexto y la autoconciencia marcan la diferencia.",
                        "Las señales de alerta de un equipo aparecen antes que los fallos técnicos. Nadie sabe quién posee un módulo, las decisiones se repiten, las reuniones no terminan con acuerdos, el trabajo se acumula en una persona, los incidentes se resuelven a base de parches. Observar esas señales permite intervenir antes de que el sistema se degrade.",
                        "Las listas de comprobación ayudan a reducir olvidos en tareas repetibles, como una revisión de arquitectura, un despliegue o una auditoría. No sustituyen el juicio, pero liberan atención para lo importante. Una buena lista es corta, concreta y revisada con el equipo; una lista eterna se ignora.",
                    ],
                },
                {
                    "h": "Guía sin microgestión",
                    "p": [
                        "La guía eficaz ofrece principios, ejemplos y criterios, y deja que el equipo decida los detalles. Un principio como «los servicios no comparten base de datos» es más útil que una revisión caso por caso, porque permite al equipo evaluar sus propias decisiones. La regla debe explicar su razón para que se pueda aplicar a situaciones nuevas.",
                        "También conviene distinguir normas de recomendaciones. Una norma se cumple salvo excepción aprobada; una recomendación es un punto de partida. Mezclarlas genera confusión y discusiones. Si todo es obligatorio, el equipo deja de pensar; si nada lo es, la coherencia se pierde.",
                        "El arquitecto eficaz mide el efecto de su intervención. Si el equipo entrega más rápido, comete menos errores y resuelve mejor sus decisiones, la guía funciona. Si todo pasa por el arquitecto, el sistema tiene un cuello de botella con nombre. La arquitectura sostenible se reconoce porque el equipo puede explicarla y cambiarla sin depender de una sola persona.",
                    ],
                },
            ],
            "brief": [
                "Límites claros de personas, código, datos y decisiones",
                "El control se ajusta a madurez y riesgo, no se aplica igual a todos",
                "Las señales de alerta aparecen antes que los fallos técnicos",
                "Guía con principios; evita el cuello de botella del arquitecto",
            ],
            "keys": [
                "Define qué posee cada equipo y qué debe coordinar.",
                "Ajusta el nivel de control al riesgo y la madurez.",
                "Busca señales de dependencia excesiva o de decisiones repetidas.",
                "Usa listas cortas para lo repetible, no para todo.",
                "Explica la razón de cada norma para que se pueda aplicar.",
            ],
            "example": "Un arquitecto descubre que todas las decisiones de API pasan por él y el equipo espera días. Define un contrato de revisión: las APIs internas las decide el equipo con una guía; las que cruzan dominios se revisan en una sesión semanal. El número de bloqueos baja y las decisiones quedan registradas. El arquitecto recupera tiempo para los riesgos reales.",
            "caution": "Un equipo que pregunta al arquitecto hasta el nombre de una variable no es un equipo autónomo: es una extensión de la persona. La dependencia excesiva se disfraza de respeto y acaba frenando todo.",
            "search": "equipos eficaces límites autonomía control personalidades arquitecto señales alerta listas comprobación guía microgestión",
        },
        {
            "id": "fsam7l2",
            "lnum": 2,
            "title": "Negociación y liderazgo",
            "minutes": 8,
            "lead": "El arquitecto pasa buena parte del tiempo negociando: prioridades, plazos, alcance, estándares y excepciones. No siempre tiene autoridad formal, así que su influencia depende de la credibilidad, la escucha y la capacidad de enmarcar el problema. Liderar sin mando es una habilidad técnica más, y se puede practicar.",
            "diagram": ("loop", ["Escuchar", "Enmarcar", "Proponer", "Acordar"]),
            "caption": "Negociar no es imponer una solución: es entender intereses, enmarcar el problema común y acordar un camino con condiciones claras.",
            "sections": [
                {
                    "h": "Negociar intereses, no posiciones",
                    "p": [
                        "Una posición es «necesito dos semanas más». Un interés es «necesito reducir el riesgo de una caída en campaña». Cuando se negocian posiciones, alguien gana y alguien pierde. Cuando se exploran intereses, aparecen opciones: reducir el alcance, añadir una salvaguarda, desplegar por partes o cambiar la fecha de una función secundaria.",
                        "La facilitación ayuda a que la conversación produzca decisiones. Un facilitador neutral define el objetivo, da turnos, resume acuerdos y deja por escrito qué se decidió y qué queda abierto. En reuniones técnicas, la falta de facilitación suele producir debates largos que no cierran nada. El arquitecto puede ejercer ese papel sin imponer su solución.",
                        "También hay que saber cuándo no negociar. Algunas restricciones son legales, de seguridad o de integridad y no admiten excepción. Otras son preferencias disfrazadas de requisito. Distinguirlas evita ceder en lo importante y gastar energía en lo accesorio. La claridad sobre lo no negociable hace más fácil negociar el resto.",
                    ],
                },
                {
                    "h": "Liderazgo sin autoridad",
                    "p": [
                        "El liderazgo técnico se construye con credibilidad. Un arquitecto que entiende el código, escucha a quien opera y reconoce sus errores obtiene más influencia que uno que solo tiene el título. La credibilidad se pierde rápido cuando las decisiones ignoran la realidad o cuando se atribuye el mérito del equipo.",
                        "Liderar también es proteger el foco. El arquitecto ayuda a decir que no a lo que no encaja con los drivers, a frenar la complejidad innecesaria y a mantener las decisiones visibles. Esa protección no es paternalismo: es crear condiciones para que el equipo pueda hacer su mejor trabajo.",
                        "La comunicación debe adaptarse a la audiencia. Con negocio, habla de riesgo, coste y tiempo. Con el equipo, de contratos, dependencias y trade-offs. Con operaciones, de fallos, observabilidad y recuperación. El mismo mensaje con el mismo nivel de detalle para todos suele no convencer a nadie.",
                    ],
                },
                {
                    "h": "Integrarse con el equipo",
                    "p": [
                        "El arquitecto no es un visitante que aparece con un diagrama y se va. Participa en las decisiones difíciles, revisa los cambios críticos y está disponible cuando surge un problema. Esa presencia no significa escribir todo el código, sino compartir el contexto y ayudar a resolver.",
                        "La integración también implica aceptar que el equipo conoce detalles que el arquitecto no ve. Una decisión que ignora esos detalles suele fracasar en la implementación. Preguntar «¿qué te impide hacerlo así?» abre más puertas que explicar «así es como debe hacerse». La arquitectura se construye en diálogo.",
                        "Por último, el arquitecto debe cuidar la sostenibilidad del equipo. Los héroes que apagan fuegos todas las semanas no son un modelo. Un ritmo sostenible, turnos claros y tiempo para mejorar el sistema producen mejores resultados a largo plazo. Liderar es también proteger a las personas que sostienen la arquitectura.",
                    ],
                },
            ],
            "brief": [
                "Negocia intereses y opciones, no posiciones rígidas",
                "La facilitación cierra acuerdos y deja lo abierto por escrito",
                "La credibilidad se gana con criterio, escucha y contacto con la realidad",
                "Liderar es proteger el foco y sostener al equipo",
            ],
            "keys": [
                "Pregunta por el interés detrás de cada posición.",
                "Resume acuerdos y responsables al final de cada reunión.",
                "Distingue restricciones reales de preferencias.",
                "Adapta el mensaje a la audiencia.",
                "Participa sin convertirte en el cuello de botella.",
            ],
            "example": "Negocio pide una función nueva para una feria y el equipo dice que no llega. El arquitecto no negocia la fecha: pregunta qué se quiere demostrar en la feria. Descubre que basta una versión limitada para tres clientes. El equipo reduce el alcance, mantiene la calidad y llega con una demo funcional. La fecha se cumple porque el problema se reencuadró.",
            "caution": "Ganar una discusión técnica no es lo mismo que conseguir una decisión adoptada. Si el equipo no entiende o no comparte la razón, la cumplirá a medias y el problema volverá.",
            "search": "negociación liderazgo intereses posiciones facilitación acuerdos credibilidad audiencia equipo integración sostenibilidad",
        },
        {
            "id": "fsam7l3",
            "lnum": 3,
            "title": "La carrera del arquitecto",
            "minutes": 8,
            "lead": "La arquitectura se aprende en el trabajo, pero no por ósmosis. Requiere práctica deliberada, un radar personal de lo que cambia y una red que aporte perspectivas distintas. La carrera no es una línea recta hacia «más alto»: es una ampliación constante de criterio, contexto y capacidad de influencia.",
            "diagram": ("stack", ["Práctica diaria", "Radar personal", "Comunidad", "Reflexión"]),
            "caption": "La carrera se sostiene en hábitos: practicar, observar tendencias, contrastar con otros y revisar lo aprendido.",
            "sections": [
                {
                    "h": "La regla de los veinte minutos",
                    "p": [
                        "La regla de los veinte minutos propone dedicar un poco de tiempo cada día a aprender algo relacionado con la carrera: leer un artículo, probar una herramienta, revisar un patrón, escribir una nota. La constancia importa más que la intensidad. Veinte minutos diarios suman más de cien horas al año, suficientes para explorar varios temas.",
                        "El aprendizaje debe ser activo. Leer sin aplicar deja una sensación de conocimiento que se desvanece. Probar una idea en un proyecto pequeño, escribir un resumen o explicarla a alguien convierte la información en criterio. La práctica deliberada busca lo que aún no sabes hacer, no repetir lo que ya dominas.",
                        "También conviene alternar amplitud y profundidad. Una temporada para explorar un área nueva, otra para profundizar en un problema concreto. El arquitecto necesita ambas: la amplitud para comparar y la profundidad para no aceptar soluciones superficiales. El equilibrio cambia con el proyecto y la etapa de la carrera.",
                    ],
                },
                {
                    "h": "El radar personal y la comunidad",
                    "p": [
                        "El radar personal es una lista de temas que sigues de cerca: tecnologías, estilos, prácticas, regulación, tendencias del negocio. No se trata de leer todo, sino de saber qué existe y qué podría afectarte. Un radar bien cuidado evita la sorpresa y ayuda a distinguir una moda pasajera de un cambio estructural.",
                        "La comunidad amplía el radar. Conferencias, comunidades locales, proyectos open source, mentoría y conversaciones con colegas de otras empresas aportan perspectivas que el día a día no da. También ayudan a contrastar decisiones: quizá alguien ya recorrió el camino que estás empezando.",
                        "Compartir lo aprendido es parte del método. Escribir, dar una charla o mentorizar obliga a ordenar las ideas y revela lagunas. Además, construye reputación y red, dos activos que importan cuando hay que buscar un nuevo rol o convencer a una organización. La carrera se acelera cuando el aprendizaje se convierte en contribución.",
                    ],
                },
                {
                    "h": "Trayectoria, mentoría y decisiones",
                    "p": [
                        "La carrera del arquitecto no tiene un único camino. Algunos se especializan en un dominio, otros en plataformas, otros en liderazgo técnico o en estrategia. Lo importante es elegir con criterio y revisar la elección. Un título no define el rol; las responsabilidades y el impacto sí.",
                        "La mentoría acelera el aprendizaje porque transmite contexto, no solo técnica. Un buen mentor ayuda a ver patrones, a evitar errores repetidos y a decidir qué no hacer. También conviene ser mentor: enseñar consolida el conocimiento y mejora la capacidad de explicar, esencial para influir.",
                        "Con el tiempo, el arquitecto acumula experiencia, pero también sesgos. La práctica de revisar decisiones pasadas, pedir feedback y exponerse a ideas distintas mantiene el criterio afilado. La carrera sostenible no es la que acumula más tecnologías, sino la que conserva la curiosidad y la humildad para cambiar de opinión.",
                    ],
                },
            ],
            "brief": [
                "Veinte minutos diarios de aprendizaje sostenido superan los atracones",
                "El radar personal distingue tendencia de moda",
                "La comunidad contrasta decisiones y amplía perspectivas",
                "La carrera se revisa; no es una línea recta",
            ],
            "keys": [
                "Reserva tiempo diario para aprender y aplicar.",
                "Alterna amplitud y profundidad según el momento.",
                "Mantén un radar de temas y revísalo con periodicidad.",
                "Comparte lo aprendido para consolidarlo y crear red.",
                "Busca mentores y sé mentor; revisa tus sesgos.",
            ],
            "example": "Una arquitecta dedica veinte minutos antes de empezar a probar una idea nueva o leer un caso. Cada viernes anota qué aprendió y qué quiere explorar. Una vez al mes comparte una nota con su equipo. En un año ha probado tres tecnologías, ha mejorado su criterio y ha ganado confianza para proponer un cambio de estilo que antes no se atrevía a defender.",
            "caution": "Coleccionar cursos y certificados sin aplicar lo aprendido produce una carrera amplia en apariencia y frágil en la práctica. El criterio se construye con decisiones reales y reflexión, no con insignias.",
            "search": "carrera arquitecto regla veinte minutos radar personal comunidad mentoría aprendizaje práctica deliberada amplitud profundidad",
        },
    ],
    "quiz": {
        "id": "fsam7q",
        "title": "Cierre del módulo 07",
        "summary": [
            "Los equipos eficaces necesitan límites claros y un nivel de control ajustado al riesgo.",
            "Negociar intereses y facilitar acuerdos influye más que imponer posiciones.",
            "El liderazgo técnico se sostiene en credibilidad, escucha y protección del foco.",
            "La carrera se construye con práctica diaria, radar, comunidad y reflexión.",
        ],
        "questions": [
            {
                "q": "¿Qué caracteriza a un arquitecto «de sillón»?",
                "options": [
                    "Diseña desde la distancia, sin contacto con el código ni con las fricciones reales",
                    "Revisa cada línea de código del equipo",
                    "Solo se dedica a negociar presupuestos",
                    "Trabaja únicamente en producción",
                ],
                "answer": 0,
                "why": "El arquitecto de sillón produce diseños que no resisten el contacto con la implementación. La falta de contexto real hace que sus decisiones ignoren costes y límites.",
            },
            {
                "q": "En una negociación, ¿qué diferencia hay entre posición e interés?",
                "options": [
                    "La posición es lo que se pide; el interés es la necesidad que hay detrás",
                    "Son sinónimos",
                    "El interés es siempre económico",
                    "La posición solo existe en reuniones formales",
                ],
                "answer": 0,
                "why": "Explorar intereses permite encontrar opciones que satisfagan a ambas partes. Negociar solo posiciones suele producir un ganador y un perdedor.",
            },
            {
                "q": "¿Para qué sirve la regla de los veinte minutos?",
                "options": [
                    "Para limitar las reuniones a veinte minutos",
                    "Para sostener un aprendizaje diario y constante sobre la carrera",
                    "Para revisar el código cada veinte minutos",
                    "Para desplegar veinte veces al día",
                ],
                "answer": 1,
                "why": "La constancia diaria acumula conocimiento y práctica. Es más eficaz que estudiar mucho de forma esporádica y sin aplicación.",
            },
            {
                "q": "¿Qué señal indica que un equipo depende demasiado del arquitecto?",
                "options": [
                    "El equipo propone alternativas y decide sus detalles",
                    "Todas las decisiones, incluso las locales, esperan la aprobación del arquitecto",
                    "El equipo documenta sus propios ADR",
                    "El equipo revisa sus dependencias",
                ],
                "answer": 1,
                "why": "La dependencia total convierte al arquitecto en cuello de botella y frena al equipo. La autonomía se recupera definiendo qué decisiones son locales y cuáles cruzan fronteras.",
            },
        ],
        "exercises": [
            "Identifica una decisión que hoy bloquea a tu equipo y define quién debería poder tomarla.",
            "Prepara una negociación reciente en términos de intereses y opciones, no de posiciones.",
            "Diseña tu radar personal con cinco temas y un plan de veinte minutos diarios para un mes.",
        ],
        "search": "cierre equipos autonomía control negociación liderazgo carrera radar mentoría práctica deliberada",
    },
}
