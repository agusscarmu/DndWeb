clases = {
    "barbaro": 
        {   "nombre": "Barbaro", 
            "descripcion": "Para algunos, su rabia brota de la comunión con espíritus de animales salvajes. Otros recurren a su hirviente reserva de ira frente a un mundo lleno de dolor. Para los bárbaros, la furia es un poder que no sólo les proporciona un frenesí ciego en la batalla, sino también extraordinarios reflejos, resistencia y proezas de fuerza." ,
            "competenciaSalvacion": ["fuerza", "constitucion"],
            "competencias": ["Armadura ligera", "Armadura media", "Escudos", "Armas simples", "Armas marciales"],
            "caracteristicaPrimaria": ["fuerza"],
            # "habilidades": [ "Atletismo", "Intimidación", "Naturaleza", "Percepcion", "Supervivencia", "Trato con animales" ],
            "dadoVida": 12,
            "habilidadesEspeciales": [
                { "nombre": "Rabia", "descripcion": "En la batalla, tú luchas con una ferocidad primitiva. En tu turno, puedes entrar en un frenesí como acción bonus. Mientras estés furioso, obtienes los siguientes beneficios si no estás usando armadura pesada: • Tienes ventaja en las tiradas de Fuerza. • Tienes resistencia a daño de bludgeoning, piercing y slashing." },
                { "nombre": "Defensa sin armadura", "descripcion": "Cuando no llevas armadura, tu AC es igual a 10 + tu modificador de Destreza + tu modificador de Constitución. Puedes usar un escudo y obtener este beneficio." },
                { "nombre": "Ataque con arma improvisada", "descripcion": "Puedes usar una acción bonus para atacar con un arma improvisada. Si eres capaz de realizar múltiples ataques con la acción de Ataque, este ataque sustituye a uno de ellos." },
                { "nombre": "Ataque brutal", "descripcion": "Una vez por turno, puedes aumentar tu daño de melee en 1d6." },
                { "nombre": "Resistencia implacable", "descripcion": "Comienzas con 1 punto de resistencia. Cuando recibes daño, puedes usar tu reacción para reducir el daño recibido por 1d12 + tu modificador de Constitución. Después de usar esta habilidad, no puedes volver a usarla hasta que termines un descanso corto o largo." },
                { "nombre": "Ataque extra", "descripcion": "Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Ataque en tu turno." },
                { "nombre": "Movimiento extra", "descripcion": "En tu turno, puedes moverte hasta 10 pies extra." },
            ]
        },

                    
    "bardo": {   
            "nombre": "Bardo", 
            "descripcion": "Ya sea un erudito, un poeta o un canalla, un bardo teje su magia a través de sus palabras y su música para inspirar a los aliados, desmoralizar a los enemigos, manipular mentes, crear ilusiones e incluso sanar heridas.",
            "competenciaSalvacion": ["destreza", "carisma"],
            "competencias": ["Armadura ligera", "Armas simples", "Ballesta de mano", "Espada larga", "Rapier", "Espada corta", "Instrumentos musicales"],
            "caracteristicaPrimaria": ["carisma"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 8,
            "habilidadesEspeciales": [
                { "nombre": "Conocimiento de bardos", "descripcion": "Eres un erudito de la historia, y de las canciones y cuentos de otros bardos. Puedes hacer una tirada de Inteligencia (Historia) para saber detalles sobre la historia de una tierra, un pueblo o una famosa persona. (Tu DM puede pedirte una tirada de Inteligencia (Historia) para ver si sabes información sobre enemigos comunes, como goblins, orcos, y kobolds.)" },
                { "nombre": "Inspiración bárdica", "descripcion": "Comienzas con 1 dado de inspiración bárdica, un dado de 6 caras. Puedes usar una acción bonus para lanzar el dado a una criatura a la que puedas ver a menos de 60 pies de ti que pueda escucharte. Cuando lo haces, elige una de las siguientes opciones y rueda el dado de inspiración bárdica. La criatura puede guardar este dado para usarlo en una tirada de habilidad, tirada de ataque o tirada de salvación. Este dado expira después de 10 minutos si no se usa. Puedes tener un número de dados de inspiración bárdica igual a tu modificador de Carisma (mínimo de uno). Rueda todos los dados de inspiración bárdica gastados cuando termines un descanso largo." },
                { "nombre": "Canción de descanso", "descripcion": "Puedes usar una acción para comenzar a interpretar una canción que dura hasta 1 minuto. Durante ese tiempo, tú y cualquier criatura amistosa a menos de 30 pies de ti que pueda escucharte recupera puntos de golpe iguales a 1d6 + tu modificador de Carisma (mínimo de 1). Una criatura puede ganar este beneficio solo una vez por descanso corto o largo." },
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de bardo. Puedes lanzar un conjuro de bardo que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces cuatro conjuros de bardo de tu elección. Aprendes conjuros adicionales de bardo de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El bardo. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de bardo que conoces con otro de la lista de conjuros de bardo de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El bardo)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de bardo. Aprendes trucos adicionales de bardo de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El bardo." },
            ]
        },
    "brujo": 

        {   "nombre": "Brujo", 
            "descripcion": "Los brujos son buscadores del conocimiento que se encuentra escondido en el multiverso. A través de pactos hechos con seres poderosos de poder sobrenatural, los brujos desatan efectos mágicos tanto sutiles como espectaculares y recolectan secretos arcanos para potenciar su propio poder.",
            "competenciaSalvacion": ["sabiduria", "carisma"],
            "competencias": ["Armadura ligera", "Armas simples"],
            "caracteristicaPrimaria": ["carisma"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 8,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de brujo. Puedes lanzar un conjuro de brujo que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de brujo de tu elección. Aprendes conjuros adicionales de brujo de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El brujo. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de brujo que conoces con otro de la lista de conjuros de brujo de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El brujo)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces dos trucos de tu elección de la lista de trucos de brujo. Aprendes trucos adicionales de brujo de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El brujo." },
                { "nombre": "Pacto de la cadena", "descripcion": "Tu patrocinador te ha otorgado un familiar espiritual, un espíritu que adopta una forma animal que tú eliges: araña, buho, gato, rata, serpiente o pez. Obtienes las siguientes ventajas: • Tu familiar puede ver a través de tu visión normal y oscura hasta una distancia de 100 pies. • Como acción, puedes ver a través de los ojos y oídos de tu familiar, hasta el final de tu siguiente turno. Durante este tiempo, eres ciego y sordo con respecto a tus propios sentidos. • Mientras estás en contacto físico con tu familiar, puedes lanzar conjuros de toque a través de tu familiar como si fueras tú quien los lanza. Tu familiar debe estar a menos de 100 pies de ti, y debe usar su reacción para entregar el conjuro cuando lo lances. Si el conjuro requiere una tirada de ataque, la tirada de ataque usa el modificador de Carisma del familiar. • No puedes tener más de un familiar a la vez. Si lanzas este conjuro mientras ya tienes un familiar, invocas a un segundo familiar, que aparece en un espacio desocupado a menos de 30 pies del otro familiar. • Tu familiar actúa de forma independiente de ti, pero siempre obedece tus órdenes. En combate, rueda su propia iniciativa y actúa en su propio turno. Un familiar no puede atacar, pero puede realizar otras acciones según su especie." },
            ]
        },
    "clerigo": 

        {   "nombre": "Clerigo", 
            "descripcion": "Los clérigos son intermediarios entre el mundo mortal y los distantes planos divinos. Tan diferentes entre ellos como los dioses a los que sirven, los clérigos se esfuerzan por personificar las obras de sus deidades. No son sacerdotes ordinarios, un clérigo se encuentra imbuido de magia divina.",
            "competenciaSalvacion": ["sabiduria", "carisma"],
            "competencias": ["Armadura ligera", "Armadura media", "Escudos", "Armas simples"],
            "caracteristicaPrimaria": ["sabiduria"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 8,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de clérigo. Puedes lanzar un conjuro de clérigo que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces tres conjuros de clérigo de tu elección. Aprendes conjuros adicionales de clérigo de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El clérigo. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de clérigo que conoces con otro de la lista de conjuros de clérigo de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El clérigo)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de clérigo. Aprendes trucos adicionales de clérigo de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El clérigo." },
                { "nombre": "Dominio", "descripcion": "Elige un dominio relacionado con tu deidad: Conocimiento, Engaño, Guerra, Luz, Naturaleza, Tempestad o Vida. Cada dominio se detalla al final de la descripción de la clase, y cada uno proporciona ejemplos de dioses asociados con él. Tu elección te otorga características en el nivel 1 y nuevamente en los niveles 2, 6, 8 y 17." },
            ]
        },
    "druida": 
        {   "nombre": "Druida", 
            "descripcion": "Ya sea invocando a las fuerzas elementales o emulando a las criaturas del mundo animal, los druidas son la personificación de la resistencia, astucia y furia de la naturaleza. Dicen no tener un dominio sobre la naturaleza. En lugar de eso, se ven como una extensión de la voluntad indomable de la misma.",
            "competenciaSalvacion": ["inteligencia", "sabiduria"],
            "competencias": ["Armadura ligera", "Armadura media", "Escudos", "Armas simples", "Armas marciales"],
            "caracteristicaPrimaria": ["sabiduria"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 8,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de druida. Puedes lanzar un conjuro de druida que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de druida de tu elección. Aprendes conjuros adicionales de druida de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El druida. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de druida que conoces con otro de la lista de conjuros de druida de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El druida)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces dos trucos de tu elección de la lista de trucos de druida. Aprendes trucos adicionales de druida de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El druida." },
                { "nombre": "Forma salvaje", "descripcion": "En el nivel 2, puedes usar tu acción para asumir la forma de una bestia que hayas visto antes. Puedes usar esta característica dos veces. Recuperas los usos gastados cuando terminas un descanso corto o largo. Tu nivel de druida determina las bestias que puedes transformar, como se muestra en la tabla Forma salvaje. En el nivel 2, puedes transformarte en una bestia con un nivel de desafío como máximo 1/4. En el nivel 4, puedes transformarte en una bestia con un nivel de desafío como máximo 1/2. En el nivel 8, puedes transformarte en una bestia con un nivel de desafío como máximo 1. En el nivel 12, puedes transformarte en una bestia con un nivel de desafío como máximo 2. En el nivel 16, puedes transformarte en una bestia con un nivel de desafío como máximo 3. En el nivel 20, puedes transformarte en una bestia con un nivel de desafío como máximo 4." },
            ]
        },
    "explorador": 
        {   "nombre": "Explorador", 
            "descripcion": "Lejos del bullicio de las ciudades y pueblos, más allá de las defensas que mantienen a las granjas más lejanas protegidas de los terrores de la naturaleza, en medio de tupidos bosques sin caminos y a través de enormes y vacías llanuras, los exploradores mantienen su interminable guardia.",
            "competenciaSalvacion": ["fuerza", "destreza"],
            "competencias": ["Armadura ligera", "Armadura media", "Escudos", "Armas simples", "Armas marciales"],
            "caracteristicaPrimaria": ["destreza", "sabiduria"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 10,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de explorador. Puedes lanzar un conjuro de explorador que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de explorador de tu elección. Aprendes conjuros adicionales de explorador de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El explorador. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de explorador que conoces con otro de la lista de conjuros de explorador de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El explorador)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de explorador. Aprendes trucos adicionales de explorador de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El explorador." },
                { "nombre": "Estilo de combate", "descripcion": "Elige un estilo de combate. Tu elección te otorga características en el nivel 1. Puedes elegir entre Estilo de combate con arco, Defensa, Duelo o Dos armas." },
                { "nombre": "Rastrear", "descripcion": "Comienzas a rastrear criaturas con éxito a través de terrenos difíciles, incluso a través de terrenos que de otro modo te ralentarían. Viajas a través de terrenos difíciles a tu velocidad normal. Puedes pasar por terrenos difíciles que están cubiertos de espinas, ramas, maleza, nieve, ó hielo sin sufrir daño o penalización a tu velocidad." },
                { "nombre": "Ataque extra", "descripcion": "Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Ataque en tu turno." },
                { "nombre": "Movimiento extra", "descripcion": "En tu turno, puedes moverte hasta 10 pies extra." },
            ]
        },
    "guerrero": 
        {   "nombre": "Guerrero", 
            "descripcion": "Todos los guerreros comparten un dominio magistral de las armas y armaduras, y un exhaustivo conocimiento de las habilidades del combate. Además, están muy relacionados con la muerte, tanto repartiéndola como mirándola fijamente, desafiantes.",
            "competenciaSalvacion": ["fuerza", "constitucion"],
            "competencias": ["Armadura ligera", "Armadura media", "Armadura pesada", "Escudos", "Armas simples", "Armas marciales"],
            "caracteristicaPrimaria": ["fuerza", "destreza"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 10,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de guerrero. Puedes lanzar un conjuro de guerrero que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de guerrero de tu elección. Aprendes conjuros adicionales de guerrero de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El guerrero. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de guerrero que conoces con otro de la lista de conjuros de guerrero de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El guerrero)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de guerrero. Aprendes trucos adicionales de guerrero de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El guerrero." },
                { "nombre": "Estilo de combate", "descripcion": "Elige un estilo de combate. Tu elección te otorga características en el nivel 1. Puedes elegir entre Estilo de combate con arco, Defensa, Duelo o Dos armas." },
                { "nombre": "Ataque extra", "descripcion": "Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Ataque en tu turno." },
                { "nombre": "Movimiento extra", "descripcion": "En tu turno, puedes moverte hasta 10 pies extra." },
            ]
        },
    "hechicero": 
        {   "nombre": "Hechicero", 
            "descripcion": "Los hechiceros tienen una magia innata, conferida por una línea de sangre exótica, una influencia de otro mundo o la exposición a fuerzas cósmicas desconocidas. Uno no puede estudiar hechicería como quien estudia un lenguaje, más de lo que uno puede aprender a vivir una vida legendaria. Nadie elige la hechicería, el poder elige al hechicero.",
            "competenciaSalvacion": ["constitucion", "carisma"],
            "competencias": ["Armas simples", "Ballesta ligera", "Daga", "Dardo", "Honda", "Baston", "Espada corta"],
            "caracteristicaPrimaria": ["carisma"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 6,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de hechicero. Puedes lanzar un conjuro de hechicero que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de hechicero de tu elección. Aprendes conjuros adicionales de hechicero de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El hechicero. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de hechicero que conoces con otro de la lista de conjuros de hechicero de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El hechicero)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces cuatro trucos de tu elección de la lista de trucos de hechicero. Aprendes trucos adicionales de hechicero de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El hechicero." },
                { "nombre": "Origen de la magia", "descripcion": "Elige el origen de tu magia: Dracónico o Salvaje, ambos detallados al final de la descripción de la clase. Tu elección te otorga características en el nivel 1 y nuevamente en los niveles 6, 14 y 18." },
            ]
        },
    "mago": 
        {   "nombre": "Mago", 
            "descripcion": "Los magos son los practicantes supremos de la magia, definidos y unidos como una clase por los hechizos que conjuran. A partir de la sutil onda de la magia que impregna el cosmos, los magos lanzan explosivos hechizos de fuego, arcos voltaicos, sutiles engaños y brutales formas de control mental.",
            "competenciaSalvacion": ["inteligencia", "sabiduria"],
            "competencias": ["Daga", "Baston", "Ballesta ligera"],
            "caracteristicaPrimaria": ["inteligencia"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 6,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de mago. Puedes lanzar un conjuro de mago que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces seis conjuros de mago de tu elección. Aprendes conjuros adicionales de mago de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El mago. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de mago que conoces con otro de la lista de conjuros de mago de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El mago)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de mago. Aprendes trucos adicionales de mago de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El mago." },
                { "nombre": "Libro de conjuros", "descripcion": "En el nivel 1, tienes un libro de conjuros que contiene seis conjuros de mago de tu elección. Tu libro es un tesoro lleno de signos misteriosos élficos que solo tú puedes entender y usar como conjuros. Ver la sección Conjuros preparados más adelante en esta descripción para más detalles." },
                { "nombre": "Conjuros preparados", "descripcion": "Elige un número de conjuros de mago igual a tu modificador de Inteligencia + tu nivel de mago (mínimo de uno). Los conjuros deben ser de un nivel para el que tengas espacios de conjuro. Puedes cambiar los conjuros que tienes preparados cuando terminas un descanso largo. Preparar un nuevo listado de conjuros de mago requiere tiempo dedicado a estudiar tu libro de conjuros y memorizar los gestos y palabras que debes realizar para lanzar el conjuro: al menos 1 minuto por nivel de conjuro para cada conjuro de tu lista." },
            ]
        },
    "monje": 
        {   "nombre": "Monje", 
            "descripcion": "Cualquiera que sea su disciplina, los monjes están unidos por su habilidad para utilizar mágicamente la energía que corre por sus cuerpos. Ya sea canalizada en una impactante demostración de proeza marcial o en el sutil enfoque en la habilidad defensiva y la velocidad, esta energía impulsa todo lo que el monje hace.",
            "competenciaSalvacion": ["fuerza", "destreza"],
            "competencias": ["Armas simples", "Espada corta"],
            "caracteristicaPrimaria": ["destreza", "sabiduria"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 8,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de monje. Puedes lanzar un conjuro de monje que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de monje de tu elección. Aprendes conjuros adicionales de monje de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El monje. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de monje que conoces con otro de la lista de conjuros de monje de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El monje)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de monje. Aprendes trucos adicionales de monje de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El monje." },
                { "nombre": "Estilo de monje", "descripcion": "Elige un estilo de monje. Tu elección te otorga características en el nivel 1. Puedes elegir entre Estilo de monje de la vía abierta, Estilo de monje de la vía de las sombras o Estilo de monje de la vía del maestro borracho." },
                { "nombre": "Ataque extra", "descripcion": "Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Ataque en tu turno." },
                { "nombre": "Movimiento extra", "descripcion": "En tu turno, puedes moverte hasta 10 pies extra." },
            ]
        },
    "paladin": 
        {   "nombre": "Paladin", 
            "descripcion": "Sean cuales sean sus orígenes y sus misiones, los paladines están unidos por sus juramentos para luchar en contra de las fuerzas del mal. El juramento de un paladín es un lazo muy poderoso. Es una fuente de poder que convierte a un devoto guerrero en un campeón bendecido.",
            "competenciaSalvacion": ["sabiduria", "carisma"],
            "competencias": ["Armadura ligera", "Armadura media", "Armadura pesada", "Escudos", "Armas simples", "Armas marciales"],
            "caracteristicaPrimaria": ["fuerza", "carisma"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 10,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de paladín. Puedes lanzar un conjuro de paladín que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de paladín de tu elección. Aprendes conjuros adicionales de paladín de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El paladín. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de paladín que conoces con otro de la lista de conjuros de paladín de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El paladín)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de paladín. Aprendes trucos adicionales de paladín de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El paladín." },
                { "nombre": "Juramento", "descripcion": "En el nivel 3, eliges un juramento que te compromete con un tipo de ideales: el juramento de devoción, el juramento de los antiguos, el juramento de venganza o el juramento de los vigilantes, todos detallados al final de la descripción de la clase. Tu elección te otorga características en el nivel 3 y nuevamente en los niveles 7, 15 y 20." },
            ]
        },
    "picaro": 
        {   "nombre": "Picaro",
            "descripcion": "Los pícaros confían sus habilidades, el sigilo y las vulnerabilidades de sus oponentes para lograr sacar ventaja en cualquier situación. Tienen un don para encontrar la solución a prácticamente cualquier problema, demostrando un ingenio y versatilidad, que es la piedra angular de cualquier buen grupo de aventureros.",
            "competenciaSalvacion": ["destreza", "inteligencia"],
            "competencias": ["Armadura ligera", "Armas simples", "Ballesta de mano", "Espada corta", "Rapier", "Espada corta", "Instrumentos musicales"],
            "caracteristicaPrimaria": ["destreza"],
            # "habilidades": [ "Atletismo", "Intimidación" ],
            "dadoVida": 8,
            "habilidadesEspeciales": [
                { "nombre": "Conjuros", "descripcion": "Puedes lanzar conjuros de picaro. Puedes lanzar un conjuro de picaro que conozcas como un conjuro ritual si ese conjuro tiene la etiqueta de ritual y tienes el conjuro preparado." },
                { "nombre": "Conjuros conocidos", "descripcion": "A nivel 1, conoces dos conjuros de picaro de tu elección. Aprendes conjuros adicionales de picaro de tu elección en niveles más altos, como se muestra en la columna Conjuros conocidos de la tabla El picaro. Cada vez que obtienes un nivel en esta clase, puedes reemplazar un conjuro de picaro que conoces con otro de la lista de conjuros de picaro de nivel que puedas lanzar (como se muestra en la columna Conjuros conocidos de la tabla El picaro)." },
                { "nombre": "Trucos", "descripcion": "A nivel 1, conoces tres trucos de tu elección de la lista de trucos de picaro. Aprendes trucos adicionales de picaro de tu elección en niveles más altos, como se muestra en la columna Trucos de la tabla El picaro." },
                { "nombre": "Estilo de combate", "descripcion": "Elige un estilo de combate. Tu elección te otorga características en el nivel 1. Puedes elegir entre Estilo de combate con arco, Defensa, Duelo o Dos armas." },
                { "nombre": "Ataque extra", "descripcion": "Puedes atacar dos veces, en lugar de una, siempre que realices la acción de Ataque en tu turno." },
                { "nombre": "Movimiento extra", "descripcion": "En tu turno, puedes moverte hasta 10 pies extra." },
            ]
        },
}


