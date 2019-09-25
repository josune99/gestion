from urllib.request import urlopen

import json,datetime

class ExchangeAPIClient:
    def get_rates(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        rates = json.loads(response.read())
        return rates['rates']

    def convert(self,palabras):
        rates = self.get_rates()
        if palabras[0]=='EUR':
            return float(palabras[1])
        else:
            return float(palabras[1])/rates[palabras[0]]

def separar_palabras(linea):
    palabra=linea.split()
    palabra[0]=palabra[0].rstrip(',')
    return palabra

def leer_archivo(archivo,api):
    total=0
    f=open(archivo,'r')
    for linea in f:
        palabras=separar_palabras(linea)
        cantidad_en_euros = api.convert(palabras)
        print('{} son {} euros'.format(linea, cantidad_en_euros))
        total+=cantidad_en_euros
    f.close()
    return(total)

def escribir_archivo(archivo,total):
    x = str(datetime.datetime.now())
    x=x.split()
    x=x[0]
    f=open(archivo,'a')
    f.write(x+', '+str(total)+"\n")
    f.close()
    
api= ExchangeAPIClient()
total=leer_archivo('divisas.txt',api)
total=(int(total))
escribir_archivo('ahorros.txt',total)


