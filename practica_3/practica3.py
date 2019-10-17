from flask import Flask
import sqlite3
import json
from json2html import *
import sys


if (len(sys.argv)<2):
	base=input("No se ha introducido el nombre de la base, introduzcalo por favor: ")
else:
	base=sys.argv[1]

print("La base utilizada es: {}".format(base))

app = Flask(__name__)

@app.route("/")
def home():
	return "PRACTICA 3 DE GESTIÓN, JOSUNE SORBET"

@app.route("/tablas")
def mostrar_tablas():
	res=""
	conn = sqlite3.connect(base)
	c = conn.cursor()
	c.execute("SELECT name FROM sqlite_master where TYPE='table';")
	res = c.fetchall()
	print(res)
	jsonfile = json.dumps(res)
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nombre_tablas>")
def registros_tabla(nombre_tablas):
	conn = sqlite3.connect(base)
	c = conn.cursor()
	ejecutar="SELECT * FROM "+str(nombre_tablas)
	c.execute(ejecutar)
	res = c.fetchall()
	print(res)
	jsonfile = json.dumps(res)
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nombre_tablas>/info")
def info_tabla(nombre_tablas):
	aux1=""
	conn = sqlite3.connect(base)
	c = conn.cursor()
	ejecutar="SELECT * FROM "+str(nombre_tablas)
	c.execute(ejecutar)
	res = c.fetchall()
	lineas=len(res)
	c.execute('PRAGMA TABLE_INFO({})'.format(nombre_tablas))
	res = c.fetchall()
	for i in res:
		aux=(str(i)).split(",")
		aux1=aux1+" "+aux[1][1:]+', '
	aux1="[("+aux1+"Numero de registros: "+str(lineas)+")]"
	print(aux1)
	jsonfile = json.dumps(aux1) 
	return json2html.convert(json = jsonfile)

if __name__ == "__main__":
 app.run()
