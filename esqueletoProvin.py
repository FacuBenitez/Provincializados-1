print ("Bienvenido a Provincializados!, una trivia en homenaje a la provincialización del Chaco en...epa casi te digo la respuesta de una pregunta...Como te estaras dando cuenta en esta trivia encontraras preguntas referidas a la provincialización de esta provincia del Nordeste argentino, como asi también algunas referidas a cuestiones de cultura general vinculadas al Chaco")


def juego_nuevo():

    respuestas = []
    respuestas_correctas = 0
    num_pregunta = 1

    for key in preguntas:
        print("-------------------------")
        print(key)
        for i in opciones[num_pregunta-1]:
            print(i)
        respuesta = input("Selecciona (1, 2, o 3 ): ")
        respuesta = respuesta.upper()
        respuestas.append(respuesta)

        respuestas_correctas += check_answer(preguntas.get(key), respuesta)
        num_pregunta += 1

    display_score(respuestas_correctas, respuestas)

def check_answer(answer, respuesta):

    if answer == respuesta:
        print("Correcto! Bien Ahí")
        return 1
    else:
        print("No che, le pifiaste")
        return 0

def display_score(respuestas_correctas, respuesta):
    print("-------------------------")
    print("Resultado")
    print("-------------------------")

    #print("Answers: ", end="")
    #for i in questions:
       # print(questions.get(i), end=" ")
   # print()

    #print("Guesses: ", end="")
    #for i in guesses:
     #   print(i, end=" ")
    #print()

    promedio = int((respuestas_correctas/len(preguntas))*100)
    if (promedio <= 30):
      print("Tu nivel de chaqueñidad es: "+"("+str(promedio)+"%) Porteñito")
    elif (promedio >30 & promedio <= 70):
      print("Tu nivel de chaqueñidad es: "+"("+str(promedio)+"%) Maso")
    elif (promedio > 70 & promedio <= 90):
                            print("Tu nivel de chaqueñidad es: "+"("+str(promedio)+"%) Bueno, tomas terere en la vereda")
    else:
     print("Tu nivel de chaqueñidad es: "+"("+str(promedio)+"%) Muy bueno, entras gratis a los recitales de Lluvia y la Banda")



def jugar_denuevo():

    response = input("¿Queres jugar de nuevo (si o no)? ")
    response = response.upper()

    if response == "Si":
        return True
    else:
        return False


preguntas = {
 "¿En que año fue la provincialización del Chaco?: ": "1",
 "¿Cual fue el número de ley nacional que dispuso la provincialización del territorio nacional del Chaco?: ": "2",
 "¿Cual fue el primer nombre que tuvo la provincia?: ": "3",
 "¿Quien fue el primer gobernador?: ": "1",
 "¿Cuantos habitantes tenía el Territorio Nacional del Chaco en el Censo Nacional de 1947?: ": "2",
 "¿Cuantos habitantes tenía la Provincia del Chaco en 1960, su primer censo como provincia?: ": "3",
 "¿En que año la provincia adquiere su nombre actual?: ": "1",
 "¿En que año se creo la bandera actual del Chaco?: ": "2",
 "¿Quién fue el campeón de la Liga Chaqueña de Futbol en el año de la provincialización?: ": "3",
 "¿Que edad tenía el Perro Fernando cuando se provincializo el Chaco?: ": "1",
 "¿Cómo se llamaba el Ferrocarril que unía a Resistencia con Retiro (Buenos Aires) en 1951?: ": "2",
 "En 1915 una ciudad chaqueña fue la primera en ser una comuna socialista en Latinoamerica, ¿cual fue?: ": "3",
 "Una ciudad chaqueña fue la primera de la Argentina en contar con red eléctrica ¿cual fue?: ": "1",
 "¿Cuál era el mayor cultivo en la época de la provincialización?: ": "2",
 "Un escritor reconocido en el ámbito chaqueño recibió el Premio Pionero de la Letras Chaqueñas, otorgado por la provincia del Chaco y la SADE local en 1985. ¿Quién fue?: ": "3",
 "¿Cuál es la flor provincial del Chaco?: ": "1",
 "¿Con que provincias no limita el Chaco?: ": "2",
 "¿De que ciudad chaqueña es Luis Landriscina?: ": "3"
 }

opciones = [["1. 1951", "2. 1952", "3. 1953"],
          ["1. 14036", "2. 14037", "3. 14038"],
          ["1. Provincia Eva Perón", "2. Provincia del Chaco", "C. Provincia Presidente Perón"],
          ["1. Felipe Gallardo", "2. Deolindo Bittel", "3. Florencio Tenev"],
          ["1. 401002", "2. 430555", "3. 500010"],
          ["1. 460002", "2, 500120", "3. 543331"],
          ["1. 1955", "2. 1954", "3. 1956"],
          ["1. 2006", "2. 2007", "3. 2008"],
          ["1. Sarmiento", "2. Villa Alvear", "3. Chaco For Ever"],
          ["1. 2 años", "2. 3 años", "3. 4 años"],
          ["1. Ferrocarril San Martín", "2. Ferrocarril General Belgrano", "3. Ferrocarril Sarmiento"],
          ["1. Barranqueras", "2. Presidencia Roque Saenz Peña", "3. Resistencia"], 
          ["1. Las Palmas", "2. Presidencia Roque Saenz Peña", "3. Charata"],
          ["1. Maíz", "2. Algodón", "3. Trigo"],
          ["1. Tete Romero", "2. Mempo Giardinelli", "3. Luis Meloni"],
          ["1. Flor rosada del palo borracho", "2. Flor del Ceibo", "3. Flor de Irupe"],
          ["1. Santa Fe", "2. Entre Rios", "3. Salta"],
          ["1. Resistencia", "2. Charata", "3. Villa Angela"]
          ]

juego_nuevo()

while jugar_denuevo():
    juego_nuevo()

print("Chau! Nos vemos")

preguntas = {
 "¿En que año fue la provincialización del Chaco?: ": "1",
 "¿Cual fue el número de ley nacional que dispuso la provincialización del territorio nacional del Chaco?: ": "2",
 "¿Cual fue el primer nombre que tuvo la provincia?: ": "3",
 "¿Quien fue el primer gobernador?: ": "1",
  "¿Cuantos habitantes tenía el Territorio Nacional del Chaco en el Censo Nacional de 1947?: ": "2",
 "¿Cuantos habitantes tenía la Provincia del Chaco en 1960, su primer censo como provincia?: ": "3",
 "¿En que año la provincia adquiere su nombre actual?: ": "1",
 "¿En que año se creo la bandera actual del Chaco?: ": "2",
 "¿Quién fue el campeón de la Liga Chaqueña de Futbol en el año de la provincialización?: ": "3",
 "¿Que edad tenía el Perro Fernando cuando se provincializo el Chaco?: ": "1",
 "¿Cómo se llamaba el Ferrocarril que unía a Resistencia con Retiro (Buenos Aires) en 1951?: ": "2",
 "En 1915 una ciudad chaqueña fue la primera en ser una comuna socialista en Latinoamerica, ¿cual fue?: ": "3",
 "Una ciudad chaqueña fue la primera de la Argentina en contar con red eléctrica ¿cual fue?: ": "1",
 "¿Cuál era el mayor cultivo en la época de la provincialización?: ": "2",
 "Un escritor reconocido en el ámbito chaqueño recibió el Premio Pionero de la Letras Chaqueñas, otorgado por la provincia del Chaco y la SADE local en 1985. ¿Quién fue?: ": "3",
 "¿Cuál es la flor provincial del Chaco?: ": "1",
 "¿Con que provincias no limita el Chaco?: ": "2",
 "¿De que ciudad chaqueña es Luis Landriscina?: ": "3"
}

opciones = [["1. 1951", "2. 1952", "3. 1953"],
          ["1. 14036", "2. 14037", "3. 14038"],
          ["1. Provincia Eva Perón", "2. Provincia del Chaco", "C. Provincia Presidente Perón"],
          ["1. Felipe Gallardo", "2. Deolindo Bittel", "3. Florencio Tenev"],
          ["1. 401002", "2. 430555", "3. 500010"],
          ["1. 460002", "2, 500120", "3. 543331"],
          ["1. 1955", "2. 1954", "3. 1956"],
          ["1. 2006", "2. 2007", "3. 2008"],
          ["1. Sarmiento", "2. Villa Alvear", "3. Chaco For Ever"],
          ["1. 2 años", "2. 3 años", "3. 4 años"],
          ["1. Ferrocarril San Martín", "2. Ferrocarril General Belgrano", "3. Ferrocarril Sarmiento"],
          ["1. Barranqueras", "2. Presidencia Roque Saenz Peña", "3. Resistencia"], 
          ["1. Las Palmas", "2. Presidencia Roque Saenz Peña", "3. Charata"],
          ["1. Maíz", "2. Algodón", "3. Trigo"],
          ["1. Tete Romero", "2. Mempo Giardinelli", "3. Luis Meloni"],
          ["1. Flor rosada del palo borracho", "2. Flor del Ceibo", "3. Flor de Irupe"],
          ["1. Santa Fe", "2. Entre Rios", "3. Salta"],
          ["1. Resistencia", "2. Charata", "3. Villa Angela"]]

juego_nuevo()

while jugar_denuevo():
    juego_nuevo()

print("Chau! Nos vemos") 