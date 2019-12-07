from os import rename, listdir, path
from sys import argv
import shutil


#argv[1] es el nombre donde estan los pdb originales.
#argv[2] es la carpeta de complejos, donde cambiare los nombres.

def lista_archive(carpeta):
    return listdir(carpeta)


def lista_nueva(lista):
    nombre_actual=[]
    for i in lista:
        nombre_actual.append(i.split(".")[0])
    return nombre_actual


def renombrar(lista_sin_extencion, carpeta):
    i=0
    for nombres in lista_sin_extencion:
        base = carpeta + '/' + lista_sin_extencion[i] + '/PROT/'

        ruta_proteina = base + 'prot.pdb'
        nombre_nuevo = base + lista_sin_extencion[i] +'.pdb'

        if path.exists(ruta_proteina):
            rename(ruta_proteina, nombre_nuevo)
            print( str(i + 1) + ') prot.pdb -->', lista_sin_extencion[i] + '.pdb already!')
            i+=1
        else:
            print(str(i+1) + ') No existe!')
            i+=1
            pass

#complejos, lista_sin_extencion, proteina, nombre_actual
#variables

print('Inicio')
lista = argv[1]
lista_sin_extencion = lista_nueva(lista_archive(lista))
carpeta = argv[2]
print('Configuré variables')

print(len(lista_sin_extencion))

renombrar(lista_sin_extencion, carpeta)
print('Final')



