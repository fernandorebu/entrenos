from entrenos import *
def Test_leer_entrenos(ruta_fichero):
    datos = lee_entrenos(ruta_fichero)
    print(datos[:1])



ruta_fichero = 'data\entrenos.csv'
datos =lee_entrenos(ruta_fichero)
def test_tipos_entrenos(datos):
    tipos = tipo_entreno(datos)
    print(tipos)


ruta_fichero = 'data\entrenos.csv'
datos =lee_entrenos(ruta_fichero)
d = 120
def test_entrenos_duracio_superior(datos, d):
    tipos = entrenos_duracio_superior(datos, d)
    print(tipos)

ruta_fichero = 'data\entrenos.csv'
datos =lee_entrenos(ruta_fichero)
fecha_inicio = (2/3/2017)
fecha_fin = (3/6/2020)
def test_suma_calorias(lista_entrenos, fecha_inicio, fecha_fin):
    tipos = suma_calorias(lista_entrenos, fecha_inicio, fecha_fin)
    print(tipos)


if __name__ == '__main__':
    ruta_fichero = 'data\entrenos.csv'
    #Prueba = Test_leer_entrenos(ruta_fichero)
    #test_tipos_entrenos(datos)
    test_entrenos_duracio_superior(datos, d)
    
    