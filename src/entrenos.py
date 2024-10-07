import csv
from collections import namedtuple
from datetime import *

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    lista = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora, '%d/%m/%Y %H:%M')
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = parsea_compartidos(compartido)
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            lista.append(tupla)
        return lista



def parsea_compartidos(valor):
    if valor == 'S':
        return True
    else:
        return False
    

def tipo_entreno(lista_entrenos):
    entreno_coj = set()
    for e in lista_entrenos:
        entreno_coj.add(e.tipo)
    return sorted(entreno_coj)


def entrenos_duracio_superior(lista_entrenos, d):
    res = []
    for e in lista_entrenos:
        if e.duracion > d:
            res.append(e)
    return res

def suma_calorias(lista_entrenos, fecha_inicio:date, fecha_fin:date):
    res = 0
    for e in lista_entrenos:
        if e.fechahora.date() > fecha_inicio and e.fechahora.date() <= fecha_fin:
            res = res + e.calorias
        else:
            res =  res + 0
    return res