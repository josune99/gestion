Para esta práctica hemos usado la clase ExchangeApiClient para todo lo relacionado con comunicarse con la página y para convertir las monedas a euros.
Por otro lado hemos creado dos funciones: una para lo relacionado con abrir el fichero divisas.txt y leer de él y otra para escribir en el fichero ahorros.txt.
He supuesto que siempre se van a llamar divisas.txt y ahorros.txt, si quisieramos usar otros ficheros tendríamos que comunicarnos con el usuario a través de la terminal y por la lectura de la práctica no creo que haya que realizar dicha comunicación.
El programa principal tan sólo crea un obejeto de la clase ExchangeApiClient, llama a la función leer archivo, guarda el total y llama a la función escribir_archivo.
Además de esto hay una función auxiliar que sirve para separar las lineas que leemos desde el archivo en palabras.
