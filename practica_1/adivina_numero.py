

#"blablalba {} dg".format(variable)
import random
import sys

class Jugador:
    def __init__(self,name):
        self.name=name
    
if __name__ =="__main__":
    s="s"
    nombre=input("Hola! Cómo te llamas? ")
    player=Jugador(nombre)
    while s=="s":
        player.intentos=0
        num=random.randrange(0,10)
        print("Bueno, {} estoy pensando en un número entre 1 y 10. Intenta adivinarlo.".format(player.name))
        a=-1
        while num!=a:
            a=input("Introduce un numero: ")
            a=int(a)
            if num<a:
                print("El numero a adivinar es menor")
            elif num>a:
                print("El numero a adivinar es mayor")
            player.intentos+=1
        print("Buen trabajo,{}!Has adivinado en {}. Ahora te toca pensar en un número".format(player.name,player.intentos))
        respuesta='falso'
        menor=0
        mayor=10
        intentos2=0
        while 'correcto'!=respuesta:
            if(menor!=mayor):
                num=random.randrange(menor,mayor)
            else:
                num=menor
            print("El número que has pensado es el {}".format(num))
            respuesta=input("mayor/menor/correcto? ")
            if respuesta=='mayor':
                menor=num+1
            elif respuesta=='menor':
                mayor=num-1
            intentos2+=1
        if(intentos2<player.intentos):
            print("Yo gano. He acertado en {} intentos".format(intentos2))
        elif(player.intentos<intentos2):
            print("Tú ganas. He acertado en {} intentos".format(intentos2))
        else:
            print("Hemos empatado. He acertado en {} intentos".format(intentos2))
        s=input("Quieres volver a jugar s/n ")
    sys.exit()
