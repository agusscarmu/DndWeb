export const clases = {
    barbaro: {
      nombre: "Bárbaro",
      descripcion:
        "Para algunos, su rabia brota de la comunión con espíritus de animales salvajes. Otros recurren a su hirviente reserva de ira frente a un mundo lleno de dolor. Para los bárbaros, la furia es un poder que no solo les proporciona un frenesí ciego en la batalla, sino también extraordinarios reflejos, resistencia y proezas de fuerza.",
      competenciaSalvacion: ["fuerza", "constitucion"],
      competencias: ["armas simples", "armas marciales", "escudos", "armaduras ligeras", "armaduras medias"],
      habilidades: ["Atletismo", "Intimidación", "Naturaleza", "Percepción", "Supervivencia", "Trato con animales"],
      aElegir: 2,
    },
    bardo: {
      nombre: "Bardo",
      descripcion:
        "Ya sea un erudito, un poeta o un canalla, un bardo teje su magia a través de sus palabras y su música para inspirar a los aliados, desmoralizar a los enemigos, manipular mentes, crear ilusiones e incluso sanar heridas.",
      competenciaSalvacion: ["destreza", "carisma"],
      competencias: ["armas simples", "armas marciales", "armaduras ligeras"],
      habilidades: [],
      aElegir: 3,
    },
    brujo: {
      nombre: "Brujo",
      descripcion:
        "Los brujos son buscadores del conocimiento que se encuentra escondido en el multiverso. A través de pactos hechos con seres poderosos de poder sobrenatural, los brujos desatan efectos mágicos tanto sutiles como espectaculares y recolectan secretos arcanos para potenciar su propio poder.",
      competenciaSalvacion: ["sabiduria", "carisma"],
      competencias: ["armas simples", "armaduras ligeras"],
      habilidades: ["Arcanos", "Engaño", "Intimidación", "Investigación", "Naturaleza", "Religión", "Historia"],
      aElegir: 2,
    },
    clerigo: {
      nombre: "Clérigo",
      descripcion:
        "Los clérigos son intermediarios entre el mundo mortal y los distantes planos divinos. Tan diferentes entre ellos como los dioses a los que sirven, los clérigos se esfuerzan por personificar las obras de sus deidades. No son sacerdotes ordinarios, un clérigo se encuentra imbuido de magia divina.",
      competenciaSalvacion: ["sabiduria", "carisma"],
      competencias: ["armas simples", "armaduras ligeras", "armaduras medias", "escudos"],
      habilidades: ["Historia", "Medicina", "Persuasión", "Religión","Perspicacia"],
      aElegir: 2,
    },
    druida: {
      nombre: "Druida",
      descripcion:
        "Ya sea invocando a las fuerzas elementales o emulando a las criaturas del mundo animal, los druidas son la personificación de la resistencia, astucia y furia de la naturaleza. Dicen no tener un dominio sobre la naturaleza. En lugar de eso, se ven como una extensión de la voluntad indomable de la misma.",
      competenciaSalvacion: ["inteligencia", "sabiduria"],
      competencias: ["armadura intermedia","armaduras ligeras", "escudos"],
      habilidades: ["Arcanos", "Medicina", "Naturaleza", "Percepción", "Religión", "Supervivencia", "Trato con animales", "Perspicacia"],
      aElegir: 2,
    },
    explorador: {
      nombre: "Explorador",
      descripcion:
        "Lejos del bullicio de las ciudades y pueblos, más allá de las defensas que mantienen a las granjas más lejanas protegidas de los terrores de la naturaleza, en medio de tupidos bosques sin caminos y a través de enormes y vacías llanuras, los exploradores mantienen su interminable guardia.",
      competenciaSalvacion: ["fuerza", "destreza"],
      competencias: ["armas simples", "armas marciales", "armaduras ligeras", "armaduras medias", "escudos"],
      habilidades: ["Atletismo", "Supervivencia", "Trato con animales", "Percepción", "Naturaleza", "Sigilo", "Investigación", "Perspicacia"],
      aElegir: 3,
    },
    guerrero: {
      nombre: "Guerrero",
      descripcion:
        "Todos los guerreros comparten un dominio magistral de las armas y armaduras, y un exhaustivo conocimiento de las habilidades del combate. Además, están muy relacionados con la muerte, tanto repartiéndola como mirándola fijamente, desafiantes.",
      competenciaSalvacion: ["fuerza", "constitucion"],
      competencias: ["armas simples", "armas marciales", "armaduras ligeras", "armaduras medias", "escudos"],
      habilidades: ["Atletismo", "Supervivencia", "Trato con animales", "Percepción", "Acrobacias", "Historia", "Intimidar", "Perspicacia"],
      aElegir: 2,
    },
    hechicero: {
      nombre: "Hechicero",
      descripcion:
        "Los hechiceros tienen una magia innata, conferida por una línea de sangre exótica, una influencia de otro mundo o la exposición a fuerzas cósmicas desconocidas. Uno no puede estudiar hechicería como quien estudia un lenguaje, más de lo que uno puede aprender a vivir una vida legendaria. Nadie elige la hechicería, el poder elige al hechicero.",
      competenciaSalvacion: ["constitucion", "carisma"],
      competencias: ["armas simples"],
      habilidades: ["Arcanos", "Engaño", "Intimidación", "Perspicacia", "Persuasion", "Religión"],
      aElegir: 2,
    },
    mago: {
      nombre: "Mago",
      descripcion:
        "Los magos son los practicantes supremos de la magia, definidos y unidos como una clase por los hechizos que conjuran. A partir de la sutil onda de la magia que impregna el cosmos, los magos lanzan explosivos hechizos de fuego, arcos voltaicos, sutiles engaños y brutales formas de control mental.",
      competenciaSalvacion: ["inteligencia", "sabiduria"],
      competencias: ["armas simples"],
      habilidades: ["Arcanos", "Historia", "Investigación", "Medicina", "Perspicacia", "Religión"],
      aElegir: 2,
    },
    monje: {
      nombre: "Monje",
      descripcion:
        "Cualquiera que sea su disciplina, los monjes están unidos por su habilidad para utilizar mágicamente la energía que corre por sus cuerpos. Ya sea canalizada en una impactante demostración de proeza marcial o en el sutil enfoque en la habilidad defensiva y la velocidad, esta energía impulsa todo lo que el monje hace.",
      competenciaSalvacion: ["fuerza", "destreza"],
      competencias: ["armas simples", "instrumentos musicales"],
      habilidades: ["Acrobacias", "Atletismo", "Historia", "Religión", "Sigilo", "Perspicacia"],
      aElegir: 2,
    },
    paladin: {
      nombre: "Paladín",
      descripcion:
        "Sean cuales sean sus orígenes y sus misiones, los paladines están unidos por sus juramentos para luchar en contra de las fuerzas del mal. El juramento de un paladín es un lazo muy poderoso. Es una fuente de poder que convierte a un devoto guerrero en un campeón bendecido.",
      competenciaSalvacion: ["sabiduria", "carisma"],
      competencias: ["armas simples", "armas marciales", "armaduras ligeras", "armaduras medias", "escudos"],
      habilidades: ["Atletismo", "Intimidación", "Medicina", "Perspicacia", "Persuasión", "Religión"],
      aElegir: 2,
    },
    picaro: {
      nombre: "Pícaro",
      descripcion:
        "Los pícaros confían sus habilidades, el sigilo y las vulnerabilidades de sus oponentes para lograr sacar ventaja en cualquier situación. Tienen un don para encontrar la solución a prácticamente cualquier problema, demostrando un ingenio y versatilidad, que es la piedra angular de cualquier buen grupo de aventureros.",
      competenciaSalvacion: ["destreza", "inteligencia"],
      competencias: ["armas simples", "armas marciales", "armaduras ligeras"],
      habilidades: ["Acrobacias", "Atletismo", "Engaño", "Intimidación", "Investigación", "Juego de manos", "Percepción", "Perspicacia", "Persuasión", "Sigilo"],
      aElegir: 4,
    },
  };
  
//   // Ejemplo de cómo acceder a la información de una clase específica:
//   console.log(clases.barbaro.nombre); // "Bárbaro"
//   console.log(clases.barbaro.descripcion); // Descripción del bárbaro
//   console.log(clases.barbaro.competenciaSalvacion); // ["Fuerza", "Constitución"]
  