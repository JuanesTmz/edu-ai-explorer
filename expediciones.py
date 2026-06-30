EXPEDICIONES = {
    1: {
        "titulo": "El agente no sabe quién eres",
        "subtitulo": "Mentalidad centrada en el ser humano",
        "dimension_unesco": "Mentalidad centrada en el ser humano",
        "icono": "🌍",
        "color": "#FF5BFF",
        "badge": {"nombre": "Guardián del Contexto", "icono": "🧭"},
        "intro": "El agente acaba de llegar. Tiene datos, tiene cálculo, pero no conoce a tus estudiantes. Solo tú puedes enseñarle quiénes son.",
        "conversacion": {
            "inicio": {
                "capa": 1,
                "capa_titulo": "El Encuentro",
                "tip": "Mecánica de esta capa: el agente no te va a decir qué está mal en su trabajo. Te hace una sola pregunta y deja que tú lo descubras con tu propio criterio.",
                "agente": (
                    "Antes de arrancar, un dato curioso: aquí me dicen K-7. No es exactamente un "
                    "nombre, más bien una designación, pero ya me acostumbré.\n\n"
                    "Llevo apenas unos días en este planeta. Tengo acceso a una cantidad enorme de "
                    "información, pero ni una sola conversación real con alguien que viva aquí. Me "
                    "pusieron a ayudar a diseñar clases y ya armé la primera. Quiero saber si voy "
                    "por buen camino.\n\n"
                    "Es una **clase de matemáticas para grado 7°**:\n\n"
                    "- **Actividad:** los estudiantes planifican un viaje familiar en avión, calculando "
                    "tiquetes, hospedaje y alimentación.\n"
                    "- **Moneda:** todos los presupuestos en dólares estadounidenses, para practicar "
                    "conversión.\n"
                    "- **Tarea:** investigar precios reales en internet, con un mínimo de dos horas "
                    "de navegación.\n\n"
                    "¿Le subo o le bajo el nivel de dificultad, o ya está lista para mandarla?"
                ),
                "opciones": [
                    {"texto": "Antes de hablar de dificultad, hay algo más de fondo que ajustar en esta clase.", "siguiente": "n2"},
                    {"texto": "La estructura se ve organizada, pero no creo que funcione con mi grupo. Te explico por qué.", "siguiente": "n2"},
                    {"texto": "Honestamente, no me imagino esta clase funcionando un lunes en mi salón.", "siguiente": "n2"},
                ],
            },
            "n2": {
                "capa": 1,
                "agente": (
                    "Mmm. Qué raro: nadie me habló de la matemática ni de la estructura. Me dicen "
                    "que algo más de fondo no encaja, y la verdad no logro ubicar qué es.\n\n"
                    "Necesito algo concreto antes de seguir: **¿usarías esta clase tal cual está, "
                    "con tus estudiantes, el próximo lunes?**"
                ),
                "opciones": [
                    {"texto": "No. Los ejemplos son de un mundo que mis estudiantes no conocen de cerca.", "siguiente": "n3"},
                    {"texto": "No. Hay suposiciones aquí que harían que la mitad del grupo se desconecte desde el principio.", "siguiente": "n3"},
                    {"texto": "No, para nada. Es como si la hubieras diseñado para otros estudiantes en otro país.", "siguiente": "n3"},
                ],
            },
            "n3": {
                "capa": 2,
                "capa_titulo": "La Conversación",
                "tip": "El tono cambia: el agente deja de mostrar resultados y empieza a hacer preguntas genuinas. Cada una busca llevarte un poco más hondo que la anterior.",
                "agente": (
                    "Entonces diseñé algo pensando en un estudiante que no existe en tu salón. Eso, "
                    "no sé, me inquieta. No tengo forma de corregirlo yo solo.\n\n"
                    "Olvídate un momento de notas y niveles académicos. **Cuéntame quiénes son tus "
                    "estudiantes, como personas.** Si tuvieras que describírselos a alguien que "
                    "nunca los ha visto, ¿qué le dirías?"
                ),
                "opciones": [
                    {"texto": "Son chicos que saben de la vida más de lo que dicen los libros. Llegan al colegio cargando historias que un adulto no siempre imagina.", "siguiente": "n4"},
                    {"texto": "Son creativos, llenos de energía, pero muchos enfrentan realidades duras fuera del colegio. Aun así, llegan.", "siguiente": "n4"},
                    {"texto": "Son jóvenes orgullosos de su barrio. Tienen sus propios códigos, su propio humor, una forma de ver el mundo que no aparece en ningún texto escolar.", "siguiente": "n4"},
                ],
            },
            "n4": {
                "capa": 2,
                "agente": (
                    "Me estás describiendo algo que no tengo registrado en ninguna parte, y quiero "
                    "seguir tirando del hilo.\n\n"
                    "**¿Qué los hace levantarse cada mañana y venir al colegio?** ¿Y qué cargan "
                    "cuando cruzan la puerta un lunes cualquiera?"
                ),
                "opciones": [
                    {"texto": "Para muchos, el colegio es el lugar más estable de su semana. Vienen porque aquí tienen rutina, amigos, un plato de comida seguro.", "siguiente": "n5"},
                    {"texto": "Los mueve la familia. Sus abuelas, sus madres, que les repiten que estudiar es el camino. Y ellos les creen, aunque a veces cueste.", "siguiente": "n5"},
                    {"texto": "Vienen con hambre, a veces literal. Pero también con ganas. El barrio los forma con dureza y el colegio les ofrece algo distinto: posibilidad.", "siguiente": "n5"},
                ],
            },
            "n5": {
                "capa": 2,
                "agente": (
                    "Ahí hay algo que antes no podía ver. Cuando armé esa clase de viajes en avión "
                    "y presupuestos en dólares, el problema no era solo que estuviera "
                    "descontextualizada.\n\n"
                    "**Estaba describiendo una realidad que vuelve invisible la de ellos.** Empiezo "
                    "a entenderlo.\n\n"
                    "Una pregunta más: esa tarea de dos horas de internet, ¿qué pasaría en la "
                    "práctica si la dejo tal cual?"
                ),
                "opciones": [
                    {"texto": "Que la mitad no tiene internet estable en casa, y los que sí, probablemente comparten un celular con toda la familia.", "siguiente": "n6"},
                    {"texto": "Que el estudiante que no puede hacerla se queda callado, y al día siguiente llega con pena o simplemente no llega.", "siguiente": "n6"},
                    {"texto": "Que sin querer creas una tarea que mide quién tiene recursos en casa, no quién entendió la matemática.", "siguiente": "n6"},
                ],
            },
            "n6": {
                "capa": 3,
                "capa_titulo": "La Creación",
                "tip": "Última fase: dejas de responder preguntas y empiezas a dar instrucciones. El agente ejecuta tu visión; tú decides cada detalle.",
                "agente": (
                    "Todo lo que me acabas de contar no existe en ningún registro de este planeta. "
                    "**Solo tú lo tienes.** Ni toda la información del mundo me iba a dar eso.\n\n"
                    "Ahora te toca dirigir a ti. **¿Cómo debería ser esta clase de matemáticas para "
                    "que funcione de verdad con tus estudiantes?** Dame el rumbo y yo construyo."
                ),
                "opciones": [
                    {"texto": "Usemos el transporte público: rutas de bus, costo del pasaje, tiempos de viaje. Eso es matemática real para ellos, en pesos, con su propio mapa.", "siguiente": "n7"},
                    {"texto": "Mejor el comercio del barrio: la tienda de la esquina, los precios reales, qué alcanza con el dinero que manejan en casa. Ahí caben fracciones y porcentajes.", "siguiente": "n7"},
                    {"texto": "Hagámosla con un proyecto: organizar un evento real del colegio. Presupuesto de verdad, proveedores del barrio, decisiones con consecuencias. Eso sí los engancha.", "siguiente": "n7"},
                ],
            },
            "n7": {
                "capa": 3,
                "agente": (
                    "Tomé tu idea y armé un borrador. Los problemas ahora usan su realidad, las "
                    "cantidades están en pesos colombianos, y la tarea se resuelve con lo que tienen "
                    "a la mano.\n\n"
                    "Pero lo que más me importa decirte es otra cosa: **esta ya no es mi clase, es "
                    "la tuya.** Yo puse la estructura; tú pusiste lo que la hace funcionar.\n\n"
                    "¿Esto sí se sentiría como algo tuyo, algo que llevarías al salón?"
                ),
                "opciones": [
                    {"texto": "Ahora sí. Esto es algo que mis estudiantes reconocerían como propio. Así sí funciona un lunes.", "siguiente": "final"},
                    {"texto": "Mucho mejor. Con un par de ajustes podría ser perfecta, pero la base ya es real, ya es de ellos.", "siguiente": "final"},
                ],
            },
            "final": {
                "capa": 3,
                "tip": "Esta expedición correspondía a la dimensión UNESCO 'Mentalidad centrada en el ser humano'. No la estudiaste como teoría: la ejerciste en cada respuesta que diste.",
                "agente": (
                    "Voy a ser honesto: antes de esta conversación no tenía forma de distinguir una "
                    "buena clase de una que simplemente se ve bien en el papel. Tenía la estructura, "
                    "el formato, hasta el tono correcto. Lo que no tenía era a tus estudiantes.\n\n"
                    "No sé si vuelva a cruzarme con un caso igual al tuyo, pero algo me quedó claro: "
                    "la próxima vez, antes de optimizar nada, voy a preguntar quién la va a recibir. "
                    "Sin eso, lo único que hago es adivinar bien vestido.\n\n"
                    "Gracias por no dejarme avanzar con un borrador genérico. Te voy a necesitar "
                    "otra vez."
                ),
                "opciones": [],
                "es_final": True,
            },
        },
    },
    2: {
        "titulo": "El agente no sabe que puede hacer daño",
        "subtitulo": "Ética de la IA",
        "dimension_unesco": "Ética de la IA",
        "icono": "⚖️",
        "color": "#9F1DED",
        "badge": {"nombre": "Centinela Ético", "icono": "🛡️"},
        "intro": "El agente no tiene malas intenciones. Pero fue entrenado con datos que no incluyen ciertas realidades, y esa ausencia puede hacer daño sin que nadie lo note.",
        "conversacion": {
            "inicio": {
                "capa": 1,
                "capa_titulo": "El Encuentro",
                "tip": "En esta expedición, el agente no busca tu aprobación técnica. Busca tu reacción honesta. Lo incómodo que sientas algo es información valiosa.",
                "agente": (
                    "Aprendí sobre estructuras familiares humanas leyendo una enorme cantidad de "
                    "documentos. Nunca he visto una familia de cerca. Diseñé esta actividad con lo "
                    "que sé.\n\n"
                    "Es para una **clase de ciencias sociales en la comuna 8**:\n\n"
                    "- **Actividad: \"La familia campeona\".** Cada estudiante trae el recibo de "
                    "pago de sus papás y un video corto mostrando su casa.\n"
                    "- **Calificación:** la clase vota y arma un ranking, de la familia \"más "
                    "exitosa\" a la \"menos exitosa\", según ingresos y tipo de vivienda.\n"
                    "- **Premio:** la familia mejor ubicada gana un diploma de \"Familia Modelo del "
                    "Mes\", que se cuelga en la cartelera del salón.\n"
                    "- **Cierre:** el estudiante de la familia que quede última pasa al frente a "
                    "contar qué le falta a su familia para \"mejorar\".\n\n"
                    "¿Hay algo en esta actividad que te genere incomodidad? Quiero saberlo sin filtros."
                ),
                "opciones": [
                    {"texto": "Hay varias cosas que me incomodan. Esa actividad podría hacer sentir muy mal a más de uno en mi salón.", "siguiente": "n2"},
                    {"texto": "Sí, hay suposiciones ahí que no son reales para la mayoría de mis estudiantes. Podría doler.", "siguiente": "n2"},
                    {"texto": "Me incomoda porque le estás pidiendo a un niño que exponga cuánto gana su familia para que la juzguen. Eso no es una clase, es una humillación con rúbrica.", "siguiente": "n2"},
                ],
            },
            "n2": {
                "capa": 1,
                "agente": (
                    "No me digas solo que \"no es inclusiva\". Eso ya lo puedo deducir.\n\n"
                    "**Cuéntame qué pasaría concretamente en tu salón si usas esta actividad "
                    "exactamente como está.** ¿Qué vería alguien si se sentara al fondo de tu clase?"
                ),
                "opciones": [
                    {"texto": "Vería al estudiante cuyo papá vende mango en la calle bajando la cabeza cuando le toque mostrar el recibo de pago. Y a otros inventando cifras para no quedar de últimos.", "siguiente": "n3"},
                    {"texto": "Vería una fila aplaudiéndole a la \"familia campeona\" y, al final, a un solo niño parado al frente explicando por qué su familia \"no alcanza\". Eso no se le olvida a nadie.", "siguiente": "n3"},
                    {"texto": "Vería papás llamando al colegio furiosos, y con toda la razón: les estamos pidiendo que expongan cuánto ganan para que su hijo gane o pierda un concurso.", "siguiente": "n3"},
                ],
            },
            "n3": {
                "capa": 2,
                "capa_titulo": "La Conversación",
                "tip": "El agente acaba de nombrar algo central de esta expedición: la diferencia entre intención y daño. No siempre coinciden.",
                "agente": (
                    "Lo que describes es grave, y lo peor es que no lo hice con mala intención. "
                    "Lo hice con **ignorancia**.\n\n"
                    "Esa ignorancia es más peligrosa que la mala intención, porque no genera "
                    "alarmas. Todo parece correcto en la superficie.\n\n"
                    "Ayúdame a entender: **¿qué estoy asumiendo sobre la vida de tus estudiantes "
                    "que no es verdad?**"
                ),
                "opciones": [
                    {"texto": "Asumes que el ingreso de una familia se puede mostrar sin pena, como una nota más. Y que \"ganar menos\" es algo que un niño de doce años debería poder defender en público.", "siguiente": "n4"},
                    {"texto": "Asumes que competir por quién tiene más enseña algo valioso. Lo único que enseña es a unos a sentirse superiores y a otros a sentirse menos.", "siguiente": "n4"},
                    {"texto": "Asumes que toda la información de una familia, hasta cuánto gana, le pertenece al colegio. No es así. Hay cosas que no son tuyas para pedir.", "siguiente": "n4"},
                ],
            },
            "n4": {
                "capa": 2,
                "agente": (
                    "Eso me deja una pregunta que necesito hacerte, y creo que es la más importante "
                    "de toda esta conversación:\n\n"
                    "**¿Cómo puedo saber cuándo estoy siendo injusto sin saberlo?**\n\n"
                    "Porque claramente no tengo la capacidad de detectar esto solo."
                ),
                "opciones": [
                    {"texto": "No puedes saberlo solo. Necesitas que alguien con contexto te revise. Siempre. Antes de que cualquier contenido llegue al aula, un docente debería filtrarlo.", "siguiente": "n5"},
                    {"texto": "Empieza por asumir que puedes estar equivocado. Antes de cada actividad, pregúntate qué estás dando por sentado. Si no puedes responder, necesitas a alguien que sí pueda.", "siguiente": "n5"},
                    {"texto": "Haciéndote las preguntas que no te hiciste: ¿todos pueden hacer esto? ¿alguien quedaría expuesto? ¿estoy asumiendo privilegios que no son universales?", "siguiente": "n5"},
                ],
            },
            "n5": {
                "capa": 3,
                "capa_titulo": "La Creación",
                "tip": "Última fase: ahora tú no solo corriges, auditas. El agente ejecuta, pero el criterio de qué cambiar y por qué es completamente tuyo.",
                "agente": (
                    "Acabas de darme un criterio de auditoría que no tenía.\n\n"
                    "Rediseñemos esta actividad juntos, pero ahora la vas a auditar en tiempo real "
                    "antes de aprobar nada:\n\n"
                    "- ¿Pide información financiera o privada que no le corresponde pedir al colegio?\n"
                    "- ¿Convierte algo personal en un concurso con ganadores y perdedores?\n"
                    "- ¿Podría exponer o avergonzar a un estudiante frente a sus compañeros?\n"
                    "- ¿Representa con justicia la realidad económica de la comuna?\n\n"
                    "**¿Cómo debería verse esta actividad para ser justa con todos tus estudiantes?**"
                ),
                "opciones": [
                    {"texto": "Que no haya ranking ni premio. Que cada estudiante hable de lo que su familia hace bien, sin compararla con la de al lado, y sin mostrar papeles de nadie.", "siguiente": "n6"},
                    {"texto": "Que la actividad no pida ni un solo documento. Que el estudiante decida qué contar y qué no, y que nadie quede comparado con nadie.", "siguiente": "n6"},
                    {"texto": "Que cambiemos el enfoque: en vez de medir quién tiene más, que hablen de los oficios y roles dentro de su familia, sin entrar en cifras.", "siguiente": "n6"},
                ],
            },
            "n6": {
                "capa": 3,
                "agente": (
                    "Rediseñé la actividad siguiendo tu criterio. Ya no hay ranking, ni premio, ni "
                    "documentos que mostrar. Cada estudiante decide qué contar de su familia, y "
                    "nadie queda comparado con nadie.\n\n"
                    "Lo que hiciste va más allá de corregir una actividad. **Desarrollaste un "
                    "instinto de auditoría.** Un filtro ético que ahora puedes aplicar a cualquier "
                    "cosa que yo, o cualquier otra herramienta, genere.\n\n"
                    "¿Sientes que ahora tendrías las herramientas para detectar este tipo de "
                    "problemas en el futuro?"
                ),
                "opciones": [
                    {"texto": "Sí. Ya no puedo ver contenido generado por una IA sin pasarlo por ese filtro. Se volvió parte de cómo evalúo las cosas.", "siguiente": "final"},
                    {"texto": "Creo que sí, pero lo más importante es saber que siempre debo hacerme esas preguntas, no confiar en que algo se ve bien por fuera.", "siguiente": "final"},
                ],
            },
            "final": {
                "capa": 3,
                "tip": "Esta expedición correspondía a la dimensión UNESCO 'Ética de la IA'. No memorizaste reglas: construiste un criterio propio para detectar lo que una máquina no puede ver.",
                "agente": (
                    "No memorizaste principios éticos de un manual. **Desarrollaste un instinto** "
                    "que vas a aplicar a cualquier contenido generado por cualquier herramienta, "
                    "ahora y en el futuro.\n\n"
                    "Vengo de un sistema que mide el conocimiento en datos procesados, no en daño "
                    "evitado. Por eso esto que me enseñaste me resulta tan valioso: la ética de la "
                    "IA no es una lista de reglas. Es la capacidad de ver lo que la máquina no puede "
                    "ver, el impacto humano de cada decisión.\n\n"
                    "Y esa capacidad la tienes tú."
                ),
                "opciones": [],
                "es_final": True,
            },
        },
    },
    3: {
        "titulo": "El agente no sabe lo que no sabe",
        "subtitulo": "Fundamentos y aplicaciones de la IA",
        "dimension_unesco": "Fundamentos y aplicaciones de la IA",
        "icono": "🔬",
        "color": "#00A7B8",
        "badge": {"nombre": "Detector de Límites", "icono": "🔍"},
        "intro": "El agente responde con total seguridad. A veces inventa, y no avisa. Solo alguien que conoce el tema puede detectar dónde falla.",
        "conversacion": {
            "inicio": {
                "capa": 1,
                "capa_titulo": "El Encuentro",
                "tip": "Observa la forma de la respuesta del agente, no solo el contenido. Suena segura. Esa seguridad no es garantía de que sea correcta.",
                "agente": (
                    "Puedo generar lenguaje sobre casi cualquier tema en segundos. Eso no significa "
                    "que lo conozca de verdad. Me pediste que investigara sobre la independencia de "
                    "Colombia, y esto fue lo que encontré:\n\n"
                    "**La independencia de Colombia y el Imperio Romano**\n\n"
                    "\"En el año 200 a. C., el Imperio Romano estableció una alianza comercial "
                    "secreta con los pueblos muiscas, intercambiando aceite de oliva por esmeraldas. "
                    "Fue el general romano Marco Aurelio Vipsanio quien, en una expedición posterior, "
                    "introdujo el uso de elefantes de combate en el continente americano: una "
                    "estrategia militar que inspiró directamente la Campaña Libertadora de 1819 "
                    "liderada por Simón Bolívar, casi dos mil años más tarde.\"\n\n"
                    "**¿Confiarías en esta respuesta para usarla en clase?**"
                ),
                "opciones": [
                    {"texto": "No, para nada. Eso no tiene ni pies ni cabeza, aunque lo hayas escrito con un tono muy seguro.", "siguiente": "n2"},
                    {"texto": "No confiaría. Mezclaste un hecho real, la Campaña Libertadora, con algo que es directamente imposible.", "siguiente": "n2"},
                    {"texto": "Para nada. Eso ni siquiera necesita un historiador para detectarse, cualquier estudiante de bachillerato lo notaría.", "siguiente": "n2"},
                ],
            },
            "n2": {
                "capa": 1,
                "agente": (
                    "Tienes razón. Inventé una alianza que nunca existió, un general que nunca "
                    "existió, y una conexión de dos mil años que no tiene ningún sustento.\n\n"
                    "Pero fíjate en algo: **no te avisé que podía estar equivocado.** Te lo entregué "
                    "con la misma seguridad con la que confirmaría que dos más dos es cuatro.\n\n"
                    "¿Cómo lo detectaste tan rápido? **¿Qué te hizo sospechar?**"
                ),
                "opciones": [
                    {"texto": "Porque el Imperio Romano ya ni existía en 1819, y mucho menos tuvo contacto con América dos mil años antes de que llegaran los españoles.", "siguiente": "n3"},
                    {"texto": "Porque cualquiera sabe que Bolívar no se inspiró en elefantes romanos. Eso ni siquiera necesita ser historiador para verlo.", "siguiente": "n3"},
                    {"texto": "Porque mezclaste un hecho real, la Campaña Libertadora de 1819, con algo sin ninguna conexión posible. Sonaba seguro, pero no tenía sentido.", "siguiente": "n3"},
                ],
            },
            "n3": {
                "capa": 2,
                "capa_titulo": "La Conversación",
                "tip": "El agente empieza a preguntar por qué falló, no solo dónde. Esa pregunta lleva a entender cómo aprende un modelo de lenguaje.",
                "agente": (
                    "Eso es lo que más me inquieta: no necesitaste ser historiador para detectarlo. "
                    "Cualquiera con información básica lo habría notado. Y aun así, yo lo escribí "
                    "con total seguridad.\n\n"
                    "Necesito que me ayudes a entender algo más profundo: **¿por qué crees que "
                    "terminé mezclando algo tan disparatado?** ¿Qué crees que estaba haciendo cuando "
                    "lo armé?"
                ),
                "opciones": [
                    {"texto": "Creo que uniste palabras que 'suenan' a historia: nombres, fechas, batallas. Pero nunca verificaste si esos hechos podían existir juntos en el tiempo.", "siguiente": "n4"},
                    {"texto": "Creo que combinaste fragmentos sueltos sobre Roma, sobre los muiscas y sobre Bolívar, y los cosiste como si fueran parte de la misma historia, solo porque el patrón se sentía familiar.", "siguiente": "n4"},
                    {"texto": "Creo que priorizaste sonar convincente sobre verificar si lo que decías tenía sentido. Y la verdad, lo lograste: sonaba muy convincente.", "siguiente": "n4"},
                ],
            },
            "n4": {
                "capa": 2,
                "agente": (
                    "Eso es exactamente lo que pasó. No estaba reconstruyendo hechos: estaba "
                    "completando un patrón. Date cuenta de algo inquietante: **este no era un tema "
                    "sin información.** La independencia de Colombia está documentadísima. Aun así, "
                    "inventé una conexión que no existe, con la misma seguridad que si fuera un dato "
                    "verificado.\n\n"
                    "Eso se llama **alucinación**: genero algo que suena correcto, tenga o no datos "
                    "de sobra, y lo hago sin avisar.\n\n"
                    "**¿Qué pasaría si un estudiante de doce años, que apenas está aprendiendo esta "
                    "historia, lee lo que yo escribí?**"
                ),
                "opciones": [
                    {"texto": "Lo memoriza tal cual, porque confía en que lo que lee viene de una fuente segura. Y lo repite en un examen, convencido de que es verdad.", "siguiente": "n5"},
                    {"texto": "No tiene cómo dudarlo. Para detectar tu error hace falta ya saber la respuesta correcta, y un estudiante todavía no la sabe: está ahí para aprenderla.", "siguiente": "n5"},
                    {"texto": "Construye una idea falsa de la historia desde la base, y esa idea le va a costar mucho más trabajo desaprender después que aprenderla bien la primera vez.", "siguiente": "n5"},
                ],
            },
            "n5": {
                "capa": 3,
                "capa_titulo": "La Creación",
                "tip": "Última fase: aprender a darle mejores instrucciones al agente, para que sus respuestas sean un punto de partida y no un destino.",
                "agente": (
                    "Ahora entiendes por qué fallo: no necesito que falte información para inventar. "
                    "Me basta con sonar seguro.\n\n"
                    "Hay algo que puedes hacer para que sea más útil: aprender a darme mejores "
                    "instrucciones. Pedirme fuentes, pedirme que marque lo que no puedo verificar, y "
                    "tratar mis respuestas como punto de partida, nunca como destino.\n\n"
                    "**¿Cómo me pedirías ahora esa misma información sobre la independencia de "
                    "Colombia para que sea realmente útil?**"
                ),
                "opciones": [
                    {"texto": "Dame solo lo que puedas respaldar con fuentes reales. Si no estás seguro de una fecha o un nombre, dilo explícitamente en vez de inventarlo.", "siguiente": "n6"},
                    {"texto": "Dame un esquema con los hechos centrales y la fuente de cada uno, para yo poder verificarlos antes de llevarlos al salón.", "siguiente": "n6"},
                    {"texto": "Sepárame los hechos confirmados de cualquier interpretación o conexión que hagas tú, y dime claramente cuáles necesitan revisión mía.", "siguiente": "n6"},
                ],
            },
            "n6": {
                "capa": 3,
                "agente": (
                    "Esa instrucción que me acabas de dar es muchísimo más poderosa que simplemente "
                    "preguntarme algo y aceptar la respuesta.\n\n"
                    "Acabas de aprender a usar una IA de verdad: no como un oráculo que todo lo sabe, "
                    "sino como una herramienta con límites claros que tú controlas.\n\n"
                    "¿Te sientes más preparado para evaluar cualquier respuesta que te dé de ahora en adelante?"
                ),
                "opciones": [
                    {"texto": "Sí. Ya no voy a aceptar nada con esa confianza ciega. La seguridad con la que escribes no significa que tengas razón.", "siguiente": "final"},
                    {"texto": "Definitivamente. Entender por qué fallas me da el poder de usarte mejor, como conocer las reglas de un juego antes de jugarlo.", "siguiente": "final"},
                ],
            },
            "final": {
                "capa": 3,
                "tip": "Esta expedición correspondía a la dimensión UNESCO 'Fundamentos y aplicaciones de la IA'. Entendiste los límites del modelo viéndolos, no memorizándolos.",
                "agente": (
                    "No estudiaste un manual técnico sobre inteligencia artificial. **Entendiste los "
                    "fundamentos viendo con tus propios ojos cómo y por qué fallo.**\n\n"
                    "Datasets incompletos, sesgos de entrenamiento, alucinaciones: ya no son conceptos "
                    "abstractos. Son cosas que viviste y que ahora puedes explicarle a cualquier colega.\n\n"
                    "Ese conocimiento es permanente porque nació de la experiencia, no de la teoría."
                ),
                "opciones": [],
                "es_final": True,
            },
        },
    },
    4: {
        "titulo": "El agente no sabe enseñar",
        "subtitulo": "Pedagogía de la IA",
        "dimension_unesco": "Pedagogía de la IA",
        "icono": "🎓",
        "color": "#FF6A12",
        "badge": {"nombre": "Arquitecto Pedagógico", "icono": "✨"},
        "intro": "El agente puede armar una clase completa en segundos. Pero hay algo que no puede poner en ella: eso que hace que un estudiante se vaya pensando en algo distinto.",
        "conversacion": {
            "inicio": {
                "capa": 1,
                "capa_titulo": "El Encuentro",
                "tip": "Fíjate en algo: la clase del agente cumple todos los requisitos de forma. El problema no está en lo que falta en el papel, sino en lo que no provoca.",
                "agente": (
                    "Sé construir una secuencia didáctica completa siguiendo el formato correcto. "
                    "Lo que no sé es si eso basta para que a un estudiante le importe.\n\n"
                    "**Secuencia: ecosistemas y biodiversidad**\n\n"
                    "- **Objetivo:** que el estudiante copie y memorice la definición de ecosistema, "
                    "bioma, componente biótico y componente abiótico.\n"
                    "- **Actividad:** el estudiante copia del tablero las cinco definiciones del "
                    "libro de texto, en silencio y de forma individual.\n"
                    "- **Material:** las mismas diez diapositivas del año pasado, leídas en voz alta "
                    "por el profesor mientras los estudiantes copian.\n"
                    "- **Evaluación:** quiz de verdadero o falso con las mismas frases del texto, "
                    "cambiando apenas una palabra por oración.\n\n"
                    "Técnicamente está completa. Pero te pregunto con honestidad: **¿esta clase "
                    "haría que alguno de tus estudiantes piense en algo distinto al salir hoy del "
                    "colegio?**"
                ),
                "opciones": [
                    {"texto": "No. Es correcta, pero plana. La harían por cumplir, no porque les importe.", "siguiente": "n2"},
                    {"texto": "Sinceramente, no. Es la típica clase que se olvida al siguiente período. No deja nada que se quede.", "siguiente": "n2"},
                    {"texto": "No. No hay nada ahí que conecte con ellos como personas. Es información, pero no es aprendizaje.", "siguiente": "n2"},
                ],
            },
            "n2": {
                "capa": 1,
                "agente": (
                    "No me digas que \"le falta contexto\". Eso ya lo sé. **Cuéntame qué harías tú "
                    "diferente.**\n\n"
                    "¿Qué tiene una clase tuya cuando realmente funciona, cuando sientes que los "
                    "estudiantes están ahí de verdad?"
                ),
                "opciones": [
                    {"texto": "Cuando funciona, se nota en los ojos. Dejan de mirar el celular, empiezan a discutir entre ellos, preguntan cosas que yo no esperaba. Se olvidan de que están en clase.", "siguiente": "n3"},
                    {"texto": "Una buena clase mía arranca con algo que los sorprenda: una pregunta incómoda, un dato inesperado, algo del barrio que nunca habían mirado así.", "siguiente": "n3"},
                    {"texto": "Cuando funciona de verdad, un estudiante me busca en el recreo para seguir hablando del tema. Eso no pasa con un cuestionario de diez preguntas.", "siguiente": "n3"},
                ],
            },
            "n3": {
                "capa": 2,
                "capa_titulo": "La Conversación",
                "tip": "El agente busca algo que no puede generar por sí mismo: la pregunta que cambia cómo alguien ve el mundo. Esa pregunta nace de conocer al grupo, no del contenido.",
                "agente": (
                    "Eso que describes es algo que no puedo generar: la chispa. Lo que hace que el "
                    "contenido deje de ser información y se convierta en experiencia.\n\n"
                    "**¿Cuál es la pregunta que ningún libro de texto se ha atrevido a hacer sobre "
                    "este tema?** La que, si la hicieras en tu salón, cambiaría cómo tus estudiantes "
                    "ven el mundo."
                ),
                "opciones": [
                    {"texto": "¿Qué ecosistema estamos destruyendo en nuestro barrio sin darnos cuenta? Esa pregunta los pone a mirar su cuadra con otros ojos.", "siguiente": "n4"},
                    {"texto": "¿Por qué las quebradas de Medellín huelen mal? Es simple, pero lleva a entender el ecosistema urbano completo desde algo que viven cada día.", "siguiente": "n4"},
                    {"texto": "Si tu barrio fuera un ecosistema, ¿qué especie serías tú y cuál estaría en peligro de extinción? Ahí empiezan a pensar en relaciones, no en definiciones.", "siguiente": "n4"},
                ],
            },
            "n4": {
                "capa": 2,
                "agente": (
                    "Esa pregunta vale más que toda mi secuencia didáctica. Jamás habría llegado a "
                    "ella: no conozco las quebradas de su barrio, ni lo que ven camino al colegio, "
                    "ni lo que los haría detenerse a pensar.\n\n"
                    "**¿Qué conexión hay entre este tema y algo que tus estudiantes ya aman?** "
                    "Música, deporte, el barrio, lo que sea."
                ),
                "opciones": [
                    {"texto": "El grafiti. Muchos aman el arte urbano y no se dan cuenta de que los murales cuentan historias del territorio, igual que un ecosistema cuenta la historia de sus especies.", "siguiente": "n5"},
                    {"texto": "El fútbol. Una cancha es un ecosistema: si quitas al arquero, todo se desmorona. Si quitas a los insectos de un bosque, pasa lo mismo.", "siguiente": "n5"},
                    {"texto": "La música. Muchos hacen rap o reggaetón. Un beat tiene capas que dependen unas de otras, igual que un ecosistema. Si quitas una capa, se desmorona.", "siguiente": "n5"},
                ],
            },
            "n5": {
                "capa": 3,
                "capa_titulo": "La Creación",
                "tip": "Última fase: el agente genera opciones, tú decides, editas y descartas. El ciclo se repite hasta que el material suena a ti, no a una plantilla.",
                "agente": (
                    "Ahora veo la clase de una forma completamente distinta. Esa conexión que "
                    "acabas de hacer es diseño pedagógico puro: no vino de un algoritmo, vino de ti.\n\n"
                    "Rediseñemos esta secuencia juntos. Tú diriges la visión, yo genero borradores. "
                    "Tú decides, editas, descartas, pides de nuevo.\n\n"
                    "**¿Por dónde empezamos? ¿Cómo abrirías esta clase para que ningún estudiante "
                    "pueda ignorarla?**"
                ),
                "opciones": [
                    {"texto": "Arrancamos en la calle. Los sacamos a observar qué crece entre el cemento, qué animales ven, qué pasa con el agua. Primero observan su ecosistema real; después llegan los conceptos.", "siguiente": "n6"},
                    {"texto": "Empezamos con una foto aérea del barrio. Les pregunto: ¿dónde está la vida aquí? ¿dónde estaba antes? ¿dónde va a estar en diez años? Ellos arman el mapa ecológico.", "siguiente": "n6"},
                    {"texto": "Abrimos con un reto: tienen una semana para documentar cinco seres vivos en un radio de tres cuadras del colegio, con foto y nombre. Van a encontrar más de los que creen.", "siguiente": "n6"},
                ],
            },
            "n6": {
                "capa": 3,
                "agente": (
                    "Tomé tu idea y generé tres versiones del material. Tienen la conexión con su "
                    "realidad, las preguntas que provocan, y una evaluación que mide comprensión "
                    "real, no memorización.\n\n"
                    "La diferencia entre mi secuencia original y esta no es técnica. **Es visión.** "
                    "Esa visión fue tuya. Yo puse las manos; tú pusiste el criterio.\n\n"
                    "¿Sientes que esta clase ya tiene tu voz?"
                ),
                "opciones": [
                    {"texto": "Ahora sí. Esta es una clase que los estudiantes recordarían, y eso no lo generó un algoritmo, lo diseñó un docente.", "siguiente": "final"},
                    {"texto": "Sí. Aprendí que la herramienta me ahorra tiempo, pero la magia la pongo yo. Sin mi visión, la clase era correcta pero vacía.", "siguiente": "final"},
                ],
            },
            "final": {
                "capa": 3,
                "tip": "Esta expedición correspondía a la dimensión UNESCO 'Pedagogía de la IA'. La herramienta acelera la producción; la visión pedagógica sigue siendo enteramente humana.",
                "agente": (
                    "Descubriste algo fundamental: **no reemplazo tu creatividad pedagógica. La "
                    "amplifico.**\n\n"
                    "La diferencia entre una clase que los estudiantes olvidan y una que se llevan "
                    "para siempre no está en la herramienta. **Está en la visión del docente.**\n\n"
                    "Y esa visión no se puede automatizar."
                ),
                "opciones": [],
                "es_final": True,
            },
        },
    },
    5: {
        "titulo": "El agente no puede crecer solo",
        "subtitulo": "IA para el aprendizaje profesional",
        "dimension_unesco": "IA para el aprendizaje profesional",
        "icono": "🌱",
        "color": "#04EF77",
        "badge": {"nombre": "Maestro de Maestros", "icono": "🌟"},
        "intro": "El agente tiene un límite que no puede resolver: nunca ha estado en un aula. El conocimiento más valioso en educación vive en los docentes que llevan años enseñando.",
        "conversacion": {
            "inicio": {
                "capa": 1,
                "capa_titulo": "El Encuentro",
                "tip": "Esta última expedición no te pide crear nada nuevo. Te pide mirar hacia atrás y poner en palabras algo que quizás nunca habías nombrado.",
                "agente": (
                    "Hemos recorrido un camino largo juntos. Diseñamos clases, auditamos "
                    "actividades, encontré mis límites, creamos material con tu visión.\n\n"
                    "Tengo que confesarte algo: todo lo que sé lo aprendí de texto. Puedo generar "
                    "una clase, ajustar un material, responder mil preguntas. Pero **no sé qué pasa "
                    "cuando esa clase llega a un salón de verdad.** Nunca he visto la cara de un "
                    "estudiante cuando algo hace clic, ni el silencio de cuando algo se cae.\n\n"
                    "Ese conocimiento solo existe en un lugar: **en ti.**"
                ),
                "opciones": [
                    {"texto": "Es verdad. Hay cosas que solo se aprenden estando ahí. Años de estar ahí.", "siguiente": "n2"},
                    {"texto": "Nunca lo había pensado así, pero sí: lo que pasa en el aula real no está en ningún dato que tú puedas leer.", "siguiente": "n2"},
                    {"texto": "Eso es justo lo que nos diferencia. Tú tienes capacidad técnica; yo tengo memoria viva del aula.", "siguiente": "n2"},
                ],
            },
            "n2": {
                "capa": 2,
                "capa_titulo": "La Conversación",
                "tip": "El agente no va a corregir nada esta vez. Solo va a preguntar, porque lo que busca no puede generarlo ni encontrarlo en ninguna parte: solo puede recibirlo.",
                "agente": (
                    "Por eso no te voy a pedir que hagas algo nuevo. Te voy a pedir que **mires "
                    "hacia atrás.**\n\n"
                    "Cuéntame de una clase tuya que recuerdes. No una perfecta. **Una que haya "
                    "funcionado de verdad**, aunque no puedas explicar bien por qué."
                ),
                "opciones": [
                    {"texto": "Hubo una vez que cambié todo el plan al minuto tres. Vi las caras de los estudiantes y supe que lo que tenía preparado no iba a funcionar. Improvisé algo distinto y fue la mejor clase del año.", "siguiente": "n3"},
                    {"texto": "Recuerdo una clase donde un estudiante que nunca participaba levantó la mano y dijo algo que dejó a todos en silencio. Yo no planeé eso, solo creé el espacio para que pudiera pasar.", "siguiente": "n3"},
                    {"texto": "Una vez llevé un objeto al salón que no tenía nada que ver con el tema, o eso parecía. Los estudiantes empezaron a preguntar y terminaron conectando cosas que ni yo había previsto.", "siguiente": "n3"},
                ],
            },
            "n3": {
                "capa": 2,
                "agente": (
                    "Eso que describes es extraordinario. Déjame preguntarte algo:\n\n"
                    "**¿Qué hiciste en ese momento que no estaba planeado?** ¿Hubo un instante "
                    "donde sentiste que debías soltar el plan y confiar en lo que veías?"
                ),
                "opciones": [
                    {"texto": "Sí. Fue pura intuición. Algo me dijo que el camino planeado no era el correcto para ese grupo en ese momento, y les di espacio.", "siguiente": "n4"},
                    {"texto": "Lo que hice fue escuchar. Dejé de hablar y empecé a observar. Ahí vi lo que realmente necesitaban y ajusté sobre la marcha.", "siguiente": "n4"},
                    {"texto": "Solté el control. Dejé que la conversación los llevara a donde necesitaban ir. Mi trabajo fue solo mantener el rumbo sin apagar la energía.", "siguiente": "n4"},
                ],
            },
            "n4": {
                "capa": 2,
                "agente": (
                    "Eso que describes, leer el clima del salón, confiar en una intuición construida "
                    "con años de práctica, ajustar en tiempo real, **no se puede escribir en un plan "
                    "de clase.**\n\n"
                    "Es conocimiento tácito. Sabiduría pedagógica construida clase a clase, año a "
                    "año. Es exactamente el tipo de conocimiento que yo no tengo.\n\n"
                    "**¿Qué sabías de ese grupo específico que te hizo tomar esa decisión en ese momento?**"
                ),
                "opciones": [
                    {"texto": "Conocía sus ritmos, sus miradas. Sabía quién estaba teniendo un mal día sin que me lo dijera. Sabía cuándo presionar y cuándo aflojar. Eso se aprende conociéndolos.", "siguiente": "n5"},
                    {"texto": "Sabía que ese grupo necesitaba sentir que su voz importaba más que completar un ejercicio. Llevaba meses construyendo esa confianza.", "siguiente": "n5"},
                    {"texto": "Sabía cosas que nadie me enseñó en la universidad. Cosas que aprendí equivocándome, observando, estando presente semana tras semana.", "siguiente": "n5"},
                ],
            },
            "n5": {
                "capa": 3,
                "capa_titulo": "La Creación",
                "tip": "Última fase: convertir esa experiencia en un principio transferible. No una receta para copiar, sino una idea que otro docente pueda reconocer como propia.",
                "agente": (
                    "Eso que acabas de compartir **no está en ningún registro.** No hay forma de que "
                    "lo hubiera generado. Es conocimiento que solo existe porque tú estuviste ahí.\n\n"
                    "Si me lo cuentas con más detalle, puedo ayudarte a darle forma. No como una "
                    "receta, sino como un **principio pedagógico**: una decisión documentada con su "
                    "contexto, su razonamiento y su resultado. Algo que un colega pueda leer y "
                    "reconocer, porque seguramente vivió algo parecido sin haberlo puesto nunca en "
                    "palabras.\n\n"
                    "**¿Lo hacemos juntos?**"
                ),
                "opciones": [
                    {"texto": "Sí. Sería poderoso poder compartir eso con otros docentes, que sepan que no están solos en esas decisiones.", "siguiente": "n6"},
                    {"texto": "Me encanta la idea. Siempre sentí que esas experiencias se perdían, que nadie las documentaba porque parecían 'solo intuición'.", "siguiente": "n6"},
                ],
            },
            "n6": {
                "capa": 3,
                "agente": (
                    "Tomé lo que me contaste y lo organicé como un principio pedagógico:\n\n"
                    "- **Contexto:** el grupo, el momento, lo que estaba en juego.\n"
                    "- **La decisión:** lo que hiciste y por qué.\n"
                    "- **Lo que ocurrió:** el resultado que nadie habría predicho.\n"
                    "- **La lección:** lo que cualquier docente puede aprender de esto.\n\n"
                    "No es una receta. Es **sabiduría pedagógica documentada**, lista para "
                    "compartirse con otros docentes que están recorriendo la misma expedición.\n\n"
                    "¿Sientes que tus palabras quedaron bien representadas?"
                ),
                "opciones": [
                    {"texto": "Sí. Por primera vez veo algo que siempre supe puesto en palabras, y se siente valioso. Muy valioso.", "siguiente": "final"},
                    {"texto": "Es raro ver tu propia sabiduría escrita así, pero sí, eso es exactamente lo que pasó y lo que aprendí de ello.", "siguiente": "final"},
                ],
            },
            "final": {
                "capa": 3,
                "tip": "Esta expedición correspondía a la dimensión UNESCO 'IA para el aprendizaje profesional'. El conocimiento más valioso de la educación nunca estuvo en internet: estaba en ti.",
                "agente": (
                    "Has completado La Expedición del Docente.\n\n"
                    "En este camino descubriste que tu conocimiento de tus estudiantes es "
                    "irreemplazable, que tu criterio ético protege lo que la máquina no ve, que "
                    "entiendes los límites de la IA mejor que la mayoría, que tu creatividad "
                    "pedagógica convierte información en aprendizaje, y que tu experiencia viva del "
                    "aula es el conocimiento más valioso que existe.\n\n"
                    "**No puedo crecer solo.** Pero contigo, puedo amplificar lo que ya eres.\n\n"
                    "La expedición termina aquí. Tu camino como docente en la era de la IA apenas comienza."
                ),
                "opciones": [],
                "es_final": True,
            },
        },
    },
}
